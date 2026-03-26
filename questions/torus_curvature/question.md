# Curvature of an Embedded Torus

## Problem

Let $T$ be a smooth, closed surface embedded in $\mathbb{R}^3$ that is topologically a torus. Prove that $T$ must have:

1. At least one point where the Gaussian curvature $K > 0$, and
2. At least one point where the Gaussian curvature $K < 0$.

You may use the **Gauss-Bonnet theorem**: for a closed surface $S$,
$$\iint_S K \, dA = 2\pi \chi(S)$$
where $\chi(S)$ is the Euler characteristic.

---

## Field
Differential Geometry

## Why It's Beautiful

You can *feel* this result geometrically: the outer equator of a doughnut curves like a sphere (positive curvature), while the inner ring curves like a saddle (negative curvature). But making this rigorous requires a global theorem — Gauss-Bonnet — which converts local curvature into a topological invariant.

The result shows that **topology constrains geometry**: the torus cannot be "non-negatively curved throughout," no matter how you embed it. A sphere can be made uniformly positively curved (as a round sphere in $\mathbb{R}^3$), but a torus cannot — the topology forbids it.

## Key Idea / Trick

Two ingredients:
1. **Compactness** gives a point of positive $K$: the point on $T$ farthest from the origin lies on a sphere that $T$ touches from inside, forcing $K > 0$ there.
2. **Gauss-Bonnet** forces a point of negative $K$: since $\chi(T^2) = 0$, we have $\iint K \, dA = 0$. But $K > 0$ somewhere means the integral can only be zero if $K < 0$ somewhere else.

## Difficulty
3 / 5

## Tags
Differential geometry, Gauss-Bonnet, Gaussian curvature, Euler characteristic, Topology, Torus, Compactness
