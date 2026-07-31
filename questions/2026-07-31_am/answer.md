# Answer: Sums That Know Their Parts

## Key Idea / Intuition

The constraint $a_1 \leq a_2 \leq \cdots \leq a_k \leq a_1 + 1$ forces all the $a_i$ to be nearly equal — they can take at most **two consecutive integer values**. So a valid partition of $n$ into $k$ parts is really just a way to write $n = k \cdot q + r$ where $r$ parts equal $q+1$ and $k - r$ parts equal $q$. The number of such decompositions turns out to equal the number of **divisors of $n$**.

The key observation: a valid representation is completely determined by the choice of $k$ (the number of parts), because once you fix $k$, the Euclidean division $n = kq + r$ (with $0 \le r < k$) uniquely determines $q$ and $r$, hence the entire multiset $\{q, \ldots, q, q+1, \ldots, q+1\}$.

---

## Formal Proof / Solution

**Step 1: Characterize valid representations.**

Suppose $n = a_1 + a_2 + \cdots + a_k$ with $a_1 \leq a_2 \leq \cdots \leq a_k \leq a_1 + 1$.

Since consecutive terms differ by at most $1$, and the sequence is non-decreasing with max $\leq \min + 1$, every $a_i$ is either $\lfloor n/k \rfloor$ or $\lceil n/k \rceil$. More precisely, there exist integers $q \geq 1$ and $0 \leq r < k$ such that:
- $r$ of the parts equal $q+1$, and
- $k - r$ of the parts equal $q$,

giving $n = r(q+1) + (k-r)q = kq + r$, i.e., $q = \lfloor n/k \rfloor$ and $r = n \mod k$.

**Step 2: Each $k$ gives exactly one representation.**

For any $k$ with $1 \leq k \leq n$, the Euclidean division $n = kq + r$ with $0 \leq r < k$ is unique. This uniquely defines the multiset of parts (all $q$'s and $(q+1)$'s). We need $q \geq 1$, which holds iff $k \leq n$.

So there is **exactly one** valid representation for each $k \in \{1, 2, \ldots, n\}$. But wait — do we require all parts to be positive? Yes: $q = \lfloor n/k \rfloor \geq 1$ iff $k \leq n$. ✓

**Step 3: Count the representations.**

Every $k \in \{1, 2, \ldots, n\}$ yields a valid representation. But wait — should we count separately representations that differ only by $k$?

Let's verify with $n = 4$:
- $k=1$: $4$ ✓
- $k=2$: $2+2$ ✓
- $k=3$: $1+1+2$ ✓
- $k=4$: $1+1+1+1$ ✓

That's 4 representations for $n=4$, and indeed all values $k=1,2,3,4$ are valid.

**Step 4: Identify which $k$ are valid — the divisor connection.**

Actually, let's be more careful. A representation has $r=0$ (all parts equal) if and only if $k \mid n$. In that case it's a uniform partition. If $r > 0$, the parts are not all equal but still valid. Every $k \in \{1, \ldots, n\}$ gives a valid, distinct representation (different $k$ means different number of parts).

**Therefore, the total number of valid representations equals $n$.**

$$\boxed{n}$$

*Check:* $n=1$: only $1$ itself. ✓ &nbsp; $n=2$: $2$ and $1+1$. ✓ &nbsp; $n=3$: $3$, $1+2$, $1+1+1$. ✓ &nbsp; $n=4$: four ways, as given. ✓
