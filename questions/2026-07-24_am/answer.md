# Answer: A Polynomial Taking Only Non-Negative Integer Values

## Key Idea / Intuition

Any polynomial that vanishes at $0, 1, 2$ must be divisible (as a polynomial) by $x(x-1)(x-2)$. The natural basis for polynomials that take integer values at integers is the **binomial coefficient basis**: $\binom{x}{k} = \frac{x(x-1)\cdots(x-k+1)}{k!}$. These are integer-valued at all integers. The constraint that $p(n) \geq 0$ for all non-negative integers, combined with the vanishing conditions, forces $p(3)$ to be at least $1$, and the polynomial $\binom{x}{3} \cdot \text{(something)}$ achieves this.

The key insight: write $p(x)$ in the basis of falling-factorial / binomial-coefficient polynomials. The vanishing at $0,1,2$ forces the first nonzero basis term to involve $\binom{x}{3}$, and positivity at $n=3$ forces the coefficient to be a positive integer, giving minimum value $1$.

---

## Formal Proof / Solution

**Step 1: Integer-valued polynomials have a canonical basis.**

Every polynomial that maps non-negative integers to integers can be written uniquely as
$$p(x) = \sum_{k=0}^{d} c_k \binom{x}{k}, \quad c_k \in \mathbb{Z}.$$

This is a classical fact: the binomial coefficient polynomials $\binom{x}{0}, \binom{x}{1}, \binom{x}{2}, \ldots$ form a $\mathbb{Z}$-basis for integer-valued polynomials.

**Step 2: Apply the vanishing conditions.**

Note that $\binom{n}{k} = 0$ for $0 \leq n < k$ (integers). So:
- $p(0) = c_0 = 0$
- $p(1) = c_0 + c_1 = 0 \Rightarrow c_1 = 0$
- $p(2) = c_0 + 2c_1 + c_2 = 0 \Rightarrow c_2 = 0$

Thus $p(x) = \sum_{k=3}^{d} c_k \binom{x}{k}$.

**Step 3: Evaluate at $n = 3$.**

$$p(3) = \sum_{k=3}^{d} c_k \binom{3}{k} = c_3 \binom{3}{3} + c_4 \binom{3}{4} + \cdots = c_3 \cdot 1 + 0 + \cdots = c_3.$$

(Since $\binom{3}{k} = 0$ for $k > 3$.)

**Step 4: Apply the non-negativity condition.**

We need $p(n) \geq 0$ for all non-negative integers $n$, and $p$ is not identically zero, so some $c_k \neq 0$.

In particular, $p(3) = c_3 \geq 0$.

Since $p$ is not identically zero and $p(n)$ must be a **non-negative integer** for all $n \geq 0$, we need $p(3) \in \mathbb{Z}_{\geq 0}$. If $c_3 = 0$, then the leading behavior of $p$ for large $n$ is determined by the smallest $k \geq 4$ with $c_k \neq 0$. But in that case $p(3) = 0$ still, and we need to check consistency — but actually $p(3) = c_3$ exactly, so to have $p(3) > 0$ we need $c_3 \geq 1$.

Can $c_3 = 0$ while $p \not\equiv 0$? Yes — for example $p(x) = \binom{x}{4}$ gives $p(3) = 0$. But the question asks for the **minimum positive value** achieved (since the problem says $p$ is not identically zero and asks for the minimum of $p(3)$).

Wait — actually $p(3)$ can equal $0$ (e.g., $p(x) = \binom{x}{4}$ gives $p(0)=p(1)=p(2)=p(3)=0$). The question as stated asks for the minimum **positive** value of $p(3)$, i.e., the smallest $p(3) > 0$.

From Step 3, $p(3) = c_3$, so the minimum positive integer value is $c_3 = 1$, achieved by:

$$\boxed{p(x) = \binom{x}{3} = \frac{x(x-1)(x-2)}{6}.}$$

**Verification:**
- $p(0) = p(1) = p(2) = 0$ ✓
- $p(3) = \binom{3}{3} = 1$ ✓
- $p(n) = \binom{n}{3} \geq 0$ for all $n \geq 0$ ✓
- $p(n)$ is an integer for all integers $n$ ✓

**The minimum positive value of $p(3)$ is $\mathbf{1}$**, achieved by $p(x) = \frac{x(x-1)(x-2)}{6}$.

This is beautiful because $\frac{x(x-1)(x-2)}{6}$ is not obviously integer-valued — yet it counts $\binom{n}{3}$, the number of 3-element subsets of an $n$-element set, which is always a non-negative integer!
