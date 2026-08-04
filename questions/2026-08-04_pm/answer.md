# Answer: The Torus and the Annulus: A Quotient Surprise

## Key Idea / Intuition

The torus is a product $S^1 \times S^1$. The equivalence relation only acts on the **second** $S^1$ factor — it reflects each circle $\{pt\} \times S^1$ across the "real axis" by conjugation $e^{i\theta_2} \mapsto e^{-i\theta_2}$. Each circle $S^1$ under the reflection $\theta \mapsto -\theta$ collapses to a closed interval $[0, \pi]$ (since $e^{i\theta} \sim e^{-i\theta}$ identifies antipodal-in-angle points). So the torus becomes a **cylinder**: a circle's worth of intervals, i.e., $S^1 \times [0, \pi] \cong S^1 \times [0,1]$.

---

## Formal Proof / Solution

**Step 1: Analyze each fiber.**

Fix $z = e^{i\theta_1} \in S^1$. The fiber over $z$ is $\{z\} \times S^1$, and the equivalence relation restricts to:

$$e^{i\theta_2} \sim e^{-i\theta_2}$$

on this copy of $S^1$. This is exactly the reflection of the circle across the real axis. The quotient $S^1 / (e^{i\theta} \sim e^{-i\theta})$ identifies each point with its conjugate. 

The map $e^{i\theta} \mapsto \cos\theta$ is a continuous surjection $S^1 \to [-1,1]$ that identifies exactly $e^{i\theta}$ with $e^{-i\theta}$ (and fixes $\pm 1$). Since $S^1$ is compact and $[-1,1]$ is Hausdorff, this is a quotient map, so:

$$S^1 / (e^{i\theta} \sim e^{-i\theta}) \cong [-1, 1].$$

**Step 2: Assemble the quotient.**

The total equivalence relation on $T^2 = S^1 \times S^1$ acts as the identity on the first factor and as the reflection on each fiber of the second factor. Therefore the quotient map is:

$$q: S^1 \times S^1 \to S^1 \times [-1,1], \qquad q(e^{i\theta_1}, e^{i\theta_2}) = (e^{i\theta_1}, \cos\theta_2).$$

This map is continuous, surjective, and identifies exactly the pairs $(e^{i\theta_1}, e^{i\theta_2})$ and $(e^{i\theta_1}, e^{-i\theta_2})$ — which is precisely $\sim$.

**Step 3: Verify it is a quotient map.**

Since $T^2 = S^1 \times S^1$ is compact and $S^1 \times [-1,1]$ is Hausdorff, any continuous surjection from $T^2$ onto $S^1 \times [-1,1]$ that induces the right identification is automatically a quotient map (compact-to-Hausdorff continuous bijections on quotients are homeomorphisms).

**Conclusion:**

$$T^2 / {\sim} \;\cong\; S^1 \times [-1, 1],$$

which is the **closed annulus** (cylinder). 

**Why this is surprising:** The torus is a closed manifold with no boundary. Yet after this simple reflection, the quotient acquires a boundary (the two boundary circles $S^1 \times \{-1\}$ and $S^1 \times \{1\}$, corresponding to $\theta_2 = \pi$ and $\theta_2 = 0$). The "identification" of boundary circles of each fiber creates actual boundary in the quotient — a vivid illustration of how quotient spaces can drastically change topological type.
