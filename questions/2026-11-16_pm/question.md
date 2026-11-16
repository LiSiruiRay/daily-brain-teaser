---
name: "Raising the Terms of a Convergent Series to the Power 1 − 1/n"
type: "analysis"
tags: ["series", "comparison test", "dichotomy trick", "weighted AM-GM", "sharpness"]
date: "2026-11-16"
solved: false
comments: ""
related: []
redo: 0
difficulty: 2
source: "Mathematical folklore"
---
# Raising the Terms of a Convergent Series to the Power $1-\tfrac1n$

Let $a_n > 0$ and suppose $\displaystyle\sum_{n=1}^\infty a_n$ converges.

Does
$$
\sum_{n=1}^\infty a_n^{\,1-\frac{1}{n}}
$$
necessarily converge?

Since $0<a_n<1$ eventually, each new term $a_n^{1-1/n}$ is **larger** than $a_n$. For example, if $a_n$ is tiny, then $a_n^{-1/n}$ can be huge. Can these enlargements add up to a divergent series?

*(Bonus: what happens if $1-\frac1n$ is replaced by $1-\frac{1}{\sqrt n}$? By $1-\frac{1}{\log\log n}$?)*
