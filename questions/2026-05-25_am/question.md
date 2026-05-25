---
name: "Lebesgue Differentiation: Failure Everywhere?"
type: "analysis"
tags: ["Lebesgue differentiation theorem", "measure theory", "averaging", "null sets", "Lebesgue points"]
date: "2026-05-25"
solved: false
comments: ""
related: []
redo: 0
difficulty: 2
---
# The Lebesgue Differentiation Theorem: A Failure of Averaging?

Let $f: \mathbb{R} \to \mathbb{R}$ be a bounded measurable function. The Lebesgue Differentiation Theorem tells us that for **almost every** $x$,

$$\lim_{r \to 0} \frac{1}{2r} \int_{x-r}^{x+r} f(t)\, dt = f(x).$$

Now consider the following question:

**Can this fail at every point?** That is, does there exist a bounded measurable function $f: \mathbb{R} \to \mathbb{R}$ such that

$$\lim_{r \to 0} \frac{1}{2r} \int_{x-r}^{x+r} f(t)\, dt \neq f(x)$$

for **every** $x \in \mathbb{R}$?

Give a definitive yes/no answer and justify it briefly. If no, can you construct the "most extreme" example — a function where the averaging limit *exists* everywhere but equals a different function?

**Bonus:** What if we replace the symmetric interval $[x-r, x+r]$ with a non-symmetric shrinking interval? Can the limit change?
