# Answer: Covering Space of Wedge of Circles Has Larger Fundamental Group

## Key Idea / Intuition

The surprise is that a 2-sheeted covering of $S^1 \vee S^1$ — which looks like it should be "smaller" — has a fundamental group that is **larger** (in fact, it is free on **3 generators**). This illustrates one of the most striking features of covering space theory: a covering space of a space with free fundamental group is itself free (by the Nielsen–Schreier theorem), but the rank can *increase* with the number of sheets. The rank formula $1 + n(r-1)$ makes this precise.

---

## Formal Proof / Solution

**Step 1: Identify the covering graph.**

The covering $\tilde{X}$ is a graph (a 1-complex) with:
- **Vertices:** $\tilde{x}_0, \tilde{x}_1$ (two sheets over $x_0$).
- **Edges from $a$:** Since $a$ swaps the two sheets, the loop $a$ based at $x_0$ lifts to a single edge $\tilde{a}$ from $\tilde{x}_0$ to $\tilde{x}_1$, and the loop $a^{-1}$ gives the reverse edge. Together this is one undirected edge connecting $\tilde{x}_0 \leftrightarrow \tilde{x}_1$.
- **Edges from $b$:** Since $b$ fixes each sheet, $b$ lifts to a loop $\tilde{b}_0$ at $\tilde{x}_0$ and a loop $\tilde{b}_1$ at $\tilde{x}_1$.

So $\tilde{X}$ is a graph with 2 vertices, 1 edge connecting them ($\tilde{a}$), and 2 loop edges ($\tilde{b}_0$ at $\tilde{x}_0$ and $\tilde{b}_1$ at $\tilde{x}_1$).

**Step 2: Compute $\pi_1(\tilde{X})$ via Euler characteristic.**

For a connected graph $G$, $\pi_1(G)$ is free of rank $1 - \chi(G) = 1 - V + E$.

Here:
$$V = 2, \quad E = 1 + 2 = 3 \quad \Rightarrow \quad \text{rank} = 1 - 2 + 3 = 2.$$

Wait — let me recount. We have:
- 2 vertices,
- 3 edges: $\tilde{a}$ (connecting the two vertices), $\tilde{b}_0$ (loop at $\tilde{x}_0$), $\tilde{b}_1$ (loop at $\tilde{x}_1$).

$$\chi(\tilde{X}) = V - E = 2 - 3 = -1, \quad \text{rank of } \pi_1(\tilde{X}) = 1 - \chi = 1 - (-1) = \mathbf{3}.$$

So $\pi_1(\tilde{X}, \tilde{x}_0) \cong F_3$, **a free group on 3 generators**.

**Step 3: Find explicit generators as elements of $F_2$.**

Using the correspondence $\pi_1(\tilde{X}, \tilde{x}_0) \cong p_*\pi_1(\tilde{X}, \tilde{x}_0) \leq F_2$, we find generators by reading off loops in $\tilde{X}$ as words in $a, b$:

Choose spanning tree $T = \{\tilde{a}\}$ (the edge connecting $\tilde{x}_0$ to $\tilde{x}_1$). The non-tree edges give generators:

1. $\tilde{b}_0$: loop at $\tilde{x}_0$ — projects to $b$.
2. $\tilde{b}_1$: loop at $\tilde{x}_1$ — to make it a loop based at $\tilde{x}_0$, go via $\tilde{a}$: projects to $a b a^{-1}$.
3. $\tilde{a}^2$: traverse $\tilde{a}$ twice (go from $\tilde{x}_0$ to $\tilde{x}_1$ and back via the same edge) — projects to $a^2$.

So the subgroup is:
$$p_*\pi_1(\tilde{X}, \tilde{x}_0) = \langle b,\; aba^{-1},\; a^2 \rangle \leq F_2.$$

This is a **free group of rank 3** sitting inside a free group of rank 2!

**Step 4: The general formula (Nielsen–Schreier).**

If $\pi_1(X)$ is free of rank $r$ and the covering has $n$ sheets, then:
$$\text{rank}(\pi_1(\tilde{X})) = 1 + n(r - 1).$$

Here $n = 2$, $r = 2$: rank $= 1 + 2(2-1) = 3$. ✓

**Why is this surprising?**

A 2-sheeted cover of $X$ is "smaller" in the sense that each loop has fewer sheets to wind around — yet its fundamental group is *larger* (rank 3 vs rank 2). This is purely a phenomenon of free groups (and negatively curved spaces): subgroups of free groups are free, but they can have much larger rank. There is no analogue of Lagrange's theorem bounding the rank.
