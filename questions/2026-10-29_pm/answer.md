# Answer: The Function Polynomials Cannot Reach

## Key Idea / Intuition

On the circle, $\bar z = 1/z$. Polynomials are holomorphic *inside* the disk, so integrating them around the circle always gives $0$. The function $1/z$ has a pole at the center, so its integral is $2\pi i$. Uniform convergence preserves integrals, which gives a contradiction. The hole in the middle, with the pole sitting inside it, is the whole obstruction.

Once you cut a gap in the circle, the pole at $0$ is no longer trapped. You can "push" it out through the gap all the way to $\infty$, where a function with a pole looks like a polynomial.

---

## Formal Proof / Solution

### Part (a): integrate around the circle

On $\mathbb{T}$ we have $\bar z = 1/z$, so
$$
\oint_{|z|=1} \bar z \, dz = \oint_{|z|=1} \frac{dz}{z} = 2\pi i.
$$

For any polynomial $p$, Cauchy's theorem (or simply $\oint z^k\,dz = 0$ for $k \ge 0$) gives
$$
\oint_{|z|=1} p(z)\, dz = 0.
$$

Suppose $p_n \to \bar z$ uniformly on $\mathbb{T}$. Then
$$
\left| \oint p_n\,dz - \oint \bar z\,dz \right| \le 2\pi \sup_{\mathbb{T}} |p_n - \bar z| \to 0.
$$
This forces $0 \to 2\pi i$, a contradiction. $\blacksquare$

**Alternative view (maximum principle).** If $p_n$ is uniformly Cauchy on $\mathbb{T}$, then by the maximum principle it is uniformly Cauchy on the closed disk. So $p_n \to F$ uniformly on the closed disk, where $F$ is holomorphic inside and continuous up to the boundary, with $F = 1/z$ on $\mathbb{T}$.

Now consider $g(z) = zF(z) - 1$. It is holomorphic in the disk, continuous on the closed disk, and vanishes on $\mathbb{T}$. By the maximum principle $g \equiv 0$. Evaluating at $z=0$ gives $-1 = 0$, which is absurd.

This version shows clearly that the limit would have to be a holomorphic extension of $1/z$ into the disk, and none exists.

### Part (b): pole pushing through the gap

On $K$ we again have $\bar z = 1/z$, so it suffices to approximate $1/z$ uniformly on $K$ by polynomials. The set $\mathbb{C}\setminus K$ is connected: the gap near $z=1$ joins the inside of the circle to the outside. So there is a path $\gamma$ from $0$ to the point $R$ (with $R > 2$) that stays at distance at least some $\eta > 0$ from $K$. Concretely, take the real segment $[0, R]$, which passes through the gap at $z = 1$.

**Step 1 (move a pole a little).** Suppose $|a - b| < \tfrac12\operatorname{dist}(b, K)$. Then for $z \in K$,
$$
\frac{1}{z-a} = \frac{1}{(z-b) - (a-b)} = \sum_{k\ge 0} \frac{(a-b)^k}{(z-b)^{k+1}},
$$
and the ratio $\left|\frac{a-b}{z-b}\right| \le \tfrac12$ uniformly on $K$. So $1/(z-a)$ is a uniform limit on $K$ of polynomials in $1/(z-b)$.

**Step 2 (chain along the path).** Let $\mathcal{A}_b$ be the uniform closure on $K$ of polynomials in $1/(z-b)$. This set is closed under sums and products.

By Step 1, $1/(z-a) \in \mathcal{A}_b$. Since $\mathcal{A}_b$ is a closed algebra, it follows that $\mathcal{A}_a \subseteq \mathcal{A}_b$ whenever $a$ and $b$ are close relative to $\eta$.

Cover $\gamma$ by finitely many such steps $0 = a_0, a_1, \dots, a_N = R$. This gives
$$
\frac1z \in \mathcal{A}_{a_0} \subseteq \mathcal{A}_{a_1} \subseteq \cdots \subseteq \mathcal{A}_R.
$$

**Step 3 (absorb the pole at a far point).** For $|z| = 1 < R/2$,
$$
\frac{1}{z - R} = -\frac{1}{R}\sum_{k \ge 0} \left(\frac{z}{R}\right)^k,
$$
which converges uniformly on $K$. So $1/(z-R)$ is a uniform limit of polynomials in $z$. Hence $\mathcal{A}_R$ is contained in the uniform closure of polynomials in $z$.

Combining the steps, $\bar z = 1/z$ is a uniform limit of polynomials on $K$. $\blacksquare$

### What changed?

In (a), the pole at $0$ is enclosed by $\mathbb{T}$: it lies in a bounded component of $\mathbb{C}\setminus\mathbb{T}$. Polynomials can never "reach" a bounded complementary component. In (b), $\mathbb{C}\setminus K$ is connected, so the pole can be dragged out to $\infty$.

This is exactly **Runge's theorem**: if $K$ is compact and $\mathbb{C}\setminus K$ is connected, every function holomorphic near $K$ is a uniform limit of polynomials on $K$. The stronger **Mergelyan's theorem** says that for such $K$, continuity on $K$ plus holomorphy in the interior suffices. Since $K$ here has empty interior, *every* continuous function on the arc is a uniform polynomial limit, just as in the real Weierstrass theorem.

**Contrast with Stone–Weierstrass:** on the full circle, polynomials in *both* $z$ and $\bar z$ (trigonometric polynomials) are dense in $C(\mathbb{T})$. Part (a) shows that the $\bar z$ is genuinely needed.

*Reference:* Stein & Shakarchi, *Complex Analysis*, Ch. 2, §5.4 (Runge's approximation theorem and the pole-pushing argument).
