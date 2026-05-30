# Answer: Integral of x^n ln x and Basel

## Key Idea / Intuition

The key trick is **differentiation under the integral sign** (Feynman's trick): instead of integrating $x^n \ln x$ directly, notice that $x^n \ln x = \frac{\partial}{\partial n} x^n$. So we can turn the $\ln x$ factor into a derivative with respect to a parameter, evaluate a simpler integral first, then differentiate. The series $S$ then telescopes beautifully via a geometric series identity.

---

## Formal Proof / Solution

### Step 1: Compute $J = \int_0^1 x^n \ln x \, dx$

**Feynman's trick:** For $s > -1$, define

$$F(s) = \int_0^1 x^s \, dx = \frac{1}{s+1}.$$

Differentiate both sides with respect to $s$:

$$F'(s) = \int_0^1 x^s \ln x \, dx = -\frac{1}{(s+1)^2}.$$

Setting $s = n$ (integer $\geq 0$):

$$\boxed{J = \int_0^1 x^n \ln x \, dx = -\frac{1}{(n+1)^2}.}$$

**Check for $n=1$:** Integration by parts gives $\int_0^1 x\ln x\,dx = \left[\frac{x^2}{2}\ln x\right]_0^1 - \int_0^1 \frac{x}{2}\,dx = 0 - \frac{1}{4} = -\frac{1}{4}$. ✓ (Formula gives $-\frac{1}{(1+1)^2} = -\frac{1}{4}$.)

---

### Step 2: Compute the series $S$

$$S = \sum_{n=0}^{\infty} J_n = \sum_{n=0}^{\infty} \left(-\frac{1}{(n+1)^2}\right) = -\sum_{m=1}^{\infty} \frac{1}{m^2} = -\frac{\pi^2}{6}.$$

We can also swap sum and integral (justified by dominated convergence since $|\ln x| \leq C x^{-\epsilon}$):

$$S = \int_0^1 \ln x \sum_{n=0}^{\infty} x^n \, dx = \int_0^1 \frac{\ln x}{1-x} \, dx = -\frac{\pi^2}{6}.$$

This last integral $\displaystyle\int_0^1 \frac{\ln x}{1-x}\,dx = -\frac{\pi^2}{6}$ is itself a classic — it's essentially another derivation of **the Basel problem** $\zeta(2) = \pi^2/6$!

---

### Summary

| Integral | Value |
|---|---|
| $\int_0^1 x^n \ln x\,dx$ | $-\dfrac{1}{(n+1)^2}$ |
| $\sum_{n=0}^\infty \int_0^1 x^n \ln x\,dx$ | $-\dfrac{\pi^2}{6}$ |

The satisfying payoff: a natural-looking sum of elementary integrals secretly encodes the Basel sum $\zeta(2)$.
