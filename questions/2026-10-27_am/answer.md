# Answer: A Compact Space Has No Room for a Proper Isometric Copy of Itself

## Key Idea / Intuition

Suppose an isometry missed some point $a$. Then $a$ lies at some positive distance $\varepsilon$ from the image. Push $a$ forward repeatedly: $a, f(a), f^2(a), \dots$. Because $f$ is rigid, any two points of this orbit are at least $\varepsilon$ apart, just as $a$ is from everything in the image. So we get infinitely many points that are uniformly separated. A compact space cannot hold such a set: every sequence must have a convergent, hence Cauchy, subsequence. This is the metric version of "an injection of a finite set into itself is a bijection."

---

## Formal Proof / Solution

### (a) Compactness forces surjectivity

**Step 1: The image is closed.** An isometry is continuous, since it is $1$-Lipschitz. So $f(X)$ is a continuous image of a compact space and is compact. Compact subsets of a metric space are closed, so $f(X)$ is closed.

**Step 2: A missed point is at positive distance from the image.** Suppose for contradiction that some $a \in X$ satisfies $a \notin f(X)$. The set $X \setminus f(X)$ is open, so there is an $\varepsilon > 0$ with $B(a,\varepsilon) \cap f(X) = \varnothing$. In other words,
$$d(a, y) \ge \varepsilon \quad \text{for every } y \in f(X).$$

**Step 3: The orbit of $a$ is $\varepsilon$-separated.** Define $x_0 = a$ and $x_{n+1} = f(x_n)$, so $x_n = f^n(a)$. Take indices $0 \le m < n$. Applying the isometry property $m$ times gives
$$d(x_m, x_n) = d\big(f^m(a), f^m(f^{n-m}(a))\big) = d\big(a, f^{n-m}(a)\big).$$
Since $n - m \ge 1$, the point $f^{n-m}(a)$ lies in $f(X)$. By Step 2,
$$d(x_m, x_n) \ge \varepsilon \qquad \text{for all } m \ne n.$$

**Step 4: Contradiction.** A compact metric space is sequentially compact, so $(x_n)$ has a convergent subsequence. A convergent subsequence is Cauchy, so two of its terms would be closer than $\varepsilon$. This contradicts Step 3. Hence $f(X) = X$.

**Step 5: $f$ is a homeomorphism.** $f$ is injective, because $f(x) = f(y)$ gives $d(x,y) = d(f(x), f(y)) = 0$. So $f$ is a bijection. Its inverse is also an isometry:
$$d(f^{-1}u, f^{-1}v) = d\big(f(f^{-1}u), f(f^{-1}v)\big) = d(u,v).$$
So $f^{-1}$ is continuous as well, and $f$ is a homeomorphism (in fact a surjective self-isometry). Alternatively, use the general fact that a continuous bijection from a compact space to a Hausdorff space is a homeomorphism. $\blacksquare$

### (b) Complete and bounded is not enough

Let $B = \{x \in \ell^2 : \|x\|_2 \le 1\}$ be the closed unit ball of the Hilbert space $\ell^2$. It is closed and bounded in a complete space, so it is itself complete and bounded. Define the right shift
$$S(x_1, x_2, x_3, \dots) = (0, x_1, x_2, \dots).$$
- $S$ preserves norms, so $S(B) \subseteq B$. It is linear, so $\|Sx - Sy\| = \|S(x-y)\| = \|x-y\|$, which makes $S$ an isometry.
- Every vector in $S(B)$ has first coordinate $0$. So $e_1 = (1,0,0,\dots) \in B$ is not in the image.

The proof in (a) fails here exactly as it should. The orbit $e_1, e_2, e_3, \dots$ satisfies $\|e_m - e_n\| = \sqrt{2}$ for $m \ne n$. This is a uniformly separated sequence inside a bounded set, which is possible only because $B$ is not compact.

An unbounded example is $[0,\infty)$ with $x \mapsto x+1$. It is a complete space with an isometry that misses $[0,1)$.

### Remarks
- **Source of the trick:** this is the "orbit of the hole" argument. The same idea shows that a compact metric space is never isometric to a proper subset of itself.
- **A stronger theorem (Freudenthal–Hurewicz):** on a compact metric space, any non-contracting map, meaning $d(f x, f y) \ge d(x,y)$ for all $x,y$, is automatically a surjective isometry. The proof is a more delicate version of the same compactness idea.
