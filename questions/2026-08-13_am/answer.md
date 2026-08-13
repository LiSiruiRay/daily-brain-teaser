# Answer: The Holomorphic Map That Fixes Too Many Points

## Key Idea / Intuition

The Schwarz–Pick lemma tells us that any holomorphic self-map of the disk either is an automorphism (Möbius transformation) or strictly contracts the hyperbolic metric. If $f$ fixes two points, it cannot strictly contract — so it must be an automorphism. But the only automorphism of $\mathbb{D}$ that fixes two distinct interior points is the identity, because a Möbius transformation is completely determined by three points (and two fixed points plus the structure of the disk force it to be $\mathrm{id}$).

Alternatively, one can conjugate so that one fixed point moves to the origin, apply the Schwarz lemma, and find the map must be a rotation — but a rotation fixing a nonzero point must be trivial.

---

## Formal Proof / Solution

**Step 1: Reduce to fixing the origin.**

Let $\varphi_{z_1}(z) = \dfrac{z_1 - z}{1 - \overline{z_1} z}$ be the Möbius automorphism of $\mathbb{D}$ swapping $z_1$ and $0$. Note $\varphi_{z_1} \circ \varphi_{z_1} = \mathrm{id}$.

Define the conjugated map:
$$g = \varphi_{z_1} \circ f \circ \varphi_{z_1} : \mathbb{D} \to \mathbb{D}.$$

Then $g$ is holomorphic, $g(\mathbb{D}) \subseteq \mathbb{D}$, and $g(0) = \varphi_{z_1}(f(z_1)) = \varphi_{z_1}(z_1) = 0$.

So $g$ fixes the origin.

**Step 2: Apply the Schwarz lemma.**

Since $g: \mathbb{D} \to \mathbb{D}$ is holomorphic with $g(0) = 0$, the Schwarz lemma gives:
$$|g(z)| \leq |z| \quad \text{for all } z \in \mathbb{D},$$
with equality at any nonzero point (or $|g'(0)| = 1$) only if $g(z) = e^{i\theta} z$ for some $\theta \in \mathbb{R}$.

**Step 3: The second fixed point forces $g$ to be a rotation, then the identity.**

The second fixed point $z_2 \neq z_1$ is sent by $\varphi_{z_1}$ to $w_2 = \varphi_{z_1}(z_2) \neq 0$.

Since $f(z_2) = z_2$, we have:
$$g(w_2) = \varphi_{z_1}(f(\varphi_{z_1}(w_2))) = \varphi_{z_1}(f(z_2)) = \varphi_{z_1}(z_2) = w_2.$$

So $g$ fixes $w_2 \neq 0$ in $\mathbb{D}$.

By the Schwarz lemma, $|g(w_2)| \leq |w_2|$. But $g(w_2) = w_2$, so equality holds at a nonzero point. Therefore:
$$g(z) = e^{i\theta} z \quad \text{for some } \theta \in \mathbb{R}.$$

Now apply $g(w_2) = w_2$:
$$e^{i\theta} w_2 = w_2 \implies e^{i\theta} = 1 \implies g(z) = z.$$

**Step 4: Conclude $f = \mathrm{id}$.**

Since $g = \mathrm{id}$, we have:
$$\varphi_{z_1} \circ f \circ \varphi_{z_1} = \mathrm{id} \implies f = \varphi_{z_1} \circ \mathrm{id} \circ \varphi_{z_1} = \mathrm{id}. \qquad \blacksquare$$

---

**Remark.** This result is a clean illustration of the rigidity of the hyperbolic geometry of the disk: the group of automorphisms $\mathrm{Aut}(\mathbb{D})$ acts **simply transitively** on pairs (point, tangent direction), and a non-identity element can fix **at most one** interior point. Two interior fixed points is already "too much information" — it forces the map to collapse to the identity.
