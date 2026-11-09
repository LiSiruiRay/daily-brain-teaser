# Answer: There Is No Slowest Divergent Series

## Key Idea / Intuition

Think of $S$ as a function growing to infinity and $a_n$ as its increment $dS$. Then $\sum a_n/S_n$ behaves like $\int dS/S = \log S$, which still diverges, only much more slowly than $S$. Likewise $\sum a_n/S_n^2$ behaves like $\int dS/S^2 = -1/S$, which converges.

For (a), the discrete proof uses one observation. Look at a long block of terms $a_{m+1}, \dots, a_n$ and bound every denominator by the **largest** one, $S_n$. The block then contributes at least $(S_n - S_m)/S_n$. This is close to $1$ once $S_n \gg S_m$, so the tails never become small.

For (b), the bound $S_n^2 \ge S_{n-1}S_n$ turns each term into a telescoping difference $\frac{1}{S_{n-1}} - \frac{1}{S_n}$.

---

## Formal Proof / Solution

### (a) $\sum a_n/S_n$ diverges

We violate the Cauchy criterion. Fix any $m$ and let $n > m$. Since $S_k \le S_n$ for $k \le n$,
$$\sum_{k=m+1}^{n} \frac{a_k}{S_k} \;\ge\; \frac{1}{S_n}\sum_{k=m+1}^{n} a_k \;=\; \frac{S_n - S_m}{S_n} \;=\; 1 - \frac{S_m}{S_n}.$$

Because $S_n \to \infty$, for each fixed $m$ we can choose $n > m$ with $S_n \ge 2S_m$. For that $n$ the block sum is at least $\tfrac12$.

So for every $m$ there is a block of terms beyond $m$ whose sum is at least $\tfrac12$. The Cauchy criterion fails, and the series diverges. $\blacksquare$

### (b) $\sum a_n/S_n^2$ converges

For $n \ge 2$ we have $S_n \ge S_{n-1} > 0$. Hence
$$\frac{a_n}{S_n^2} \;\le\; \frac{a_n}{S_{n-1}S_n} \;=\; \frac{S_n - S_{n-1}}{S_{n-1}S_n} \;=\; \frac{1}{S_{n-1}} - \frac{1}{S_n}.$$

Summing from $n=2$ to $N$ telescopes:
$$\sum_{n=2}^{N} \frac{a_n}{S_n^2} \;\le\; \frac{1}{S_1} - \frac{1}{S_N} \;<\; \frac{1}{a_1}.$$

The partial sums are increasing and bounded, so the series converges. $\blacksquare$

(Note that (b) did not use divergence of $\sum a_n$ at all.)

### (c) No slowest divergent series

Given a divergent positive series $\sum a_n$, set $b_n = a_n/S_n$. By (a), $\sum b_n$ diverges. Moreover,
$$\frac{b_n}{a_n} = \frac{1}{S_n} \longrightarrow 0.$$

So $\sum b_n$ diverges with terms that are eventually negligible compared to those of $\sum a_n$. Its partial sums grow roughly like $\log S_n$.

Iterating the construction gives a never-ending hierarchy:
$$\sum \frac1n,\quad \sum \frac{1}{n\log n},\quad \sum \frac{1}{n\log n\,\log\log n},\ \dots$$
Each series diverges, and each diverges more slowly than the one before. No single divergent series can therefore serve as a universal comparison test for divergence. $\blacksquare$

### Bonus: $\sum a_n/S_n^{1+\varepsilon}$ converges

The function $x \mapsto x^{-1-\varepsilon}$ is decreasing. On the interval $[S_{n-1}, S_n]$, which has length $a_n$, it is therefore at least $S_n^{-1-\varepsilon}$. This gives
$$\frac{a_n}{S_n^{1+\varepsilon}} \;\le\; \int_{S_{n-1}}^{S_n} \frac{dx}{x^{1+\varepsilon}}.$$

Summing over $n \ge 2$ gives
$$\sum_{n\ge 2} \frac{a_n}{S_n^{1+\varepsilon}} \;\le\; \int_{S_1}^{\infty} \frac{dx}{x^{1+\varepsilon}} \;=\; \frac{1}{\varepsilon\, S_1^{\varepsilon}} \;<\; \infty.$$

This makes the continuous heuristic exact. The exponent $1$ is the sharp threshold: $\int dx/x$ diverges and $\int dx/x^{1+\varepsilon}$ converges, and the discrete sums inherit exactly this behaviour. $\blacksquare$

**Remark.** This is the **Abel–Dini theorem**. A dual statement holds for convergent series. If $\sum a_n$ converges with tails $r_n = \sum_{k\ge n} a_k$, then $\sum a_n/\sqrt{r_n}$ still converges. So there is no "most slowly converging" series either.
