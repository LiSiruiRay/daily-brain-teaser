---
name: "Gauss–Lucas Theorem"
type: "Complex Analysis"
tags: ["logarithmic derivative", "convex hull", "roots of derivatives", "separation theorem"]
date: "2026-06-11"
solved: false
comments: ""
related: []
redo: 0
difficulty: 3
source: "Mathematical folklore / Stein–Shakarchi Complex Analysis, standard graduate complex analysis"
---
# The Zeros of a Derivative via the Gauss–Lucas Theorem

Let $p(z) = (z-1)(z-2)(z-3)(z-4)$ be a degree-4 polynomial with all real roots at $1, 2, 3, 4$.

**(a)** The **Gauss–Lucas theorem** states: the zeros of $p'(z)$ all lie in the **convex hull** of the zeros of $p(z)$.

Without computing $p'(z)$ explicitly, use this theorem to locate the zeros of $p'(z)$.

**(b)** Now here is the surprise: prove the Gauss–Lucas theorem itself. That is, show that if $p(z)$ is any polynomial with zeros $z_1, \ldots, z_n \in \mathbb{C}$, then every zero of $p'(z)$ lies in the convex hull of $\{z_1, \ldots, z_n\}$.

**(Hint for (b)):** Write $\dfrac{p'(z)}{p(z)} = \sum_{k=1}^n \dfrac{1}{z - z_k}$ and think about what happens if $z$ is outside the convex hull.
