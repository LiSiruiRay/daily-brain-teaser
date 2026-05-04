# Answer: Dini's Theorem

$$\boxed{f_n \to f \text{ uniformly on } [0,1]}$$

---

## Intuition First

Define $g_n = f_n - f \geq 0$. We need to show $\sup_{x \in [0,1]} g_n(x) \to 0$.

The key picture: fix any $\varepsilon > 0$. For each point $x$, there is some $N(x)$ such that $g_{N(x)}(x) < \varepsilon$ (by pointwise convergence). So the open set $U_n = \{x : g_n(x) < \varepsilon\}$ expands as $n$ grows (monotonicity means $g_n \geq g_{n+1}$, so $U_n \subset U_{n+1}$), and **every point** eventually falls inside one of these sets.

The sets $\{U_n\}$ form an **open cover** of the compact set $[0,1]$. By compactness, finitely many suffice — so one single $U_N$ already covers everything. That means $g_N(x) < \varepsilon$ for **all** $x$ simultaneously. Done.

**Compactness is doing exactly one thing here:** turning "every point is eventually fine" into "there is a single $N$ that works for all points at once."

---

## Why Each Hypothesis Is Necessary

Before the proof, here's why you cannot drop any condition:

| Drop this | Counterexample |
|-----------|---------------|
| Compact domain | $f_n(x) = \frac{1}{nx+1}$ on $(0,1)$ — monotone, $f_n \to 0$, but not uniformly |
| Monotone | $f_n(x) = x^n(1-x^n)$ on $[0,1]$ — pointwise $\to 0$, not monotone, not uniform |
| Continuous limit | $f_n(x) = x^n$ on $[0,1]$ — limit is $\mathbf{1}_{\{1\}}$, discontinuous, not uniform |

---

## Formal Proof

Let $g_n = f_n - f$. Each $g_n$ is continuous (difference of continuous functions), $g_n \geq 0$, and $g_n \searrow 0$ pointwise on $[0,1]$.

**Goal:** $\|g_n\|_\infty \to 0$.

Fix $\varepsilon > 0$. Define:
$$U_n = \{x \in [0,1] : g_n(x) < \varepsilon\}$$

Each $U_n$ is open in $[0,1]$ (preimage of $(-\infty, \varepsilon)$ under the continuous function $g_n$).

Since $g_n \searrow 0$ pointwise, for each $x$ there exists $N(x)$ with $g_{N(x)}(x) < \varepsilon$, so $x \in U_{N(x)}$. Thus:
$$[0,1] = \bigcup_{n=1}^{\infty} U_n$$

Since $g_n$ is decreasing, $U_n \subset U_{n+1}$ (if $g_n(x) < \varepsilon$ then $g_{n+1}(x) \leq g_n(x) < \varepsilon$).

By **compactness** of $[0,1]$, the open cover $\{U_n\}$ has a finite subcover. Since the $U_n$ are nested, the finite subcover is just $\{U_N\}$ for the largest index $N$ appearing. So:
$$[0,1] = U_N = \{x : g_N(x) < \varepsilon\}$$

For all $n \geq N$ and all $x \in [0,1]$:
$$0 \leq g_n(x) \leq g_N(x) < \varepsilon$$

Therefore $\|g_n\|_\infty < \varepsilon$ for all $n \geq N$, which is exactly uniform convergence. $\blacksquare$
