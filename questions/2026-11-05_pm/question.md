---
name: "Iterates Cannot Escape Fixed Points"
type: "Complex Analysis"
tags: ["Picard's little theorem", "fixed points", "iteration", "entire functions", "open mapping theorem"]
date: "2026-11-05"
solved: false
comments: ""
related: []
redo: 0
difficulty: 4
source: "P. C. Rosenbloom, 'The fix-points of entire functions' (1952); complex analysis folklore"
---
# Iterates Cannot Escape Fixed Points

An entire function can easily have **no fixed points**. For example,
$$
f(z) = z + e^z
$$
satisfies $f(z) = z \iff e^z = 0$, which never happens.

Now look at the second iterate $f\circ f$.

**Problem.** Let $f:\mathbb{C}\to\mathbb{C}$ be entire. Prove that $f\circ f$ has **no** fixed point if and only if
$$
f(z) = z + b \quad\text{for some constant } b \neq 0 .
$$

In particular, for $f(z) = z + e^z$, the function $f(f(z))$ must have a fixed point, even though $f$ has none.

*You may use Picard's little theorem:* a non-constant entire function omits at most one complex value.

---

**Field:** Complex Analysis

**Why it's interesting:** The statement is surprising: fixed-point-freeness of $f$ is common, but it does not survive iteration, except for translations. The proof applies Picard's theorem twice. Each time, the key step is to build the right auxiliary function that omits two values.

**Difficulty:** 4 / 5
