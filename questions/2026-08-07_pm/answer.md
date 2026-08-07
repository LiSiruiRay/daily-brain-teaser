# Answer: Integer-Valued Polynomials and the Binomial Basis

## Key Idea / Intuition

The standard monomials $1, x, x^2, \ldots$ are not the natural basis here. The **right** basis consists of the binomial coefficients $\binom{x}{k} = \frac{x(x-1)\cdots(x-k+1)}{k!}$. These are "integer-valued polynomials," and they form a $\mathbb{Z}$-basis for the lattice of all integer-valued polynomials. Once you write $p(x)$ in this basis, integer-valuedness at non-negative integers forces all coefficients to be integers, and then evaluating at negative integers is automatic.

---

## Formal Proof / Solution

**Step 1: The Newton forward difference basis.**

Define the polynomials
$$\binom{x}{k} = \frac{x(x-1)(x-2)\cdots(x-k+1)}{k!}, \quad k = 0, 1, 2, \ldots$$

These satisfy $\binom{n}{k} \in \mathbb{Z}$ for all $n \in \mathbb{Z}$ (standard combinatorics fact, verified by induction using $\binom{n}{k} = \binom{n-1}{k-1} + \binom{n-1}{k}$, which also works for negative $n$).

**Step 2: Write $p(x)$ in this basis.**

Any polynomial of degree $d$ can be written uniquely as
$$p(x) = \sum_{k=0}^{d} c_k \binom{x}{k}$$
for some real coefficients $c_k$. The coefficients are recovered by the **Newton forward difference formula**:
$$c_k = \Delta^k p(0)$$
where $\Delta$ is the forward difference operator $\Delta f(x) = f(x+1) - f(x)$. Explicitly:
$$c_k = \sum_{j=0}^{k} (-1)^{k-j} \binom{k}{j} p(j).$$

**Step 3: Integrality of coefficients.**

Since $p(0), p(1), \ldots, p(k)$ are all integers (by hypothesis), the formula above shows $c_k \in \mathbb{Z}$ for every $k$.

**Step 4: Integer-valuedness at all integers.**

Now for any $n \in \mathbb{Z}$ (including negative integers):
$$p(n) = \sum_{k=0}^{d} c_k \binom{n}{k}.$$

Each $\binom{n}{k} \in \mathbb{Z}$ for all $n \in \mathbb{Z}$, and each $c_k \in \mathbb{Z}$. Therefore $p(n) \in \mathbb{Z}$. $\blacksquare$

---

**Why $\binom{n}{k} \in \mathbb{Z}$ for negative $n$:**

For $n = -1, k = 2$: $\binom{-1}{2} = \frac{(-1)(-2)}{2} = 1 \in \mathbb{Z}$. In general,
$$\binom{-n}{k} = (-1)^k \binom{n+k-1}{k},$$
which is always an integer.

---

**The elegant punchline:** The set $\left\{\binom{x}{0}, \binom{x}{1}, \binom{x}{2}, \ldots\right\}$ is a $\mathbb{Z}$-basis for the ring of integer-valued polynomials. Integer-valuedness at $\{0,1,2,\ldots\}$ forces integer coefficients in this basis, which then automatically extends to all of $\mathbb{Z}$.
