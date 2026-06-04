# Answer: Maximum Modulus & Schwarz Equality Case

## Key Idea / Intuition

A holomorphic function cannot have an interior maximum of its modulus unless it is **constant** — this is the Maximum Modulus Principle. The reason is deep: holomorphic functions satisfy the **mean value property**, so the value at the center of any disk is the average of values on the boundary circle. If the modulus achieves a maximum at an interior point, the averaging forces all nearby values to have the same modulus, which then forces $f$ to be constant via the open mapping theorem.

The second part is precisely the **Schwarz Lemma** (previously given), but here we derive the equality case from the maximum modulus principle directly.

---

## Formal Proof / Solution

### Part 1: $f$ Must Be Constant

**Theorem (Maximum Modulus Principle):** If $f$ is holomorphic and non-constant on a connected open set $U$, then $|f|$ has no local maximum in $U$.

**Proof sketch via the mean value property:**

For any disk $\overline{D}(z_0, r) \subset U$, the mean value property gives:
$$f(z_0) = \frac{1}{2\pi} \int_0^{2\pi} f(z_0 + re^{i\theta})\, d\theta.$$

Taking moduli:
$$|f(z_0)| \leq \frac{1}{2\pi} \int_0^{2\pi} |f(z_0 + re^{i\theta})|\, d\theta.$$

If $|f(z_0)|$ is a maximum, then $|f(z_0)| \geq |f(z)|$ for all $z$ near $z_0$, so equality holds in the above. Equality in this integral inequality for a continuous function means $|f(z_0 + re^{i\theta})| = |f(z_0)|$ for **all** $\theta$ — the modulus is constantly equal to $|f(z_0)|$ on the circle.

Since $r > 0$ was arbitrary, $|f|$ is locally constant near $z_0$. By the **open mapping theorem**, $f$ must be constant (a non-constant holomorphic map is open, hence cannot have constant modulus on any open set).

**Conclusion for Part 1:** $f \equiv c$ for some constant $c$ with $|c| = 1$.

---

### Part 2: The Schwarz Equality Case

Now $f : \mathbb{D} \to \mathbb{D}$ is holomorphic, $f(0) = 0$, and $|f(z_0)| = |z_0|$ for some $z_0 \neq 0$.

Define $g(z) = \frac{f(z)}{z}$ for $z \neq 0$ and $g(0) = f'(0)$. Then $g$ is holomorphic on $\mathbb{D}$ (the singularity at $0$ is removable since $f(0) = 0$).

On the boundary $|z| = 1$: since $f : \mathbb{D} \to \mathbb{D}$, we get $|f(z)| \leq 1 = |z|$, so $|g(z)| \leq 1$.

By the Maximum Modulus Principle applied to $g$:
$$|g(z)| \leq 1 \quad \text{for all } z \in \mathbb{D},$$
which gives $|f(z)| \leq |z|$ — this is the Schwarz Lemma.

Now, the assumption $|f(z_0)| = |z_0|$ means $|g(z_0)| = 1$.

So $g$ achieves modulus $1$ at an **interior point** $z_0 \in \mathbb{D}$.

By Part 1 (Maximum Modulus Principle), $g$ must be **constant**:
$$g(z) = e^{i\theta} \quad \text{for some } \theta \in \mathbb{R}.$$

Therefore:
$$\boxed{f(z) = e^{i\theta} z,}$$
i.e., $f$ is a **rotation**. $\blacksquare$

---

### Why This Is Beautiful

The maximum modulus principle says holomorphic functions are "anti-extremal" in the interior — all extremes happen on the boundary. The equality case of Schwarz reveals that the only holomorphic self-maps of the disk fixing $0$ and touching the "size bound" $|f(z)| = |z|$ anywhere are rigid rotations. The mean value averaging property of holomorphic functions is doing all the heavy lifting.
