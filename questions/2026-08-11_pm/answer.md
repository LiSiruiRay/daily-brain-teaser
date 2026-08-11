# Answer: Punctured Torus Has Free Fundamental Group

## Key Idea / Intuition

Think of the torus as a square with opposite sides identified. When you remove a point from the interior of this square, the punctured square deformation retracts onto its boundary frame — a loop that traces all four edges. After the identifications that define the torus, this boundary becomes exactly the wedge $S^1 \vee S^1$. Since $\pi_1(S^1 \vee S^1) \cong F_2$ (the free group on two generators), the punctured torus has the same fundamental group — and crucially, it is **free**, hence non-abelian.

---

## Formal Proof / Solution

### Step 1: Represent the torus as a square with identifications

Recall that $T^2$ is the quotient of the unit square $[0,1]^2$ by the equivalence relation
$$
(x,0) \sim (x,1), \quad (0,y) \sim (1,y).
$$
Choose the removed point $p$ to be the image of an interior point, say $(\tfrac{1}{2}, \tfrac{1}{2})$.

### Step 2: Deformation retract the punctured square onto its boundary

The punctured square $[0,1]^2 \setminus \{(\tfrac{1}{2},\tfrac{1}{2})\}$ deformation retracts onto its boundary $\partial([0,1]^2)$. Concretely: push radially outward from $(\tfrac{1}{2},\tfrac{1}{2})$ toward the nearest boundary point. This is a continuous deformation retraction
$$
r_t(x) = (1-t)x + t \cdot \rho(x), \quad t \in [0,1],
$$
where $\rho(x)$ denotes the radial projection from $(\tfrac{1}{2},\tfrac{1}{2})$ to $\partial([0,1]^2)$.

### Step 3: Identify what the boundary becomes after quotient

The boundary $\partial([0,1]^2)$ consists of the four edges of the square. Under the torus identifications:
- The bottom edge $(x,0)$ is identified with the top edge $(x,1)$ → these form **one circle** (call it $a$).
- The left edge $(0,y)$ is identified with the right edge $(1,y)$ → these form **another circle** (call it $b$).
- The four corners are all identified to a single point $* $.

So the boundary $\partial([0,1]^2)$ under the quotient becomes two circles glued at a single point: **$S^1 \vee S^1$**.

### Step 4: Conclude about $\pi_1$

The deformation retract is compatible with the quotient map (since the puncture is in the interior and the retraction is radial), so we get:
$$
T^2_* \simeq S^1 \vee S^1.
$$
By Van Kampen's theorem (or by direct computation),
$$
\pi_1(S^1 \vee S^1) \cong F_2 = \langle a, b \rangle,
$$
the free group on two generators.

### Step 5: Why the full torus is different

In the **full** torus, the two loops $a$ and $b$ are related by the boundary word $aba^{-1}b^{-1} = 1$ (reading around $\partial([0,1]^2)$ gives the null-homotopic loop because the boundary bounds the square). This relation forces $ab = ba$, giving $\pi_1(T^2) \cong \mathbb{Z}^2$.

When we **remove** the interior point, the square is no longer present to fill in the commutator loop. The boundary loop $aba^{-1}b^{-1}$ now goes around the puncture and is **no longer null-homotopic** — it is the generator of $\pi_1$ around the hole. So the relation disappears, and the group is free.

### Summary

$$
\boxed{\pi_1(T^2 \setminus \{p\}) \cong F_2 = \langle a, b \rangle.}
$$

Removing a point from the torus "undoes" the commutativity relation — a beautiful example of how topology can change drastically under small surgery.
