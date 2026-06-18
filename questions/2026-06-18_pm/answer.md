# Answer: Schwarz–Pick Lemma: Holomorphic Maps Contract the Disk

## Key Idea / Intuition

The pseudo-hyperbolic distance $\rho(z, w) = \left|\frac{z-w}{1-\bar{w}z}\right|$ is precisely the quantity that **Möbius automorphisms of $\mathbb{D}$ preserve**. The strategy is: conjugate $f$ by two Möbius maps so that the resulting function fixes the origin, then apply the **Schwarz Lemma** (which says a holomorphic self-map of $\mathbb{D}$ fixing $0$ contracts distances from the origin). The inequality pops out automatically.

---

## Formal Proof / Solution

**Step 1: Recall the Möbius automorphisms of $\mathbb{D}$.**

For any $a \in \mathbb{D}$, define the automorphism

$$\varphi_a(z) = \frac{z - a}{1 - \bar{a}\, z}.$$

This is a biholomorphism $\mathbb{D} \to \mathbb{D}$ with $\varphi_a(a) = 0$, and $\varphi_a \circ \varphi_a = \mathrm{id}$.

**Step 2: Reduce to the Schwarz Lemma.**

Fix $w \in \mathbb{D}$ and define

$$g = \varphi_{f(w)} \circ f \circ \varphi_w : \mathbb{D} \to \mathbb{D}.$$

This is a holomorphic map from $\mathbb{D}$ to $\mathbb{D}$ (since $f : \mathbb{D} \to \mathbb{D}$ and $\varphi_{f(w)} : \mathbb{D} \to \mathbb{D}$), and

$$g(0) = \varphi_{f(w)}(f(\varphi_w(0))) = \varphi_{f(w)}(f(w)) = 0.$$

**Step 3: Apply the Schwarz Lemma.**

Since $g : \mathbb{D} \to \mathbb{D}$ is holomorphic with $g(0) = 0$, the **Schwarz Lemma** gives

$$|g(\zeta)| \leq |\zeta| \quad \text{for all } \zeta \in \mathbb{D}.$$

**Step 4: Unwind the conjugation.**

Set $\zeta = \varphi_w(z)$ (so $z = \varphi_w(\zeta)$). Then

$$g(\zeta) = \varphi_{f(w)}(f(z)).$$

The Schwarz bound becomes

$$|\varphi_{f(w)}(f(z))| \leq |\varphi_w(z)|,$$

which is exactly

$$\left| \frac{f(z) - f(w)}{1 - \overline{f(w)}\, f(z)} \right| \leq \left| \frac{z - w}{1 - \bar{w}\, z} \right|. \qquad \blacksquare$$

---

**Equality case.**

Equality $|g(\zeta)| = |\zeta|$ for *some* $\zeta \neq 0$ forces (by the equality case of the Schwarz Lemma) that $g(\zeta) = e^{i\theta}\zeta$ for some $\theta \in \mathbb{R}$, i.e., $g$ is a rotation. Unwinding, $f$ itself must be a **Möbius automorphism** of $\mathbb{D}$. Thus:

> Equality holds (for some $z \neq w$) if and only if $f$ is a biholomorphic automorphism of $\mathbb{D}$ — i.e., $f(z) = e^{i\theta} \varphi_a(z)$ for some $a \in \mathbb{D}$ and $\theta \in \mathbb{R}$.

---

**Geometric punchline.** The Schwarz–Pick Lemma says that $\mathbb{D}$ equipped with the **Poincaré (hyperbolic) metric** $ds = \frac{2|dz|}{1-|z|^2}$ has the property that **every holomorphic self-map is a contraction** (isometry iff it's an automorphism). This is a cornerstone of hyperbolic geometry and complex dynamics.
