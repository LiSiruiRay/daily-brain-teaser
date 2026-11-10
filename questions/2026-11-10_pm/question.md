---
name: "Peano Curves Exist, but Peano Bijections Don't"
type: "topology"
tags: ["compactness", "Hausdorff", "homeomorphism", "cut points", "space-filling curve"]
date: "2026-11-10"
solved: false
comments: ""
related: []
redo: 0
difficulty: 2
source: "Munkres, Topology (2nd ed.), Thm 26.6 and §44 (Space-Filling Curve)"
---
# Peano Curves Exist, but Peano Bijections Don't

In 1890 Peano constructed a **continuous surjection**
$$\gamma : [0,1] \to [0,1]^2,$$
a curve that passes through every point of the unit square. (Munkres §44 gives a construction.)

**Problem.** Prove that there is **no continuous bijection** $f : [0,1] \to [0,1]^2$.

In other words, every space-filling curve must pass through some point of the square at least twice.

**Bonus (the role of compactness).** Give an example of a continuous bijection $g : [0,1) \to S^1$ that is *not* a homeomorphism. Explain which step of your proof breaks down for $g$.

---

**Field:** Point-set topology

**Why it's interesting:** Space-filling curves show that continuous maps can increase dimension in a dramatic way. You might expect the cleverness of the construction to be the only obstacle to making the curve injective. In fact the obstruction is a two-line topological argument that combines two classical tools:
- compact $\to$ Hausdorff bijections are automatically homeomorphisms;
- cut points are a topological invariant.

**Difficulty:** 2 / 5

**Tags:** compactness, Hausdorff, homeomorphism, connectedness, cut points, space-filling curves
