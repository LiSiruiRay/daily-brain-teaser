# Answer: Growth Bound Forces Singularity Type

## Key Idea / Intuition

The growth rate of $|f(z)|$ near a singularity is the fingerprint of what kind of singularity it is. A pole of order $n$ behaves exactly like $1/|z|^n$ near $0$. An essential singularity has no definite growth rate (it oscillates wildly). A removable singularity stays bounded. Here, $|f(z)| \leq C/|z|^{3/2}$ tells us $f$ blows up no faster than $|z|^{-3/2}$ — but $3/2$ is not an integer! Poles have integer orders. So the singularity cannot be a pole of any integer order. But it also cannot be essential (essential singularities are not bounded by any power of $1/|z|$). The key resolution: multiplying by $z^2$ makes the product bounded near $0$, so the singularity of $z^2 f(z)$ is removable — and working backward pins down exactly what $f$ must look like.

---

## Formal Proof / Solution

**Step 1: Rule out essential singularity.**

Near an essential singularity, by Casorati–Weierstrass, $f$ takes values dense in $\mathbb{C}$; in particular it cannot satisfy $|f(z)| \leq C|z|^{-3/2}$ for small $|z|$ (a controlled growth bound). So $z = 0$ is **not** an essential singularity.

**Step 2: Consider $g(z) = z^2 f(z)$.**

By hypothesis,
$$|g(z)| = |z|^2 |f(z)| \leq C |z|^{2 - 3/2} = C |z|^{1/2} \to 0 \quad \text{as } z \to 0.$$

So $g(z) \to 0$ as $z \to 0$. Since $g$ is analytic on $0 < |z| < 1$ and bounded near $0$, by **Riemann's removable singularity theorem**, $g$ extends to an analytic function on the full disk $|z| < 1$ with $g(0) = 0$.

**Step 3: Determine $f$.**

Since $g(0) = 0$ and $g$ is analytic, we can write
$$g(z) = z^k h(z)$$
for some integer $k \geq 1$ and $h$ analytic with $h(0) \neq 0$.

Therefore
$$f(z) = \frac{g(z)}{z^2} = z^{k-2} h(z).$$

- If $k \geq 2$: then $f(z) = z^{k-2} h(z)$ extends to an analytic function at $0$ (removable singularity).
- If $k = 1$: then $f(z) = z^{-1} h(z)$, a **pole of order 1** (simple pole).

**Step 4: Check consistency with the growth bound.**

- A **pole of order $n$** satisfies $|f(z)| \sim C|z|^{-n}$ near $0$.
- The bound $|f(z)| \leq C|z|^{-3/2}$ is satisfied by poles of order $n \leq 3/2$, i.e., $n \leq 1$ (since $n$ must be a non-negative integer).

So $f$ has either:
- A **removable singularity** at $z = 0$, or
- A **pole of order 1** (simple pole) at $z = 0$.

**Conclusion:**

$$\boxed{z = 0 \text{ is either a removable singularity or a simple pole.}}$$

The bound $|f(z)| = O(|z|^{-3/2})$ is not tight enough to force a pole, but it rules out poles of order $\geq 2$ and rules out essential singularities entirely. The precise answer: **the order of the singularity is at most 1**.

**Elegant takeaway:** The non-integer exponent $3/2$ is the surprise — it forces the singularity to be "between" a simple pole and a removable singularity, and the argument via $z^2 f(z)$ cleanly resolves this.
