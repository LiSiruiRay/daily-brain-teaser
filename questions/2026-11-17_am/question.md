---
name: "Loops in a Topological Group Commute"
type: "topology"
tags: ["fundamental group", "topological groups", "Eckmann-Hilton", "H-spaces"]
date: "2026-11-17"
solved: false
comments: ""
related: []
redo: 0
difficulty: 2
source: "Munkres, Topology (2nd ed.), §52, Exercise 7"
---
# Loops in a Topological Group Commute

Let $G$ be a path-connected topological group with identity $e$. For loops $f, g : [0,1] \to G$ based at $e$, there are two natural ways to combine them:

- **Concatenation:** $(f * g)(s)$ traverses $f$ at double speed, then $g$ at double speed. This is the operation defining $\pi_1(G,e)$.
- **Pointwise product:** $(f \cdot g)(s) = f(s)\,g(s)$, using the group multiplication of $G$.

**(a)** Show that $f * g \simeq f \cdot g$ rel endpoints.

**(b)** Deduce that $\pi_1(G, e)$ is **abelian**.

**(c)** Conclude that neither the Klein bottle nor the figure-eight $S^1 \vee S^1$ admits the structure of a topological group.

*Hint:* What happens if you take the pointwise product of "$f$, then stand still" with "stand still, then $g$"?

---

**Field:** Algebraic topology / topological groups

**Why it's interesting:** This is the simplest instance of the **Eckmann–Hilton argument**: if a set carries two compatible binary operations with a common unit, then the two operations coincide and are commutative. The same principle explains why the higher homotopy groups $\pi_n$ for $n \ge 2$ are abelian. Here it gives a cheap but strong obstruction: any space whose fundamental group is non-abelian cannot be a topological group.

**Difficulty:** 2.5 / 5

**Tags:** fundamental group, topological groups, Eckmann–Hilton, H-spaces

**Source:** Munkres, *Topology* (2nd ed.), §52, Exercise 7.
