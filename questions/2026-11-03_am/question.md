---
name: "Maps from RP² to the Circle (and Borsuk–Ulam)"
type: "topology"
tags: ["covering spaces", "lifting criterion", "fundamental group", "Borsuk-Ulam", "torsion"]
date: "2026-11-03"
solved: false
comments: ""
related: []
redo: 0
difficulty: 3
source: "Munkres, Topology (2nd ed.), §54 (lifting correspondence) and §57 (Borsuk–Ulam theorem); Lee, Introduction to Topological Manifolds, Ch. 11 (lifting criterion)"
---
# Maps from $\mathbb{RP}^2$ to the Circle

**(a)** Prove that every continuous map
$$f:\mathbb{RP}^2\to S^1$$
is null-homotopic.

**(b) (Payoff.)** Use (a) to show that there is **no** continuous map $h:S^2\to S^1$ satisfying
$$h(-x)=-h(x)\qquad\text{for all }x\in S^2.$$

**(c) (Corollary, one line.)** Deduce the $2$-dimensional Borsuk–Ulam theorem: every continuous $\varphi:S^2\to\mathbb{R}^2$ has a point $x$ with $\varphi(x)=\varphi(-x)$. For example, at any moment there are two antipodal points on Earth with the same temperature *and* the same pressure.

*You may use $\pi_1(\mathbb{RP}^2)\cong\mathbb{Z}/2$, $\pi_1(S^1)\cong\mathbb{Z}$, and the lifting criterion for covering spaces.*

---

**Field:** Algebraic topology (fundamental group, covering spaces)

**Why it's interesting:** Part (a) is a small piece of algebra, "$\mathbb{Z}/2$ has no nontrivial homomorphism into the torsion-free group $\mathbb{Z}$," turned into a geometric statement. Parts (b) and (c) then turn that into Borsuk–Ulam, a theorem with real-world content. You get the full chain *torsion $\Rightarrow$ lifting $\Rightarrow$ antipodal coincidence*, and none of the steps involves a computation.

**Difficulty:** 3/5
