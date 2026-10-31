---
name: "The Quartic That Folds onto Itself"
type: "Integration"
tags: ["substitution", "inversion symmetry", "x - 1/x trick", "integration bee"]
date: "2026-10-31"
solved: false
comments: ""
related: []
redo: 0
difficulty: 2
---
# The Quartic That Folds onto Itself

Evaluate

$$
I \;=\; \int_0^{\infty} \frac{dx}{1+x^4}.
$$

You may not use residues or the Beta function. Find a substitution argument that fits in a few lines.

**Bonus:** Use the same idea to evaluate

$$
\int_0^{\infty} \frac{x^2+1}{x^4+x^2+1}\,dx .
$$

---

**Field:** Integration (real-variable substitution tricks)

**Why it's interesting:** Partial fractions over $\mathbb{R}$ work here, but they are messy: $1+x^4=(x^2+\sqrt2x+1)(x^2-\sqrt2x+1)$, followed by logs and arctangents. The elegant route uses two ideas. The inversion $x\mapsto 1/x$ produces a "partner" integral equal to $I$. Adding the two creates an integrand that becomes a single arctangent after the substitution $u=x-\tfrac1x$. This "divide by $x^2$ and use $x\mp 1/x$" trick is a classic of integration bees.

**Difficulty:** 2 / 5

**Tags:** substitution, inversion symmetry, reciprocal substitution, integration bee
