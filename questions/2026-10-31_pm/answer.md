# Answer: Poisson's Log-Cosine Integral

## Key Idea / Intuition

The expression $1 - 2a\cos x + a^2$ is the squared distance from $a$ to the point $e^{ix}$ on the unit circle:

$$
1 - 2a\cos x + a^2 = |1 - a e^{ix}|^2 = |a - e^{ix}|^2 .
$$

So the integral is (up to constants) the **average of $\ln|1 - az|$ over the unit circle**.

- If $|a|<1$, the function $\ln|1-az|$ is harmonic on the whole closed disk. Its circle-average therefore equals its value at the center, which is $\ln 1 = 0$.
- If $|a|>1$, factor out $a$ to reduce to the case $1/a$, which lies inside the disk.

The elementary version of the same idea: discretize the circle at the $n$-th roots of unity. The product $\prod_k (1 - a\omega^k)$ collapses to $1 - a^n$.

**Answer:**

$$
I(a)=\begin{cases} 0, & |a|<1,\\[2pt] 2\pi\ln|a|, & |a|>1.\end{cases}
$$

---

## Formal Proof / Solution

**Step 0: Reduce to a full period.** The integrand is even in $x$ and $2\pi$-periodic. Hence

$$
I(a) = \tfrac12\int_0^{2\pi} \ln\!\left(1 - 2a\cos x + a^2\right)dx = \tfrac12\int_0^{2\pi}\ln|1-ae^{ix}|^2\,dx = \int_0^{2\pi}\ln|1-ae^{ix}|\,dx .
$$

### Proof 1: Mean value property

**Step 1: The case $|a|<1$.** Consider $f(z) = \log(1-az)$, using the principal branch. For $|z|\le 1$ we have $\operatorname{Re}(1-az) \ge 1-|a| > 0$, so $f$ is holomorphic on a neighbourhood of the closed unit disk. Then $u(z) = \operatorname{Re} f(z) = \ln|1-az|$ is harmonic there.

By the mean value property,

$$
\frac{1}{2\pi}\int_0^{2\pi} \ln|1 - a e^{ix}|\,dx = u(0) = \ln 1 = 0 .
$$

You can also see this concretely through the power series:

$$
\ln|1-ae^{ix}| = \operatorname{Re}\Big(-\sum_{n\ge1}\frac{a^n e^{inx}}{n}\Big).
$$

The series converges uniformly in $x$ because $|a|<1$, and every term integrates to $0$ over a period. Hence $I(a)=0$.

**Step 2: The case $|a|>1$.** Factor out $a^2$:

$$
1 - 2a\cos x + a^2 = a^2\Big(1 - \tfrac{2}{a}\cos x + \tfrac{1}{a^2}\Big).
$$

Therefore

$$
I(a) = \int_0^\pi \ln a^2\,dx + I(1/a) = 2\pi\ln|a| + 0 = 2\pi\ln|a|,
$$

since $|1/a|<1$.

### Proof 2: Riemann sums and roots of unity (fully elementary)

Let $\omega = e^{2\pi i/n}$. The integrand $\ln|1-ae^{ix}|^2$ is continuous because $|a|\neq1$. So the full-period integral is the limit of Riemann sums at the points $x_k = 2\pi k/n$:

$$
2I(a) = \lim_{n\to\infty}\frac{2\pi}{n}\sum_{k=0}^{n-1}\ln|1-a\omega^k|^2
= \lim_{n\to\infty}\frac{4\pi}{n}\ln\Big|\prod_{k=0}^{n-1}(1-a\omega^k)\Big| .
$$

Since $\prod_{k=0}^{n-1}(z-\omega^k) = z^n - 1$, substituting $z = 1/a$ and multiplying by $a^n$ gives

$$
\prod_{k=0}^{n-1}(1-a\omega^k) = 1 - a^n .
$$

So

$$
2I(a) = \lim_{n\to\infty}\frac{4\pi}{n}\ln|1-a^n| .
$$

- **If $|a|<1$:** $\ln|1-a^n|\to 0$, so $I(a) = 0$.
- **If $|a|>1$:** write $\ln|1-a^n| = n\ln|a| + \ln|1-a^{-n}|$. The second term tends to $0$, so $2I(a) = 4\pi\ln|a|$, i.e. $I(a) = 2\pi\ln|a|$.

### Bonus: $a = 1$

Here $1 - 2\cos x + 1 = 4\sin^2(x/2)$, so

$$
I(1) = \pi\ln 4 + 2\int_0^\pi \ln\sin\tfrac{x}{2}\,dx = 2\pi\ln 2 + 4\int_0^{\pi/2}\ln\sin u\,du = 2\pi\ln 2 + 4\Big(-\tfrac{\pi}{2}\ln 2\Big) = 0 .
$$

This is consistent with both formulas, since $2\pi\ln 1 = 0$. The function $a\mapsto I(a)$ is continuous across the unit circle, but it has a "kink" there. This is exactly the behaviour of $2\pi\ln^+|a|$, the simplest instance of Jensen's formula.
