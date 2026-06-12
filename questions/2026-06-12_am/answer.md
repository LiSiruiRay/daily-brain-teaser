# Answer: A Sequence That Always Hits a Perfect Square

## Key Idea / Intuition

The sequence is constant exactly when it hits a perfect square — because if $a_k = m^2$, then $S(a_k) = 0$, so $a_{k+1} = a_k$. The question is: starting from $A$, does the sequence always reach a perfect square, or can it wander forever?

The key insight is to track what happens modulo small numbers, or more cleverly, to notice that perfect squares are the **only fixed points**, and the sequence is non-decreasing. Once you see that $S(n) = 0 \iff n$ is a perfect square, the question becomes: does every starting integer eventually land on a perfect square?

The answer is: **the sequence eventually becomes constant if and only if $A$ is a perfect square**, because for non-square $A$, the sequence strictly increases and — surprisingly — *skips over* every perfect square it approaches.

---

## Formal Proof / Solution

**Step 1: Fixed points are exactly perfect squares.**

If $n = m^2$, then $S(n) = n - m^2 = 0$, so the sequence is constant. If $n$ is not a perfect square, $S(n) \geq 1$, so the sequence strictly increases.

**Step 2: What happens near a perfect square?**

Suppose $n = m^2 - j$ for some $1 \leq j \leq 2m - 1$ (i.e., $n$ lies just *below* $m^2$). The largest perfect square $\leq n$ is $(m-1)^2$, so:

$$S(n) = n - (m-1)^2 = m^2 - j - (m-1)^2 = 2m - 1 - j.$$

Therefore:

$$a_{k+1} = n + S(n) = m^2 - j + 2m - 1 - j = m^2 + (2m - 1 - 2j).$$

**Step 3: Does the sequence land on $m^2$?**

For the sequence to land exactly on $m^2$, we need $2m - 1 - 2j = 0$, i.e., $j = \frac{2m-1}{2}$. But $j$ must be an integer, and $2m - 1$ is **odd**, so this is impossible!

This is the key surprise: **the sequence always jumps over $m^2$ entirely** — landing either below or strictly above $m^2$.

**Step 4: Conclusion.**

If $A$ is a perfect square, the sequence is immediately constant. If $A$ is not a perfect square, then the sequence is strictly increasing and never lands on any perfect square (since by Step 3, you always overshoot). Therefore, the sequence grows without bound and is never constant.

Hence the sequence eventually becomes constant **if and only if $A$ is a perfect square**.

**Example verification:** Start at $A = 7$.
- $m = 2$ (since $2^2 = 4 \leq 7 < 9 = 3^2$), $S(7) = 7 - 4 = 3$, so $a_1 = 10$.
- $m = 3$ (since $9 \leq 10 < 16$), $S(10) = 10 - 9 = 1$, so $a_2 = 11$.
- $m = 3$, $S(11) = 2$, so $a_3 = 13$.
- $m = 3$, $S(13) = 4$, so $a_4 = 17$.
- And so on — it keeps jumping past every perfect square (skipping 16, 25, ...).

Compare with $A = 9$: $S(9) = 0$, so it's immediately constant. ✓
