# Answer: The Integral That Knows Its Own Interval

## Key Idea / Intuition

At first glance, the integrand has a singularity at both $x = 0$ (where $\ln x \to -\infty$) and $x = 1$ (where $x - 1 \to 0$). But both are removable in the sense that the integrand stays integrable — the two singularities "cooperate." The key trick is to expand $\frac{1}{1-x}$ as a geometric series and integrate term by term, turning the integral into a famous sum: $\sum_{n=1}^\infty \frac{1}{n^2} = \frac{\pi^2}{6}$.

---

## Formal Proof / Solution

**Step 1: Rewrite the integrand.**

Note that $\frac{\ln x}{x-1} = \frac{-\ln x}{1-x}$, and for $0 < x < 1$ we have the geometric series:
$$\frac{1}{1-x} = \sum_{n=0}^{\infty} x^n.$$

So:
$$\frac{\ln x}{x-1} = -\ln x \cdot \sum_{n=0}^{\infty} x^n = \sum_{n=0}^{\infty} (-x^n \ln x).$$

**Step 2: Check that term-by-term integration is valid.**

Each term $-x^n \ln x \geq 0$ on $(0,1)$ (since $\ln x \leq 0$ there). By the Monotone Convergence Theorem, we may interchange sum and integral:
$$I = \sum_{n=0}^{\infty} \int_0^1 (-x^n \ln x)\, dx.$$

**Step 3: Compute each term.**

For fixed $n \geq 0$:
$$\int_0^1 x^n (-\ln x)\, dx.$$

Use the substitution $x = e^{-t}$, $dx = -e^{-t}\,dt$:
$$\int_0^\infty e^{-nt} \cdot t \cdot e^{-t}\, dt = \int_0^\infty t\, e^{-(n+1)t}\, dt = \frac{1}{(n+1)^2},$$

where we used $\int_0^\infty t\, e^{-at}\, dt = \frac{1}{a^2}$ for $a > 0$.

**Step 4: Sum the series.**

$$I = \sum_{n=0}^{\infty} \frac{1}{(n+1)^2} = \sum_{m=1}^{\infty} \frac{1}{m^2} = \frac{\pi^2}{6}.$$

**Conclusion:**
$$\boxed{I = \int_0^1 \frac{\ln x}{x-1}\,dx = \frac{\pi^2}{6}.}$$

**Why this is beautiful:** The integral secretly encodes all the information of the Basel problem. Both singularities at $x=0$ and $x=1$ are integrable (the integrand extends continuously to the value $1$ at $x=1$ and vanishes at $x=0$), and the geometric series expansion converts the analytic problem into an arithmetic one.
