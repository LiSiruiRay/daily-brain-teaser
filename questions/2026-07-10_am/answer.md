# Answer: A Polynomial Evaluated at Consecutive Integers

## Key Idea / Intuition

If $p(n) = 0$ for some integer $n$, then $(x - n)$ divides $p(x)$ over the integers. This forces $p(k) = (k-n) \cdot q(k)$ for all integers $k$, where $q$ has integer coefficients. Among any two consecutive integers $k$ and $k+1$, one of $k - n$ and $k+1 - n$ is even — so at least one of $p(k), p(k+1)$ would be **even**. But we are told all 2025 values are odd — a contradiction.

---

## Formal Proof / Solution

**Claim:** $p$ has no integer roots.

**Proof by contradiction.** Suppose $n \in \mathbb{Z}$ is a root of $p$, so $p(n) = 0$.

Since $p$ has integer coefficients and $n$ is an integer root, the **factor theorem over $\mathbb{Z}$** gives:
$$p(x) = (x - n)\, q(x)$$
for some polynomial $q(x)$ with integer coefficients.

Now consider any integer $k$. We have:
$$p(k) = (k - n)\, q(k),$$
where both $(k-n)$ and $q(k)$ are integers.

**Key observation:** Among any two consecutive integers $k$ and $k+1$, exactly one of the differences $(k - n)$ and $(k+1 - n)$ is even (since they differ by 1, they have opposite parity). Therefore, at least one of $p(k)$ and $p(k+1)$ is **even**.

Apply this to the consecutive pairs $(1,2),\, (2,3),\, \ldots,\, (2024, 2025)$. In each pair, at least one value is even.

But by hypothesis, $p(1), p(2), \ldots, p(2025)$ are **all odd** — so in particular, both elements of every consecutive pair are odd.

This is a **contradiction**.

Therefore, $p$ has **no integer roots**. $\blacksquare$

---

**Remark:** The argument works for any set of consecutive integers of size $\geq 2$. Even two consecutive odd values of a polynomial (e.g., $p(1)$ and $p(2)$ both odd) is already enough to rule out integer roots. The number 2025 is irrelevant — even knowing $p(1)$ and $p(2)$ are both odd suffices!
