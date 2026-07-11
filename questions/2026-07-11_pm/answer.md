# Answer: The Dirichlet Beta Integral

## Key Idea / Intuition

Near $x=1$ the denominator $x^2-1$ vanishes, but so does the numerator $\ln x$, so the integrand is actually continuous there — no real singularity. The trick is to expand $\frac{1}{1-x^2}$ as a geometric series in $x^2$, interchange sum and integral, and recognise the resulting series as a classical constant: $\frac{\pi^2}{8}$.

---

## Formal Proof / Solution

**Step 1: Rewrite the sign.**

Note $x^2 - 1 < 0$ on $(0,1)$ and $\ln x < 0$ on $(0,1)$, so the integrand is positive. Write:

$$I = \int_0^1 \frac{\ln x}{x^2-1}\,dx = \int_0^1 \frac{-\ln x}{1-x^2}\,dx$$

**Step 2: Expand as a geometric series.**

For $0 \le x < 1$:

$$\frac{1}{1-x^2} = \sum_{n=0}^{\infty} x^{2n}$$

So:

$$I = -\int_0^1 \ln x \sum_{n=0}^{\infty} x^{2n}\,dx = \sum_{n=0}^{\infty} \left(-\int_0^1 x^{2n}\ln x\,dx\right)$$

The interchange is justified by the monotone convergence theorem (all terms are positive).

**Step 3: Evaluate each term.**

For any $\alpha > -1$:

$$\int_0^1 x^\alpha \ln x\,dx = \frac{-1}{(\alpha+1)^2}$$

(Differentiate $\int_0^1 x^\alpha dx = \frac{1}{\alpha+1}$ with respect to $\alpha$.)

With $\alpha = 2n$:

$$-\int_0^1 x^{2n}\ln x\,dx = \frac{1}{(2n+1)^2}$$

**Step 4: Sum the series.**

$$I = \sum_{n=0}^{\infty} \frac{1}{(2n+1)^2} = 1 + \frac{1}{3^2} + \frac{1}{5^2} + \cdots$$

This is the **Leibniz/Dirichlet beta** sum. Since $\sum_{n=1}^\infty \frac{1}{n^2} = \frac{\pi^2}{6}$ and the even terms contribute $\frac{1}{4}\cdot\frac{\pi^2}{6} = \frac{\pi^2}{24}$:

$$\sum_{n=0}^{\infty}\frac{1}{(2n+1)^2} = \frac{\pi^2}{6} - \frac{\pi^2}{24} = \frac{\pi^2}{8}$$

**Result:**

$$\boxed{I = \dfrac{\pi^2}{8}}$$
