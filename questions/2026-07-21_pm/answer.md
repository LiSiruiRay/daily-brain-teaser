# Answer: The Quotient of a Torus by an Involution

## Key Idea / Intuition

Think of $T^2$ as a product: the involution only acts on the first $S^1$ factor, leaving the second alone. So the quotient is really doing $(S^1/\mathbb{Z}_2) \times S^1$. The key observation is that identifying antipodal points on a circle collapses it to another circle — not a sphere — because $S^1/\mathbb{Z}_2 \cong S^1$. Putting the two circles back together gives another torus!

This is a genuinely surprising answer: quotienting $T^2$ by a natural involution gives back $T^2$ itself.

---

## Formal Proof / Solution

**Step 1: Decompose the action.**

Since $\varphi(z, w) = (-z, w)$, the action is the product of the map $z \mapsto -z$ on the first factor and the identity on the second factor. Therefore:

$$T^2 / \mathbb{Z}_2 = (S^1 \times S^1) / ({\mathbb{Z}_2 \times \{e\}}) \cong (S^1/\mathbb{Z}_2) \times S^1.$$

This factoring of quotients is valid because the group acts on each fiber $S^1 \times \{w\}$ independently, and the action is free and proper.

**Step 2: Identify $S^1 / \mathbb{Z}_2$.**

Represent $S^1 = \{e^{i\theta} : \theta \in [0, 2\pi)\}$. The involution sends $e^{i\theta} \mapsto e^{i(\theta + \pi)}$, i.e., antipodal rotation by $\pi$.

Consider the map:
$$f: S^1 \to S^1, \qquad e^{i\theta} \mapsto e^{2i\theta}.$$

This map satisfies $f(e^{i\theta}) = f(e^{i(\theta+\pi)})$ (since $e^{2i(\theta+\pi)} = e^{2i\theta}$), so it factors through the quotient:

$$S^1 \xrightarrow{\pi} S^1/\mathbb{Z}_2 \xrightarrow{\bar{f}} S^1.$$

The induced map $\bar{f}$ is a continuous bijection from the compact Hausdorff space $S^1/\mathbb{Z}_2$ to $S^1$, hence a **homeomorphism**:

$$S^1/\mathbb{Z}_2 \cong S^1.$$

Intuitively: $e^{i\theta}$ and $e^{i(\theta+\pi)}$ get identified, so the equivalence classes are parametrized by $\theta \in [0, \pi)$, which is itself a circle when you wrap it around.

**Step 3: Conclude.**

$$T^2/\mathbb{Z}_2 \cong (S^1/\mathbb{Z}_2) \times S^1 \cong S^1 \times S^1 = T^2.$$

**The quotient is again a torus.**

---

## Why This Is Surprising

One might expect the quotient to be "smaller" or more degenerate (like a Klein bottle or $S^2 \times S^1$). Instead, the torus is self-similar under this involution. Compare with the antipodal map on both factors simultaneously: $\varphi(z,w) = (-z,-w)$, which gives the quotient $T^2/\mathbb{Z}_2 \cong$ Klein bottle — a genuinely different space.
