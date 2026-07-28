# Answer: Open Identity Forces Discrete Topological Group

## Key Idea / Intuition

In a topological group, the topology is "homogeneous" — it looks the same at every point, because left-translation $g \mapsto ag$ is a homeomorphism. So if one point (the identity) has an open neighborhood, you can translate that neighborhood to make **every** singleton open. Discreteness then follows immediately. The $\mathbb{Q}$ example grounds the abstraction: singletons in $\mathbb{Q}$ are never open in $\mathbb{R}$'s topology, so the hypothesis fails, and indeed $\mathbb{Q}$ is not discrete.

---

## Formal Proof / Solution

**Setup.** Recall that in a topological group $G$, for any fixed $a \in G$, the left-translation map
$$L_a : G \to G, \quad L_a(g) = ag$$
is a homeomorphism (it is continuous with continuous inverse $L_{a^{-1}}$).

**Step 1: Every singleton is open.**

Suppose $\{e\}$ is open in $G$. Let $g \in G$ be any element. We want to show $\{g\}$ is open.

Apply the homeomorphism $L_g$:
$$L_g(\{e\}) = \{g \cdot e\} = \{g\}.$$

Since $L_g$ is a homeomorphism and $\{e\}$ is open, its image $\{g\}$ is open.

**Step 2: Conclude $G$ is discrete.**

Since every singleton $\{g\}$ is open, every subset $S \subseteq G$ is a union of open sets:
$$S = \bigcup_{g \in S} \{g\},$$
so $S$ is open. Thus every subset of $G$ is open, which is exactly the **discrete topology**.

$\blacksquare$

---

**Why $\mathbb{Q}$ is not discrete.**

In $\mathbb{Q}$ with the subspace topology from $\mathbb{R}$, the open sets are intersections of open intervals with $\mathbb{Q}$. Every open set in $\mathbb{Q}$ is **infinite** — no singleton $\{q\}$ is open (since any open interval around $q$ contains other rationals). In particular, $\{0\}$ is **not** open in $\mathbb{Q}$.

By the theorem above (contrapositively), $\mathbb{Q}$ is not discrete. And indeed it isn't: every neighborhood of $0$ contains infinitely many other rationals, so we cannot isolate any point.

---

**Conceptual takeaway.** In a topological group, the topology is completely determined by the neighborhoods of the identity (you can translate any neighborhood of $e$ to a neighborhood of any $g$). So "the identity is isolated" is equivalent to "every point is isolated" — a beautiful rigidity that has no analogue in general topological spaces.
