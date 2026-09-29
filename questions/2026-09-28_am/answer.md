# Answer: The Equicontinuous Sequence That Must Converge

## Key Idea / Intuition

Equicontinuity is the key: it lets us "spread" convergence from a dense set to the whole interval without losing control. Since $[0,1]$ is compact and the family is equicontinuous, a dense set of convergence points is actually enough — every other point is sandwiched between nearby dense points where we already know convergence holds, and the equicontinuity gap is small.

---

## Formal Proof / Solution

**Step 1: $f$ is well-defined and $f_n \to f$ pointwise on all of $[0,1]$.**

Fix any $x \in [0,1]$. Given $\varepsilon > 0$, by equicontinuity, there exists $\delta > 0$ such that for all $n$ and all $y$ with $|x - y| < \delta$:
$$|f_n(x) - f_n(y)| < \varepsilon.$$

Since $D$ is dense, pick $d \in D$ with $|x - d| < \delta$. Then:
$$|f_n(x) - f_m(x)| \leq |f_n(x) - f_n(d)| + |f_n(d) - f_m(d)| + |f_m(d) - f_m(x)| < 2\varepsilon + |f_n(d) - f_m(d)|.$$

Since $f_n(d) \to f(d)$, the sequence $(f_n(d))$ is Cauchy, so for large $n, m$:
$$|f_n(x) - f_m(x)| < 3\varepsilon.$$

Hence $(f_n(x))$ is Cauchy, so $f_n(x) \to f(x)$ for every $x \in [0,1]$, and $f$ is well-defined.

**Step 2: Uniform convergence.**

Let $\varepsilon > 0$. By equicontinuity, there exists $\delta > 0$ such that for all $n$ and all $x, y \in [0,1]$ with $|x - y| < \delta$:
$$|f_n(x) - f_n(y)| < \varepsilon.$$

Taking $n \to \infty$, by pointwise convergence we also get:
$$|f(x) - f(y)| \leq \varepsilon \quad \text{for } |x-y| < \delta.$$

Now cover $[0,1]$ by finitely many balls $B(x_k, \delta)$, $k = 1, \ldots, K$ (by compactness). For each center $x_k$, since $f_n(x_k) \to f(x_k)$, there exists $N_k$ such that for $n \geq N_k$:
$$|f_n(x_k) - f(x_k)| < \varepsilon.$$

Let $N = \max_k N_k$. For any $x \in [0,1]$, pick $x_k$ with $|x - x_k| < \delta$. Then for $n \geq N$:
$$|f_n(x) - f(x)| \leq |f_n(x) - f_n(x_k)| + |f_n(x_k) - f(x_k)| + |f(x_k) - f(x)| < \varepsilon + \varepsilon + \varepsilon = 3\varepsilon.$$

Since $\varepsilon > 0$ and $N$ are independent of $x$, we conclude $f_n \to f$ **uniformly** on $[0,1]$. $\blacksquare$

**Remark:** This is essentially the proof of the **Arzelà–Ascoli theorem** from the inside out — the theorem guarantees subsequential limits; this problem shows that once pointwise limits on a dense set exist, the whole sequence converges uniformly.
