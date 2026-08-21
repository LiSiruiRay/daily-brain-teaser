# Answer: The Polynomial Pigeonhole

## Key Idea / Intuition

The core trick is that for any polynomial with integer coefficients, $p(m) - p(n)$ is always divisible by $m - n$ whenever $m, n$ are integers. Since $p$ hits 7 at three distinct integer points, the value $p(d) - 7$ must be divisible by $(d-a)(d-b)(d-c)$ — a product of three distinct nonzero integers. But $p(d) - 7 = 7$ forces this product of three distinct integers to divide 7, which is impossible.

---

## Formal Proof / Solution

**Key lemma:** For any polynomial $p(x)$ with integer coefficients and any integers $m, n$, we have $(m - n) \mid p(m) - p(n)$.

*Proof of lemma:* This follows from the factorization $m^k - n^k = (m-n)(m^{k-1} + \cdots + n^{k-1})$, applied term by term. $\square$

**Now the main argument.**

Since $p(a) = p(b) = p(c) = 7$, define:
$$q(x) = p(x) - 7.$$

Then $q(x)$ is a polynomial with integer coefficients, and $a, b, c$ are roots of $q$. Therefore:
$$q(x) = (x - a)(x - b)(x - c) \cdot r(x)$$
for some polynomial $r(x)$ with integer coefficients (by the factor theorem, applied iteratively over $\mathbb{Z}[x]$).

Now suppose for contradiction that there exists an integer $d$ with $p(d) = 14$. Then:
$$q(d) = p(d) - 7 = 14 - 7 = 7.$$

But substituting into the factored form:
$$(d - a)(d - b)(d - c) \cdot r(d) = 7.$$

Since $d, a, b, c$ are all integers, the factors $(d-a)$, $(d-b)$, $(d-c)$, and $r(d)$ are all integers. Also, $d \neq a, b, c$ (since $p(d) = 14 \neq 7$), so $d - a$, $d - b$, $d - c$ are **three distinct nonzero integers**.

The product of four integers equals 7 (a prime). In particular, the absolute value of the product of the three factors $(d-a)(d-b)(d-c)$ divides $7$, so:
$$|(d-a)(d-b)(d-c)| \leq 7.$$

But $(d-a)$, $(d-b)$, $(d-c)$ are **three distinct nonzero integers**, so their absolute values are at least three distinct positive integers, giving:
$$|(d-a)(d-b)(d-c)| \geq 1 \cdot 2 \cdot 3 = 6.$$

For this product to divide $7$ (a prime), we need $|(d-a)(d-b)(d-c)| \in \{1, 7\}$.

- It cannot be $1$ or $7$ while being a product of three distinct nonzero integers:
  - $|(d-a)(d-b)(d-c)| = 1$ requires three distinct nonzero integers with product $\pm 1$. The only factorizations of $\pm 1$ into three distinct integers would require $\{-1, 1, \pm1\}$, but we cannot have three **distinct** integers all with absolute value $\leq 1$.
  - $|(d-a)(d-b)(d-c)| = 7$ requires three distinct nonzero integers with absolute product $7$. The only way to write $7 = |p||q||r|$ with $p, q, r$ distinct nonzero integers is $\{1, 1, 7\}$ or $\{-1, -1, 7\}$ etc., but these require repeated values — impossible for distinct integers.

In both cases we reach a contradiction. Therefore, no such integer $d$ exists. $\blacksquare$

---

**Remark:** The same argument shows more generally: if $p$ takes the same value at $n$ distinct integers $a_1, \ldots, a_n$, then $p(d) - p(a_1)$ must be divisible by $(d-a_1)\cdots(d-a_n)$, a product of $n$ distinct nonzero integers — a powerful constraint.
