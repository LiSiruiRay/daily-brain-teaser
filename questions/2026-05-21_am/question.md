---
name: "Logarithmic Derivative and Integrality of Winding"
type: "Complex Analysis"
tags: ["winding number", "logarithmic derivative", "argument principle", "contour integral", "complex logarithm"]
date: "2026-05-21"
solved: false
comments: ""
related: []
redo: 0
difficulty: 2
source: "Stein & Shakarchi, Complex Analysis, Chapter 3"
---
# The Argument of a Product: Winding and the Logarithm

Let $f(z) = z^n$ for a positive integer $n$. As $z$ traverses the unit circle $|z| = 1$ once counterclockwise (from $z = 1$ back to $z = 1$), by how much does $\arg f(z)$ increase in total?

Now consider the more general question: suppose $f : \mathbb{C} \to \mathbb{C}$ is analytic and nonvanishing on a closed curve $\gamma$. Express the **total change in argument** of $f$ along $\gamma$ in terms of a contour integral involving $f'/f$.

Use this to prove:

$$\frac{1}{2\pi i} \oint_\gamma \frac{f'(z)}{f(z)}\, dz \in \mathbb{Z}$$

for any closed curve $\gamma$ on which $f$ is analytic and nonvanishing.
