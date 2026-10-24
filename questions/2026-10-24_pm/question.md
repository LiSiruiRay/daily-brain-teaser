---
name: "Lobachevsky's Folding Trick"
type: "Integration"
tags: ["integration bee", "Lobachevsky integral formula", "periodic folding", "partial fractions of cosecant", "Mittag-Leffler", "conditionally convergent integral"]
date: "2026-10-24"
solved: false
comments: ""
related: []
redo: 0
difficulty: 4
---
# Lobachevsky's Folding Trick

Evaluate

$$
I=\int_0^\infty \frac{\sin x}{x}\cdot\frac{1}{1+\cos^2 x}\,dx .
$$

*Bonus.* Show more generally that if $f$ is continuous, $\pi$-periodic, and satisfies $f(\pi-x)=f(x)$, then

$$
\int_0^\infty \frac{\sin x}{x}\,f(x)\,dx=\int_0^{\pi/2} f(x)\,dx .
$$

As a check, $f\equiv 1$ gives the Dirichlet integral $\pi/2$.

*Hint.* You may use the partial fraction expansion of the cosecant:
$$
\frac{1}{\sin u}=\sum_{m\in\mathbb Z}\frac{(-1)^m}{u+m\pi},
$$
where the sum is taken symmetrically.
