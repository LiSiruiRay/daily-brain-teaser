# Answer: The Integers That Sum to Their Product

## Key Idea / Intuition

The product grows much faster than the sum, so large numbers or many factors quickly make the product dwarf the sum. This means we only need to search a tiny region. The clever move is to bound $n$ (the number of terms) by noticing that if all $a_i \geq 2$, the product is at least $2^n$ while the sum is at most $2n \cdot \max(a_i)$ — forcing $n$ to be small. Then we handle small $n$ by direct casework.

---

## Formal Proof / Solution

**Step 1: Bound the number of terms.**

If we have $n$ integers each at least 2, then:
$$\text{Product} \geq 2^n, \qquad \text{Sum} \leq n \cdot a_n \leq n \cdot \text{Product}/2^{n-1}.$$

More directly: with all $a_i \geq 2$,
$$\text{Sum} = a_1 + \cdots + a_n \leq n \cdot a_n, \quad \text{Product} = a_1 \cdots a_n \geq 2^{n-1} a_n.$$

So the equation forces $n \cdot a_n \geq 2^{n-1} a_n$, giving $n \geq 2^{n-1}$. This only holds for $n \leq 2$ ... wait, let's be more careful. We need sum $=$ product, so:
$$\text{Product} = \text{Sum} \leq n \cdot a_n.$$
But also $\text{Product} \geq 2^{n-1} \cdot a_n$ (since there are $n-1$ other factors each $\geq 2$).

So $2^{n-1} a_n \leq n \cdot a_n$, giving $2^{n-1} \leq n$.

Checking: $n=1$: $1 \leq 1$ ✓; $n=2$: $2 \leq 2$ ✓; $n=3$: $4 \leq 3$ ✗.

So **$n \leq 2$** only? But wait — we're assuming all are $\geq 2$. Let me redo more carefully for $n=3$.

Actually $2^{n-1} \leq n$ fails for $n \geq 3$, so there are **no solutions with $n \geq 3$ when all $a_i \geq 2$?** Let's verify directly.

**Step 2: Case $n = 1$.**

$a_1 = a_1$. Any single integer works trivially, but the product equals $a_1$ and sum equals $a_1$, so every single integer is a solution. However, this is trivial/degenerate. Most formulations require $n \geq 2$.

**Step 3: Case $n = 2$.**

$a_1 + a_2 = a_1 a_2$. Rearrange:
$$a_1 a_2 - a_1 - a_2 = 0 \implies (a_1 - 1)(a_2 - 1) = 1.$$
Since $a_1, a_2 \geq 2$, we need $a_1 - 1 = a_2 - 1 = 1$, so $a_1 = a_2 = 2$.

**Check:** $2 + 2 = 4 = 2 \times 2$. ✓

**Step 4: Case $n = 3$.**

$a_1 + a_2 + a_3 = a_1 a_2 a_3$ with $2 \leq a_1 \leq a_2 \leq a_3$.

Take $a_1 = 2$: then $2 + a_2 + a_3 = 2a_2 a_3$, so $a_2 + a_3 - 2a_2 a_3 = -2$, i.e.,
$$2a_2 a_3 - a_2 - a_3 = 2.$$
With $a_2 = 2$: $4a_3 - 2 - a_3 = 2 \Rightarrow 3a_3 = 4$. Not an integer.

With $a_2 = 3$: $6a_3 - 3 - a_3 = 2 \Rightarrow 5a_3 = 5 \Rightarrow a_3 = 1$. But $a_3 \geq a_2 = 3$, contradiction.

With $a_2 \geq 4$: LHS $\geq 2 \cdot 4 \cdot 4 - 4 - 4 = 24 > 2$. No solution.

Take $a_1 = 3$: $3 + a_2 + a_3 = 3a_2 a_3$. With $a_2 = 3$: $3a_3 \cdot 3 - 3 - a_3 = 3 \Rightarrow 9a_3 - a_3 = 6 \Rightarrow a_3 = 3/4$. No.

Larger $a_1$ only makes the product larger. **No solutions for $n=3$.**

Wait — I made an error in Step 1. Let me recheck: for $n=3$ with a **1** included.

Actually the problem states each $a_i \geq 2$, so indeed $n=3$ has no solutions as shown.

**Step 5: Case $n \geq 3$ — general argument.**

With all $a_i \geq 2$ and $n \geq 3$: the product $P \geq 2^n$ but the sum $S \leq n \cdot a_{\max}$. Since $P = a_1 \cdots a_n \geq 2^{n-1} a_n$, we need $2^{n-1} a_n \leq S = P = a_1 \cdots a_n$, yet also $S \leq n a_n$, so $2^{n-1} \leq n$, which fails for $n \geq 3$. Hence no solutions.

---

## Complete Solution Set

The only solution (with all integers $\geq 2$ and $n \geq 2$) is:

$$\boxed{(2,\ 2) \quad : \quad 2 + 2 = 2 \times 2 = 4.}$$

If we allow $n = 1$: every single integer $a$ satisfies $a = a$ trivially (degenerate).

---

## Why This Is Beautiful

The factoring trick $(a_1-1)(a_2-1) = 1$ is a classic rearrangement. The bounding argument $2^{n-1} \leq n$ shows in one line why large $n$ is impossible — the product wins. The problem has exactly one nontrivial answer, which is both surprising and satisfying.
