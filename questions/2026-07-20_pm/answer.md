# Answer: Dini's Theorem via Compactness

## Key Idea / Intuition

The gap $g_n(x) = f_n(x) - f(x)$ is a decreasing sequence of non-negative continuous functions converging pointwise to $0$. The key is that on a compact set, you cannot have pointwise-but-not-uniform convergence to $0$ for *monotone decreasing* continuous functions: any hypothetical "escape to non-zero" would force a subsequence of points whose limit contradicts pointwise convergence, via compactness.

The argument is clean: the **superlevel sets** $\{x : g_n(x) \geq \varepsilon\}$ are closed (by continuity of $g_n$), nested (by monotonicity), and their intersection is empty (by pointwise convergence). Compactness forces one of them to already be empty.

---

## Formal Proof / Solution

**Setup.** Define $g_n = f_n - f$. Then:
- Each $g_n$ is **continuous** (difference of continuous functions).
- $g_n(x) \geq 0$ for all $x$ (since $f_n \geq f$ pointwise).
- $g_n(x) \searrow 0$ pointwise (monotone decreasing to $0$).

We want to show $\sup_{x \in [0,1]} g_n(x) \to 0$.

**Fix $\varepsilon > 0$.** Define the closed sets

$$K_n = \{ x \in [0,1] : g_n(x) \geq \varepsilon \}.$$

Each $K_n$ is **closed** since $g_n$ is continuous.

**The $K_n$ are nested:** since $g_n(x) \geq g_{n+1}(x)$ for all $x$, we have $K_{n+1} \subseteq K_n$.

**The intersection is empty:** if $x \in \bigcap_n K_n$, then $g_n(x) \geq \varepsilon$ for all $n$, contradicting $g_n(x) \to 0$.

So $\bigcap_{n=1}^\infty K_n = \emptyset$.

**Apply compactness:** $[0,1]$ is compact and the $K_n$ are closed nested subsets with empty intersection. By the **finite intersection property**, there must exist some $N$ such that $K_N = \emptyset$.

This means: for all $x \in [0,1]$, $g_N(x) < \varepsilon$.

Since $g_n$ is decreasing, for all $n \geq N$ and all $x \in [0,1]$:

$$0 \leq g_n(x) \leq g_N(x) < \varepsilon.$$

Hence $\sup_x g_n(x) < \varepsilon$ for all $n \geq N$, i.e., $f_n \to f$ uniformly. $\blacksquare$

---

## Why Each Hypothesis Is Necessary

| Hypothesis dropped | Counterexample |
|---|---|
| **Continuity of $f$** | $f_n(x) = x^n$ on $[0,1]$: continuous, monotone decreasing, pointwise limit is discontinuous, convergence is not uniform |
| **Monotonicity** | $f_n(x) = \sin^n(nx)$: pointwise $\to 0$ but not uniformly |
| **Compactness** | $f_n(x) = x/n$ on $(0,\infty)$: all hypotheses hold but $\sup g_n = \infty$ |

The compactness argument via nested closed sets is the heart of the proof — it's a perfect illustration of how compactness "forces finiteness" even in a purely analytic statement.
