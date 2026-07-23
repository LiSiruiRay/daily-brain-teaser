---
name: "The Cauchy Integral That Evaluates Itself"
type: "Complex Analysis"
tags: ["contour integration", "residue theorem", "trigonometric integrals", "unit circle substitution"]
date: "2026-07-23"
solved: false
comments: ""
related: []
redo: 0
difficulty: 3
source: "Stein & Shakarchi, Complex Analysis, Chapter 2 exercises; classical folklore"
---
# The Cauchy Integral That Evaluates Itself

Let $f$ be analytic on and inside a simple closed curve $\gamma$, and suppose $z_0$ is a point inside $\gamma$. Everyone knows the Cauchy integral formula:

$$f(z_0) = \frac{1}{2\pi i} \oint_\gamma \frac{f(z)}{z - z_0}\, dz.$$

Now use this to evaluate the following real integral in closed form:

$$I = \int_0^{2\pi} \frac{\cos\theta}{2 - \cos\theta}\, d\theta.$$

*Hint: think about what contour to use and what rational function of $e^{i\theta}$ appears.*
