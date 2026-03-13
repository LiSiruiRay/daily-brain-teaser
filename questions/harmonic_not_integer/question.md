# The Harmonic Series Is Never an Integer

**Type:** Putnam / Number Theory
**Tags:** Harmonic series, Primes, Bertrand's postulate, LCM, Divisibility
**Date:** 2026-03-13
**Difficulty:** 3/5

**Why it's beautiful:**
$H_n = 1 + \frac{1}{2} + \frac{1}{3} + \cdots + \frac{1}{n}$ grows without bound, so you might expect it to eventually hit an integer. It never does (for $n \geq 2$). The proof uses a clever "lonely prime" argument: there is always one prime that appears exactly once in the denominators, and that prime poisons the entire sum, preventing it from being an integer.

---

## Problem

Let $H_n = 1 + \frac{1}{2} + \frac{1}{3} + \cdots + \frac{1}{n}$.

**Prove that $H_n$ is not an integer for any $n \geq 2$.**

---

*Hint: Let $p$ be the largest prime $\leq n$. By Bertrand's postulate, $p > n/2$, so $2p > n$ — meaning $p$ appears only once among $\{1, 2, \ldots, n\}$. Now multiply $H_n$ by $L = \text{lcm}(1, 2, \ldots, n)$ and think about divisibility by $p$.*
