// Server-only: uses Node.js `fs`. Never import this in a "use client" component.
import fs from "fs";
import path from "path";
import matter from "gray-matter";
import type { Question } from "./types";

export type { Question } from "./types";
export { typeColor, TYPE_COLOR } from "./types";

// questions/ lives one level above web/
const QUESTIONS_DIR = path.join(process.cwd(), "..", "questions");

function parseFrontmatter(filePath: string): { data: Record<string, unknown>; content: string } {
  if (!fs.existsSync(filePath)) return { data: {}, content: "" };
  const raw = fs.readFileSync(filePath, "utf-8");
  const { data, content } = matter(raw);
  return { data, content: content.trim() };
}

export function getQuestion(slug: string): Question | null {
  const qPath = path.join(QUESTIONS_DIR, slug, "question.md");
  const aPath = path.join(QUESTIONS_DIR, slug, "answer.md");
  if (!fs.existsSync(qPath)) return null;

  const { data: fm, content: qContent } = parseFrontmatter(qPath);
  const { content: aContent } = parseFrontmatter(aPath);

  return {
    slug,
    name:            (fm.name as string)      ?? slug,
    type:            (fm.type as string)      ?? "",
    tags:            (fm.tags as string[])    ?? [],
    date:            (fm.date as string)      ?? "",
    difficulty:      (fm.difficulty as number) ?? 0,
    solved:          (fm.solved as boolean)   ?? false,
    comments:        (fm.comments as string)  ?? "",
    related:         (fm.related as string[]) ?? [],
    redo:            (fm.redo as number)      ?? 0,
    source:          (fm.source as string)    ?? "",
    questionContent: qContent,
    answerContent:   aContent,
  };
}

export function getAllSlugs(): string[] {
  const listPath = path.join(QUESTIONS_DIR, "Problem_list.md");
  const text = fs.readFileSync(listPath, "utf-8");
  const slugs: string[] = [];
  for (const line of text.split("\n")) {
    const m = line.match(/\[.+?\]\((.+?)\/question\.md\)/);
    if (m) slugs.push(m[1]);
  }
  return slugs;
}

export function getAllQuestions(): Question[] {
  return getAllSlugs()
    .map((slug) => getQuestion(slug))
    .filter((q): q is Question => q !== null)
    .sort((a, b) => b.date.localeCompare(a.date));
}

function todayET(): string {
  return new Date().toLocaleDateString("en-CA", { timeZone: "America/New_York" });
}

export function getTodayQuestions(): { am: Question | null; pm: Question | null } {
  const today = todayET();
  return {
    am: getQuestion(`${today}_am`),
    pm: getQuestion(`${today}_pm`),
  };
}
