---
name: "Punctured Torus Has Free Fundamental Group"
type: "topology"
tags: ["fundamental group", "deformation retract", "free group", "torus", "Van Kampen"]
date: "2026-08-11"
solved: false
comments: ""
related: []
redo: 0
difficulty: 3
source: "Topology (Munkres); Introduction to Topological Manifolds (Lee)"
---
# The Punctured Torus Has a Surprising Fundamental Group

Let $T^2 = S^1 \times S^1$ be the torus, and let $T^2_* = T^2 \setminus \{p\}$ be the torus with one point removed.

**Claim:** The fundamental group $\pi_1(T^2_*)$ is a free group on **two** generators.

This is surprising: the full torus has $\pi_1(T^2) \cong \mathbb{Z} \times \mathbb{Z}$, which is abelian. But removing a single point makes the fundamental group **non-abelian** (in fact, free).

**Your task:** Explain why this is true by constructing an explicit deformation retract of $T^2_*$ onto a familiar space whose fundamental group you already know.
