# Polynomial with No Integer Roots — Answer

---

## Key Fact: The Factoring Trick

For any polynomial $p(x)$ with integer coefficients and any integers $a, b$:

$$a - b \mid p(a) - p(b)$$

Why? Because $a - b$ divides $a^k - b^k$ for every positive integer $k$, so it divides every term of $p(a) - p(b)$.

---

## Proof

Suppose for contradiction that $n$ is an integer root, so $p(n) = 0$.

**Case 1: $n$ is even.**

Apply the factoring trick with $a = n$, $b = 0$:

$$n - 0 \mid p(n) - p(0) \implies n \mid 0 - p(0) \implies n \mid p(0)$$

Since $n$ is even, $p(0)$ must be even. But $p(0)$ is odd — contradiction.

**Case 2: $n$ is odd.**

Apply the factoring trick with $a = n$, $b = 1$:

$$n - 1 \mid p(n) - p(1) \implies (n-1) \mid 0 - p(1) \implies (n-1) \mid p(1)$$

Since $n$ is odd, $n - 1$ is even, so $p(1)$ must be even. But $p(1)$ is odd — contradiction.

In both cases we reach a contradiction, so $p$ has no integer roots. $\square$

---

## Why it works

The two conditions $p(0)$ odd and $p(1)$ odd serve as "parity guards" for even and odd candidates respectively. Any integer root must be one or the other, and each case kills itself via divisibility.

The key insight: you don't need to know anything about the degree of $p$ or the size of the root. The single fact $a - b \mid p(a) - p(b)$ does all the work.

---

## Ray's Solution

Write $p(x) = \sum_{i=0}^n a_i x^i$.

Since $p(0) = a_0$ is odd, $a_0$ is odd.
Since $p(1) = \sum_{i=0}^n a_i$ is odd and $a_0$ is odd, we get $\sum_{i=1}^n a_i$ is even.

Suppose $x_0$ is an integer root, so $p(x_0) = a_0 + \sum_{i=1}^n a_i x_0^i = 0$.

**Case 1: $x_0$ is even.**

Each $x_0^i$ is even, so each term $a_i x_0^i$ is even. Thus $\sum_{i=1}^n a_i x_0^i$ is even (sum of even numbers). So:

$$p(x_0) = \underbrace{a_0}_{\text{odd}} + \underbrace{\sum_{i=1}^n a_i x_0^i}_{\text{even}} = \text{odd} \neq 0 \quad \text{— contradiction}$$

**Case 2: $x_0$ is odd.**

Each $x_0^i$ is odd, so $x_0^i \equiv 1 \pmod{2}$ for all $i \geq 1$. Therefore:

$$\sum_{i=1}^n a_i x_0^i \equiv \sum_{i=1}^n a_i \cdot 1 = \sum_{i=1}^n a_i \equiv 0 \pmod{2}$$

So $\sum_{i=1}^n a_i x_0^i$ is even, and again:

$$p(x_0) = \underbrace{a_0}_{\text{odd}} + \underbrace{\sum_{i=1}^n a_i x_0^i}_{\text{even}} = \text{odd} \neq 0 \quad \text{— contradiction}$$

In both cases $p(x_0) \neq 0$, so $p$ has no integer roots. $\square$

This approach is more elementary than the divisibility trick — it works directly from the coefficients, using that mod 2, all odd numbers are 1, so multiplying by an odd number preserves parity of the sum.
