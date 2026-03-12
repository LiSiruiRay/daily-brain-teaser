# The Schwarz Lemma

**Type:** Complex Analysis
**Tags:** Maximum modulus principle, Holomorphic functions, Unit disk, Conformal maps
**Date:** 2026-03-12
**Difficulty:** 3/5

**Why it's beautiful:**
The Schwarz Lemma says that any holomorphic self-map of the unit disk fixing the origin must be a *contraction* — it can only shrink distances. And the only maps that preserve distances exactly are rotations. The proof uses just one trick: divide by $z$ and apply the maximum modulus principle. Short, surprising, and foundational in complex analysis.

---

## Problem

Let $\mathbb{D} = \{z \in \mathbb{C} : |z| < 1\}$ be the open unit disk.

Suppose $f : \mathbb{D} \to \mathbb{D}$ is holomorphic and $f(0) = 0$.

**Prove that $|f(z)| \leq |z|$ for all $z \in \mathbb{D}$.**

**Bonus:** Show that if equality holds at any single point $z_0 \neq 0$, then $f$ must be a rotation: $f(z) = e^{i\theta} z$ for some $\theta \in \mathbb{R}$.

---

*Hint: Consider the function $g(z) = f(z)/z$. What can you say about it?*
