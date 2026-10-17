---
name: "Why π Is Less Than 22/7"
type: "Integration"
tags: ["polynomial division", "evaluation at i", "pi approximation", "Beta integral", "Putnam"]
date: "2026-10-17"
solved: false
comments: ""
related: []
redo: 0
difficulty: 2
source: "Putnam 1968 A1; D. P. Dalzell (1944)"
---
# Why π Is Less Than 22/7

Evaluate

$$
I \;=\; \int_0^1 \frac{x^4(1-x)^4}{1+x^2}\,dx .
$$

Then:

1. Explain why your answer proves the inequality $\pi < \dfrac{22}{7}$.
2. **(Bonus)** With one more line of work, show
$$
\frac{1}{1260} \;<\; \frac{22}{7}-\pi \;<\; \frac{1}{630}.
$$

*Hint to resist:* Try to predict the remainder of $x^4(1-x)^4$ modulo $x^2+1$ **without** doing long division.

---

**Field:** Integration / Real Analysis (with a pinch of algebra)

**Why it is interesting / classic:**
This is Putnam 1968 A1, and the identity goes back to D. P. Dalzell (1944). A positive integrand on $(0,1)$ produces exactly $22/7 - \pi$. That turns the schoolbook approximation of $\pi$ into a one-line rigorous inequality. The numerator looks arbitrary, but the exponent $4$ is the reason everything is rational except for a single $\pi$.

**Difficulty:** 2 / 5

**Tags:** polynomial division, evaluation at $i$, rational approximations of $\pi$, Beta integral
