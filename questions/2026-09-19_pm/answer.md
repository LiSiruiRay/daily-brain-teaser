# Answer: Sophomore's Dream: Integral of x^x

## Key Idea / Intuition

The function $x^x = e^{x \ln x}$ looks complicated, but expanding it as a power series in $x \ln x$ reduces it to integrals of the form $\int_0^1 x^k (\ln x)^k \, dx$. Each such integral evaluates to a clean closed form via the substitution $x = e^{-t}$, and the resulting sum is exactly the alternating series $\sum (-1)^{n+1}/n^n$. This is Johann Bernoulli's **sophomore's dream** — a striking closed form for an integral with no elementary antiderivative.

---

## Formal Proof / Solution

**Step 1: Series expansion.**

Write

$$x^x = e^{x \ln x} = \sum_{n=0}^{\infty} \frac{(x \ln x)^n}{n!}.$$

So

$$I = \int_0^1 x^x \, dx = \sum_{n=0}^{\infty} \frac{1}{n!} \int_0^1 x^n (\ln x)^n \, dx.$$

(Interchange of sum and integral is justified by uniform/dominated convergence on $[0,1]$, since $|x \ln x| \le 1/e$ there.)

**Step 2: Evaluate $\int_0^1 x^n (\ln x)^n \, dx$.**

Substitute $x = e^{-t}$, so $dx = -e^{-t} dt$, $\ln x = -t$, and the limits go from $t = \infty$ to $t = 0$:

$$\int_0^1 x^n (\ln x)^n \, dx = \int_0^{\infty} e^{-nt} (-t)^n e^{-t} \, dt = (-1)^n \int_0^{\infty} t^n e^{-(n+1)t} \, dt.$$

Now use the standard formula $\int_0^\infty t^n e^{-\alpha t} dt = n!/\alpha^{n+1}$ with $\alpha = n+1$:

$$\int_0^1 x^n (\ln x)^n \, dx = (-1)^n \cdot \frac{n!}{(n+1)^{n+1}}.$$

**Step 3: Sum the series.**

$$I = \sum_{n=0}^{\infty} \frac{1}{n!} \cdot (-1)^n \cdot \frac{n!}{(n+1)^{n+1}} = \sum_{n=0}^{\infty} \frac{(-1)^n}{(n+1)^{n+1}}.$$

Re-index with $m = n+1$:

$$\boxed{I = \sum_{m=1}^{\infty} \frac{(-1)^{m-1}}{m^m} = 1 - \frac{1}{4} + \frac{1}{27} - \frac{1}{256} + \cdots}$$

**Numerically:** $I \approx 0.7834305107...$

This result is surprising because the integrand $x^x$ has no elementary antiderivative, yet the integral has this delightful explicit series representation.
