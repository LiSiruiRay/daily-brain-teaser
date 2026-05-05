"use client";

import { useState } from "react";
import Link from "next/link";
import MathContent from "./MathContent";
import { Question, typeColor } from "@/lib/types";

interface Props {
  question: Question;
  slot?: "AM" | "PM";
  defaultOpen?: boolean;
}

export default function QuestionCard({ question, slot, defaultOpen = false }: Props) {
  const [showAnswer, setShowAnswer] = useState(defaultOpen);

  const difficultyDots = Array.from({ length: 5 }, (_, i) => (
    <span
      key={i}
      className={`inline-block w-2 h-2 rounded-full mr-0.5 ${
        i < question.difficulty ? "bg-slate-600" : "bg-slate-200"
      }`}
    />
  ));

  return (
    <div className="bg-white rounded-2xl border border-slate-200 shadow-sm overflow-hidden">
      {/* Card header */}
      <div className="px-6 py-4 border-b border-slate-100 flex items-start justify-between gap-4">
        <div className="flex-1 min-w-0">
          <div className="flex items-center gap-2 mb-1">
            {slot && (
              <span className="text-xs font-semibold tracking-widest text-slate-400 uppercase">
                {slot}
              </span>
            )}
            <span
              className={`text-xs font-medium px-2 py-0.5 rounded-full ${typeColor(question.type)}`}
            >
              {question.type}
            </span>
            {question.solved && (
              <span className="text-xs font-medium px-2 py-0.5 rounded-full bg-emerald-100 text-emerald-700">
                ✓ solved
              </span>
            )}
          </div>
          <Link
            href={`/q/${question.slug}`}
            className="text-lg font-semibold text-slate-800 hover:text-blue-700 leading-snug"
          >
            {question.name}
          </Link>
          <div className="flex items-center gap-3 mt-1">
            <span className="text-xs text-slate-400">{question.date}</span>
            {question.difficulty > 0 && (
              <span className="flex items-center gap-0.5">{difficultyDots}</span>
            )}
          </div>
        </div>
        <a
          href={`https://github.com/LiSiruiRay/brain_teaser/edit/main/questions/${question.slug}/question.md`}
          target="_blank"
          rel="noopener noreferrer"
          className="shrink-0 text-xs text-slate-300 hover:text-slate-500 mt-1"
          title="Edit metadata on GitHub"
        >
          ✏︎
        </a>
      </div>

      {/* Question body */}
      <div className="px-6 py-5">
        <MathContent>{question.questionContent}</MathContent>
      </div>

      {/* Tags */}
      {question.tags.length > 0 && (
        <div className="px-6 pb-4 flex flex-wrap gap-1">
          {question.tags.map((t) => (
            <span key={t} className="text-xs px-2 py-0.5 rounded bg-slate-100 text-slate-500">
              {t}
            </span>
          ))}
        </div>
      )}

      {/* Reveal toggle */}
      <div className="px-6 pb-5">
        <button
          onClick={() => setShowAnswer((v) => !v)}
          className="w-full py-2 rounded-lg border border-slate-200 text-sm font-medium text-slate-600 hover:bg-slate-50 hover:border-slate-300 transition-colors"
        >
          {showAnswer ? "Hide Answer ↑" : "Reveal Answer ↓"}
        </button>
      </div>

      {/* Answer */}
      {showAnswer && (
        <div className="border-t border-slate-100 bg-slate-50 px-6 py-5">
          <MathContent>{question.answerContent}</MathContent>
          {question.source && (
            <p className="mt-4 text-xs text-slate-400 italic">Source: {question.source}</p>
          )}
        </div>
      )}

      {/* Personal notes */}
      {question.comments && (
        <div className="border-t border-slate-100 px-6 py-3 bg-yellow-50">
          <p className="text-xs text-yellow-700">
            <span className="font-semibold">Notes: </span>
            {question.comments}
          </p>
        </div>
      )}
    </div>
  );
}
