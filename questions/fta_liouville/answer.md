# Fundamental Theorem of Algebra via Liouville — Answer

## Liouville's Theorem (given)
Every bounded entire function $f: \mathbb{C} \to \mathbb{C}$ is constant.

---

## Proof

Let $p(z)$ be a non-constant polynomial. Suppose for contradiction that $p(z) \neq 0$ for all $z \in \mathbb{C}$.

**Step 1.** Since $p$ has no roots, the function
$$f(z) = \frac{1}{p(z)}$$
is holomorphic on all of $\mathbb{C}$ (i.e., entire).

**Step 2.** Since $p$ is a non-constant polynomial, $|p(z)| \to \infty$ as $|z| \to \infty$.

Therefore $|f(z)| = 1/|p(z)| \to 0$ as $|z| \to \infty$.

In particular, there exists $R > 0$ such that $|f(z)| \leq 1$ for all $|z| > R$.

On the compact disk $|z| \leq R$, a continuous function attains its maximum, so $|f(z)| \leq M$ for some $M < \infty$.

Now $\mathbb{C}$ is covered by these two regions:
$$\mathbb{C} = \underbrace{\{|z| \leq R\}}_{\text{bounded by }M} \cup \underbrace{\{|z| > R\}}_{\text{bounded by }1}$$

Hence $|f(z)| \leq \max(M, 1)$ for all $z \in \mathbb{C}$, so $f$ is bounded on all of $\mathbb{C}$.

**Step 3.** By Liouville's Theorem, $f$ is constant. But then $p = 1/f$ is also constant — contradicting our assumption that $p$ is non-constant. $\blacksquare$

---

## Why $|p(z)| \to \infty$?

For $p(z) = a_n z^n + \cdots + a_0$ with $a_n \neq 0$:
$$|p(z)| = |z|^n \left| a_n + \frac{a_{n-1}}{z} + \cdots + \frac{a_0}{z^n} \right| \xrightarrow{|z|\to\infty} \infty$$
since the parenthesized expression $\to a_n \neq 0$.

---

## Why This Proof is Surprising

Elementary proofs of FTA (e.g., topological, via winding numbers) require more machinery or case analysis. This proof reduces everything to one theorem and one observation:

> A polynomial grows without bound. Its reciprocal is therefore bounded and entire. Liouville kills it.

The algebra–analysis bridge is the real surprise: a fact about roots of polynomials (algebra) follows from a fact about bounded holomorphic functions (analysis).

---

## Bonus: Full FTA (all $n$ roots)

Liouville gives existence of one root $z_0$. Then $p(z) = (z - z_0) q(z)$ for some degree-$(n-1)$ polynomial $q$ (polynomial long division). Apply induction: a degree-$n$ polynomial has exactly $n$ roots (counted with multiplicity) in $\mathbb{C}$.
