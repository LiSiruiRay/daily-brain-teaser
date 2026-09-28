# Answer: The Integral That Knows Its Own Symmetry

## Key Idea / Intuition

The integrand looks tricky because of the $x^2 - 1$ in the denominator, which vanishes at $x=1$. The key is to recognize that $\frac{1}{x^2-1} = -\frac{1}{1-x^2}$, and then expand as a geometric series in $x^2$. This converts the integral into a sum of elementary moments $\int_0^1 x^{2k} \ln x \, dx$, each of which is easily computed by integration by parts. The resulting series is a famous one — it evaluates to $\frac{\pi^2}{8}$.

---

## Formal Proof / Solution

**Step 1: Rewrite the denominator.**

$$I = \int_0^1 \frac{\ln x}{x^2 - 1} \, dx = -\int_0^1 \frac{\ln x}{1 - x^2} \, dx.$$

Note: at $x = 1$, $\ln x = 0$ and $1 - x^2 = 0$, but by L'Hôpital the integrand $\to \frac{-1}{-2} = \frac{1}{2}$, so the singularity is removable and the integral converges.

**Step 2: Geometric series expansion.**

For $0 \le x < 1$:

$$\frac{1}{1 - x^2} = \sum_{k=0}^{\infty} x^{2k}.$$

So

$$I = -\int_0^1 \ln x \sum_{k=0}^{\infty} x^{2k} \, dx = -\sum_{k=0}^{\infty} \int_0^1 x^{2k} \ln x \, dx.$$

(Interchange is justified by dominated convergence / monotone convergence, since $\ln x \le 0$ on $(0,1)$.)

**Step 3: Compute each moment.**

By integration by parts (or the formula $\int_0^1 x^n \ln x \, dx = -\frac{1}{(n+1)^2}$):

$$\int_0^1 x^{2k} \ln x \, dx = \left[\frac{x^{2k+1}}{2k+1} \ln x\right]_0^1 - \int_0^1 \frac{x^{2k}}{2k+1} \, dx = 0 - \frac{1}{(2k+1)^2}.$$

**Step 4: Sum the series.**

$$I = -\sum_{k=0}^{\infty} \left(-\frac{1}{(2k+1)^2}\right) = \sum_{k=0}^{\infty} \frac{1}{(2k+1)^2}.$$

This is the sum over odd positive integers of $\frac{1}{n^2}$. Since

$$\sum_{n=1}^{\infty} \frac{1}{n^2} = \frac{\pi^2}{6}, \quad \sum_{k=1}^{\infty} \frac{1}{(2k)^2} = \frac{1}{4} \cdot \frac{\pi^2}{6} = \frac{\pi^2}{24},$$

we get

$$\sum_{k=0}^{\infty} \frac{1}{(2k+1)^2} = \frac{\pi^2}{6} - \frac{\pi^2}{24} = \frac{\pi^2}{8}.$$

**Conclusion:**

$$\boxed{I = \dfrac{\pi^2}{8}.}$$

The beautiful surprise: a completely elementary-looking integral on $[0,1]$ hides $\pi^2$ inside it, and the bridge is the Basel-type sum over odd integers.
