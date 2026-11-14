---
name: "The Integral That Doesn't Notice x − 1/x"
type: "Integration"
tags: ["Glasser master theorem", "Cauchy–Schlömilch substitution", "Vieta's formulas", "measure-preserving map", "integration bee"]
date: "2026-11-14"
solved: false
comments: ""
related: []
redo: 0
difficulty: 2
source: "Folklore; M. L. Glasser, 'A Remarkable Property of Definite Integrals', Math. Comp. 40 (1983)"
---
# The Integral That Doesn't Notice $x - 1/x$

Evaluate

$$
I \;=\; \int_{-\infty}^{\infty} \frac{x^2}{x^4 - x^2 + 1}\,dx .
$$

You could factor the quartic and use partial fractions, or use residues. Try instead to find a solution that needs no factoring at all.

**Hint (only if stuck):** Divide the numerator and the denominator by $x^2$.

**Follow-up:** Show that for every integrable $f:\mathbb{R}\to\mathbb{R}$,

$$
\int_{-\infty}^{\infty} f\!\left(x - \frac1x\right)dx \;=\; \int_{-\infty}^{\infty} f(u)\,du .
$$

This identity is known as the Cauchy–Schlömilch transformation, a special case of Glasser's Master Theorem.

---

- **Field:** Integration / Real analysis
- **Why it's interesting:** The integrand looks like a partial-fractions exercise. It is really the Cauchy density $\frac{1}{1+u^2}$ composed with $u = x - 1/x$, and that map preserves Lebesgue measure on $\mathbb{R}$. The proof of this is a short application of Vieta's formulas.
- **Difficulty:** 2 / 5
