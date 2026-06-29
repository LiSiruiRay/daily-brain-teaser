# Answer: Conditionally Convergent Series of Functions: Pointwise but Not Uniform

## Key Idea / Intuition

The series converges pointwise by the **Dirichlet test**: the partial sums of $\sin(nx)$ are bounded (they satisfy a telescoping geometric sum estimate) and $1/n \searrow 0$. But uniform convergence fails because near $x = 0$ the terms $\sin(nx)/n$ don't die uniformly — you can always find an $x$ small enough that the partial sums are large. In short: pointwise convergence can hold everywhere while uniform convergence fails because the "trouble spot" chases $x \to 0$.

---

## Formal Proof / Solution

### Part (a): Pointwise Convergence

Fix $x \in (0, 2\pi)$. We apply the **Dirichlet test for series**: if $b_n = 1/n \searrow 0$ and the partial sums $A_N(x) = \sum_{n=1}^N (-1)^n \sin(nx)$ are bounded in $N$, then the series converges.

We bound the partial sums using the identity
$$\sum_{n=1}^N (-1)^n \sin(nx) = \text{Im}\!\left(\sum_{n=1}^N (-e^{ix})^n\right) = \text{Im}\!\left(\frac{-e^{ix}(1-(-e^{ix})^N)}{1+e^{ix}}\right).$$

Since $x \in (0, 2\pi)$, we have $e^{ix} \neq -1$, so $|1 + e^{ix}| = 2|\cos(x/2)| > 0$. Therefore
$$|A_N(x)| \leq \frac{2}{|1 + e^{ix}|} = \frac{1}{|\cos(x/2)|} < \infty.$$

This bound is finite for each fixed $x \in (0, 2\pi)$, so by the Dirichlet test, the series converges pointwise. $\checkmark$

---

### Part (b): Convergence Is Not Uniform

Suppose for contradiction the convergence were uniform on $(0, 2\pi)$. Then the partial sums
$$S_N(x) = \sum_{n=1}^{N} \frac{(-1)^n}{n}\sin(nx)$$
satisfy $\sup_{x \in (0,2\pi)} |f(x) - S_N(x)| \to 0$.

In particular, the **tail** $R_N(x) = f(x) - S_N(x)$ would go to zero uniformly, so in particular $S_N(x)$ would be uniformly Cauchy, meaning

$$\sup_{x \in (0,2\pi)} \left|\sum_{n=N+1}^{M} \frac{(-1)^n}{n}\sin(nx)\right| \to 0 \quad \text{as } N \to \infty.$$

Now consider the single term remainder: take $M = N+1$, so we need
$$\sup_{x \in (0,2\pi)} \left|\frac{(-1)^{N+1}}{N+1}\sin((N+1)x)\right| = \frac{1}{N+1}\sup_{x} |\sin((N+1)x)| = \frac{1}{N+1} \to 0.$$

This part is fine. The real issue is more subtle — let us use a **necessary condition for uniform convergence**.

**Key test:** If $\sum f_n$ converges uniformly on $(0,2\pi)$, then $\sup_x |f_n(x)| \to 0$. Here $f_n(x) = \frac{(-1)^n}{n}\sin(nx)$, and
$$\sup_{x \in (0,2\pi)} \left|\frac{\sin(nx)}{n}\right| = \frac{1}{n} \to 0.$$
This is consistent, so this test does not immediately give a contradiction. We need a sharper argument.

**Better approach — look at $S_N$ near $x = 0$.**

It is a classical fact (Fourier series of a sawtooth) that the series $\sum_{n=1}^\infty \frac{(-1)^{n+1}}{n}\sin(nx)$ represents $x/2$ on $(-\pi, \pi)$. Rearranging signs,

$$\sum_{n=1}^{\infty} \frac{(-1)^n}{n}\sin(nx) = -\frac{x}{2}, \quad x \in (0, 2\pi).$$

So $f(x) = -x/2$, which is **continuous** on $(0,2\pi)$ but has a jump discontinuity at $0$ and $2\pi$.

Now, each partial sum $S_N(x)$ is a finite sum of continuous functions, hence continuous and bounded on $[0, 2\pi]$ with $S_N(0) = 0$ for all $N$.

If $S_N \to f = -x/2$ uniformly on $(0, 2\pi)$, then $f$ would extend to a continuous function on $[0, 2\pi]$ (as the uniform limit of continuous functions). But $f(x) = -x/2 \to 0$ as $x \to 0^+$ while we also have $S_N(0) = 0$ for all $N$. So far no contradiction.

**The actual non-uniformity is near $x = 2\pi$:** As $x \to 2\pi^-$, $f(x) = -x/2 \to -\pi$, but $S_N(2\pi) = 0$ for all $N$ (since $\sin(2\pi n) = 0$). So

$$\sup_{x \in (0, 2\pi)} |f(x) - S_N(x)| \geq \lim_{x \to 2\pi^-} |{-x/2} - S_N(x)| = |-\pi - 0| = \pi.$$

This shows $\sup |f - S_N| \geq \pi > 0$ for all $N$, so convergence is **not** uniform. $\blacksquare$

---

### Summary

| | What holds |
|---|---|
| Pointwise convergence on $(0,2\pi)$ | ✓ (Dirichlet test) |
| Uniform convergence on $(0,2\pi)$ | ✗ (limit function has a boundary jump) |

The moral: the Weierstrass M-test is **sufficient but not necessary** for uniform convergence. Conditional convergence (via Dirichlet) gives pointwise results, but the boundary behavior can destroy uniformity.
