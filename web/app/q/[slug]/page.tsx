import { notFound } from "next/navigation";
import Link from "next/link";
import { getAllSlugs, getQuestion, typeColor } from "@/lib/questions";
import QuestionCard from "@/components/QuestionCard";

export async function generateStaticParams() {
  return getAllSlugs().map((slug) => ({ slug }));
}

export const revalidate = 3600;

export default function QuestionPage({ params }: { params: { slug: string } }) {
  const question = getQuestion(params.slug);
  if (!question) notFound();

  return (
    <div>
      <div className="mb-4">
        <Link href="/archive" className="text-sm text-slate-400 hover:text-slate-600">
          ← Archive
        </Link>
      </div>

      <QuestionCard question={question} defaultOpen />

      {/* Metadata footer */}
      <div className="mt-4 flex flex-wrap gap-3 text-xs text-slate-400">
        <span>
          <strong>Type:</strong>{" "}
          <span className={`px-2 py-0.5 rounded-full font-medium ${typeColor(question.type)}`}>
            {question.type}
          </span>
        </span>
        {question.source && <span><strong>Source:</strong> {question.source}</span>}
        <a
          href={`https://github.com/LiSiruiRay/brain_teaser/edit/main/questions/${question.slug}/question.md`}
          target="_blank"
          rel="noopener noreferrer"
          className="ml-auto underline hover:text-slate-600"
        >
          Edit on GitHub ↗
        </a>
      </div>
    </div>
  );
}
