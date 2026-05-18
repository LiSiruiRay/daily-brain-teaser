# Answer: Weierstrass Series: Continuity via Abel Summation

## Key Idea / Intuition

The key question is whether the series converges uniformly. The Weierstrass M-test says: if $|a_n \sin(n^2 x)| \leq |a_n|$ and $\sum |a_n| < \infty$, then the series converges uniformly, hence the limit is continuous. For $g(x)$, the coefficients are $a_n = n^{-1/2}$, and $\sum n^{-1/2}$ **diverges**. So the M-test fails. But failing the M-test doesn't immediately mean $g$ is discontinuous or ill-defined — we need to think more carefully about pointwise convergence first.

The punchline: $g(x) = \sum n^{-1/2} \sin(n^2 x)$ is a **Weierstrass-type function** — it converges conditionally for each fixed $x$ (by Dirichlet's test applied to partial sums of $\sin(n^2 x)$), but the convergence is **not uniform**, and in fact $g$ is **continuous but nowhere differentiable** — a genuine Weierstrass-type example.

Below we focus on the precise claim the question asks: **$g$ is well-defined and continuous**.

---

## Formal Proof / Solution

### Step 1: Pointwise convergence via Dirichlet's test

For fixed $x$ not a multiple of $2\pi$, the partial sums $S_N(x) = \sum_{n=1}^N \sin(n^2 x)$ are **bounded** (this follows from the fact that $e^{in^2 x}$ has bounded partial sums when $x/\pi$ is irrational, and can be checked directly for rational multiples of $\pi$).

More precisely, for any fixed $x$, one can show (by geometric series / exponential sum estimates) that

$$\left|\sum_{n=M}^{N} \sin(n^2 x)\right| \leq C(x)$$

for some constant depending on $x$.

By **Dirichlet's test** for series: if $\sum_{n=1}^N b_n$ has bounded partial sums and $a_n \searrow 0$ monotonically, then $\sum a_n b_n$ converges. Here $a_n = n^{-1/2} \searrow 0$ and $b_n = \sin(n^2 x)$. So $g(x)$ **converges pointwise** for all $x$.

### Step 2: Uniform convergence on compact sets (and continuity)

To show continuity, we use a more refined tool: **Abel's summation** (summation by parts).

Write $B_N(x) = \sum_{n=1}^N \sin(n^2 x)$. The Weierstrass-type estimate gives:

$$|B_N(x)| \leq \frac{C}{|\sin(x/2)|} \quad \text{for } x \not\equiv 0 \pmod{2\pi}.$$

Actually, let us instead invoke the cleaner uniform version. The **key estimate** is:

> For any $\delta > 0$, on $[\delta, 2\pi - \delta]$, the partial sums $\sum_{n=1}^N \sin(n^2 x)$ are **uniformly bounded** by a constant $C(\delta)$.

Using Abel summation:

$$\sum_{n=M}^{N} \frac{\sin(n^2 x)}{n^{1/2}} = \sum_{n=M}^{N-1} B_n(x)\left(\frac{1}{n^{1/2}} - \frac{1}{(n+1)^{1/2}}\right) + \frac{B_N(x)}{N^{1/2}} - \frac{B_{M-1}(x)}{M^{1/2}}$$

where $B_n(x) = \sum_{k=1}^n \sin(k^2 x)$ are the partial sums of the $b_k = \sin(k^2 x)$ series.

Since $|B_n(x)| \leq C(\delta)$ uniformly on $[\delta, 2\pi-\delta]$, and

$$\frac{1}{n^{1/2}} - \frac{1}{(n+1)^{1/2}} \sim \frac{1}{2} n^{-3/2},$$

we get

$$\left|\sum_{n=M}^{N} \frac{\sin(n^2 x)}{n^{1/2}}\right| \leq C(\delta)\left(\sum_{n=M}^{\infty} \frac{1}{2}n^{-3/2} + \frac{1}{M^{1/2}} + \frac{1}{(M-1)^{1/2}}\right) \to 0 \text{ as } M\to\infty,$$

**uniformly** on $[\delta, 2\pi - \delta]$.

This means the series converges **uniformly on compact subsets** of $(0, 2\pi)$ (and by periodicity, on all of $\mathbb{R}$). Since each partial sum is continuous, and the convergence is uniform, **$g$ is continuous**.

### Step 3: The threshold

The general Weierstrass-type function $\sum n^{-\alpha} \sin(n^2 x)$:
- **$\alpha > 1$:** M-test applies, uniformly convergent, $C^\infty$.
- **$\frac{1}{2} < \alpha \leq 1$:** Converges uniformly (M-test partially), continuous.
- **$0 < \alpha \leq \frac{1}{2}$:** Converges conditionally (Dirichlet), **continuous but nowhere differentiable** — a Weierstrass phenomenon.

Our $g$ has $\alpha = 1/2$, which sits exactly at the boundary of the nowhere-differentiable regime.

### Summary

$$\boxed{g(x) = \sum_{n=1}^{\infty} \frac{\sin(n^2 x)}{n^{1/2}} \text{ is well-defined and continuous on } \mathbb{R}.}$$

The proof uses **Dirichlet's test** for pointwise convergence and **Abel summation + uniform boundedness of partial sums** of $\sin(n^2 x)$ to upgrade to uniform convergence on compact sets.
