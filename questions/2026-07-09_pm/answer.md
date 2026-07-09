# Answer: The Harmonic Function That Knows Its Boundary

## Key Idea / Intuition

The value of a harmonic function at the center of the disk is the **average** of its boundary values — this is the mean value property. So $u(0)$ is simply the average of $u$ over the unit circle. Since $u$ is zero on the upper half and non-negative on the lower half, the average is automatically non-negative. The exact formula drops out immediately from the mean value theorem.

---

## Formal Proof / Solution

**Step 1: The Mean Value Property.**

For any function $u$ that is continuous on $\overline{\mathbb{D}}$ and harmonic on $\mathbb{D}$, the **mean value property** states:

$$u(0) = \frac{1}{2\pi} \int_0^{2\pi} u(e^{i\theta})\, d\theta.$$

This is one of the most fundamental facts in complex analysis: the value at the center equals the average over any centered circle.

**Step 2: Split the integral by the two semicircles.**

$$u(0) = \frac{1}{2\pi} \int_0^{\pi} u(e^{i\theta})\, d\theta + \frac{1}{2\pi} \int_{\pi}^{2\pi} u(e^{i\theta})\, d\theta.$$

The first integral vanishes (since $u = 0$ on the upper semicircle), giving:

$$u(0) = \frac{1}{2\pi} \int_{\pi}^{2\pi} u(e^{i\theta})\, d\theta.$$

**Step 3: Sign.**

Since $u \geq 0$ on the lower semicircle $\{e^{i\theta} : \pi \leq \theta \leq 2\pi\}$, the integrand is non-negative, hence:

$$u(0) = \frac{1}{2\pi} \int_{\pi}^{2\pi} u(e^{i\theta})\, d\theta \geq 0.$$

**Conclusion.**

Yes, $u(0) \geq 0$ is guaranteed, with equality if and only if $u \equiv 0$ on the lower semicircle as well (which by the maximum principle would force $u \equiv 0$ everywhere).

The **exact value** is:

$$\boxed{u(0) = \frac{1}{2\pi} \int_{\pi}^{2\pi} u(e^{i\theta})\, d\theta.}$$

**Why this is beautiful:** The mean value property gives a *global* conclusion ($u(0) \geq 0$) from *local* boundary information, with no computation needed — just the realization that the center "sees" the boundary democratically and equally in every direction.
