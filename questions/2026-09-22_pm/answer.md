# Answer: Punctured RP² Has Fundamental Group ℤ

## Key Idea / Intuition

$\mathbb{RP}^2$ can be built by gluing a Möbius band to a disk along their boundary circle. When you remove a point from the interior of the disk part, the disk-minus-a-point deformation retracts to its boundary circle, leaving you with a Möbius band (glued to a circle). A Möbius band itself deformation retracts to its core circle, and a circle has fundamental group $\mathbb{Z}$. So $X$ is homotopy equivalent to a Möbius band, giving $\pi_1(X) \cong \mathbb{Z}$.

---

## Formal Proof / Solution

**Step 1: Describe $\mathbb{RP}^2$ as a CW complex / quotient of a disk.**

Represent $\mathbb{RP}^2$ as the quotient of a closed disk $D^2$ where antipodal boundary points are identified:
$$\mathbb{RP}^2 = D^2 / (x \sim -x \text{ for } x \in \partial D^2).$$

The boundary circle $\partial D^2$ under this identification becomes a circle traversed **twice** (once in each direction cancels out to give a $\mathbb{Z}/2$ word $a^2$ in the fundamental polygon language: $\mathbb{RP}^2$ has presentation $\langle a \mid a^2 \rangle$).

Concretely, $\mathbb{RP}^2$ splits into two pieces:
- A **Möbius band** $M$ (a small tubular neighborhood of the "equator" of $\mathbb{RP}^2$),
- A **disk** $D$ (a neighborhood of one "pole").

These are glued along their common boundary circle.

**Step 2: Remove a point $p$ from the disk piece.**

Choose $p$ in the interior of the disk piece $D$. Then:
$$X = \mathbb{RP}^2 \setminus \{p\} = M \cup (D \setminus \{p\}).$$

The space $D \setminus \{p\}$ (a disk minus an interior point) **deformation retracts** onto its boundary circle $\partial D = \partial M$.

Therefore:
$$X \simeq M \cup_{\partial} \partial D \simeq M,$$
since the annulus $D \setminus \{p\} \simeq S^1$ collapses, and we are left with just the Möbius band $M$ (the boundary circle of $D$ is already the boundary circle of $M$, so gluing the retracted circle just gives $M$ back).

More precisely: $X$ deformation retracts onto the Möbius band $M$.

**Step 3: Compute $\pi_1(M)$.**

The Möbius band $M$ deformation retracts onto its **core circle** (the central circle running along the middle of the band). This core circle is homeomorphic to $S^1$, so:
$$\pi_1(M) \cong \pi_1(S^1) \cong \mathbb{Z}.$$

**Step 4: Conclusion.**

Since $X \simeq M \simeq S^1$:
$$\boxed{\pi_1\!\left(\mathbb{RP}^2 \setminus \{p\}\right) \cong \mathbb{Z}.}$$

**Sanity check via van Kampen.** Alternatively, use the standard cell structure of $\mathbb{RP}^2$ (one 0-cell, one 1-cell $a$, one 2-cell attached by $a^2$). Removing the interior of the 2-cell gives the 1-skeleton, which is a circle with fundamental group $\mathbb{Z}$. Removing a point from the interior of the 2-cell gives a space homotopy equivalent to this 1-skeleton, confirming $\pi_1(X) \cong \mathbb{Z}$.

**Why is this surprising?** Even though $\pi_1(\mathbb{RP}^2) = \mathbb{Z}/2\mathbb{Z}$, removing a single point "unwraps" the torsion and gives the infinite cyclic group. The generator of $\pi_1(X) \cong \mathbb{Z}$ maps to the generator of $\pi_1(\mathbb{RP}^2) \cong \mathbb{Z}/2\mathbb{Z}$ under the inclusion-induced map—you need to go around **twice** to become contractible in the full projective plane.
