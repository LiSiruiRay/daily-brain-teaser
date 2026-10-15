---
name: "The Function That Cannot Explode at the Boundary"
type: "Complex Analysis"
tags: ["maximum modulus principle", "identity theorem", "zeros of holomorphic functions", "boundary behavior"]
date: "2026-10-15"
solved: false
comments: ""
related: []
redo: 0
difficulty: 2
source: "Folklore (classic application of the maximum modulus principle)"
---
# The Function That Cannot Explode at the Boundary

Let $\mathbb{D} = \{z \in \mathbb{C} : |z| < 1\}$ be the open unit disk.

In real analysis it is easy to blow up at the edge of a domain. For example, $g(x) = \dfrac{1}{1-x^2}$ is smooth on $(-1,1)$ and $g(x) \to \infty$ as $|x| \to 1$.

**Question.** Does there exist a holomorphic function $f : \mathbb{D} \to \mathbb{C}$ such that
$$
|f(z)| \to \infty \quad \text{as } |z| \to 1^- ?
$$
Here the limit means: for every $M > 0$ there is $r < 1$ such that $|f(z)| > M$ whenever $r < |z| < 1$.

Prove your answer.

*Hint (only if you are stuck):* What would $1/f$ look like near the boundary? What could go wrong in the interior?
