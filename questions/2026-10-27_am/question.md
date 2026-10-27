---
name: "A Compact Space Has No Room for a Proper Isometric Copy of Itself"
type: "topology"
tags: ["compactness", "metric spaces", "isometry", "sequential compactness", "counterexample"]
date: "2026-10-27"
solved: false
comments: ""
related: []
redo: 0
difficulty: 2
source: "Munkres, Topology (2nd ed.), §28 (Limit Point Compactness), Exercise 6"
---
# A Compact Space Has No Room for a Proper Isometric Copy of Itself

Let $(X,d)$ be a metric space. A map $f : X \to X$ is an **isometry** if
$$d(f(x), f(y)) = d(x,y) \quad \text{for all } x,y \in X.$$

Isometries are always injective and continuous. They need not be surjective.

**(a)** Prove that if $X$ is **compact**, then every isometry $f : X \to X$ is surjective. Conclude that $f$ is a homeomorphism.

**(b)** Show that compactness cannot be weakened to "complete and bounded." Find a closed, bounded subset $B$ of a complete metric space and an isometry $B \to B$ that is not onto.

*Hint for thinking:* For a finite set, an injection from the set to itself is automatically a bijection. Compactness says a space is "approximately finite." What would go wrong if a point $a$ were missed by $f$?
