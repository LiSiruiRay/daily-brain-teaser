import { getTodayQuestions } from "@/lib/questions";
import QuestionCard from "@/components/QuestionCard";

// Re-render on every request so "today" is always current
export const dynamic = "force-dynamic";

const DAY_SCHEDULE: Record<number, string> = {
  0: "Analysis (Stein / Rudin)",
  1: "Topology / Algebra",
  2: "Probability puzzle",
  3: "Complex Analysis / Differential Geometry",
  4: "Putnam / fun problems",
  5: "Integration bee",
  6: "ML / statistics insight",
};

function todayLabel(): { dateStr: string; schedule: string } {
  const now = new Date();
  const dateStr = now.toLocaleDateString("en-US", {
    timeZone: "America/New_York",
    weekday: "long",
    year: "numeric",
    month: "long",
    day: "numeric",
  });
  const dow = parseInt(
    now.toLocaleDateString("en-CA", { timeZone: "America/New_York", weekday: undefined })
  );
  // get weekday index (0=Sun in JS, but we want 0=Mon)
  const jsDay = new Date(
    new Date().toLocaleDateString("en-CA", { timeZone: "America/New_York" })
  ).getDay();
  const schedule = DAY_SCHEDULE[jsDay === 0 ? 6 : jsDay - 1] ?? "";
  return { dateStr, schedule };
}

export default function HomePage() {
  const { am, pm } = getTodayQuestions();
  const { dateStr, schedule } = todayLabel();

  return (
    <div>
      {/* Date header */}
      <div className="mb-6">
        <h1 className="text-2xl font-bold text-slate-800">{dateStr}</h1>
        <p className="text-sm text-slate-500 mt-1">Today's topic: {schedule}</p>
      </div>

      <div className="flex flex-col gap-6">
        {/* AM slot */}
        {am ? (
          <QuestionCard question={am} slot="AM" />
        ) : (
          <div className="bg-white rounded-2xl border border-dashed border-slate-200 px-6 py-10 text-center text-slate-400">
            <p className="text-sm font-medium">AM question not yet generated</p>
            <p className="text-xs mt-1">Scheduled for 4:00 AM ET</p>
          </div>
        )}

        {/* PM slot */}
        {pm ? (
          <QuestionCard question={pm} slot="PM" />
        ) : (
          <div className="bg-white rounded-2xl border border-dashed border-slate-200 px-6 py-10 text-center text-slate-400">
            <p className="text-sm font-medium">PM question not yet generated</p>
            <p className="text-xs mt-1">Scheduled for 4:00 PM ET</p>
          </div>
        )}
      </div>

      <p className="text-center text-xs text-slate-400 mt-8">
        Questions generated automatically twice a day ·{" "}
        <a href="/archive" className="underline hover:text-slate-600">
          browse the archive →
        </a>
      </p>
    </div>
  );
}
