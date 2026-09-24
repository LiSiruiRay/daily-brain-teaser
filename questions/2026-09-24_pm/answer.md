# Answer: Natural Boundary via Factorial Lacunary Series

## Key Idea / Intuition

The series $\sum z^{n!}$ has radius of convergence exactly $1$, so $f$ is holomorphic inside $\mathbb{D}$. The key observation is that **roots of unity are dense on the unit circle**, and at every root of unity the partial sums of $f$ blow up — meaning $f$ cannot be extended even locally past any arc of the circle. The factorials in the exponents are perfectly tuned to make this blow-up happen at a dense set, which then propagates to the whole boundary.

---

## Formal Proof / Solution

**Step 1: Radius of convergence.**

By the ratio / root test, $\limsup_{n} |a_n|^{1/n} = 1$ (since the coefficients are $0$ or $1$ and $1$'s appear), so the series converges for $|z|<1$ and diverges for $|z|>1$. Thus $f$ is holomorphic on $\mathbb{D}$ and the radius of convergence is exactly $1$.

---

**Step 2: Blow-up at roots of unity.**

Fix a **primitive $p$-th root of unity** $\zeta = e^{2\pi i k/p}$ for integers $p \geq 1$, $\gcd(k,p)=1$.

For $n \geq p$, we have $p \mid n!$, so

$$\zeta^{n!} = e^{2\pi i k \cdot n!/p} = 1.$$

Therefore, for $0 < r < 1$,

$$f(r\zeta) = \sum_{n=0}^{\infty} (r\zeta)^{n!} = \underbrace{\sum_{n=0}^{p-1} r^{n!}\zeta^{n!}}_{\text{finite, bounded}} + \sum_{n=p}^{\infty} r^{n!}.$$

The tail is a **positive real series**:

$$\sum_{n=p}^{\infty} r^{n!} \xrightarrow{r \to 1^-} \sum_{n=p}^{\infty} 1 = +\infty.$$

So $|f(r\zeta)| \to +\infty$ as $r \to 1^-$.

---

**Step 3: Every boundary point is singular.**

The set of all roots of unity $\{e^{2\pi i k/p} : p \geq 1,\, 0 \leq k < p\}$ is **dense** in the unit circle $|z|=1$.

Suppose for contradiction that there exists an arc $U$ on the unit circle and a holomorphic function $g$ on $\mathbb{D} \cup U$ extending $f$. Since $g$ is continuous on the compact set $\overline{\mathbb{D}} \cap (U \cup \mathbb{D})$, it is bounded near every point of $U$. But roots of unity are dense in $U$, and we showed $|f(r\zeta)| \to \infty$ as $r \to 1^-$ for every root of unity $\zeta$. This contradicts the boundedness of $g$ near any point in $U$.

Therefore, no analytic continuation of $f$ exists across any arc of the unit circle.

---

**Conclusion.**

Every point of $|z|=1$ is a singularity of $f$, so $\mathbb{D}$ is the **natural domain of $f$**. The unit circle is a **natural boundary**. $\blacksquare$

---

**Remark (why factorials?)**

The key property used is that $n!$ is eventually divisible by every positive integer $p$. Any lacunary series $\sum z^{a_n}$ where $a_n$ grows fast enough (Hadamard's gap condition: $a_{n+1}/a_n \geq \lambda > 1$ for all $n$) also has the unit circle as a natural boundary, but the factorial case gives the cleanest density argument via roots of unity.
