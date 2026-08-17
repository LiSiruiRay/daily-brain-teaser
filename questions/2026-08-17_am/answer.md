# Answer: The Integral That Knows Γ

## Key Idea / Intuition

The key trick is **differentiation under the integral sign with respect to a parameter**. The Gamma function $\Gamma(s) = \int_0^\infty x^{s-1} e^{-x} dx$ already contains $x^{s-1}$, and differentiating $x^{s-1} = e^{(s-1)\ln x}$ with respect to $s$ pulls down exactly one factor of $\ln x$. So the integral $I$ is literally $\Gamma'(s)$, which connects it immediately to the digamma function.

---

## Formal Proof / Solution

**Step 1: Recall the Gamma function.**

$$\Gamma(s) = \int_0^\infty x^{s-1} e^{-x} \, dx, \quad s > 0.$$

**Step 2: Differentiate under the integral sign.**

Write $x^{s-1} = e^{(s-1) \ln x}$. Differentiating formally with respect to $s$:

$$\frac{d}{ds} \Gamma(s) = \frac{d}{ds} \int_0^\infty x^{s-1} e^{-x} \, dx = \int_0^\infty \frac{\partial}{\partial s} \left( x^{s-1} e^{-x} \right) dx.$$

Since $\frac{\partial}{\partial s} x^{s-1} = x^{s-1} \ln x$, we get:

$$\Gamma'(s) = \int_0^\infty x^{s-1} e^{-x} \ln x \, dx.$$

**Step 3: Justify the differentiation.**

To swap differentiation and integration, we need dominated convergence. For $s$ in a compact interval $[\delta, M]$ with $0 < \delta \leq M < \infty$, the integrand satisfies:

$$\left| x^{s-1} e^{-x} \ln x \right| \leq C_{\delta, M} \left( x^{\delta/2 - 1} + x^{M} e^{-x/2} \right),$$

which is integrable on $(0,\infty)$. So the swap is valid for all $s > 0$.

**Step 4: Conclusion.**

$$\boxed{I = \Gamma'(s) = \Gamma(s) \, \psi(s),}$$

where $\psi(s) = \dfrac{\Gamma'(s)}{\Gamma(s)}$ is the **digamma function**.

**Special case:** At $s = 1$, $\Gamma(1) = 1$ and $\psi(1) = -\gamma$ (the Euler–Mascheroni constant), so:

$$\int_0^\infty e^{-x} \ln x \, dx = \Gamma'(1) = \psi(1) \cdot \Gamma(1) = -\gamma \approx -0.5772\ldots$$

This is a classical and beautiful result: integrating $e^{-x} \ln x$ against the simplest exponential weight recovers the Euler–Mascheroni constant exactly.
