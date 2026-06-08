# Answer: Riemann–Lebesgue Lemma

## Key Idea / Intuition

The sine function $\sin(nx)$ oscillates faster and faster as $n \to \infty$, alternating between positive and negative with increasing frequency. Over each half-period, positive and negative contributions nearly cancel. For a nearly-constant (step) function, the cancellation is exact in the limit. For a general integrable function, we approximate by step functions and use the fact that the error can be made small uniformly in $n$.

This is a beautiful **approximation argument**: prove the result for a dense class, then use a uniform bound to pass to the limit.

---

## Formal Proof / Solution

### Step 1: Prove it for step functions

A step function is a finite linear combination of indicator functions $\mathbf{1}_{[a,b]}$. By linearity, it suffices to show

$$\int_a^b \sin(nx)\, dx \to 0 \quad \text{as } n \to \infty.$$

Direct computation:

$$\int_a^b \sin(nx)\, dx = \left[-\frac{\cos(nx)}{n}\right]_a^b = \frac{\cos(na) - \cos(nb)}{n} \leq \frac{2}{n} \to 0.$$

So the result holds for all step functions. ✓

---

### Step 2: Approximate $f$ by step functions

Since $f$ is Riemann integrable on $[0, 2\pi]$, for any $\varepsilon > 0$ there exists a step function $g$ such that

$$\int_0^{2\pi} |f(x) - g(x)|\, dx < \varepsilon.$$

(This is a standard fact: Riemann integrable functions are exactly those approximable in $L^1$ by step functions.)

---

### Step 3: Triangle inequality and conclusion

Write

$$\left|\int_0^{2\pi} f(x)\sin(nx)\, dx\right| \leq \left|\int_0^{2\pi} (f(x) - g(x))\sin(nx)\, dx\right| + \left|\int_0^{2\pi} g(x)\sin(nx)\, dx\right|.$$

For the first term, since $|\sin(nx)| \leq 1$:

$$\left|\int_0^{2\pi} (f(x) - g(x))\sin(nx)\, dx\right| \leq \int_0^{2\pi} |f(x) - g(x)|\, dx < \varepsilon.$$

For the second term, by Step 1 applied to the step function $g$:

$$\left|\int_0^{2\pi} g(x)\sin(nx)\, dx\right| \to 0 \quad \text{as } n \to \infty,$$

so there exists $N$ such that for all $n > N$, this term is also $< \varepsilon$.

Combining: for all $n > N$,

$$\left|\int_0^{2\pi} f(x)\sin(nx)\, dx\right| < 2\varepsilon.$$

Since $\varepsilon > 0$ was arbitrary, the limit is $0$. $\blacksquare$

---

### Why this is beautiful

The argument is a **two-step density trick** that appears throughout analysis:
1. Prove the result on a **dense/approximating class** (here: step functions) by direct computation.
2. Use a **uniform bound** (here: $|\sin(nx)| \leq 1$) to transfer the result to the whole space.

This exact pattern also underlies proofs in $L^p$ theory, Fourier analysis, and functional analysis far beyond this specific lemma.
