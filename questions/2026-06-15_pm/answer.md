# Answer: Alternating Series Beyond the M-Test

## Key Idea / Intuition

The Weierstrass M-test is a *sufficient* condition for uniform convergence, not a necessary one. Alternating series enjoy a much more delicate cancellation mechanism — adjacent terms nearly cancel, and the error after $N$ terms is bounded by the size of the **next term**, which can be made uniformly small even when the individual terms are not summable. This example cleanly separates the concepts of "absolute uniform convergence" from "uniform convergence via cancellation."

---

## Formal Proof / Solution

### Part (a): Uniform Convergence via the Alternating Series Test (Uniform Version)

Write the partial sums $S_N(x) = \sum_{n=1}^N \frac{(-1)^n}{n+x}$.

The standard **Alternating Series Estimation** says: if $a_n(x)$ is decreasing to $0$ for each $x$ and the signs alternate, then

$$|f(x) - S_N(x)| \leq a_{N+1}(x).$$

Here $a_n(x) = \frac{1}{n+x}$. For each fixed $x \in [0,1]$ this is indeed decreasing in $n$ and tends to $0$. Moreover,

$$\sup_{x \in [0,1]} a_{N+1}(x) = \sup_{x \in [0,1]} \frac{1}{N+1+x} = \frac{1}{N+1} \xrightarrow{N \to \infty} 0.$$

Therefore

$$\sup_{x \in [0,1]} |f(x) - S_N(x)| \leq \frac{1}{N+1} \to 0,$$

which is **uniform convergence**.

---

### Part (b): Continuity of $f$

Each partial sum $S_N(x) = \sum_{n=1}^N \frac{(-1)^n}{n+x}$ is a finite sum of continuous functions on $[0,1]$, hence continuous. Since $S_N \to f$ **uniformly**, and the uniform limit of continuous functions is continuous, $f$ is continuous on $[0,1]$.

---

### Part (c): Why the Weierstrass M-Test Fails Here (and Why That's Fine)

The Weierstrass M-test requires finding constants $M_n$ with $\left|\frac{(-1)^n}{n+x}\right| \leq M_n$ for all $x$ and $\sum M_n < \infty$.

The natural bound is $M_n = \frac{1}{n+0} = \frac{1}{n}$, but $\sum \frac{1}{n} = \infty$. Any other bound $M_n$ would have to satisfy $M_n \geq \frac{1}{n+1}$, so no summable dominating sequence exists.

**But the M-test is only sufficient, not necessary.** It tests for *absolute* uniform convergence:

$$\text{M-test succeeds} \iff \sum_n \sup_x |f_n(x)| < \infty.$$

Our series converges uniformly by *cancellation* between consecutive terms, not by absolute dominance. The correct tool is the **Dirichlet/Abel test for uniform convergence** (or the uniform alternating series test used above).

> **Moral:** $\sum f_n$ can converge uniformly even when $\sum |f_n|$ diverges uniformly. Cancellation is a genuine and powerful phenomenon in analysis, and the M-test is too blunt an instrument to see it.

---

### Bonus Remark

In fact $f(x)$ has a closed form. Writing the series as a difference of harmonic series one can show

$$f(x) = \sum_{n=1}^\infty \frac{(-1)^n}{n+x} = \frac{1}{2}\left[\psi\!\left(\frac{x+2}{2}\right) - \psi\!\left(\frac{x+1}{2}\right)\right],$$

where $\psi$ is the digamma function — confirming continuity and giving a rich connection to special functions.
