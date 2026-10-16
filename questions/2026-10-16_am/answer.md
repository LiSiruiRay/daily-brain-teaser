# Answer: Twelve Lengths and an Acute Triangle

## Key Idea / Intuition

Suppose no three of the lengths form an acute triangle. Then the lengths must spread out very fast. Sort them. Each length must be "too long" for the two lengths just below it, in the sense that its **square** is at least the sum of their squares. So the squares grow at least as fast as the Fibonacci numbers. Twelve steps of Fibonacci growth starting from $1, 1$ reaches $F_{12} = 144 = 12^2$. That exceeds what the interval $(1,12)$ allows. The problem is simply the Fibonacci sequence in disguise.

---

## Formal Proof / Solution

**Step 1: What "acute" means.** Let $a \le b \le c$ be positive. They are the sides of an acute triangle if and only if
$$a^2 + b^2 > c^2.$$

This condition also guarantees that a triangle exists at all:
$$(a+b)^2 = a^2 + b^2 + 2ab > a^2 + b^2 > c^2,$$
so $a + b > c$. The largest angle lies opposite $c$. By the law of cosines, that angle is acute exactly when $a^2 + b^2 > c^2$.

**Step 2: Assume the contrary and sort.** Relabel so that
$$1 < d_1 \le d_2 \le \cdots \le d_{12} < 12.$$
Suppose no triple forms an acute triangle. In particular, no **consecutive** triple $d_k, d_{k+1}, d_{k+2}$ does. By Step 1, this means
$$d_{k+2}^2 \ \ge\ d_k^2 + d_{k+1}^2 \qquad (k = 1, \dots, 10).$$

**Step 3: Compare with Fibonacci.** Let $F_1 = F_2 = 1$ and $F_{n+2} = F_n + F_{n+1}$. We claim $d_n^2 > F_n$ for all $n$, and prove it by induction.

- The base cases hold: $d_1^2 > 1 = F_1$ and $d_2^2 > 1 = F_2$.
- For the inductive step:
$$d_{n+2}^2 \ \ge\ d_n^2 + d_{n+1}^2 \ >\ F_n + F_{n+1} = F_{n+2}.$$

The Fibonacci numbers run
$$1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144,$$
so $F_{12} = 144$.

**Step 4: Contradiction.** From Step 3,
$$d_{12}^2 > 144, \qquad \text{so} \qquad d_{12} > 12.$$
This contradicts $d_{12} < 12$. Hence some three of the $d_i$ form an acute triangle. $\blacksquare$

---

## The Follow-up: Sharpness

The bound is exactly tight. On the closed interval $[1,12]$, take
$$d_k = \sqrt{F_k}\,: \quad 1,\ 1,\ \sqrt2,\ \sqrt3,\ \sqrt5,\ \sqrt8,\ \dots,\ \sqrt{89},\ \sqrt{144} = 12.$$
Every consecutive triple satisfies $d_k^2 + d_{k+1}^2 = d_{k+2}^2$, so it forms a **right** triangle, not an acute one.

Non-consecutive triples fare no better. Take $i < j < k$ with $k \ge j+1$. Since the $F_n$ are non-decreasing,
$$F_i + F_j \ \le\ F_{k-2} + F_{k-1} = F_k.$$
So those triples are right or obtuse, or degenerate (fail to form a triangle at all).

Thus $(1,12)$ is precisely the threshold, and $12 = \sqrt{F_{12}}$ is the coincidence the problem is built around.

**Takeaway:** "Avoid a configuration among all triples" often reduces to a condition on **consecutive** elements of a sorted list. That condition then forces a recurrence, here Fibonacci, which grows too fast. The same idea explains why sets avoiding ordinary triangles have Fibonacci-like growth.
