/** @type {import('tailwindcss').Config} */
module.exports = {
  content: ["./app/**/*.{ts,tsx}", "./components/**/*.{ts,tsx}"],
  theme: {
    extend: {
      typography: {
        DEFAULT: {
          css: {
            maxWidth: "none",
            code: { backgroundColor: "#f1f5f9", borderRadius: "0.25rem", padding: "0.1em 0.3em" },
            "code::before": { content: '""' },
            "code::after":  { content: '""' },
          },
        },
      },
    },
  },
  plugins: [],
};
