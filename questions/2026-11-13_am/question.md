---
name: "The Geometric Mean Is Superadditive"
type: "Putnam"
tags: ["inequalities", "AM-GM", "normalization", "homogeneity", "Minkowski determinant inequality"]
date: "2026-11-13"
solved: false
comments: ""
related: []
redo: 0
difficulty: 2
source: "64th William Lowell Putnam Competition (2003), A2; solutions by Bhargava, Kedlaya, Ng (materials/putnam/2003s.pdf)"
---
# The Geometric Mean Is Superadditive

Let $a_1,\dots,a_n$ and $b_1,\dots,b_n$ be nonnegative real numbers. Show that

$$
(a_1a_2\cdots a_n)^{1/n} + (b_1b_2\cdots b_n)^{1/n} \;\le\; \big[(a_1+b_1)(a_2+b_2)\cdots(a_n+b_n)\big]^{1/n}.
$$

When does equality hold?

*Hint:* A direct expansion gives a messy computation. Look for a normalization that turns the inequality into one you already know.

---

**Field:** Inequalities / Algebra (Putnam)

**Why it's interesting:** The statement says the geometric mean $G(x)=(x_1\cdots x_n)^{1/n}$ is superadditive on the nonnegative orthant: $G(a)+G(b)\le G(a+b)$. This mirrors Minkowski's inequality for norms, but the direction is reversed. There is a one-line proof once you see the right symmetry. The inequality also has a striking matrix generalization, the Minkowski determinant inequality $\det(A+B)^{1/n}\ge \det(A)^{1/n}+\det(B)^{1/n}$ for positive semidefinite $A,B$. Restricted to diagonal matrices, that matrix inequality is exactly this problem.

**Difficulty:** 2 / 5

**Source:** 64th William Lowell Putnam Competition (2003), Problem A2. Solutions by M. Bhargava, K. Kedlaya, L. Ng (`materials/putnam/2003s.pdf`).
