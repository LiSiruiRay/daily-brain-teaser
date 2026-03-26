# Curvature of an Embedded Torus — Answer

## Setup

Let $T \subset \mathbb{R}^3$ be a smooth closed surface homeomorphic to the torus $T^2$. Recall:
- **Euler characteristic**: $\chi(T^2) = 0$ (since $V - E + F = 0$ for any triangulation).
- **Gauss-Bonnet**: $\iint_T K \, dA = 2\pi \chi(T^2) = 0$.

---

## Part 1: There exists a point with $K > 0$

Since $T$ is compact, it is bounded in $\mathbb{R}^3$. Let $p \in T$ be the point **farthest from the origin**, i.e., $|p| = \max_{q \in T} |q|$.

At $p$, the surface $T$ is tangent (from inside) to the sphere $S_r$ of radius $r = |p|$ centered at the origin.

Since $T$ lies entirely inside $S_r$ and touches it at $p$, the surface $T$ curves at least as much as $S_r$ at $p$ in every direction. The sphere $S_r$ has Gaussian curvature $K = 1/r^2 > 0$, so:

$$K(p) \geq \frac{1}{r^2} > 0$$

More precisely: the principal curvatures $\kappa_1, \kappa_2$ of $T$ at $p$ both satisfy $\kappa_i \geq 1/r > 0$, giving $K(p) = \kappa_1 \kappa_2 > 0$. $\checkmark$

---

## Part 2: There exists a point with $K < 0$

By Gauss-Bonnet:
$$\iint_T K \, dA = 2\pi \cdot \chi(T^2) = 2\pi \cdot 0 = 0$$

From Part 1, $K > 0$ on some open neighborhood of $p$ (by continuity), so:
$$\iint_T K \, dA \geq \iint_{U} K \, dA > 0 \quad \text{if } K \geq 0 \text{ everywhere}$$

This contradicts $\iint_T K \, dA = 0$. Therefore $K < 0$ at some point. $\blacksquare$

---

## Geometric Picture

On a standard torus of revolution (donut), you can see both signs explicitly:

- **Outer equator** (farthest from the axis): the surface curves away from you in both directions, like a sphere — $K > 0$.
- **Inner equator** (closest to the axis): the surface curves toward you in one direction, away in the other, like a saddle — $K < 0$.
- **Top and bottom circles**: $K = 0$ (one principal curvature is zero).

The Gauss-Bonnet theorem guarantees these positive and negative regions balance out exactly.

---

## Contrast with the Sphere

For $S^2$: $\chi(S^2) = 2$, so $\iint K \, dA = 4\pi > 0$. The sphere *can* be embedded with $K > 0$ everywhere (the round sphere has $K \equiv 1/R^2$).

For the torus: $\chi = 0$ forces the total curvature to vanish — positive and negative regions must perfectly cancel. No matter how cleverly you embed a torus in $\mathbb{R}^3$, you cannot avoid saddle points.

---

## Key Takeaway

> **Topology constrains geometry.** The Euler characteristic — a purely topological quantity — dictates the sign of the total curvature. A torus, having $\chi = 0$, must have mixed curvature in any smooth embedding in $\mathbb{R}^3$.
