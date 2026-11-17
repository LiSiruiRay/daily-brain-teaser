---
name: "The Ordered Square: Connected but Not Path-Connected"
type: "topology"
tags: ["order topology", "connectedness", "path-connectedness", "counterexample", "separability"]
date: "2026-11-17"
solved: false
comments: ""
related: []
redo: 0
difficulty: 2
source: "Munkres, Topology (2nd ed.), §24 Connected Subspaces of the Real Line"
---
# The Ordered Square: Connected but Not Path-Connected

Let $I_o^2$ denote the unit square $[0,1]\times[0,1]$ with the **dictionary (lexicographic) order**
$$(a,b) < (c,d) \iff a<c \ \text{ or } \ (a=c \text{ and } b<d),$$
and give it the **order topology**. Its basic open sets are open intervals $\big((a,b),(c,d)\big)$ and the half-open rays at the endpoints $(0,0)$ and $(1,1)$.

1. Show that $I_o^2$ is **connected**.
2. Show that $I_o^2$ is **not path-connected**. In particular, there is no continuous path $f:[0,1]\to I_o^2$ from $(0,0)$ to $(1,1)$.

*Hint for (2): first decide what the image of such a path would have to be. Then look at the vertical "fibers" $\{x\}\times(0,1)$.*

---

**Field:** Point-set topology

**Why it's interesting:** The topologist's sine curve is the usual example of a space that is connected but not path-connected. Its obstruction is local and analytic, coming from oscillation near a limit segment. The ordered square fails for a completely different reason, and the reason is *cardinality*. The square is compact and connected, and it is even locally connected. But it is "too wide" for an interval to sweep through it: a path would have to cover uncountably many pairwise disjoint open sets, and $[0,1]$ is separable.

**Key idea (brief):** A connected subset of a linearly ordered space must be order-convex. So a path from the minimum to the maximum must be surjective. The fibers $\{x\}\times(0,1)$ form uncountably many disjoint nonempty open sets. Their preimages would be uncountably many disjoint nonempty open subsets of $[0,1]$, and each would contain a different rational number.

**Difficulty:** 2.5 / 5

**Reference:** Munkres, *Topology* (2nd ed.), §24 "Connected Subspaces of the Real Line" (the ordered square as a linear continuum, and the example showing it is not path-connected).
