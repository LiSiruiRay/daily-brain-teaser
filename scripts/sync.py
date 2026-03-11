"""
Fetches brain teaser entries from Notion and generates README.md.
Run locally: python scripts/sync.py
"""

import os
import re
import requests
from pathlib import Path
from datetime import datetime
from dotenv import load_dotenv

load_dotenv()

NOTION_TOKEN = os.environ["NOTION_TOKEN"]
DATABASE_ID = os.environ["NOTION_DATABASE_ID"]

HEADERS = {
    "Authorization": f"Bearer {NOTION_TOKEN}",
    "Notion-Version": "2022-06-28",
    "Content-Type": "application/json",
}

# Map Notion type names → shield.io badge colors
TYPE_COLORS = {
    "Integration": "blue",
    "analysis": "9b59b6",
    "ML/Stats": "e67e22",
}

TAG_COLORS = {
    "Lp norm": "3498db",
    "Limit": "2ecc71",
    "Lim inf/sup": "1abc9c",
    "Squeeze Theorem": "e74c3c",
    "Hilbert Space": "8e44ad",
    "Dense": "2980b9",
    "Uniformly Convergence": "27ae60",
    "Convergence": "16a085",
    "L1 norm": "d35400",
    "Vector Space": "c0392b",
    "logarithm": "f39c12",
    "hyperbolic functions": "7f8c8d",
    "Logistic Regression": "2c3e50",
    "Sigmoid": "e74c3c",
    "Cross-entropy": "8e44ad",
}

REPO_ROOT = Path(__file__).parent.parent
IMAGES_DIR = REPO_ROOT / "images"
IMAGES_DIR.mkdir(exist_ok=True)


def badge(text, color):
    encoded = requests.utils.quote(text.replace("-", "--").replace("_", "__"))
    return f"![{text}](https://img.shields.io/badge/{encoded}-{color}?style=flat-square)"


def fetch_all_pages():
    url = f"https://api.notion.com/v1/databases/{DATABASE_ID}/query"
    results = []
    body = {"sorts": [{"property": "Date", "direction": "descending"}]}
    while True:
        resp = requests.post(url, headers=HEADERS, json=body)
        resp.raise_for_status()
        data = resp.json()
        results.extend(data["results"])
        if not data.get("has_more"):
            break
        body["start_cursor"] = data["next_cursor"]
    return results


def download_image(url, name):
    """Download image and return relative path. Returns None on failure."""
    try:
        safe_name = re.sub(r"[^a-zA-Z0-9_-]", "_", name)
        # Detect extension from URL
        ext = url.split("?")[0].split(".")[-1]
        if ext.lower() not in ("png", "jpg", "jpeg", "gif", "webp", "svg"):
            ext = "png"
        path = IMAGES_DIR / f"{safe_name}.{ext}"
        resp = requests.get(url, timeout=10)
        resp.raise_for_status()
        path.write_bytes(resp.content)
        return f"images/{safe_name}.{ext}"
    except Exception as e:
        print(f"  Warning: could not download image for '{name}': {e}")
        return None


def get_title(props, key="Name"):
    parts = props.get(key, {}).get("title", [])
    return "".join(p["plain_text"] for p in parts).strip()


def get_text(props, key):
    parts = props.get(key, {}).get("rich_text", [])
    return "".join(p["plain_text"] for p in parts).strip()


def get_number(props, key):
    val = props.get(key, {}).get("number")
    return str(val) if val is not None else ""


def get_checkbox(props, key):
    return "✅" if props.get(key, {}).get("checkbox") else ""


def get_date(props, key):
    d = props.get(key, {}).get("date")
    return d["start"] if d else ""


def get_url(props, key):
    """Handles both URL-type and rich_text-type fields that contain links."""
    prop = props.get(key, {})
    # URL property type
    if prop.get("type") == "url":
        url = prop.get("url") or ""
        return f"[link]({url})" if url else ""
    # Rich text — extract the first URL from text or href
    for part in prop.get("rich_text", []):
        href = part.get("href") or part.get("text", {}).get("link", {}) or {}
        if isinstance(href, dict):
            href = href.get("url", "")
        if href:
            return f"[link]({href})"
        # fallback: plain text that looks like a URL
        text = part.get("plain_text", "")
        if text.startswith("http"):
            return f"[link]({text})"
    return ""


def get_multi_select(props, key, color_map=None):
    if color_map is None:
        color_map = TAG_COLORS
    items = props.get(key, {}).get("multi_select", [])
    badges = []
    for item in items:
        color = color_map.get(item["name"], "95a5a6")
        badges.append(badge(item["name"], color))
    return " ".join(badges)


def get_slug(props):
    """Get the Slug field — used to link to local questions/{slug}/question.md and answer.md."""
    parts = props.get("Slug", {}).get("rich_text", [])
    return "".join(p["plain_text"] for p in parts).strip()


def get_local_links(slug):
    """Return (question_link, answer_link) for local markdown files if they exist."""
    if not slug:
        return "", ""
    q_path = REPO_ROOT / "questions" / slug / "question.md"
    a_path = REPO_ROOT / "questions" / slug / "answer.md"
    q_link = f"[view](questions/{slug}/question.md)" if q_path.exists() else ""
    a_link = f"[view](questions/{slug}/answer.md)" if a_path.exists() else ""
    return q_link, a_link


def get_files(props, key, entry_name):
    files = props.get(key, {}).get("files", [])
    imgs = []
    for i, f in enumerate(files):
        url = f.get("file", {}).get("url") or f.get("external", {}).get("url")
        if not url:
            continue
        img_name = f"{entry_name}_{i}"
        local_path = download_image(url, img_name)
        if local_path:
            imgs.append(f"<img src='{local_path}' width='80'>")
    return " ".join(imgs) if imgs else ""


def build_readme(pages):
    lines = []
    lines.append("# Daily Brain Teaser\n")
    lines.append("> Auto-synced from Notion. Last updated: "
                 + datetime.utcnow().strftime("%Y-%m-%d %H:%M UTC") + "\n")
    lines.append("")
    lines.append("| # | Name | Type | Date | Redo | Solved | Preview | Question | Answer | Related | Comments |")
    lines.append("|---|------|------|------|------|--------|---------|----------|--------|---------|----------|")

    for i, page in enumerate(pages, 1):
        props = page["properties"]
        name = get_title(props, "Name")
        print(f"  Processing [{i}] {name}")

        type_badge  = get_multi_select(props, "Type", TYPE_COLORS)
        date        = get_date(props, "Date")
        redo        = get_number(props, "Redo times")
        solved      = get_checkbox(props, "Solved on my own")
        preview     = get_files(props, "Files & media", name)
        slug        = get_slug(props)
        local_q, local_a = get_local_links(slug)
        answer      = local_a if local_a else get_url(props, "answer")
        related     = get_multi_select(props, "related")
        comments    = get_text(props, "comments")

        row = f"| {i} | {name} | {type_badge} | {date} | {redo} | {solved} | {preview} | {local_q} | {answer} | {related} | {comments} |"
        lines.append(row)

    lines.append("")
    lines.append("---")
    lines.append("*Generated by [scripts/sync.py](scripts/sync.py) via GitHub Actions*")
    return "\n".join(lines) + "\n"


def main():
    print("Fetching from Notion...")
    pages = fetch_all_pages()
    print(f"Found {len(pages)} entries. Downloading images and building README...")
    content = build_readme(pages)
    readme_path = REPO_ROOT / "README.md"
    readme_path.write_text(content, encoding="utf-8")
    print(f"Done. README written to {readme_path}")


if __name__ == "__main__":
    main()
