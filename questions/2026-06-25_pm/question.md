---
name: "Riemann's Removable Singularity via zf(z)→0"
type: "Complex Analysis"
tags: ["removable singularity", "holomorphic extension", "Taylor series", "Riemann's theorem"]
date: "2026-06-25"
solved: false
comments: ""
related: []
redo: 0
difficulty: 2
source: "Complex Analysis, Stein & Shakarchi, Chapter 2"
---
# Riemann's Removable Singularity Theorem: A Minimal Condition

Let $f$ be holomorphic on the punctured disk $D'(0, r) = \{z : 0 < |z| < r\}$. 

Suppose that 
$$\lim_{z \to 0} z \cdot f(z) = 0.$$

Prove that the singularity at $z = 0$ is removable — that is, $f$ extends to a holomorphic function on the full disk $D(0, r)$.

**Hint:** Define a new function $g(z) = z^2 f(z)$ (set $g(0) = 0$), and think about what it means for $g$ to be complex-differentiable at $z = 0$.
