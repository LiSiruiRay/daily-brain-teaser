---
name: "How Fast Does Iterated Sine Die?"
type: "analysis"
tags: ["sequences", "asymptotics", "Stolz-Cesaro", "Taylor expansion", "iteration"]
date: "2026-10-26"
solved: false
comments: ""
related: []
redo: 0
difficulty: 2
source: "Classical folklore (cf. Pólya–Szegő, Problems and Theorems in Analysis I)"
---
# How Fast Does Iterated Sine Die?

Pick any $x_0 \in (0, \pi)$ and define

$$
x_{n+1} = \sin x_n, \qquad n \ge 0.
$$

1. Show that $x_n \to 0$.
2. **Main question:** Find the exact rate. Prove that

$$
\lim_{n\to\infty} \sqrt{n}\, x_n = \sqrt{3},
$$

independently of the starting point $x_0$.

*Hint (only if stuck):* Rather than tracking $x_n$ directly, look for a function $g$ such that $g(x_{n+1}) - g(x_n)$ tends to a nonzero constant.

---

**Field:** Real analysis (sequences, asymptotics)

**Why it's interesting:** Press the `sin` key on a calculator over and over. The display creeps toward $0$, but very slowly. Since $\sin x \approx x$ near $0$, each step barely moves the point. The surprise is that this slow decay has a sharp, universal law. Every starting point ends up with $x_n \sim \sqrt{3/n}$, and the constant $3$ comes straight from the $x^3/6$ term of the Taylor series. The problem shows a general idea: to find the decay rate of a slowly converging iteration, change variables until the iteration becomes approximately "add a constant."

**Key technique:** Find a quantity that grows linearly. Then apply Stolz–Cesàro (Cesàro averaging of increments).

**Difficulty:** 2 / 5
