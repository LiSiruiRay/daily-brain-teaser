# Answer: The Zeros That Refuse to Accumulate

## Key Idea / Intuition

The Identity Theorem says: if the zeros of a non-zero analytic function accumulate at an **interior** point of the domain, then the function is identically zero. The sequence $z_n = 1 - 1/n$ accumulates at $z = 1$, which is **on the boundary** of $\mathbb{D}$, not inside it — so the Identity Theorem doesn't apply, and in fact a non-trivial function can vanish on this sequence. For the second case, zeros can accumulate anywhere on the boundary, as long as they don't cluster inside, so a non-zero analytic function can vanish on an arbitrary boundary-accumulating sequence — but subject to the Blaschke condition.

---

## Formal Proof / Solution

### Case 1: $z_n = 1 - 1/n$, can $f(z_n) = 0$ for all $n$?

**Answer: Yes, this is possible.**

The accumulation point of $\{z_n\}$ is $z = 1$, which lies on the **boundary** $\partial \mathbb{D}$, not inside $\mathbb{D}$. The Identity Theorem requires an accumulation point in the **domain** of analyticity. Since $z=1 \notin \mathbb{D}$, the theorem gives no contradiction.

**Explicit example:** The Blaschke product. A sequence $\{a_n\} \subset \mathbb{D}$ is the zero set of a bounded analytic function on $\mathbb{D}$ if and only if the **Blaschke condition** holds:
$$\sum_{n=1}^\infty (1 - |a_n|) < \infty.$$

For $a_n = 1 - 1/n$, we compute:
$$\sum_{n=1}^\infty (1 - |a_n|) = \sum_{n=1}^\infty \frac{1}{n} = \infty.$$

So the Blaschke condition **fails** for this sequence! This means no bounded analytic function has exactly these zeros. However, **an unbounded analytic function can still vanish on this sequence.** For instance, consider:

$$f(z) = \exp\!\left(-\frac{1}{1-z}\right).$$

This is analytic on $\mathbb{D}$ (the argument $-1/(1-z)$ has real part $\to -\infty$ as $z \to 1$ along the real axis), not identically zero, and in fact $f(z_n) = e^{-n} \neq 0$. So this particular $f$ doesn't work directly, but the key point remains:

A cleaner explicit example with zeros on the sequence $\{1 - 1/n\}$: consider the function

$$f(z) = \sin\!\left(\frac{\pi}{1-z}\right).$$

This is analytic on $\mathbb{D}$, not identically zero, and $f(z_n) = \sin(n\pi) = 0$ for all $n \geq 1$. ✓

The zeros $z_n = 1 - 1/n$ accumulate at the boundary point $1$, not at any interior point, so the Identity Theorem is not violated.

---

### Why the Identity Theorem is the right tool

**Identity Theorem:** If $f$ is analytic on a connected open set $U$ and the zero set $\{f = 0\}$ has an accumulation point **inside** $U$, then $f \equiv 0$ on $U$.

The key word is *inside*. Boundary accumulation is not controlled by analyticity of $f$ at that point.

---

### Case 2: General sequence $w_n$ with $|w_n| \to 1$

**Answer: Also possible, subject to the Blaschke condition.**

If the sequence satisfies the Blaschke condition $\sum(1 - |w_n|) < \infty$, then the **Blaschke product**

$$B(z) = \prod_{n=1}^\infty \frac{|w_n|}{w_n} \cdot \frac{w_n - z}{1 - \overline{w_n} z}$$

converges uniformly on compact subsets of $\mathbb{D}$, is analytic and bounded ($|B| \leq 1$), and vanishes exactly on $\{w_n\}$.

If the Blaschke condition **fails**, then no **bounded** analytic function can have this zero set. However, **unbounded** analytic functions may still exist with such zeros (as in Case 1 above).

---

### Summary Table

| Situation | Accumulation point | Possible? | Reason |
|---|---|---|---|
| $z_n = 1 - 1/n$ | $z=1 \in \partial\mathbb{D}$ | **Yes** | Identity Thm doesn't apply |
| $w_n \to \partial\mathbb{D}$, Blaschke holds | boundary | **Yes** | Blaschke product works |
| Zeros accumulate at interior point | $z_0 \in \mathbb{D}$ | **No** | Identity Theorem |

The elegant takeaway: **analyticity has perfect memory inside the domain, but no control on the boundary.**
