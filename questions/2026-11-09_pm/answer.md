# Answer: Shrinking Without Contracting: Edelstein's Fixed Point Theorem

## Key Idea / Intuition

Measure how far each point moves: $g(x) = d(x, f(x))$. On a compact space this continuous "displacement" attains a minimum. If the minimum were positive, applying $f$ once more would strictly reduce the displacement, which is a contradiction. So the minimum is $0$, and that point is fixed.

Without compactness, nothing guarantees that the infimum of the displacement is attained. A map can creep off to infinity while its displacement decreases towards $0$ without ever reaching it. The function $\sqrt{x^2+1}$ does exactly this: it hugs the line $y=x$ asymptotically but never touches it.

---

## Formal Proof / Solution

### (a) Existence and uniqueness

**$g$ is continuous.** Define $g(x) = d(x,f(x))$. By the triangle inequality,
$$
|g(x) - g(y)| \le d(x,y) + d\big(f(x),f(y)\big) \le 2\,d(x,y).
$$
So $g$ is Lipschitz, hence continuous.

**Existence.** Since $X$ is compact, $g$ attains its minimum at some point $p$. Suppose $f(p) \neq p$. Applying strict shrinking to the distinct points $p$ and $f(p)$ gives
$$
g\big(f(p)\big) = d\big(f(p), f(f(p))\big) < d\big(p, f(p)\big) = g(p).
$$
This contradicts the minimality of $g(p)$. Hence $f(p)=p$.

**Uniqueness.** Suppose $p \ne q$ were both fixed. Then
$$
d(p,q) = d\big(f(p),f(q)\big) < d(p,q),
$$
which is absurd. $\blacksquare$

### (b) A counterexample on $\mathbb{R}$

Let $f(x) = \sqrt{x^2+1}$. The space $\mathbb{R}$ is complete.

**No fixed point.** For every $x$ we have $f(x) > \sqrt{x^2} = |x| \ge x$, so $f(x) \neq x$.

**Strictly shrinking.** Take $x \ne y$ and rationalize:
$$
|f(x)-f(y)| = \frac{|x^2-y^2|}{\sqrt{x^2+1}+\sqrt{y^2+1}} = |x-y|\cdot\frac{|x+y|}{\sqrt{x^2+1}+\sqrt{y^2+1}}.
$$
The last fraction is less than $1$, because
$$
|x+y| \le |x|+|y| < \sqrt{x^2+1}+\sqrt{y^2+1}.
$$

**Where it breaks down.** The ratio $\frac{|x+y|}{\sqrt{x^2+1}+\sqrt{y^2+1}}$ tends to $1$ as $x,y\to+\infty$. So $f$ is not a Banach contraction. The displacement $g(x) = \sqrt{x^2+1}-x \to 0$ as $x\to\infty$, but $g$ never equals $0$: the infimum is not attained.

An alternative counterexample is $f(x) = x + 1/x$ on $[1,\infty)$. Here $0 \le f' < 1$ on $(1,\infty)$, so the mean value theorem gives strict shrinking, and $f(x) > x$ everywhere.

### (c) Bonus: iterates converge

**Step 1: distances to $p$ settle down.** Fix $x$ and set $x_n = f^n(x)$ and $r_n = d(x_n, p)$. Since $p = f(p)$, we have $r_{n+1} = d(f(x_n), f(p)) \le r_n$. So $r_n$ is non-increasing and converges to some $r \ge 0$.

**Step 2: pass to a convergent subsequence.** By compactness, some subsequence satisfies $x_{n_k} \to q$. Continuity of $d(\cdot,p)$ gives $d(q,p) = r$. Since $f$ is continuous (it is $1$-Lipschitz), $x_{n_k+1} = f(x_{n_k}) \to f(q)$. Hence $d(f(q),p) = \lim_k r_{n_k+1} = r$.

**Step 3: the limit distance must be $0$.** If $q \ne p$, strict shrinking gives
$$
r = d\big(f(q), f(p)\big) < d(q,p) = r,
$$
a contradiction. So $q = p$ and $r = 0$, which means $f^n(x) \to p$. $\blacksquare$

**Moral.** Banach's theorem buys convergence with a uniform rate $c<1$. Edelstein's theorem buys it with compactness instead. The minimum of the displacement function replaces the geometric series, and you get no rate of convergence in exchange.
