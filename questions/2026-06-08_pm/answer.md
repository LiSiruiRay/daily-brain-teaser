# Answer: Monotone Convergence Fails for Decreasing Sequences Without Integrability

## Key Idea / Intuition

The Monotone Convergence Theorem (MCT) requires functions to be **non-decreasing** (or the sequence to be dominated by an integrable function in the decreasing case). The $f_n$ sequence is *decreasing* to zero, but each function has infinite integral — the "mass escapes to infinity." Fatou's Lemma says $\int \liminf f_n \leq \liminf \int f_n$, and here $0 \leq +\infty$, which is true but useless. The example crystallizes exactly *why* the decreasing case of MCT requires an integrability assumption.

---

## Formal Proof / Solution

### Part (a): Pointwise convergence to 0

Fix any $x \in \mathbb{R}$. Choose $N > x$. Then for all $n \geq N$, we have $x < n$, so $x \notin [n, \infty)$, hence $f_n(x) = 0$. Thus $f_n(x) \to 0$ for every $x$.

---

### Part (b): Each integral is infinite

For each fixed $n$:

$$\int_{\mathbb{R}} f_n \, d\mu = \int_{\mathbb{R}} \mathbf{1}_{[n,\infty)} \, d\mu = \mu([n, \infty)) = +\infty.$$

So $\int f_n = +\infty$ for all $n$, yet $\int \lim_n f_n = \int 0 = 0$. The limit of the integrals ($+\infty$) does not equal the integral of the limit ($0$).

---

### Part (c): MCT applies to $g_n$

Define $g_n(x) = \mathbf{1}_{[0,n]}(x)$. For each $x \geq 0$, once $n \geq x$ we have $g_n(x) = 1$, so $g_n(x) \nearrow 1 = \mathbf{1}_{[0,\infty)}(x)$. For $x < 0$, $g_n(x) = 0$ for all $n$.

The sequence is **non-decreasing** and **non-negative**. MCT gives:

$$\int_{\mathbb{R}} g_n \, d\mu = n \nearrow +\infty = \int_{\mathbb{R}} \mathbf{1}_{[0,\infty)} \, d\mu.$$

MCT works perfectly: both sides are $+\infty$, and they agree.

---

### The Diagnosis: What Goes Wrong for $f_n$

The standard MCT states: if $0 \leq f_1 \leq f_2 \leq \cdots$ pointwise, then $\int f_n \to \int \lim f_n$.

The $f_n$ sequence is **decreasing**, not increasing. There is a "decreasing MCT": if $f_n \searrow f$ pointwise and $\int f_1 < \infty$, then $\int f_n \to \int f$. The critical hypothesis $\int f_1 < \infty$ fails here — $f_1 = \mathbf{1}_{[1,\infty)}$ has infinite integral.

**Fatou's Lemma** gives only:

$$\int \liminf_{n\to\infty} f_n \;\leq\; \liminf_{n\to\infty} \int f_n,$$

i.e., $0 \leq +\infty$. This is true but gives no useful information. The inequality can be **strict**, and this example shows it can be maximally strict.

**Moral:** Mass can "escape to infinity" along a decreasing sequence. Without an integrable dominator (or an integrability assumption on $f_1$), limits and integrals cannot be freely exchanged.

---

Written to [Q86.md](questions/Q86.md) and [A86.md](questions/A86.md)
