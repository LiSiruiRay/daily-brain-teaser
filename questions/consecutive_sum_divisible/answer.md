# Consecutive Subsum Divisible by $n$ — Answer

## Setup: Define Partial Sums

Define $S_0 = 0$ and $S_k = a_1 + a_2 + \cdots + a_k$ for $k = 1, 2, \ldots, n$.

This gives $n + 1$ integers: $S_0, S_1, \ldots, S_n$.

---

## Apply Pigeonhole

Each $S_k$ has some remainder when divided by $n$, taking values in $\{0, 1, \ldots, n-1\}$ — only $n$ possible remainders.

We have $n+1$ partial sums but only $n$ possible remainders, so by the **Pigeonhole Principle**, two must share the same remainder:

$$S_i \equiv S_j \pmod{n} \quad \text{for some } 0 \leq i < j \leq n$$

---

## Extract the Consecutive Subsum

$$a_{i+1} + a_{i+2} + \cdots + a_j = S_j - S_i \equiv 0 \pmod{n}$$

So the consecutive block $a_{i+1}, \ldots, a_j$ has sum divisible by $n$. $\blacksquare$

---

## Example

Take $n = 4$ and $(a_1, a_2, a_3, a_4) = (3, 1, 4, 2)$.

| $k$ | $S_k$ | $S_k \bmod 4$ |
|-----|--------|----------------|
| 0   | 0      | 0              |
| 1   | 3      | 3              |
| 2   | 4      | **0**          |
| 3   | 8      | **0**          |
| 4   | 10     | 2              |

$S_0 \equiv S_2 \equiv 0$, so $a_1 + a_2 = 3 + 1 = 4$ is divisible by 4. ✓

Also $S_2 \equiv S_3$, so $a_3 = 4$ is divisible by 4. ✓

---

## Why $S_0 = 0$ Is Needed

Including $S_0 = 0$ is crucial: it handles the case where the subsum starts at $a_1$ (i.e., $i = 0$). Without it, we'd only have $n$ partial sums $S_1, \ldots, S_n$ and Pigeonhole would give nothing.

It also captures the special case where $n \mid S_n = a_1 + \cdots + a_n$ directly (when $S_0 \equiv S_n$).

---

## Remark: Sharpness

The bound $n$ integers is tight: with $n-1$ integers you can fail. For example, with $n = 3$ and $(a_1, a_2) = (1, 1)$: partial sums are $1, 2$ — neither is $\equiv 0$ and no consecutive subsum is divisible by 3.
