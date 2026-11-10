---
name: "How Few Vertices Can a Torus Have?"
type: "topology"
tags: ["Euler characteristic", "triangulation", "simplicial complex", "double counting", "Möbius torus", "K7"]
date: "2026-11-10"
solved: false
comments: ""
related: []
redo: 0
difficulty: 2
source: "Inspired by J. M. Lee, Introduction to Topological Manifolds, Ch. 5 (Simplicial Complexes, Euler characteristic)"
---
# How Few Vertices Can a Torus Have?

A **triangulation** of a surface $S$ is a finite simplicial complex whose polyhedron is homeomorphic to $S$. This is a genuine simplicial complex, so two distinct triangles share at most one edge or one vertex, and two distinct edges never have the same pair of endpoints.

The obvious way to triangulate the torus is to divide the square $[0,1]^2$ into an $n\times n$ grid, cut each small square along a diagonal, and glue opposite sides. For $n=3$ this uses $9$ vertices. For $n=2$ it fails, because different edges would end up with the same endpoints.

**Question.**
1. Prove that **every** triangulation of the torus $T^2$ has at least $7$ vertices.
2. Show that $7$ is attained.

*Bonus:* Use the same argument to find lower bounds for the sphere $S^2$ and the projective plane $\mathbb{RP}^2$.

---

**Field:** Topology (combinatorial topology, Euler characteristic)

**Why it's interesting:** A purely topological invariant, $\chi(T^2)=0$, combined with two trivial counting facts gives a sharp lower bound. The extremal object is the famous 7-vertex Möbius torus. Its 1-skeleton is the complete graph $K_7$, which shows that $K_7$ embeds in the torus. This is the first case of the Heawood map-coloring bound.

**Difficulty:** 2/5

**Source:** Inspired by the discussion of simplicial complexes and the Euler characteristic in J. M. Lee, *Introduction to Topological Manifolds*, Ch. 5.
