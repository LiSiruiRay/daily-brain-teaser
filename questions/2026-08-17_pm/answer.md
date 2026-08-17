# Answer: The Sinc Integral: Conditional but Not Absolute

## Key Idea / Intuition

Part (b) captures a beautiful tension: $\sin x / x$ is integrable on $[0,\infty)$ only because of **cancellation** between positive and negative arches — the function is *not* absolutely integrable. This is the continuous analogue of a conditionally-but-not-absolutely convergent series. For part (c), the slickest route is **Feynman's trick** (differentiation under the integral sign): introduce a parameter $e^{-tx}$ to damp the integral, differentiate with respect to $t$, solve the resulting elementary integral, then let $t \to 0^+$.

---

## Formal Proof / Solution

### Part (a): Convergence

Write $I = \lim_{R\to\infty}\int_0^R \frac{\sin x}{x}\,dx$. Integrate by parts with $u = 1/x$, $dv = \sin x\,dx$:

$$\int_1^R \frac{\sin x}{x}\,dx = \left[-\frac{\cos x}{x}\right]_1^R - \int_1^R \frac{\cos x}{x^2}\,dx.$$

The boundary term $\to \cos 1$ as $R\to\infty$, and $\int_1^\infty |\cos x|/x^2\,dx \leq \int_1^\infty x^{-2}\,dx < \infty$. So the tail converges. Near $0$, the function $(\sin x)/x \to 1$ is bounded and continuous, so $\int_0^1$ is finite. Hence $I$ converges. $\checkmark$

---

### Part (b): Not Absolutely Convergent

On each interval $[k\pi, (k+1)\pi]$, $|\sin x| \geq 0$ and

$$\int_{k\pi}^{(k+1)\pi} \frac{|\sin x|}{x}\,dx \geq \frac{1}{(k+1)\pi}\int_{k\pi}^{(k+1)\pi}|\sin x|\,dx = \frac{2}{(k+1)\pi}.$$

(The last equality uses $\int_0^\pi \sin x\,dx = 2$.) Summing over $k = 0, 1, 2, \ldots$:

$$\int_0^\infty \frac{|\sin x|}{x}\,dx \geq \sum_{k=0}^\infty \frac{2}{(k+1)\pi} = \frac{2}{\pi}\sum_{k=1}^\infty \frac{1}{k} = +\infty.$$

So the integral diverges absolutely. $\checkmark$

---

### Part (c): Evaluation via Feynman's Trick

**Step 1.** Define
$$F(t) = \int_0^\infty \frac{\sin x}{x}\,e^{-tx}\,dx, \quad t > 0.$$

The factor $e^{-tx}$ ensures absolute convergence for every $t > 0$, so differentiation under the integral is justified.

**Step 2.** Differentiate:
$$F'(t) = -\int_0^\infty \sin(x)\,e^{-tx}\,dx.$$

This is a standard Laplace transform. Integrating by parts twice (or using the known formula):

$$\int_0^\infty e^{-tx}\sin x\,dx = \frac{1}{1+t^2}.$$

Hence $F'(t) = -\dfrac{1}{1+t^2}$.

**Step 3.** Integrate:
$$F(t) = -\arctan(t) + C.$$

As $t \to +\infty$, $F(t) \to 0$ (by dominated convergence or the Riemann–Lebesgue lemma), so $C = \pi/2$.

$$F(t) = \frac{\pi}{2} - \arctan(t).$$

**Step 4.** Take $t \to 0^+$. One can justify $F(t) \to I$ (the dominated convergence theorem applies after part (a)'s analysis, or by the monotone convergence theorem for the absolute value). Thus:

$$\boxed{I = \int_0^\infty \frac{\sin x}{x}\,dx = \frac{\pi}{2}.}$$

---

### Summary Table

| Part | Key Tool | Result |
|------|----------|--------|
| (a) | Integration by parts + comparison | $I$ converges |
| (b) | Arch-by-arch lower bound + harmonic series | Not absolutely convergent |
| (c) | Feynman trick (Laplace parameter) | $I = \pi/2$ |
