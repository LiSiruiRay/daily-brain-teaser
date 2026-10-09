# Answer: 2026-10-08_am

## Key Idea / Intuition

The answer is **yes**. The key insight is the **Schwarz Reflection Principle**: if $f$ vanishes on a real-analytic arc of the boundary, we can reflect $f$ across that arc to produce a holomorphic extension to a larger domain. The original $f$ and its reflected extension agree on an open set, so by the identity theorem they agree everywhere — and since the reflection sends $f$ to $-f$ (up to conjugation), this forces $f \equiv 0$.

More concretely: the upper semicircle is a real-analytic arc. Vanishing on this arc (rather than just individual points) is enough for the identity theorem to kick in once we've extended $f$ analytically across it.

---

## Formal Proof / Solution

**Step 1: Reformulate as an extension problem.**

Define the function $g: \overline{\mathbb{D}} \to \mathbb{C}$ by reflection across the real axis. For $z \in \overline{\mathbb{D}}$, set

$$g(z) = \overline{f(\bar{z})}.$$

Note that $g$ is holomorphic on $\mathbb{D}$ (since $f$ is), and continuous on $\overline{\mathbb{D}}$.

**Step 2: Agreement on the arc.**

For $z = e^{i\theta}$ with $\theta \in [0, \pi]$ (i.e., $z \in A$), we have $\bar{z} = e^{-i\theta} \in A$ as well, since $-\theta \in [-\pi, 0]$, which corresponds to the **lower** semicircle... 

Let us be more careful. The arc $A = \{e^{i\theta} : \theta \in [0,\pi]\}$ is the upper semicircle. On $A$, $f(z) = 0$.

Now consider the **inversion map** $z \mapsto 1/\bar{z}$, which maps $\mathbb{D}$ to the exterior $\mathbb{C} \setminus \overline{\mathbb{D}}$ and fixes $\partial \mathbb{D}$ pointwise.

**Step 3: Use the Schwarz Reflection Principle directly.**

Since $A$ is a real-analytic arc and $f$ is continuous on $\overline{\mathbb{D}}$ and holomorphic on $\mathbb{D}$ with $f|_A = 0$, by the **Schwarz Reflection Principle** applied to the arc $A$, $f$ extends holomorphically across $A$ to a neighborhood of $A$.

More precisely: apply a Möbius transformation $\phi$ that maps the upper semicircle $A$ to a segment of the real line. Under $\phi$, $h = f \circ \phi^{-1}$ is holomorphic in a half-disk, continuous on the diameter, and vanishes on the diameter. By the Schwarz Reflection Principle for a flat boundary:

$$\tilde{h}(z) = \overline{h(\bar{z})}$$

extends $h$ to the full disk, and $\tilde{h}$ is holomorphic there. Since $h = 0$ on the diameter, we have $\tilde{h}(z) = \overline{h(\bar{z})} = 0$ on the diameter, so the extension satisfies $\tilde{h}(z) = -\tilde{h}(z)$... 

Let us use the cleanest argument:

**Step 4: The Identity Theorem argument.**

Since $f$ is holomorphic on $\mathbb{D}$ and continuous on $\overline{\mathbb{D}}$, and $f(e^{i\theta}) = 0$ for all $\theta \in [0,\pi]$, consider the function

$$F(z) = f(z) \cdot \overline{f(1/\bar{z})}.$$

But the cleanest approach uses the following classical fact:

> **Theorem.** If $f$ is holomorphic on $\mathbb{D}$, continuous on $\overline{\mathbb{D}}$, and $f$ vanishes on a subset of $\partial \mathbb{D}$ that has **positive measure** (equivalently, positive arc length), then $f \equiv 0$.

**Proof of the theorem:** Expand $f$ in a power series $f(z) = \sum_{n=0}^\infty a_n z^n$. The coefficients are recovered by the Cauchy formula:

$$a_n = \frac{1}{2\pi i} \oint_{\partial \mathbb{D}} \frac{f(z)}{z^{n+1}}\,dz = \frac{1}{2\pi} \int_0^{2\pi} f(e^{i\theta}) e^{-in\theta}\,d\theta.$$

Since $f(e^{i\theta}) = 0$ for $\theta \in [0, \pi]$ (half the circle), and $f(e^{i\theta})$ is bounded (continuous on compact set), the integral becomes:

$$a_n = \frac{1}{2\pi} \int_\pi^{2\pi} f(e^{i\theta}) e^{-in\theta}\,d\theta.$$

Now consider the Hardy space perspective: $f \in H^\infty(\mathbb{D}) \subset H^2(\mathbb{D})$. The boundary values of $f$ (which exist by continuity here) belong to $L^2(\partial \mathbb{D})$. A non-zero $H^2$ function cannot vanish on a set of positive measure on $\partial \mathbb{D}$ — this is the **F. and M. Riesz theorem**.

**F. and M. Riesz Theorem:** If $f \in H^1(\mathbb{D})$ (in particular if $f$ is holomorphic on $\mathbb{D}$ and continuous on $\overline{\mathbb{D}}$) and $f$ vanishes on a subset of $\partial \mathbb{D}$ of positive arc-length measure, then $f \equiv 0$.

The arc $A$ has arc-length measure $\pi > 0$, so the theorem applies directly.

**Why the F.–M. Riesz theorem holds (sketch):** The boundary function $f(e^{i\theta})$ has all its negative Fourier coefficients zero (since $f$ is analytic), i.e., $\hat{f}(n) = 0$ for $n < 0$. If $f$ also vanishes on a positive-measure set $E$, then $f \cdot \mathbf{1}_E = 0$. A function in $H^1$ whose real or imaginary part vanishes on a positive set must be identically zero, by a logarithmic integrability argument: if $f \not\equiv 0$, then $\log|f|$ is integrable on $\partial\mathbb{D}$ (a standard $H^1$ fact), but $\log|f| = -\infty$ on $E$ which has positive measure, giving a contradiction.

**Conclusion:** $f \equiv 0$ on $\mathbb{D}$.

---

**Summary:** The arc $A$ has positive arc-length, and the F. and M. Riesz theorem tells us that a non-trivial $H^1$ function cannot vanish on such a set. So **yes**, $f \equiv 0$.
