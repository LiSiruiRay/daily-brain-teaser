# Answer: The Continuous Function That Cannot Be Monotone on Any Interval

## Key Idea / Intuition

The condition says every point has a "witness" to its right that is higher — one might expect this forces some local monotone increase. But the answer is **No**: the condition only guarantees $f$ is not eventually decreasing everywhere, yet a continuous function can still be **nowhere monotone** (neither increasing nor decreasing on any interval). The Weierstrass nowhere-differentiable function, for instance, is nowhere monotone — and one can craft a simple self-referential example to see why the condition fails to force monotonicity.

In fact, a cleaner way to see this: the condition in the problem is equivalent to saying $f$ does not attain its maximum at $x=0$ while being non-increasing, but it says **nothing** like "locally increasing." We exhibit a concrete counterexample.

---

## Formal Proof / Solution

**Claim:** No. The condition does **not** force $f$ to be non-decreasing on any subinterval.

### Step 1: Construct a Counterexample

Define $f:[0,1]\to\mathbb{R}$ by
$$f(x) = x + \varepsilon \cdot g(x),$$
where $g(x)$ is the Weierstrass nowhere-differentiable function (continuous, nowhere monotone on any interval), and $\varepsilon > 0$ is chosen very small. But let us use an even more elementary construction.

**Elementary counterexample.** Let
$$f(x) = x\sin\!\Bigl(\frac{1}{x}\Bigr) \quad (x \in (0,1]),\qquad f(0) = 0.$$

This $f$ is continuous on $[0,1]$. On **any** subinterval $[a,b]$ with $0 < a < b$, the function oscillates (the zeros $x_n = 1/(n\pi)$ accumulate at 0), so $f$ is neither non-decreasing nor non-increasing on $[a,b]$ near zero.

**Check the condition:** For any $x \in [0,1)$, we need some $y > x$ with $f(y) > f(x)$.

- For $x = 0$: $f(0) = 0$. Take $y = 1/(2\pi + \pi/2) = 2/(5\pi)$, where $\sin(1/y) = 1$, so $f(y) = y > 0 = f(0)$. ✓
- For any $x > 0$: the function $x \mapsto x$ grows, and the oscillation $x\sin(1/x)$ reaches values near $x$ on each "bump." More precisely, in any interval $(x, x+\delta)$ there are points where $\sin(1/t) = 1$, giving $f(t) = t > x \geq f(x)$ when $f(x) \leq x$. Even when $f(x) = x$ (i.e., $\sin(1/x)=1$), take $y$ slightly larger where $\sin(1/y)$ is again near 1; then $f(y) \approx y > x = f(x)$. ✓

So the condition holds everywhere, yet $f$ is **nowhere monotone** near $0$.

### Step 2: Why the Condition Is Weaker Than It Looks

The condition "$\forall x$, $\exists y > x$ with $f(y) > f(x)$" says precisely:

> $f$ does not achieve a **global** right-maximum at any point, i.e., for every $x$, $f$ is not maximized over $[x,1]$ at $x$.

This is a **global** condition (there exists some $y$ far away), not a **local** one. It does not say $f$ is increasing in a neighborhood of $x$.

### Step 3: The Contrast with a True Theorem

A correct theorem in this spirit is: if $f'(x) > 0$ at every point, then $f$ is strictly increasing (by the MVT). The condition in the problem is far weaker — it only provides one witness point per $x$, which may be far away and cannot be used to construct a monotone piece.

### Conclusion

The answer is **No**. A continuous function satisfying the condition need not be non-decreasing on any subinterval. The example $f(x) = x\sin(1/x)$ (with $f(0)=0$) demonstrates this: it satisfies the "witness" condition at every point yet is nowhere monotone near 0.
