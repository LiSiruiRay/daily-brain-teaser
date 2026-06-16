# Answer: 2026-06-16_pm

## Key Idea / Intuition

The comb space looks like it should behave nicely — it is connected, simply connected, and even contractible. But the "top of the left spine," the point $p = (0,1)$, has no contractible neighborhood: any neighborhood of $p$ must contain points on the high teeth $\{1/n\} \times \{1\}$ for large $n$, and no path from those points can reach $p$ and then contract back, because the teeth are isolated from each other near the top. This is a perfect illustration that **contractible $\not\Rightarrow$ locally contractible**, and it explains why the comb space is a standard counterexample in topology.

---

## Formal Proof / Solution

### Part (a): Path-Connectedness

We show any point $q \in C$ can be connected to $p = (0,1)$ by a path.

- **Points on the base** $[0,1] \times \{0\}$: go along the base to $(0,0)$, then up the left spine to $(0,1)$.
- **Points on a tooth** $\{1/n\} \times [0,1]$: travel down the tooth to $(1/n, 0)$, along the base to $(0,0)$, then up the left spine.
- **Points on the left spine** $\{0\} \times [0,1]$: travel directly up or down the spine.

All these are explicit continuous paths, so $C$ is **path-connected**. $\checkmark$

---

### Part (b): Contractibility

Define a homotopy $H : C \times [0,1] \to C$ in two stages:

**Stage 1** ($t \in [0, 1/2]$): "Comb down all teeth to the base." Define

$$H(x, y, t) = \left(x,\, (1 - 2t)\,y\right) \quad \text{for } t \in [0, 1/2].$$

At $t = 0$ this is the identity; at $t = 1/2$ every point is mapped to $(x, 0)$, i.e., the base $[0,1] \times \{0\}$.

*Check it stays in $C$:* For a point $(1/n, y)$ on a tooth, $H(1/n, y, t) = (1/n, (1-2t)y) \in \{1/n\} \times [0,1] \subset C$. For $(0, y)$, it goes to $(0,(1-2t)y) \in \{0\} \times [0,1]$. For $(x,0)$, it stays on the base. ✓

**Stage 2** ($t \in [1/2, 1]$): "Slide everything along the base to $(0,0)$, then up the spine to $(0,1)$."

$$H(x, 0, t) = \left((1 - 2(t - 1/2))\,x,\; 0\right) \quad t \in [1/2, 3/4],$$

$$H(0, 0, t) = \left(0,\; 2(t - 3/4) \cdot 1\right) \quad t \in [3/4, 1].$$

Combining, $H(\cdot, 1) = (0,1) = p$ for all points. Since each piece is continuous and they agree on overlaps, $H$ is a contraction of $C$ to the point $p$. Thus $C$ is **contractible**. $\checkmark$

---

### Part (c): $p = (0,1)$ Has No Contractible Neighborhood

**Claim:** Every open neighborhood $U$ of $p = (0,1)$ in $C$ is **not** locally path-connected (and in particular cannot deformation retract onto $p$).

Take any open ball $B_\epsilon(p) \cap C$ for small $\epsilon > 0$. For $n$ large enough that $1/n < \epsilon$, the point $q_n = (1/n, 1) \in B_\epsilon(p) \cap C$ lies on the tip of the $n$-th tooth.

**Key observation:** Any path $\gamma : [0,1] \to C$ starting at $q_n = (1/n, 1)$ that reaches $p = (0,1)$ must at some time pass through the base (since the only connection between different teeth and the spine is through the base $y = 0$). Explicitly:

- The tooth $\{1/n\} \times [0,1]$ is connected only to the rest of $C$ via $(1/n, 0)$ on the base.
- So any path from $q_n$ to $p$ must dip down to $y = 0$ at some point.

But then the path **leaves** $B_\epsilon(p)$ (since the base is at distance $\geq 1 - \epsilon$ from $p$ vertically when $\epsilon < 1$).

Therefore, within $U = B_\epsilon(p) \cap C$, the points $q_n$ for large $n$ **cannot be connected to $p$ by a path staying in $U$**. Hence $U$ is **not path-connected**, and certainly admits no deformation retraction of $U$ onto $p$.

---

### The Lesson

| Property | Comb Space $C$ |
|---|---|
| Connected | ✓ |
| Path-connected | ✓ |
| Contractible | ✓ (global homotopy exists) |
| Locally contractible at $(0,1)$ | ✗ |
| Locally path-connected at $(0,1)$ | ✗ |

This shows: **contractible spaces need not be locally contractible**. The global homotopy "cheats" by routing everything through the base, but no local neighborhood of the spine-tip can do the same. This is why **CW complexes** or **ANRs** (absolute neighborhood retracts) are better-behaved: they are always locally contractible.

Written to: [questions/Q103_comb_contractible_not_locally.md](questions/Q103_comb_contractible_not_locally.md)

Answer written to: [questions/A103_comb_contractible_not_locally.md](questions/A103_comb_contractible_not_locally.md)
