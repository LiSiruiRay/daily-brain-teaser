"""
Generates one brain teaser via Claude API and commits it to the repo.
Called by GitHub Actions at 4am and 4pm ET.

Usage:
  python scripts/generate_question.py am
  python scripts/generate_question.py pm
  SLOT=am python scripts/generate_question.py
"""

import os
import re
import sys
import random
from pathlib import Path
from datetime import datetime, timezone, timedelta

import anthropic

try:
    from pypdf import PdfReader
    HAS_PYPDF = True
except ImportError:
    HAS_PYPDF = False

REPO_ROOT = Path(__file__).parent.parent
QUESTIONS_DIR = REPO_ROOT / "questions"
MATERIALS_DIR = REPO_ROOT / "materials"

# Eastern Time offset (EDT = -4). GitHub Actions cron doesn't track DST;
# the 1-hour drift between EDT/EST is acceptable for a personal site.
ET = timezone(timedelta(hours=-4))

SCHEDULE = {
    0: ("Analysis (Stein / Rudin)",              ["analysis"],              "analysis"),
    1: ("Topology / Algebra",                    ["topology", "algebra"],   "topology"),
    2: ("Probability puzzle",                    ["probability"],           "Probability"),
    3: ("Complex Analysis / Differential Geometry", ["complex", "diff_geo"], "Complex Analysis"),
    4: ("Putnam / fun problems",                 ["putnam", "olympiad", "fun_problems"], "Putnam"),
    5: ("Integration bee",                       ["integration_bee"],       "Integration"),
    6: ("ML / statistics insight",               ["ML", "stats"],           "ML/Stats"),
}

RESPONSE_FORMAT = """\
Reply in exactly this structure (keep the XML tags):

<QUESTION>
# [Problem Title]

[Full question body in markdown with LaTeX. Do NOT include frontmatter.]
</QUESTION>

<ANSWER>
## Key Idea / Intuition

[2-4 sentences. High-level picture before any symbols.]

---

## Formal Proof / Solution

[Step-by-step solution with LaTeX.]
</ANSWER>

<METADATA>
name: "Short problem title"
type: "one of: Integration | ML/Stats | analysis | algebra | topology | Probability | Complex Analysis | Differential Geometry | Putnam"
tags: ["tag1", "tag2", "tag3"]
difficulty: 2
source: "Book or source name (leave empty string if none)"
</METADATA>"""


# ── helpers ──────────────────────────────────────────────────────────────────

def today_et() -> str:
    return datetime.now(ET).strftime("%Y-%m-%d")


def get_slot() -> str:
    if len(sys.argv) > 1 and sys.argv[1] in ("am", "pm"):
        return sys.argv[1]
    return os.environ.get("SLOT", "am")


def list_pdfs(folders: list[str]) -> list[Path]:
    pdfs = []
    for folder in folders:
        d = MATERIALS_DIR / folder
        if d.exists():
            pdfs.extend(d.glob("*.pdf"))
    return pdfs


def extract_excerpt(folders: list[str], max_chars: int = 3500) -> tuple[str, str]:
    """Return (excerpt_text, source_filename). Falls back to ('', '') on any error."""
    if not HAS_PYPDF:
        return "", ""
    pdfs = list_pdfs(folders)
    if not pdfs:
        return "", ""
    pdf_path = random.choice(pdfs)
    try:
        reader = PdfReader(str(pdf_path))
        total = len(reader.pages)
        if total == 0:
            return "", pdf_path.name
        start = random.randint(0, max(0, total - 8))
        parts = []
        for i in range(start, min(start + 8, total)):
            t = (reader.pages[i].extract_text() or "").strip()
            if t:
                parts.append(t)
        text = "\n".join(parts)
        if not text.strip():
            return "", pdf_path.name
        if len(text) > max_chars:
            text = text[:max_chars] + "\n[... truncated ...]"
        return text, pdf_path.name
    except Exception as e:
        print(f"  Warning: could not read {pdf_path.name}: {e}")
        return "", pdf_path.name


def read_existing_names() -> list[str]:
    path = QUESTIONS_DIR / "Problem_list.md"
    names = []
    for line in path.read_text().splitlines():
        m = re.match(r"\|\s*\d+\s*\|\s*\[(.+?)\]", line)
        if m:
            names.append(m.group(1))
    return names


def read_claude_md() -> str:
    p = REPO_ROOT / ".claude" / "CLAUDE.md"
    return p.read_text() if p.exists() else ""


# ── Claude call ───────────────────────────────────────────────────────────────

def call_claude(slot: str, topic: str, canonical_type: str,
                pdf_files: list[Path], excerpt: str, source_file: str,
                existing: list[str]) -> str:
    client = anthropic.Anthropic(api_key=os.environ["ANTHROPIC_API_KEY"])

    files_str = "\n".join(f"  - {p.parent.name}/{p.name}" for p in pdf_files) or "  (none)"
    existing_str = "\n".join(f"  - {n}" for n in existing)

    excerpt_section = ""
    if excerpt:
        excerpt_section = f"""
**Excerpt from {source_file} (use if a good problem is visible here):**
```
{excerpt}
```
"""

    user_msg = f"""Generate one brain teaser.

**Slot:** {slot.upper()} ({"morning" if slot == "am" else "afternoon"})
**Today's topic:** {topic}
**Preferred `type` value:** {canonical_type}

**Available reference books for this topic:**
{files_str}
{excerpt_section}
**Already given — do NOT repeat or substantially overlap in technique:**
{existing_str}

{RESPONSE_FORMAT}"""

    system = (
        read_claude_md()
        + "\n\nCritical: always open the answer with high-level intuition before any formal proof. "
        "Use $...$ for inline LaTeX and $$...$$ for display math."
    )

    msg = client.messages.create(
        model="claude-sonnet-4-6",
        max_tokens=2048,
        system=system,
        messages=[{"role": "user", "content": user_msg}],
    )
    return msg.content[0].text


# ── response parsing ──────────────────────────────────────────────────────────

def extract_tag(text: str, tag: str) -> str:
    m = re.search(rf"<{tag}>(.*?)</{tag}>", text, re.DOTALL)
    return m.group(1).strip() if m else ""


def parse_metadata(raw: str) -> dict:
    meta: dict = {}
    for line in raw.splitlines():
        m = re.match(r'^(\w+):\s*(.+)$', line.strip())
        if not m:
            continue
        key, val = m.group(1), m.group(2).strip()
        if val.startswith('['):
            meta[key] = re.findall(r'"([^"]*)"', val)
        elif val.startswith('"') and val.endswith('"'):
            meta[key] = val[1:-1]
        elif val.lstrip('-').isdigit():
            meta[key] = int(val)
        else:
            meta[key] = val
    return meta


# ── file writing ──────────────────────────────────────────────────────────────

def build_frontmatter(meta: dict, date: str) -> str:
    tags = meta.get("tags", [])
    tags_yaml = "[" + ", ".join(f'"{t}"' for t in tags) + "]"
    source = meta.get("source", "")
    lines = [
        "---",
        f'name: "{meta.get("name", "")}"',
        f'type: "{meta.get("type", "")}"',
        f"tags: {tags_yaml}",
        f'date: "{date}"',
        "solved: false",
        'comments: ""',
        "related: []",
        "redo: 0",
        f'difficulty: {meta.get("difficulty", 2)}',
    ]
    if source:
        lines.append(f'source: "{source}"')
    lines.append("---")
    return "\n".join(lines) + "\n"


def append_to_problem_list(slug: str, name: str, date: str):
    path = QUESTIONS_DIR / "Problem_list.md"
    content = path.read_text()
    nums = re.findall(r"^\|\s*(\d+)\s*\|", content, re.MULTILINE)
    next_num = max(int(n) for n in nums) + 1 if nums else 1
    new_row = f"| {next_num} | [{name}]({slug}/question.md) | {date} |"
    path.write_text(content.rstrip() + "\n" + new_row + "\n")


# ── main ──────────────────────────────────────────────────────────────────────

def main():
    slot = get_slot()
    date = today_et()
    slug = f"{date}_{slot}"

    topic_name, folders, canonical_type = SCHEDULE[datetime.now(ET).weekday()]
    print(f"Generating [{slot.upper()}] {date} — topic: {topic_name}")

    out_dir = QUESTIONS_DIR / slug
    if (out_dir / "question.md").exists():
        print(f"  Already exists: {slug}. Nothing to do.")
        return

    pdf_files = list_pdfs(folders)
    print(f"  PDFs available: {len(pdf_files)}")

    excerpt, source_file = extract_excerpt(folders)
    print(f"  PDF excerpt: {'yes (' + source_file + ')' if excerpt else 'no'}")

    existing = read_existing_names()
    print(f"  Existing problems: {len(existing)}")

    print("  Calling Claude API...")
    response = call_claude(slot, topic_name, canonical_type,
                           pdf_files, excerpt, source_file, existing)

    question_body = extract_tag(response, "QUESTION")
    answer_body   = extract_tag(response, "ANSWER")
    meta          = parse_metadata(extract_tag(response, "METADATA"))

    if not question_body or not answer_body:
        print("ERROR: could not parse Claude response:\n")
        print(response)
        sys.exit(1)

    name = meta.get("name", slug)
    print(f"  Problem: {name}")

    out_dir.mkdir(parents=True, exist_ok=True)
    (out_dir / "question.md").write_text(build_frontmatter(meta, date) + question_body + "\n")
    (out_dir / "answer.md").write_text(f"# Answer: {name}\n\n{answer_body}\n")

    append_to_problem_list(slug, name, date)

    # Rebuild README
    import subprocess
    subprocess.run([sys.executable, str(REPO_ROOT / "scripts" / "sync.py")], check=True)

    print(f"  Done → questions/{slug}/")


if __name__ == "__main__":
    main()
