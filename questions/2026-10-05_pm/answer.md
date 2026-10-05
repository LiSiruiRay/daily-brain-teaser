# Answer: The Sequence That Must Have a Convergent Subsequence... or Does It?

## Key Idea / Intuition

The sequence $\sin(nx)$ is bounded in $L^2[0,1]$, and by the Riemann–Lebesgue lemma its $L^2$-norm doesn't vanish — it stays at $1/\sqrt{2}$. By a soft functional-analysis argument, every subsequence converges weakly to zero in $L^2$, but any pointwise-everywhere convergent subsequence would have to converge to a measurable limit, and then by dominated convergence the $L^2$ norms would have to be $1/\sqrt{2}$ while the limit is zero — giving a contradiction. A more elementary route uses the **Weyl equidistribution theorem**: for any fixed irrational $x/\pi$, the values $\sin(n_k x)$ are equidistributed and can't converge. One cannot avoid such irrationalities simultaneously for all $x$.

---

## Formal Proof / Solution

**Step 1: Weak convergence to zero.**

For any $g \in L^2[0,1]$, by the Riemann–Lebesgue lemma:
$$\int_0^1 \sin(nx)\, g(x)\, dx \to 0 \quad \text{as } n \to \infty.$$

So $f_n \rightharpoonup 0$ weakly in $L^2[0,1]$, and the same holds for any subsequence.

**Step 2: $L^2$-norm stays bounded away from zero.**

$$\|f_n\|_{L^2}^2 = \int_0^1 \sin^2(nx)\, dx = \frac{1}{2} - \frac{\sin(2n)}{4n} \to \frac{1}{2}.$$

So $\|f_{n_k}\|_{L^2}^2 \to 1/2 \neq 0$ for any subsequence.

**Step 3: Pointwise a.e. convergence implies $L^2$ convergence via DCT.**

Suppose, for contradiction, that some subsequence $\sin(n_k x) \to h(x)$ pointwise **everywhere** on $[0,1]$.

Since $|\sin(n_k x)| \leq 1$, dominated convergence gives:
$$\int_0^1 h(x)^2\, dx = \lim_{k\to\infty} \int_0^1 \sin^2(n_k x)\, dx = \frac{1}{2}.$$

But weak convergence forces $h = 0$ a.e.: for any measurable set $A$,
$$\int_A h(x)\, dx = \lim_{k\to\infty} \int_0^1 \sin(n_k x)\, \mathbf{1}_A(x)\, dx = 0$$
by Riemann–Lebesgue (since $\mathbf{1}_A \in L^2 \subset L^1$).

If $\int_A h\, dx = 0$ for all measurable $A$, then $h = 0$ a.e., contradicting $\|h\|_{L^2}^2 = 1/2 > 0$.

**Conclusion.**

No subsequence $\sin(n_k x)$ can converge pointwise **everywhere** on $[0,1]$. (It can converge **almost everywhere** — that follows from the fact that $\sin(n_k x) \rightharpoonup 0$ in $L^2$ and by Banach–Saks or Komlós-type arguments a subsequence of Cesàro means converges a.e., but the full sequence itself already fails everywhere off a measure-zero set by Weyl equidistribution.)

**Bonus elegant version via Weyl.**

Fix any $x$ with $x/\pi$ irrational (a full-measure set). The sequence $\{n_k x / \pi \pmod{1}\}$ is equidistributed mod 1 for any lacunary subsequence, so $\sin(n_k x)$ visits both positive and negative values infinitely often — hence diverges. Since irrationals have full measure, no subsequence can converge everywhere.
