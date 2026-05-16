# Answer: The Basel-Flavored Integral

## Key Idea / Intuition

The integrand $\frac{\ln(1+x)}{x}$ looks innocent, but expanding $\ln(1+x)$ as a power series and integrating term-by-term reveals the famous alternating Basel-type series $1 - \frac{1}{4} + \frac{1}{9} - \frac{1}{16} + \cdots$. This series has a beautiful closed form related to $\pi^2$, and the whole computation reduces to recognizing it.

---

## Formal Proof / Solution

**Step 1: Power series expansion.**

Recall the Taylor series for $\ln(1+x)$ valid on $(-1, 1]$:

$$\ln(1+x) = x - \frac{x^2}{2} + \frac{x^3}{3} - \frac{x^4}{4} + \cdots = \sum_{n=1}^{\infty} \frac{(-1)^{n-1} x^n}{n}.$$

**Step 2: Divide by $x$.**

$$\frac{\ln(1+x)}{x} = \sum_{n=1}^{\infty} \frac{(-1)^{n-1} x^{n-1}}{n}.$$

**Step 3: Integrate term by term.**

On $[0,1]$, the series converges uniformly (by Abel's theorem / Dirichlet test), so we may integrate term by term:

$$I = \int_0^1 \sum_{n=1}^{\infty} \frac{(-1)^{n-1} x^{n-1}}{n}\, dx = \sum_{n=1}^{\infty} \frac{(-1)^{n-1}}{n} \int_0^1 x^{n-1}\, dx = \sum_{n=1}^{\infty} \frac{(-1)^{n-1}}{n^2}.$$

**Step 4: Identify the series.**

We recognize the alternating sum:

$$\sum_{n=1}^{\infty} \frac{(-1)^{n-1}}{n^2} = 1 - \frac{1}{4} + \frac{1}{9} - \frac{1}{16} + \cdots$$

This is a classical result. From the Euler identity $\sum_{n=1}^\infty \frac{1}{n^2} = \frac{\pi^2}{6}$, one can split by parity:

$$\sum_{n=1}^{\infty} \frac{(-1)^{n-1}}{n^2} = \sum_{\text{odd}} \frac{1}{n^2} - \sum_{\text{even}} \frac{1}{n^2}.$$

Let $S = \sum_{n=1}^\infty \frac{1}{n^2} = \frac{\pi^2}{6}$ and $E = \sum_{k=1}^\infty \frac{1}{(2k)^2} = \frac{1}{4}S$. Then:

$$\sum_{n=1}^{\infty} \frac{(-1)^{n-1}}{n^2} = S - 2E = S - \frac{S}{2} = \frac{S}{2} = \frac{\pi^2}{12}.$$

**Result:**

$$\boxed{I = \frac{\pi^2}{12}.}$$

**Why this is beautiful:** A completely elementary-looking integral over $[0,1]$ secretly encodes $\pi^2$. The bridge is the Basel series — a recurring miracle in analysis.
