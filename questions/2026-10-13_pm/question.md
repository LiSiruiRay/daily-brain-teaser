---
name: "Cofinite Topology: T₁ but Not Hausdorff"
type: "topology"
tags: ["separation axioms", "cofinite topology", "T1", "Hausdorff", "counterexample"]
date: "2026-10-13"
solved: false
comments: ""
related: []
redo: 0
difficulty: 2
source: "Munkres, Topology, Chapter 2 (Separation Axioms)"
---
# The Topological Space That Is $T_1$ but Not Hausdorff

Let $X$ be an infinite set equipped with the **cofinite topology**: a set $U \subseteq X$ is open if and only if $U = \emptyset$ or $X \setminus U$ is finite.

**(a)** Show that $(X, \tau_\text{cof})$ is $T_1$: for any two distinct points $x \neq y$, there exist open sets $U \ni x$, $V \ni y$ with $y \notin U$ and $x \notin V$.

**(b)** Show that $(X, \tau_\text{cof})$ is **not** Hausdorff: no two distinct points can be separated by disjoint open sets.

**(c)** Conclude: *$T_1$ does not imply Hausdorff*. What goes wrong?
