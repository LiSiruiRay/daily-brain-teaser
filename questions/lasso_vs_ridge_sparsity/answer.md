# Answer: Why Does LASSO Produce Sparse Solutions but Ridge Does Not?

## Key Idea

The $L^1$ ball has **corners on the coordinate axes**. The $L^2$ ball is a smooth sphere with **no corners**. The optimal constrained solution is found where the loss level set first touches the constraint region — and touching a corner forces a coordinate to be exactly zero.

---

## Geometric Argument

The constrained problem is equivalent (by Lagrange duality) to the penalized form:

$$\min_\beta \, L(\beta) + \lambda \|\beta\|_1 \quad \text{vs} \quad \min_\beta \, L(\beta) + \lambda \|\beta\|_2^2$$

Think of "inflating" the level sets of $L$ outward from the unconstrained minimizer $\hat\beta^{\text{OLS}}$ until they first touch the constraint set.

### LASSO ($L^1$ ball)

In $\mathbb{R}^2$, the $L^1$ ball $\|\beta\|_1 \leq t$ is a **diamond** (rotated square) with vertices at $(\pm t, 0)$ and $(0, \pm t)$.

The expanding elliptical level sets of $L$ generically hit one of these **corners first** — points of the form $(\beta_1, 0)$ or $(0, \beta_2)$.

At a corner, one (or more) coordinates is **exactly zero**. That is sparsity.

### Ridge ($L^2$ ball)

The $L^2$ ball $\|\beta\|_2^2 \leq t$ is a **sphere**, which is **strictly convex and smooth** — no corners anywhere.

A level set ellipse touches the sphere at an interior point of the boundary, generically where **both coordinates are nonzero**.

There is no mechanism to "snap" a coordinate to zero.

---

## Why Corners Are Decisive

A corner of the $L^1$ ball is a point where the **subdifferential of $\|\cdot\|_1$ is large** (it contains an entire interval, not just a single gradient direction). This gives the KKT conditions "room" to be satisfied even when the gradient of $L$ is not pointing exactly along a coordinate axis — so a wide range of loss functions get pinned to the corner.

Formally, at a corner like $\beta = (t, 0)$, the KKT condition for LASSO is:

$$-\nabla_{\beta_2} L(\hat\beta) \in \lambda \cdot \partial |\beta_2| = [-\lambda, \lambda]$$

This is satisfiable for any $\nabla_{\beta_2} L$ with magnitude $\leq \lambda$ — a non-trivial range. Ridge has no such mechanism because the subdifferential of $\|\beta\|_2^2$ is the singleton $\{2\beta\}$, giving no slack.

---

## Summary

| | LASSO | Ridge |
|--|-------|-------|
| Constraint region | $L^1$ ball (diamond, has corners) | $L^2$ ball (sphere, smooth) |
| Level sets touch at | Corner $\Rightarrow$ coordinate = 0 | Smooth boundary $\Rightarrow$ all nonzero |
| Sparsity | Yes, exact zeros | No, only shrinkage toward 0 |
| Use case | Feature selection | Coefficient shrinkage |

The punchline: **LASSO does feature selection not because we asked it to, but because sharp corners make it geometrically inevitable.**
