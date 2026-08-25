# Answer: The Torus That Forgets a Disk

## Key Idea / Intuition

Think of the torus as a square with opposite edges identified. The punctured torus is exactly that square (a compact 2-cell) with the interior of the disk removed — but since the disk's hole can be "inflated" to fill the square's interior, the punctured torus collapses down to just the boundary of the square. That boundary, after the identifications of the torus, becomes precisely a figure-eight (wedge of two circles). Attaching the 2-cell back (i.e., filling the hole) introduces exactly one relation — that the attaching map (the commutator $aba^{-1}b^{-1}$) is trivial — which abelianizes $F_2$ to $\mathbb{Z}^2$.

---

## Formal Proof / Solution

### Step 1: Model the torus as a CW complex

Represent $T^2$ as the unit square $[0,1]^2$ with the standard identifications:
- $(0,t) \sim (1,t)$ (left/right edges identified, labeled $a$)
- $(s,0) \sim (s,1)$ (top/bottom edges identified, labeled $b$)

This gives $T^2$ a CW structure with:
- one 0-cell: the single vertex $v$ (all four corners identified),
- two 1-cells: $a$ and $b$,
- one 2-cell: the open square interior, attached via the loop $aba^{-1}b^{-1}$.

### Step 2: Remove a disk

Remove a small open disk $D$ from the interior of the 2-cell (the open square). What remains is the square with a hole — topologically, a compact surface with one boundary circle (the hole's boundary) and the four edges of the square.

### Step 3: Deformation retract

The region $[0,1]^2 \setminus D$ (with interior hole) deformation retracts onto its boundary. But we must respect the edge identifications.

More precisely: $T^2 \setminus D$ deformation retracts onto the **1-skeleton** of the CW complex, which consists of just the two 1-cells $a$ and $b$ glued at the single vertex $v$. This is exactly $S^1 \vee S^1$.

**Why?** The punctured square is homotopy equivalent to its boundary $\partial([0,1]^2)$ — just push every point radially outward from the center of the removed disk to the boundary of the square. After the edge identifications of the torus, $\partial([0,1]^2)$ becomes the loop $a b a^{-1} b^{-1}$ based at $v$, which is the 1-skeleton $S^1 \vee S^1$.

### Step 4: Apply van Kampen / standard result

Since $T^2 \setminus D \simeq S^1 \vee S^1$, we immediately get

$$\pi_1(T^2 \setminus D) \cong \pi_1(S^1 \vee S^1) \cong F_2 = \langle a, b \rangle.$$

### Bonus: Recovering $\pi_1(T^2) \cong \mathbb{Z}^2$

$T^2$ is obtained from $T^2 \setminus D$ by **gluing back** the 2-cell along the loop $\partial D$, which in the 1-skeleton is the commutator $aba^{-1}b^{-1}$.

By van Kampen's theorem applied to $T^2 = (T^2 \setminus D) \cup_{\partial D} D^2$:

$$\pi_1(T^2) \cong F_2 \big/ \langle\!\langle aba^{-1}b^{-1} \rangle\!\rangle = \langle a, b \mid aba^{-1}b^{-1} = 1 \rangle \cong \mathbb{Z}^2.$$

So $\pi_1(T^2)$ is exactly the **abelianization** of $\pi_1(T^2 \setminus D)$. The one 2-cell that fills the puncture is precisely responsible for making $a$ and $b$ commute. Geometrically: the disk "kills" all non-commutativity, and the free group collapses to $\mathbb{Z}^2$.

### Summary

| Space | Homotopy type | $\pi_1$ |
|---|---|---|
| $T^2 \setminus D$ | $S^1 \vee S^1$ | $F_2$ (free, non-abelian) |
| $T^2$ | torus | $\mathbb{Z}^2$ (abelian) |

The single 2-cell is the exact algebraic "commutator killer."
