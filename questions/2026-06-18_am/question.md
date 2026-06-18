---
name: "Argument of a Product Along a Circle"
type: "Complex Analysis"
tags: ["logarithmic derivative", "argument principle", "residue theorem", "winding number", "polynomials"]
date: "2026-06-18"
solved: false
comments: ""
related: []
redo: 0
difficulty: 2
source: "Stein & Shakarchi, Complex Analysis, Chapter 3"
---
# The Argument of a Product Along a Circle

Let $f(z) = z^n + a_{n-1}z^{n-1} + \cdots + a_0$ be a monic polynomial of degree $n \geq 1$ with complex coefficients. 

Consider the integral
$$I = \frac{1}{2\pi i} \int_{|z|=R} \frac{f'(z)}{f(z)}\, dz$$
for $R$ large enough that all zeros of $f$ lie inside $|z| < R$.

**Without using the Argument Principle as a black box**, prove from first principles (using partial fractions and residues) that $I = n$.

Then use this to conclude: as $z$ traverses the circle $|z| = R$ once counterclockwise, the argument of $f(z)$ increases by exactly $2\pi n$.
