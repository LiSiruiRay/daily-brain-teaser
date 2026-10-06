---
name: "Vanishing Fourier Coefficients Force Zero"
type: "analysis"
tags: ["Fourier series", "Weierstrass approximation", "orthogonality", "density argument", "continuous functions"]
date: "2026-10-05"
solved: false
comments: ""
related: []
redo: 0
difficulty: 3
---
# The Fourier Series That Oversteps Its Bounds

Let $f: [0, 2\pi] \to \mathbb{R}$ be a continuous, $2\pi$-periodic function. Suppose that all of its Fourier coefficients vanish:
$$\hat{f}(n) = \frac{1}{2\pi}\int_0^{2\pi} f(x)\, e^{-inx}\, dx = 0 \quad \text{for all } n \in \mathbb{Z}.$$

Prove that $f \equiv 0$.

*(No advanced machinery allowed — no $L^2$ completeness, no Plancherel. Use only the tools of basic analysis.)*
