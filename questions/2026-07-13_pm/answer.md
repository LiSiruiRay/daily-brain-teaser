# Answer: Monotone Function with Countably Many Discontinuities

## Key Idea / Intuition

A monotone function can only have **jump discontinuities** — at each point of discontinuity, there is a positive "gap" between the left and right limits. The beautiful insight is that these gaps are **disjoint intervals** sitting inside $\mathbb{R}$, and the rationals thread through each one, giving a canonical injection from discontinuities into $\mathbb{Q}$.

---

## Formal Proof / Solution

**Step 1: Monotone functions have only jump discontinuities.**

Since $f$ is increasing, at every point $x \in (0,1)$ the one-sided limits exist:
$$f(x^-) = \lim_{t \nearrow x} f(t), \quad f(x^+) = \lim_{t \searrow x} f(t),$$
and satisfy $f(x^-) \leq f(x) \leq f(x^+)$.

A point $x$ is a discontinuity if and only if
$$f(x^-) < f(x^+),$$
i.e., there is a **positive jump** of size $\delta_x = f(x^+) - f(x^-) > 0$.

(Handle endpoints $0$ and $1$ similarly with one-sided limits.)

**Step 2: The jump intervals are pairwise disjoint.**

For each discontinuity $x$, associate the open interval
$$I_x = \bigl(f(x^-),\, f(x^+)\bigr) \subset \mathbb{R}.$$

Claim: if $x < y$ are both discontinuities, then $I_x \cap I_y = \emptyset$.

Indeed, since $f$ is increasing, $f(x^+) \leq f(y^-)$, so the interval $I_x$ lies entirely to the left of $I_y$:
$$f(x^-) < f(x^+) \leq f(y^-) < f(y^+).$$

**Step 3: Inject discontinuities into $\mathbb{Q}$.**

Since the intervals $\{I_x\}$ are pairwise disjoint, non-empty, and open, by density of $\mathbb{Q}$ in $\mathbb{R}$, each $I_x$ contains a rational number $q_x \in \mathbb{Q}$.

The map $x \mapsto q_x$ is injective (distinct discontinuities have disjoint intervals, hence different chosen rationals).

This gives an injection
$$\{\text{discontinuities of } f\} \hookrightarrow \mathbb{Q},$$
and since $\mathbb{Q}$ is countable, the set of discontinuities is **at most countable**. $\blacksquare$

---

**Remark (Sharpness).** The result is sharp: every countable set $S \subset [0,1]$ can be realized as the exact set of discontinuities of some increasing function. For instance, enumerate $S = \{x_1, x_2, \ldots\}$ and set
$$f(x) = \sum_{n:\, x_n \leq x} 2^{-n},$$
which is increasing with a jump of $2^{-n}$ at each $x_n$.
