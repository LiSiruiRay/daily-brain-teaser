# Answer: Fundamental Group of S¹ ∨ S²

## Key Idea / Intuition

The wedge sum $S^1 \vee S^2$ glues a circle and a sphere at a single point. Intuitively, any loop based at the wedge point can either wind around the $S^1$ part or venture into the $S^2$ part — but every loop in $S^2$ is contractible (since $S^2$ is simply connected). So the $S^2$ contributes **nothing** to $\pi_1$, and the fundamental group is just $\mathbb{Z}$, as if the sphere weren't there at all. The surprise is that $S^2$ does contribute to *higher* homotopy groups ($\pi_2$), but not to $\pi_1$.

---

## Formal Proof / Solution

**Setup via van Kampen's Theorem.**

Write $X = S^1 \vee S^2$ with wedge point $x_0$. We apply the Seifert–van Kampen theorem.

**Choose open sets.** Let:
- $U$ = a small open neighborhood of $S^1$ in $X$, which deformation retracts onto $S^1$ (formally, take $S^1$ union a small contractible cap into $S^2$).
- $V$ = the $S^2$ component together with a small open arc of $S^1$ near $x_0$, which deformation retracts onto $S^2$.

More precisely, thicken slightly so that:
$$U \simeq S^1, \quad V \simeq S^2, \quad U \cap V \simeq \{x_0\} \text{ (contractible)}.$$

**Apply van Kampen.** Since $U \cap V$ is path-connected and contractible,
$$\pi_1(X) \cong \pi_1(U) *_{\pi_1(U \cap V)} \pi_1(V) = \pi_1(S^1) * \pi_1(S^2).$$

(The amalgamation over $\pi_1(U \cap V) = \{1\}$ is just the free product.)

**Compute the pieces:**
$$\pi_1(S^1) = \mathbb{Z}, \qquad \pi_1(S^2) = \{1\}.$$

The free product with a trivial group is:
$$\pi_1(S^1 \vee S^2) \cong \mathbb{Z} * \{1\} \cong \mathbb{Z}.$$

**Conclusion.**

$$\boxed{\pi_1(S^1 \vee S^2) \cong \mathbb{Z}.}$$

**The conceptual punchline:** Even though the sphere $S^2$ is a nontrivial topological object (indeed $\pi_2(S^1 \vee S^2)$ is *huge* — it's infinitely generated as a $\mathbb{Z}[\mathbb{Z}]$-module by the universal cover construction), it is **invisible** to the fundamental group. The sphere's contribution to homotopy only begins at dimension 2. This illustrates a key principle: $\pi_1$ only "sees" one-dimensional holes; higher-dimensional cavities are detected only by higher homotopy groups or homology.

**Contrast with $S^1 \vee S^1$:** There, $\pi_1 \cong \mathbb{Z} * \mathbb{Z}$, a non-abelian free group, because both pieces contribute. The sphere is fundamentally different because it is simply connected.
