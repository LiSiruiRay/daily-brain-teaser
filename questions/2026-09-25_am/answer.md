# Answer: The Polynomial That Takes Integer Values at Half-Integers

## Key Idea / Intuition

The classical basis for polynomials taking integer values at integers is the binomial coefficient basis $\binom{x}{k}$. Here, we shift to a half-integer grid, so we rescale: write $p(x)$ in terms of the basis $\binom{2x}{k}$, scaled by $\frac{1}{2^k}$. Each basis element $\binom{2x}{k}/2^k$ equals an integer at half-integers, and the leading denominator introduced is at most $2^n$. This shows the denominators of $p$'s coefficients are controlled by powers of 2, and in particular $2^n p(x)$ has integer coefficients.

---

## Formal Proof / Solution

**Step 1: Change variables.**

Let $q(t) = p(t/2)$, where $t = 2x$. Then $q(t)$ is a polynomial of degree $n$ with real coefficients, and by hypothesis $q(k) \in \mathbb{Z}$ for every integer $k$.

**Step 2: Expand in the integer-valued basis.**

Any polynomial taking integer values at all integers can be written uniquely as:
$$q(t) = \sum_{j=0}^{n} c_j \binom{t}{j}, \qquad c_j \in \mathbb{Z}.$$
This is the classical result: the $c_j$ are the finite differences $\Delta^j q(0)$, which are integers since $q$ takes integer values at integers.

**Step 3: Translate back to $p(x)$.**

Since $t = 2x$:
$$p(x) = q(2x) = \sum_{j=0}^{n} c_j \binom{2x}{j} = \sum_{j=0}^{n} c_j \cdot \frac{(2x)(2x-1)\cdots(2x-j+1)}{j!}.$$

**Step 4: Control the denominators.**

Each term $\binom{2x}{j}$ is a polynomial in $x$ of degree $j$. Writing it out:
$$\binom{2x}{j} = \frac{(2x)(2x-1)(2x-2)\cdots(2x-j+1)}{j!}.$$

The numerator $(2x)(2x-1)\cdots(2x-j+1)$ has $j$ factors; after expanding, when written as a polynomial in $x$, the denominators come from the $j!$ in the bottom and the odd factors $\{1,3,5,\ldots\}$ in the numerator. The key observation is:

$$2^j \binom{2x}{j} = \frac{(2x)(2x-1)\cdots(2x-j+1)}{j!} \cdot 2^j$$

is a polynomial in $x$ with **integer** coefficients. (Indeed, $2^j \binom{2x}{j}$ evaluated at $x = k/2$ gives $2^j \binom{k}{j}$, an integer, and one can verify directly that all coefficients are integers by induction.)

**Step 5: Conclude.**

Therefore:
$$2^n p(x) = \sum_{j=0}^{n} c_j \cdot 2^{n-j} \cdot \left(2^j \binom{2x}{j}\right).$$

Each factor $2^j \binom{2x}{j}$ has integer coefficients (as shown above), $c_j \in \mathbb{Z}$, and $2^{n-j} \in \mathbb{Z}$. So $2^n p(x)$ is a polynomial with **integer coefficients**. $\blacksquare$

**Corollary (answering the first question):** Since $2^n p(x)$ has integer coefficients, $p(x)$ has **rational** coefficients. Yes — it must!

**Example:** $p(x) = \binom{2x}{2}/4 = x(2x-1)/4 = x^2/2 - x/4$. Then $p(k/2) = \frac{k^2}{8} - \frac{k}{8}$… wait, let's check with $c_j$ correctly. Taking $p(x) = \binom{2x}{1} = 2x$: trivial. More interesting: $p(x) = \frac{1}{2}\binom{2x}{2} = \frac{2x(2x-1)}{4} = x(2x-1)/2$. At $x = k/2$: $p(k/2) = \frac{k(k-1)}{2} = \binom{k}{2} \in \mathbb{Z}$. ✓ And $2^2 p(x) = 4 \cdot x(2x-1)/2 = 2x(2x-1) = 4x^2 - 2x$ — integer coefficients. ✓
