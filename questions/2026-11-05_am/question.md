---
name: "Injective Entire Functions Are Linear"
type: "Complex Analysis"
tags: ["singularity at infinity", "Casorati-Weierstrass", "open mapping theorem", "automorphisms of C", "entire functions"]
date: "2026-11-05"
solved: false
comments: ""
related: []
redo: 0
difficulty: 3
source: "Stein & Shakarchi, Complex Analysis, Chapter 3, Exercise 14"
---
# Injective Entire Functions Are Linear

Let $f:\mathbb{C}\to\mathbb{C}$ be an **entire** function that is **injective**.

Prove that $f$ must be affine:
$$
f(z) = az + b \qquad \text{for some } a,b\in\mathbb{C},\ a\neq 0.
$$

*Corollary to keep in mind:* the biholomorphic automorphisms of $\mathbb{C}$ are exactly the maps $z\mapsto az+b$.

*Hint (if you want one):* study the behavior of $f$ near $\infty$, that is, the singularity of $g(w)=f(1/w)$ at $w=0$. Which of the three singularity types are compatible with injectivity?
