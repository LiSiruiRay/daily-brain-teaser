# Answer: The Polynomial That Stays Small on Integers

## Key Idea / Intuition

The integers $0, 1, \ldots, n$ give us $n+1$ points, and a monic degree-$n$ polynomial is completely pinned by its values there — in fact, the *unique* monic degree-$n$ polynomial that passes through prescribed values at $0, 1, \ldots, n$ is determined by the Newton forward difference formula. The key insight is that the leading coefficient of a monic polynomial forces a specific alternating sum of its values at these integer points to equal exactly $n!$, so those values can't all be small.

---

## Formal Proof / Solution

**Step 1: The finite difference operator.**

Define the $n$-th finite difference of any function $f$ at $0$ by

$$\Delta^n f(0) = \sum_{k=0}^{n} (-1)^{n-k} \binom{n}{k} f(k).$$

A key fact from finite difference calculus: if $p(x)$ is a polynomial of degree $n$ with leading coefficient $a_n$, then

$$\Delta^n p(0) = n! \cdot a_n.$$

*Quick proof:* It suffices to check on the basis $\{1, x, x^2, \ldots, x^n\}$. One can show $\Delta^n x^n = n!$ and $\Delta^n x^j = 0$ for $j < n$.

**Step 2: Apply to our monic polynomial.**

Since $p(x)$ is monic of degree $n$, we have $a_n = 1$, so

$$\Delta^n p(0) = \sum_{k=0}^{n} (-1)^{n-k} \binom{n}{k} p(k) = n!.$$

**Step 3: Bound via the maximum.**

Let $M = \max_{0 \le k \le n} |p(k)|$. Then by the triangle inequality:

$$n! = \left|\sum_{k=0}^{n} (-1)^{n-k} \binom{n}{k} p(k)\right| \le \sum_{k=0}^{n} \binom{n}{k} |p(k)| \le M \sum_{k=0}^{n} \binom{n}{k} = M \cdot 2^n.$$

**Step 4: Conclude.**

Rearranging gives

$$M = \max_{0 \le k \le n} |p(k)| \ge \frac{n!}{2^n}.$$

$\blacksquare$

---

**Sharpness:** The bound is essentially achieved by the polynomial $p(x) = \prod_{k=0}^{n-1}(x - k/1) \cdot \text{(shifted)}$... more precisely, the Chebyshev-like polynomial on $\{0,\ldots,n\}$ comes close. A clean equality case is $p(x) = x(x-1)(x-2)\cdots(x-n+1) \cdot$ (adjusted), but note $q(x) = x(x-1)\cdots(x-n+1)$ is already monic of degree $n$ and $\max_{0\le k \le n} |q(k)| = 0$ since $q$ vanishes at all of $0,1,\ldots,n-1$... wait, $q(n) = n!$. So $q$ itself achieves the bound with equality: $\max |q(k)| = n! \ge n!/2^n$. The bound is non-trivial precisely because we're claiming $n!/2^n$ is a *lower* bound, and $q$ exceeds it.
