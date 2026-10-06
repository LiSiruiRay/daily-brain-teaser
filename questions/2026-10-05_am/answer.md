# Answer: Vanishing Fourier Coefficients Force Zero

## Key Idea / Intuition

The key insight is a two-step bootstrap: **trigonometric polynomials are dense in continuous functions** (Weierstrass's theorem), so if $f$ is orthogonal to every complex exponential $e^{inx}$, it is orthogonal to every trig polynomial, and hence to itself — which forces $\|f\|^2 = 0$.

More concretely, the Weierstrass approximation theorem for trig polynomials says we can find $p_n \to f$ uniformly. Since $\int f \cdot e^{ikx} = 0$ for all $k$, we get $\int f \cdot p_n = 0$ for all $n$. Passing to the limit gives $\int f \cdot f = 0$.

---

## Formal Proof / Solution

**Step 1: Orthogonality extends to all trig polynomials.**

A trigonometric polynomial is any finite linear combination
$$T(x) = \sum_{|k| \le N} c_k e^{ikx}.$$
By linearity of the integral and the hypothesis $\hat{f}(k) = 0$ for all $k$:
$$\int_0^{2\pi} f(x)\, T(x)\, dx = \sum_{|k|\le N} \bar{c}_k \int_0^{2\pi} f(x)\, e^{ikx}\, dx = \sum_{|k|\le N} \bar{c}_k \cdot 2\pi\, \overline{\hat{f}(-k)} = 0.$$

Wait — more cleanly: $\int_0^{2\pi} f(x)\, e^{ikx}\,dx = 2\pi\,\widehat{f}(-k) = 0$, so indeed $\int f \cdot T = 0$ for every trig polynomial $T$.

**Step 2: Approximate $\overline{f}$ uniformly by trig polynomials.**

By the **Weierstrass theorem for trigonometric polynomials** (which follows from the ordinary polynomial version via $x \mapsto e^{ix}$, or from Fejér's theorem on Cesàro means of the Fourier series of continuous functions):

For any $\varepsilon > 0$, there exists a trig polynomial $T_\varepsilon$ such that
$$\|T_\varepsilon - \overline{f}\|_\infty < \varepsilon.$$

**Step 3: Conclude $f \equiv 0$.**

Consider
$$\int_0^{2\pi} |f(x)|^2\, dx = \int_0^{2\pi} f(x)\, \overline{f(x)}\, dx.$$

Write $\overline{f} = T_\varepsilon + (\overline{f} - T_\varepsilon)$. Then:
$$\int_0^{2\pi} f(x)\,\overline{f(x)}\,dx = \underbrace{\int_0^{2\pi} f(x)\,T_\varepsilon(x)\,dx}_{=\,0 \text{ by Step 1}} + \int_0^{2\pi} f(x)\,(\overline{f(x)} - T_\varepsilon(x))\,dx.$$

The error term satisfies:
$$\left|\int_0^{2\pi} f(x)\,(\overline{f(x)} - T_\varepsilon(x))\,dx\right| \le \|f\|_\infty \cdot \|\overline{f} - T_\varepsilon\|_\infty \cdot 2\pi < \|f\|_\infty \cdot \varepsilon \cdot 2\pi.$$

Since $\varepsilon > 0$ is arbitrary:
$$\int_0^{2\pi} |f(x)|^2\, dx = 0.$$

Since $|f|^2$ is continuous and non-negative, this forces $f \equiv 0$. $\blacksquare$

---

**Why this is the "right" proof:** It reveals that the true reason is density, not Hilbert space abstraction. The continuous functions are a metric space; the trig polynomials are a dense subspace; and the linear functional $T \mapsto \int fT$ is bounded and zero on a dense set, hence zero everywhere — including when $T = \overline{f}$.
