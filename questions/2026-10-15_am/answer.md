# Answer: The Function That Cannot Explode at the Boundary

## Key Idea / Intuition

**No such function exists.** If $|f|$ became huge all along the boundary, then $1/f$ would become tiny all along the boundary. By the maximum modulus principle, a holomorphic function that is tiny on the boundary is tiny everywhere inside, so $1/f \equiv 0$. That is absurd.

The only obstacle is that $f$ might have zeros, where $1/f$ is not defined. Blowing up near the boundary forces every zero into a compact set, so there are only finitely many. We can divide them out with a polynomial.

The underlying principle is that holomorphic functions cannot be "all large on the boundary" unless they compensate with zeros inside. Dividing out the zeros removes that compensation.

---

## Formal Proof / Solution

Suppose, for contradiction, that $f$ is holomorphic on $\mathbb{D}$ and $|f(z)| \to \infty$ as $|z| \to 1^-$.

**Step 1: $f$ has only finitely many zeros.**
Choose $r < 1$ such that $|f(z)| > 1$ for $r < |z| < 1$. Then every zero of $f$ lies in the compact disk $\overline{D(0,r)}$.

Clearly $f \not\equiv 0$. By the identity theorem, the zeros of a nonzero holomorphic function have no accumulation point inside $\mathbb{D}$. A set with no accumulation point inside a compact subset of $\mathbb{D}$ is finite. Let the zeros be $a_1, \dots, a_N$, listed with multiplicity. Possibly $N = 0$.

**Step 2: Divide out the zeros.**
Let
$$
P(z) = \prod_{k=1}^N (z - a_k), \qquad g(z) = \frac{f(z)}{P(z)}.
$$
Then $g$ is holomorphic on $\mathbb{D}$, since its singularities are removable, and $g$ has **no zeros** in $\mathbb{D}$.

On $\mathbb{D}$ we have $|z - a_k| \le 2$, so $|P(z)| \le 2^N$. Therefore
$$
|g(z)| \ge \frac{|f(z)|}{2^N} \longrightarrow \infty \quad \text{as } |z| \to 1^-.
$$

**Step 3: Apply the maximum modulus principle to $h = 1/g$.**
Since $g$ never vanishes, $h = 1/g$ is holomorphic on $\mathbb{D}$. Also $|h(z)| \to 0$ as $|z| \to 1^-$.

Fix any $z_0 \in \mathbb{D}$ and any $\varepsilon > 0$. Choose $\rho$ with $|z_0| < \rho < 1$ such that $|h(z)| < \varepsilon$ on the circle $|z| = \rho$. By the maximum modulus principle on the closed disk $\overline{D(0,\rho)}$,
$$
|h(z_0)| \le \max_{|z| = \rho} |h(z)| < \varepsilon.
$$
Since $\varepsilon$ was arbitrary, $h(z_0) = 0$. Since $z_0$ was arbitrary, $h \equiv 0$.

**Step 4: Contradiction.**
This is impossible, because $h = 1/g$ satisfies $h(z)\,g(z) = 1$ and so never vanishes. Hence no such $f$ exists. $\blacksquare$

---

### Remarks

- **The same proof works on any bounded domain $\Omega$.** No holomorphic function on $\Omega$ can tend to $\infty$ at every boundary point. Boundedness of $\Omega$ is what keeps $|P|$ bounded in Step 2.
- **The contrast with $\mathbb{C}$.** On the whole plane, the "boundary" is the point $\infty$, and the polynomial $p(z) = z$ does satisfy $|p(z)| \to \infty$. In fact, the entire functions with $|f| \to \infty$ at $\infty$ are exactly the non-constant polynomials. The disk has too much boundary for this to happen.
- **The real-variable contrast.** $1/(1-x^2)$ on $(-1,1)$ works because real-smooth functions obey no maximum principle. Rigidity is what separates "holomorphic" from merely "smooth."
- **What does exist.** $f(z) = 1/(1-z)$ blows up at a single boundary point. Lacunary series such as $\sum z^{2^n}$ blow up along a dense set of radii. But no holomorphic function can blow up along the *entire* boundary at once.
