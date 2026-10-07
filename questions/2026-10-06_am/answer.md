# Answer: Torus Minus Disk: Free Group Appears

## Key Idea / Intuition

The torus has a standard CW decomposition with one 0-cell $v$, two 1-cells $a$ and $b$, and one 2-cell $e^2$ attached via the word $aba^{-1}b^{-1}$. Removing an open disk from the interior of $e^2$ is the same as removing the 2-cell entirely — but keeping its boundary loop. This turns the 2-cell into an annulus, whose boundary contributes a new free loop, giving $X$ the homotopy type of a **wedge of two circles** $S^1 \vee S^1$.

---

## Formal Proof / Solution

**Step 1: CW structure of $T^2$.**

The torus $T^2$ is built from:
- one 0-cell: $v$,
- two 1-cells: $a$, $b$ (both loops at $v$),
- one 2-cell: $e^2$ attached via the commutator word $aba^{-1}b^{-1}$.

So $T^2 = v \cup a \cup b \cup e^2$.

**Step 2: What does removing an open disk do?**

The 2-cell $e^2$ is homeomorphic to a closed disk $\overline{D}^2$. Removing a small open disk from its interior leaves an annulus $S^1 \times [0,1]$.

One boundary circle of this annulus is the attaching map (the loop $aba^{-1}b^{-1}$ around the 1-skeleton), and the other boundary circle is the new boundary $\partial D$ of the removed disk.

**Step 3: Homotopy type of $X$.**

The space $X = T^2 \setminus \text{int}(D)$ deformation retracts onto its 1-skeleton $S^1 \vee S^1$:

- The 2-cell $e^2$ with a hole is an annulus, which deformation retracts onto any one of its boundary circles.
- But one boundary circle is the attaching loop $aba^{-1}b^{-1}$, which already lives in the 1-skeleton $a \vee b$.

Concretely: the annulus (= $e^2$ minus a disk) deformation retracts onto its outer boundary, which is the 1-skeleton. There is **no 2-cell left** to impose any relation on $\pi_1$.

Therefore:
$$X \simeq S^1 \vee S^1.$$

**Step 4: Fundamental group.**

Since $X \simeq S^1 \vee S^1$, by the Seifert–van Kampen theorem (or directly):
$$\pi_1(X) \cong \mathbb{Z} * \mathbb{Z},$$
the free group on two generators.

**Contrast with $T^2$ itself:**

For the full torus, the 2-cell attaches via $aba^{-1}b^{-1}$, imposing the relation $aba^{-1}b^{-1} = 1$, i.e., $ab = ba$. This kills all commutators and gives $\pi_1(T^2) = \mathbb{Z} \times \mathbb{Z}$.

Removing the disk **removes the 2-cell**, which **removes the relation**, freeing the group from commutativity:

$$\pi_1(T^2 \setminus \text{int}(D)) \cong \mathbb{Z} * \mathbb{Z}.$$

**Geometric intuition:** A torus with a hole is like a square with a hole, with opposite edges identified — which is homotopy equivalent to an $\infty$-shaped figure (wedge of two circles). The hole prevents the square from "closing up" and imposing commutativity.
