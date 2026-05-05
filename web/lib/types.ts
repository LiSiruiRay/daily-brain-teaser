export interface Question {
  slug: string;
  name: string;
  type: string;
  tags: string[];
  date: string;
  difficulty: number;
  solved: boolean;
  comments: string;
  related: string[];
  redo: number;
  source: string;
  questionContent: string;
  answerContent: string;
}

export const TYPE_COLOR: Record<string, string> = {
  "Integration":            "bg-blue-100 text-blue-800",
  "ML/Stats":               "bg-orange-100 text-orange-800",
  "analysis":               "bg-purple-100 text-purple-800",
  "algebra":                "bg-green-100 text-green-800",
  "topology":               "bg-cyan-100 text-cyan-800",
  "Probability":            "bg-yellow-100 text-yellow-800",
  "Complex Analysis":       "bg-red-100 text-red-800",
  "Differential Geometry":  "bg-pink-100 text-pink-800",
  "Putnam":                 "bg-amber-100 text-amber-800",
};

export function typeColor(type: string): string {
  return TYPE_COLOR[type] ?? "bg-gray-100 text-gray-700";
}
