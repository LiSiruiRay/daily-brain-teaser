import Link from "next/link";
import { getAllQuestions, typeColor } from "@/lib/questions";

export const revalidate = 3600;

export default function ArchivePage() {
  const questions = getAllQuestions();

  const types = Array.from(new Set(questions.map((q) => q.type).filter(Boolean))).sort();

  return (
    <div>
      <div className="mb-6 flex items-baseline justify-between">
        <h1 className="text-2xl font-bold text-slate-800">Archive</h1>
        <span className="text-sm text-slate-400">{questions.length} problems</span>
      </div>

      <div className="bg-white rounded-2xl border border-slate-200 overflow-hidden shadow-sm">
        <table className="w-full text-sm">
          <thead>
            <tr className="border-b border-slate-100 text-xs font-semibold text-slate-400 uppercase tracking-wide">
              <th className="text-left px-4 py-3 w-8">#</th>
              <th className="text-left px-4 py-3">Problem</th>
              <th className="text-left px-4 py-3 hidden sm:table-cell">Type</th>
              <th className="text-left px-4 py-3 hidden md:table-cell">Date</th>
              <th className="text-center px-4 py-3 w-16">✓</th>
              <th className="text-center px-4 py-3 w-12 hidden sm:table-cell">↩</th>
            </tr>
          </thead>
          <tbody>
            {questions.map((q, i) => (
              <tr
                key={q.slug}
                className="border-b border-slate-50 hover:bg-slate-50 transition-colors"
              >
                <td className="px-4 py-3 text-slate-300 text-xs">{questions.length - i}</td>
                <td className="px-4 py-3">
                  <Link
                    href={`/q/${q.slug}`}
                    className="font-medium text-slate-800 hover:text-blue-700"
                  >
                    {q.name}
                  </Link>
                  {q.comments && (
                    <p className="text-xs text-slate-400 mt-0.5 truncate max-w-xs">{q.comments}</p>
                  )}
                </td>
                <td className="px-4 py-3 hidden sm:table-cell">
                  {q.type && (
                    <span className={`text-xs px-2 py-0.5 rounded-full font-medium ${typeColor(q.type)}`}>
                      {q.type}
                    </span>
                  )}
                </td>
                <td className="px-4 py-3 text-slate-400 text-xs hidden md:table-cell">{q.date}</td>
                <td className="px-4 py-3 text-center">
                  {q.solved ? (
                    <span className="text-emerald-500 text-base">✓</span>
                  ) : (
                    <span className="text-slate-200">○</span>
                  )}
                </td>
                <td className="px-4 py-3 text-center text-slate-300 text-xs hidden sm:table-cell">
                  {q.redo > 0 ? q.redo : ""}
                </td>
              </tr>
            ))}
          </tbody>
        </table>
      </div>
    </div>
  );
}
