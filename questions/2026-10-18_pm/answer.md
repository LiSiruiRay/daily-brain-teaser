# Answer: Ridge Regression with Cloned Features

## Key Idea / Intuition

The loss sees only the **sum** $s = \beta_1 + \cdots + \beta_m$, because every column is the same vector $x$. So the problem splits into two steps:

1. For a fixed total effect $s$, find the cheapest way to split it among the $m$ copies under the penalty.
2. Optimize over $s$.

The $\ell_2$ penalty is strictly convex, so it prefers spreading the effect evenly. An even split costs only $s^2/m$, which means cloning a feature divides its effective ridge penalty by $m$. The $\ell_1$ penalty does not care how the effect is split, as long as all parts have the same sign. Hence the lasso solution is not unique.

---

## Formal Proof / Solution

### (a) Ridge

**Symmetry argument for equal coefficients.**

- Since $\lambda>0$, the objective $F(\beta) = \|y - X\beta\|^2 + \lambda\|\beta\|^2$ is strictly convex. It therefore has a unique minimizer $\hat\beta$.
- Permuting the coordinates of $\beta$ permutes identical columns of $X$. This leaves both $X\beta$ and $\|\beta\|^2$ unchanged, so $F(\sigma\beta) = F(\beta)$ for every permutation $\sigma$.
- Hence $\sigma\hat\beta$ is also a minimizer. By uniqueness, $\sigma\hat\beta = \hat\beta$ for all $\sigma$.
- Therefore all coordinates are equal: $\hat\beta_1 = \cdots = \hat\beta_m =: b$.

**Reduction to one variable.**

Write $s = \sum_i \beta_i$. Then $X\beta = x s$.

For fixed $s$, the Cauchy–Schwarz (or QM–AM) inequality gives
$$\sum_{i=1}^m \beta_i^2 \;\ge\; \frac{s^2}{m},$$
with equality iff all $\beta_i = s/m$. This confirms the even split directly. The problem then becomes
$$\min_s\ \|y - xs\|^2 + \frac{\lambda}{m}\, s^2 .$$

This is single-feature ridge with penalty $\lambda/m$. Its solution is
$$\hat s = \frac{x^\top y}{x^\top x + \lambda/m}.$$

**Answer.**
$$\boxed{\hat\beta_1 = \cdots = \hat\beta_m = \frac{x^\top y}{m\,x^\top x + \lambda}}, \qquad \sum_i \hat\beta_i = \frac{x^\top y}{x^\top x + \lambda/m}.$$

For example, with $m=2$ each copy gets $\dfrac{x^\top y}{2x^\top x + \lambda}$.

**Interpretation.**

- Cloning a feature $m$ times is equivalent to fitting the original feature with ridge parameter $\lambda/m$.
- Duplication therefore weakens shrinkage. The fitted total effect moves from $a$ toward the OLS value $x^\top y / x^\top x$, and reaches it as $m \to \infty$.
- Practical consequence: ridge is not invariant to redundant features. Highly correlated groups of predictors are collectively shrunk less, and their coefficients are spread evenly across the group. This is the "grouping effect".

### (b) Lasso

For fixed $s$, the triangle inequality gives
$$\sum_i |\beta_i| \ge |s|,$$
with equality iff all nonzero $\beta_i$ share the sign of $s$.

The problem therefore reduces to
$$\min_s \|y - xs\|^2 + \lambda |s|,$$
which is the single-feature lasso with the **same** $\lambda$. Its solution is
$$\hat s = \frac{\operatorname{sign}(x^\top y)\,\big(|x^\top y| - \lambda/2\big)_+}{x^\top x}.$$

Conclusions:

- The total effect is unchanged by duplication.
- Any split $\beta_i = w_i \hat s$ with $w_i \ge 0$ and $\sum_i w_i = 1$ is optimal. For $\hat s \ne 0$ and $m \ge 2$ this is a whole simplex of solutions, so the solution is **not unique**.
- In practice, an algorithm such as coordinate descent typically picks one copy arbitrarily and sets the others to zero.

This contrast motivates the **elastic net**. Adding a small $\ell_2$ term restores strict convexity. The symmetry argument above then forces equal coefficients on identical features, recovering the grouping effect.

*Reference: Hastie, Tibshirani & Friedman, *The Elements of Statistical Learning* (2nd ed.), Exercise 3.29 (ridge with an exact copy of a variable); see also §3.4.1 and the elastic net discussion in §18.4.*
