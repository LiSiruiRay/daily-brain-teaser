# Harmonic Series Is Never an Integer — Answer

---

## Setup: The "Lonely Prime" Idea

**Bertrand's Postulate** states: for every integer $n \geq 1$, there exists a prime $p$ with $n < p \leq 2n$.

Equivalently: the largest prime $p \leq n$ satisfies $p > n/2$, so $2p > n$.

This means $p$ is the **only** multiple of $p$ in $\{1, 2, \ldots, n\}$ — hence "lonely."

---

## Proof

Let $n \geq 2$, and let $p$ be the largest prime $\leq n$.

**Step 1: Multiply through by $L = \text{lcm}(1, 2, \ldots, n)$.**

$$L \cdot H_n = \frac{L}{1} + \frac{L}{2} + \cdots + \frac{L}{n}$$

Every term $L/k$ is an integer (since $k \mid L$ by definition of lcm). So $L \cdot H_n$ is an integer.

If $H_n$ were also an integer, then $p \mid L \cdot H_n$ (since $p \mid L$). We will show this is impossible.

---

**Step 2: Determine the exact power of $p$ in $L$.**

Since $p > n/2$, we have $p^2 > n$, so $p^2$ does not divide any $k \leq n$. Therefore:

$$p^1 \,\Big\|\, L \quad \text{(i.e., } p \mid L \text{ but } p^2 \nmid L\text{)}$$

---

**Step 3: Analyze each term $L/k$ modulo $p$.**

- If $k \neq p$: since $p \nmid k$ (because $p$ is the only multiple of $p$ in $\{1,\ldots,n\}$), and $p^1 \| L$, we get $p \mid L/k$.

- If $k = p$: since $p^1 \| L$, removing one factor of $p$ gives $p \nmid L/p$.

So modulo $p$:

$$L \cdot H_n = \underbrace{\frac{L}{p}}_{\not\equiv\, 0} + \underbrace{\sum_{k \neq p} \frac{L}{k}}_{\equiv\, 0} \not\equiv 0 \pmod{p}$$

---

**Step 4: Conclude.**

We have shown $p \nmid L \cdot H_n$.

But if $H_n = m$ were an integer, then $L \cdot H_n = L \cdot m$, and since $p \mid L$, we'd have $p \mid L \cdot m$ — contradiction.

Therefore $H_n$ is not an integer. $\square$

---

## Why each step is needed

| Step | Role |
|------|------|
| Bertrand's postulate | Guarantees $p$ appears exactly once in $\{1,\ldots,n\}$ |
| $p^1 \| L$ | Ensures $L/p$ is not divisible by $p$, but all other $L/k$ are |
| Mod $p$ analysis | Shows $L \cdot H_n \not\equiv 0 \pmod{p}$, killing integrality |

The lonely prime $p$ is the obstruction. Every other denominator cancels cleanly — but $p$ has no partner to cancel with, so it leaves a remainder that can never be an integer.
