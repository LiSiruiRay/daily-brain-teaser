# Answer: Hairy Ball Theorem via Degree Theory

## Key Idea / Intuition

If a nowhere-vanishing tangent vector field existed, we could use it to "rotate" every point of $S^2$ continuously toward its antipode, producing a homotopy from the identity map $\mathrm{id}_{S^2}$ to the antipodal map $a: x \mapsto -x$. But these two maps have **different degrees** — the identity has degree $+1$ and the antipodal map on $S^2$ has degree $-1$ — and homotopic maps must have the same degree. Contradiction.

---

## Formal Proof / Solution

**Step 1: Assume for contradiction that $v$ is nowhere zero.**

Suppose $v: S^2 \to \mathbb{R}^3$ is continuous, $v(x) \perp x$, and $v(x) \neq 0$ for all $x \in S^2$. By normalizing, we may assume $|v(x)| = 1$ for all $x$ (since $x \mapsto v(x)/|v(x)|$ is still continuous and tangent).

**Step 2: Construct a homotopy from $\mathrm{id}$ to the antipodal map.**

Define $H: S^2 \times [0,1] \to S^2$ by

$$H(x, t) = \cos(\pi t)\, x + \sin(\pi t)\, v(x).$$

We verify:
- $H(x, 0) = x$ (identity map).
- $H(x, 1) = -x$ (antipodal map).
- $|H(x,t)|^2 = \cos^2(\pi t)|x|^2 + \sin^2(\pi t)|v(x)|^2 = \cos^2(\pi t) + \sin^2(\pi t) = 1$, since $x \perp v(x)$ and both have unit length.

So $H(x,t) \in S^2$ for all $t$, and $H$ is continuous. This gives a **homotopy** between $\mathrm{id}_{S^2}$ and the antipodal map $a$.

**Step 3: Compute the degrees.**

The **degree** of a continuous map $f: S^n \to S^n$ is a homotopy invariant — maps in the same homotopy class have the same degree. In particular:

- $\deg(\mathrm{id}_{S^2}) = +1$.
- The antipodal map $a: x \mapsto -x$ on $S^2 \subset \mathbb{R}^3$ is a composition of **3 reflections** (one across each coordinate hyperplane). Each reflection has degree $-1$, so

$$\deg(a) = (-1)^3 = -1.$$

**Step 4: Reach a contradiction.**

Since $H$ is a homotopy from $\mathrm{id}_{S^2}$ to $a$, they must have the same degree:

$$+1 = \deg(\mathrm{id}_{S^2}) = \deg(a) = -1.$$

This is a contradiction. $\blacksquare$

**Conclusion:** No continuous nowhere-vanishing tangent vector field on $S^2$ exists. Every such field must vanish at at least one point — the "cowlick" in the hairy ball.

---

**Remark (contrast with the torus):** The torus $T^2 = S^1 \times S^1$ *does* admit a nowhere-vanishing tangent vector field (e.g., the constant angular direction). This corresponds to the fact that $\chi(T^2) = 0$, while $\chi(S^2) = 2 \neq 0$. The general result is the **Poincaré–Hopf theorem**: a smooth vector field on a compact manifold has total index equal to $\chi(M)$, so a nowhere-zero field requires $\chi(M) = 0$.
