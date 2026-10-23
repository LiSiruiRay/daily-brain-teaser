# Answer: Four Random Points on a Sphere: Tetrahedron Contains the Center

## Key Idea / Intuition

Choose a point on the sphere in two stages. First pick a random diameter. Then flip a fair coin to decide which endpoint to use. Fix the diameters for $P_1, P_2, P_3$ and the point $P_4$. Among the $2^3 = 8$ equally likely ways of choosing endpoints, **exactly one** gives a tetrahedron that contains the center. The probability is therefore $1/8$, and no integration is needed. The same argument gives $1/4$ on the circle and $1/2^n$ for $n+1$ points on $S^{n-1}$.

---

## Formal Proof / Solution

**Answer:** $\dfrac{1}{8}$.

**Step 1: Re-randomize.**
Let $Q_1, Q_2, Q_3$ be independent uniform points on $S^2$. Let $\varepsilon_1, \varepsilon_2, \varepsilon_3$ be independent fair $\pm 1$ signs, and let $P_4$ be uniform. All of these are independent. Set
$$P_i = \varepsilon_i Q_i, \qquad i = 1, 2, 3.$$
The uniform measure on $S^2$ is invariant under $x \mapsto -x$, so each $P_i$ is again uniform. All four points are independent, so $(P_1, \dots, P_4)$ has exactly the distribution in the problem.

We condition on $Q_1, Q_2, Q_3, P_4$. We will show that, almost surely, exactly one of the 8 sign patterns $(\varepsilon_1, \varepsilon_2, \varepsilon_3)$ produces a tetrahedron containing the origin $O$.

**Step 2: Reformulate "contains the center".**
With probability $1$:
- $Q_1, Q_2, Q_3$ are linearly independent, and
- no three of the four points lie on a plane through $O$.

Both failures happen on measure-zero sets. From now on we assume this generic situation.

$O$ lies in the tetrahedron exactly when there are weights $\lambda_1, \dots, \lambda_4 \ge 0$ with $\sum \lambda_i = 1$ and $\sum \lambda_i P_i = 0$.

- **All weights are positive.** If some $\lambda_j = 0$, then $O$ lies in the convex hull of the other three points, so those three lie on a plane through $O$. This is excluded by genericity, so every $\lambda_i > 0$.
- **Divide by $\lambda_4$.** Then $O$ lies in the tetrahedron iff
$$-P_4 = a_1 P_1 + a_2 P_2 + a_3 P_3 \quad \text{for some } a_1, a_2, a_3 > 0.$$
- **Converse.** If such $a_i > 0$ exist, then $P_4 + \sum a_i P_i = 0$. Dividing by $1 + a_1 + a_2 + a_3$ gives valid convex weights.

**Step 3: Exactly one sign pattern works.**
Since $Q_1, Q_2, Q_3$ form a basis of $\mathbb{R}^3$, there is a unique expansion
$$-P_4 = c_1 Q_1 + c_2 Q_2 + c_3 Q_3.$$
Each $c_i \neq 0$. Indeed, if $c_3 = 0$, then $P_4$ would lie in the plane spanned by $Q_1, Q_2$, which passes through $O$. That is excluded by genericity, and the same holds for $c_1, c_2$.

Now substitute $P_i = \varepsilon_i Q_i$:
$$-P_4 = \sum_i (c_i \varepsilon_i)\, P_i,$$
and by uniqueness these are the only possible coefficients. By Step 2, the tetrahedron contains $O$ iff all $c_i \varepsilon_i > 0$, that is, iff
$$\varepsilon_i = \operatorname{sign}(c_i) \quad \text{for } i = 1, 2, 3.$$
Exactly one of the 8 sign patterns satisfies this.

**Step 4: Conclude.**
Conditionally on $Q_1, Q_2, Q_3, P_4$, the signs are uniform on $\{\pm 1\}^3$, so the conditional probability is $1/8$. Averaging over the conditioning variables gives
$$\Pr(O \in \text{tetrahedron}) = \frac{1}{8}.$$

**Warm-up (circle).** The identical argument with two diameters and one free point gives $1/2^2 = 1/4$.

**Generalization.** For $n+1$ uniform points on $S^{n-1} \subset \mathbb{R}^n$, the simplex contains the center with probability $1/2^n$.

---

**Why it's beautiful.**
- A direct computation would mean integrating areas of spherical triangles, which is messy. The symmetry $x \mapsto -x$ turns the problem into counting sign patterns.
- Linear algebra (a unique expansion in a basis) does all the geometric work.
- The answer generalizes to every dimension at once.

**Difficulty:** 3/5.

**Source:** Putnam 1992, Problem A6 (see `materials/putnam/1992.pdf`).
