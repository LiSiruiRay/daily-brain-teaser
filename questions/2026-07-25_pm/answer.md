# Answer: Integral of arctan(x)/x and Catalan's Constant

## Key Idea / Intuition

The key trick is to expand $\arctan(x)$ as its Taylor series, then integrate term by term. Each term produces a simple integral of a power of $x$, and the resulting series is immediately recognizable as Catalan's constant — one of the most famous constants in mathematics, defined exactly by an alternating series of reciprocal odd squares.

---

## Formal Proof / Solution

**Step 1: Taylor expand $\arctan x$.**

Recall the Maclaurin series:
$$\arctan x = \sum_{n=0}^{\infty} \frac{(-1)^n x^{2n+1}}{2n+1}, \quad |x| \leq 1.$$

**Step 2: Divide by $x$.**

$$\frac{\arctan x}{x} = \sum_{n=0}^{\infty} \frac{(-1)^n x^{2n}}{2n+1}.$$

**Step 3: Integrate term by term.**

Since the series converges uniformly on $[0,1]$ (by Dirichlet's test or the fact that it's an alternating series with decreasing terms at $x=1$), we may integrate term by term:

$$I = \int_0^1 \sum_{n=0}^{\infty} \frac{(-1)^n x^{2n}}{2n+1}\, dx = \sum_{n=0}^{\infty} \frac{(-1)^n}{2n+1} \int_0^1 x^{2n}\, dx.$$

**Step 4: Evaluate each integral.**

$$\int_0^1 x^{2n}\, dx = \frac{1}{2n+1}.$$

**Step 5: Recognize the resulting series.**

$$I = \sum_{n=0}^{\infty} \frac{(-1)^n}{(2n+1)^2} = \frac{1}{1^2} - \frac{1}{3^2} + \frac{1}{5^2} - \frac{1}{7^2} + \cdots = G,$$

where $G$ is **Catalan's constant**, approximately $G \approx 0.9159656\ldots$

$$\boxed{I = \int_0^1 \frac{\arctan x}{x}\, dx = G \approx 0.9159656\ldots}$$

**Why this is beautiful:** The integral of $\arctan(x)/x$ — which looks complicated — reduces by the simplest possible trick (Taylor series + term-by-term integration) to Catalan's constant, which has no known closed form in terms of more elementary constants. The answer is at once explicit (as a series) and mysterious (no simpler form is known).
