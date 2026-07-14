# Answer: Open Subgroups of Topological Groups Are Closed

## Key Idea / Intuition

The key insight has two parts. First, the closure of a subgroup is automatically a subgroup — because the group operations are continuous, so they "propagate" through limits. Second, the cosets of an open subgroup tile the group into disjoint open sets; the complement of the subgroup is a union of cosets, hence open — making the subgroup closed. This is a beautiful interplay between the algebraic and topological structure.

---

## Formal Proof / Solution

### Step 1: The closure of a subgroup is a subgroup

Let $H \leq G$ be any subgroup. We claim $\overline{H} \leq G$.

- **Identity:** $e \in H \subseteq \overline{H}$. ✓

- **Inverses:** The map $\iota: G \to G$, $g \mapsto g^{-1}$ is continuous (by definition of topological group). Since $\iota(H) = H$, by continuity:
$$\iota(\overline{H}) \subseteq \overline{\iota(H)} = \overline{H}.$$

- **Closure under multiplication:** The map $\mu: G \times G \to G$, $(x,y) \mapsto xy$ is continuous. Since $\mu(H \times H) = H$:
$$\mu(\overline{H} \times \overline{H}) = \mu(\overline{H \times H}) \subseteq \overline{\mu(H \times H)} = \overline{H}.$$

So $\overline{H}$ is indeed a subgroup of $G$.

**Consequence:** If $H$ is not dense, then $\overline{H} \neq G$, so $\overline{H}$ is a *proper* closed subgroup. If $H$ is not closed, it is not dense iff $\overline{H} \subsetneq G$. Either $H$ is dense in $G$, or $\overline{H}$ is a proper closed subgroup — there is no middle ground.

---

### Step 2: Every open subgroup is closed

Let $H \leq G$ be an **open** subgroup. We show $G \setminus H$ is open.

For any $g \in G$, the **left coset** $gH$ is open: the map $L_g: x \mapsto gx$ is a homeomorphism (continuous with continuous inverse $L_{g^{-1}}$), so $gH = L_g(H)$ is open.

Now write:
$$G \setminus H = \bigsqcup_{g \notin H} gH.$$

This is because the left cosets $\{gH : g \in G\}$ partition $G$, and every coset is either equal to $H$ (if $g \in H$) or disjoint from $H$ (if $g \notin H$). Each coset $gH$ for $g \notin H$ is open, so their union is open.

Therefore $G \setminus H$ is open, which means $H$ is **closed**. $\blacksquare$

---

### Why this is elegant

Notice we used **no** specific structure of $G$ — just that multiplication and inversion are continuous and that open sets are preserved by homeomorphisms. The proof works for $\mathbb{Z} \leq \mathbb{R}$, for $\mathrm{SO}(n) \leq \mathrm{GL}(n,\mathbb{R})$, for any profinite group, etc.

A striking corollary: **any subgroup of $\mathbb{R}$ is either $\{0\}$, $\mathbb{R}$, discrete (hence closed), or dense** — a fact that follows immediately once you know $\mathbb{R}$ has the structure of a topological group.
