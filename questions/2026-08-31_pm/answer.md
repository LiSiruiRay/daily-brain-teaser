# Answer: The Lebesgue Integral That Measures Its Own Level Sets

## Key Idea / Intuition

Instead of slicing the domain horizontally (the usual Riemann picture), slice it **vertically in the range**: the integral of a non-negative function equals the "area under its graph," and that area can be computed by stacking horizontal slices of width $dt$, each slice having length equal to the measure of the level set $\{f > t\}$. This is the **layer-cake (Cavalieri) representation** — a fundamental alternative way to think about integration that replaces knowing $f$ pointwise with knowing the sizes of its superlevel sets.

---

## Formal Proof / Solution

### Step 1: Prove the layer-cake formula

Consider the product space $[0,1] \times [0,\infty)$ with the product measure $m \times m$. Look at the region under the graph:

$$E = \{(x, t) : x \in [0,1],\; 0 \leq t < f(x)\}.$$

Since $f$ is measurable, $E$ is a measurable subset of $[0,1] \times [0,\infty)$.

**Compute $m \times m(E)$ by slicing in $x$:**

For each fixed $x$, the slice $\{t : 0 \leq t < f(x)\}$ has measure $f(x)$. So by Fubini/Tonelli:

$$m \times m(E) = \int_0^1 f(x)\, dx.$$

**Compute $m \times m(E)$ by slicing in $t$:**

For each fixed $t \geq 0$, the slice $\{x \in [0,1] : t < f(x)\} = \{f > t\}$ has measure $m(\{f > t\})$. So:

$$m \times m(E) = \int_0^\infty m(\{x : f(x) > t\})\, dt.$$

Since both expressions equal $m \times m(E)$, we conclude:

$$\boxed{\int_0^1 f(x)\, dx = \int_0^\infty m(\{f > t\})\, dt.}$$

---

### Step 2: Apply it to $f(x) = x^n$

We need to compute $m(\{x \in [0,1] : x^n > t\})$ for each $t \geq 0$.

- If $t \geq 1$: the set $\{x^n > t\}$ is empty (since $x \leq 1$), so measure $= 0$.
- If $0 \leq t < 1$: the condition $x^n > t$ means $x > t^{1/n}$, so the set is $(t^{1/n}, 1]$, which has measure $1 - t^{1/n}$.

Therefore:

$$\int_0^\infty m(\{x^n > t\})\, dt = \int_0^1 \left(1 - t^{1/n}\right) dt$$

$$= \left[t - \frac{t^{1/n + 1}}{1/n + 1}\right]_0^1 = 1 - \frac{1}{1/n + 1} = 1 - \frac{n}{n+1} = \frac{1}{n+1}.$$

So we recover $\displaystyle\int_0^1 x^n\, dx = \frac{1}{n+1}$ without ever computing an antiderivative of $x^n$ directly — just by measuring level sets!

---

### Why this is beautiful

The layer-cake formula is **not just a trick** — it is the conceptual foundation for:
- The definition of the **Lebesgue integral** via the distribution function,
- **Lp interpolation** and norm identities,
- Geometric inequalities like the **Brunn–Minkowski theorem**.

It says: to integrate $f$, you don't need to know $f$ itself — knowing the **size of its superlevel sets** (its **distribution**) is enough.
