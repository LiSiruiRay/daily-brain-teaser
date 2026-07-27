# Answer: The Monotone Function That Isn't

## Key Idea / Intuition

The two cases have surprisingly different answers. When $f' \geq 0$ everywhere, the Mean Value Theorem forces $f$ to be non-decreasing — you cannot go down without having a negative derivative somewhere. When $f' > 0$ everywhere, you might expect strict monotonicity, and indeed this is true too, but the subtlety is that "strictly positive derivative everywhere" is stronger than it sounds: there is no room for $f(a) = f(b)$ with $a < b$, since the MVT would force $f' = 0$ somewhere in between.

But here is the real conceptual trap: **can a function be everywhere differentiable with $f'(x) > 0$ for all $x$, yet fail to be strictly increasing globally?** The answer is **no** — but the proof requires care. The interesting "near-miss" is that we can construct functions where $f'$ is positive but arbitrarily small (approaching zero), which are still strictly increasing, just not uniformly so.

---

## Formal Proof / Solution

### Case 1: $f' \geq 0$ implies $f$ is non-decreasing

**Claim:** Yes, $f$ must be non-decreasing.

**Proof:** Take any $a < b$ in $[0,1]$. By the Mean Value Theorem, there exists $c \in (a,b)$ such that
$$f(b) - f(a) = f'(c)(b - a).$$
Since $f'(c) \geq 0$ and $b - a > 0$, we get $f(b) - f(a) \geq 0$, i.e., $f(b) \geq f(a)$.

So $f$ is non-decreasing. $\square$

---

### Case 2: $f' > 0$ implies $f$ is strictly increasing

**Claim:** Yes, $f$ must be strictly increasing.

**Proof:** Take any $a < b$ in $[0,1]$. By the same MVT argument:
$$f(b) - f(a) = f'(c)(b-a)$$
for some $c \in (a,b)$. Now $f'(c) > 0$ and $b - a > 0$, so $f(b) - f(a) > 0$.

Hence $f$ is strictly increasing. $\square$

---

### The Punchline and Subtlety

Both claims are true, and the proofs are almost identical. So where is the interesting mathematics?

The subtlety lives in the **converse direction**. Consider:

> **A strictly increasing, differentiable function can have $f'(x) = 0$ at some points.**

A famous example: $f(x) = x^3$ is strictly increasing on $\mathbb{R}$, but $f'(0) = 0$.

More dramatically, one can construct a strictly increasing $C^\infty$ function whose derivative vanishes on a **Cantor set** of positive measure — so $f' = 0$ on a fat set, yet $f$ is still strictly increasing!

**So the logical structure is:**
$$f' > 0 \implies f \text{ strictly increasing}$$
$$f \text{ strictly increasing} \not\implies f' > 0$$
$$f' \geq 0 \implies f \text{ non-decreasing}$$
$$f \text{ non-decreasing} \not\implies f' \geq 0 \text{ (it may not even be differentiable)}$$

The deeper lesson: **positivity of the derivative is a sufficient but not necessary condition for monotonicity**, and the MVT is the clean bridge between the local (derivative) and the global (monotone behavior).
