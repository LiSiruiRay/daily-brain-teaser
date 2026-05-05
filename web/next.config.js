const path = require("path");

/** @type {import('next').NextConfig} */
const nextConfig = {
  // Allow Next.js to trace files from the parent repo directory (questions/)
  experimental: {
    outputFileTracingRoot: path.join(__dirname, "../"),
  },
};

module.exports = nextConfig;
