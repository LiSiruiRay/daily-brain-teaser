# Answer: Raising the Terms of a Convergent Series to the Power 1 − 1/n

## Key Idea / Intuition

The exponent $1-\tfrac1n$ multiplies $a_n$ by the factor $a_n^{-1/n}$. This factor is large only when $a_n$ is **exponentially small**. Split the terms into two kinds:

- **Not-too-small terms** (say $a_n \ge 2^{-n}$): the factor is at most $2$, so these terms at most double.
- **Exponentially tiny terms** ($a_n < 2^{-n}$): these are so small that, even after enlargement, they are dominated by a geometric series.

Either way, each new term is controlled by something summable. The proof is a one-line dichotomy.

---

## Formal Proof / Solution

**Answer: yes, the series always converges.**

Write $a_n^{1-1/n} = a_n \cdot a_n^{-1/n}$. For $n \ge 2$ the map $t \mapsto t^{1-1/n}$ is increasing on $(0,\infty)$. We may ignore $n=1$, since one term does not affect convergence.

**Case 1: $a_n \ge 2^{-n}$.** Then $a_n^{-1/n} \le (2^{-n})^{-1/n} = 2$, so
$$
a_n^{1-1/n} \le 2a_n .
$$

**Case 2: $a_n < 2^{-n}$.** By monotonicity,
$$
a_n^{1-1/n} \le (2^{-n})^{1-1/n} = 2^{-n+1} = 2\cdot 2^{-n}.
$$

In both cases,
$$
a_n^{1-1/n} \;\le\; 2a_n + 2\cdot 2^{-n},
$$
so by comparison
$$
\sum_{n\ge 2} a_n^{1-1/n} \le 2\sum a_n + 2\sum 2^{-n} < \infty. \qquad\blacksquare
$$

**A slicker one-liner (weighted AM–GM).** Using weights $1-\tfrac1n$ and $\tfrac1n$, and writing $1 = 2\,(2^{-n})^{1/n}$,
$$
a_n^{1-1/n} = 2\, a_n^{1-1/n}\,(2^{-n})^{1/n} \le 2\Big[\big(1-\tfrac1n\big)a_n + \tfrac1n 2^{-n}\Big] \le 2a_n + 2^{1-n}.
$$
This gives the same bound with no case split. The case split is "hidden" inside the AM–GM inequality.

---

## Bonus: How far can the exponent be pushed?

Replace $1-\frac1n$ by $1-\varepsilon_n$ with $\varepsilon_n \downarrow 0$. Run the same dichotomy with a threshold $b_n$ in place of $2^{-n}$:

- If $a_n \ge b_n$, then $a_n^{1-\varepsilon_n} \le b_n^{-\varepsilon_n}\, a_n$.
- If $a_n < b_n$, then $a_n^{1-\varepsilon_n} \le b_n^{1-\varepsilon_n}$.

Choose $b_n = e^{-c/\varepsilon_n}$. Then $b_n^{-\varepsilon_n} = e^{c}$ is bounded, and $b_n^{1-\varepsilon_n} \le e^{c}\, b_n$. So it suffices that
$$
\sum_n e^{-c/\varepsilon_n} < \infty \quad\text{for some } c>0.
$$

- **$\varepsilon_n = 1/\sqrt n$:** $\sum e^{-c\sqrt n} < \infty$, so the series still always converges.
- **$\varepsilon_n = 1/\log\log n$:** the criterion fails, since $e^{-c\log\log n} = (\log n)^{-c}$ is not summable. In fact convergence genuinely fails here. Take $a_n = \frac{1}{n(\log n)^2}$, which is summable. Then
$$
a_n^{1-\varepsilon_n} = a_n\cdot \exp\!\Big(\tfrac{\log n + 2\log\log n}{\log\log n}\Big) \ge \frac{1}{n}\cdot \frac{e^{\log n/\log\log n}}{(\log n)^2}.
$$
The last fraction tends to $\infty$, because $\frac{\log n}{\log\log n} - 2\log\log n \to \infty$. So eventually $a_n^{1-\varepsilon_n} \ge 1/n$, and the series diverges.

**Moral:** "tiny terms" and "normal terms" are dangerous for different reasons. A single cleverly chosen threshold handles both at once. This split-at-a-threshold trick recurs throughout analysis: Chebyshev-type estimates, truncation arguments, and real interpolation.
