# Answer: The Monic Polynomial That Cannot Hide Below 1

## Key Idea / Intuition

Reverse the polynomial. The map $z \mapsto z^n p(1/z)$ turns the leading coefficient $1$ into a **constant term** $1$, and on the unit circle it has the same modulus as $p$. A holomorphic function's value at the center is the average of its values on the circle. So if the value at the center is $1$, the function cannot be smaller than $1$ everywhere on the circle.

On an interval there is no such averaging constraint, because the interval does not enclose a point where a mean value property forces anything. That is why Chebyshev polynomials can make the maximum exponentially small on $[-1,1]$.

---

## Formal Proof / Solution

**Step 1: The reversed polynomial.** Define
$$q(z) = z^n\, p(1/z) = 1 + a_{n-1} z + a_{n-2} z^2 + \cdots + a_0 z^n.$$
This is a polynomial, so it is entire. Its constant term is $q(0) = 1$.

**Step 2: Same size on the circle.** For $|z| = 1$ we have $1/z = \bar z$, which also lies on the unit circle. Hence
$$|q(z)| = |z|^n\,|p(\bar z)| = |p(\bar z)|.$$
As $z$ runs over the unit circle, so does $\bar z$. Therefore
$$\max_{|z|=1}|q(z)| = \max_{|z|=1}|p(z)| =: M.$$

**Step 3: Mean value property, for part (a).** By Cauchy's integral formula, $q(0)$ is the average of $q$ on the unit circle:
$$1 = q(0) = \frac{1}{2\pi}\int_0^{2\pi} q(e^{i\theta})\,d\theta.$$
Taking absolute values gives
$$1 \le \frac{1}{2\pi}\int_0^{2\pi} |q(e^{i\theta})|\,d\theta \le M.$$
This proves (a).

**Step 4: Equality case, part (b).** Suppose $M = 1$. Then $|q| \le 1$ on $|z|=1$. By the maximum modulus principle, $|q| \le 1$ on the closed unit disk. But $|q(0)| = 1$, so $|q|$ attains its maximum at an interior point. Hence $q$ is constant, and $q \equiv q(0) = 1$.

This means $a_{n-1} = \cdots = a_0 = 0$, so $p(z) = z^n$.

Conversely, $p(z) = z^n$ has $|p| \equiv 1$ on the circle, so equality holds.

**Alternative proof via Parseval.** Since $\{e^{ik\theta}\}$ is orthonormal on the circle,
$$\frac{1}{2\pi}\int_0^{2\pi}|p(e^{i\theta})|^2\,d\theta = 1 + \sum_{k=0}^{n-1}|a_k|^2 \;\ge\; 1.$$
The maximum of $|p|^2$ is at least its average. So $M^2 \ge 1 + \sum|a_k|^2$, with equality only if every $a_k = 0$. This gives (a) and (b) at once, and even the sharper bound
$$M \ge \sqrt{1 + \textstyle\sum |a_k|^2}.$$

**About the contrast.** On $[-1,1]$, the polynomial $2^{1-n}T_n(x)$ (rescaled Chebyshev) is monic and has sup norm $2^{1-n}$. The interval is not the boundary of a region containing a point where the reversal trick applies.

In potential-theoretic language, the minimal sup norm of a monic polynomial on a compact set $K$ behaves like $\operatorname{cap}(K)^n$. The capacity of the unit circle is $1$, while the capacity of $[-1,1]$ is $1/2$.
