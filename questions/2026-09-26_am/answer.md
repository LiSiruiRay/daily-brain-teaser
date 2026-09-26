# Answer: The Integral That Sums Geometric Angles

## Key Idea / Intuition

The integrand $\frac{\ln x}{x^2-1}$ looks intimidating, but a geometric series expansion of $\frac{1}{1-x^2}$ (or $\frac{1}{x^2-1}$, handled carefully) turns the integral into a sum of elementary integrals of the form $\int_0^1 x^{2k} \ln x\, dx$. Each such integral is computable in closed form, and the resulting series is a well-known one — the Basel cousin that gives $\pi^2/8$.

---

## Formal Proof / Solution

**Step 1: Handle the sign and expand.**

On $(0,1)$ we have $x^2 < 1$, so $x^2 - 1 < 0$ and $\ln x < 0$, making the integrand positive. Write

$$\frac{\ln x}{x^2 - 1} = \frac{-\ln x}{1 - x^2} = (-\ln x)\sum_{k=0}^{\infty} x^{2k}, \quad 0 < x < 1.$$

Since all terms $(-\ln x)\, x^{2k} \geq 0$ on $(0,1)$, the interchange of sum and integral is justified by the Monotone Convergence Theorem (or Tonelli's theorem):

$$I = \sum_{k=0}^{\infty} \int_0^1 (-\ln x)\, x^{2k}\, dx.$$

**Step 2: Evaluate the inner integral.**

For each $k \geq 0$, integrate by parts (or use the standard formula):

$$\int_0^1 x^{2k}(-\ln x)\, dx = \int_0^1 x^{2k}(-\ln x)\, dx.$$

Let $u = -\ln x$, $dv = x^{2k}\,dx$, so $du = -\frac{1}{x}dx$, $v = \frac{x^{2k+1}}{2k+1}$:

$$= \left[-\frac{x^{2k+1}\ln x}{2k+1}\right]_0^1 + \int_0^1 \frac{x^{2k}}{2k+1}\, dx = 0 + \frac{1}{(2k+1)^2}.$$

(The boundary term at $x=1$ is $0$; at $x=0$, $x^{2k+1}\ln x \to 0$.)

**Step 3: Sum the series.**

$$I = \sum_{k=0}^{\infty} \frac{1}{(2k+1)^2} = 1 + \frac{1}{9} + \frac{1}{25} + \cdots$$

This is the sum over odd squares. Using the Basel result $\sum_{n=1}^{\infty}\frac{1}{n^2} = \frac{\pi^2}{6}$ and the fact that

$$\sum_{k=1}^{\infty}\frac{1}{(2k)^2} = \frac{1}{4}\cdot\frac{\pi^2}{6} = \frac{\pi^2}{24},$$

we get

$$\sum_{k=0}^{\infty} \frac{1}{(2k+1)^2} = \frac{\pi^2}{6} - \frac{\pi^2}{24} = \frac{\pi^2}{8}.$$

**Result:**

$$\boxed{I = \dfrac{\pi^2}{8}.}$$
