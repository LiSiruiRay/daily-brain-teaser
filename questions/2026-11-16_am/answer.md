# Answer: Barbalat's Lemma: When Does an Integrable Function Have to Die Out?

## Key Idea / Intuition

A finite integral only controls **area**, and a spike can have huge height with negligible area if it is thin enough. That is the source of the counterexample. Uniform continuity says that a function cannot change much over a window of fixed width $\delta$, *the same $\delta$ everywhere*. So whenever $f$ is "large" at some point, it stays large on a whole interval of width $\delta$, and that interval carries a fixed chunk of area. Infinitely many such chunks far out contradict convergence of the integral.

---

## Formal Proof / Solution

### (a) Thin tall spikes

For each integer $n\ge 2$, place a triangular "tent" centered at $x=n$ with:
- height $n$,
- half-width $w_n = n^{-3}$, so its base is $[n-n^{-3},\,n+n^{-3}]$.

Let $f$ be zero outside these tents. These bases are disjoint, so $f$ is continuous and nonnegative.

The tent at $n$ has area $\tfrac12\cdot(2n^{-3})\cdot n = n^{-2}$. Hence
$$\int_0^\infty f = \sum_{n\ge 2}\frac{1}{n^2} < \infty,$$
and the partial integrals are monotone and bounded, so they converge.

Yet $f(n)=n\to\infty$, so $\limsup f=\infty$, and certainly $f\not\to 0$.

Note that $f$ is not uniformly continuous. The slopes of the tents are $n/n^{-3}=n^4$, which are unbounded.

### (b) Uniform continuity forces decay

Suppose, for contradiction, that $f(x)\not\to 0$. Then there exist $\varepsilon>0$ and points $x_n\to\infty$ with
$$|f(x_n)|\ge \varepsilon \quad\text{for all } n.$$

**Step 1: largeness spreads to a fixed-width window.** By uniform continuity, pick $\delta>0$ such that $|x-y|\le\delta \Rightarrow |f(x)-f(y)|<\varepsilon/2$.

Take any $x\in[x_n,x_n+\delta]$. Then $f(x)$ lies within $\varepsilon/2$ of $f(x_n)$, where $|f(x_n)|\ge\varepsilon$. So $f(x)$ has the **same sign** as $f(x_n)$, and $|f(x)|>\varepsilon/2$. Therefore
$$\left|\int_{x_n}^{x_n+\delta} f(x)\,dx\right| = \int_{x_n}^{x_n+\delta} |f(x)|\,dx \;\ge\; \frac{\varepsilon\delta}{2}.$$
The sign condition matters here: there is no cancellation inside the window.

**Step 2: contradict the Cauchy criterion.** Let $F(T)=\int_0^T f$. Since $\lim_{T\to\infty}F(T)$ exists, $F$ is Cauchy at infinity:
$$\int_a^b f = F(b)-F(a)\longrightarrow 0 \quad\text{as } a,b\to\infty.$$
But with $a=x_n$ and $b=x_n+\delta$, both tending to $\infty$, Step 1 gives $|F(b)-F(a)|\ge \varepsilon\delta/2$ for every $n$. This is a contradiction.

Hence $f(x)\to 0$. $\blacksquare$

### Bonus: $\sin(x^2)$

Substituting $u=x^2$ gives $\int_1^\infty \sin(x^2)\,dx = \int_1^\infty \frac{\sin u}{2\sqrt u}\,du$. This converges by Dirichlet's test, and the full Fresnel value is $\sqrt{\pi/8}$. However, $\sin(x^2)$ oscillates between $\pm1$ forever, so it does not tend to zero.

The derivative $2x\cos(x^2)$ is unbounded, so the function is **not uniformly continuous**. Its oscillations get faster and faster, which shrinks the windows of Step 1 to zero width. Here the failure comes from cancellation between ever-thinner positive and negative lobes, rather than from spikes.

### Remark: the control-theory form

A common sufficient condition for uniform continuity is that $f'$ is bounded. This gives the version used in Lyapunov arguments:

> If $g$ is differentiable, $\lim_{t\to\infty} g(t)$ exists and is finite, and $g'$ is uniformly continuous (e.g. $g''$ is bounded), then $g'(t)\to 0$.

To get it, apply (b) to $f=g'$, using $\int_0^T g' = g(T)-g(0)$.
