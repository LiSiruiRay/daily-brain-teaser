# Answer: A Connected Metric Space Cannot Be Countable

## Key Idea / Intuition

Pick a point $x_0$ and consider the "distance from $x_0$" function. It is continuous and real-valued. If $X$ were countable, this function would take only countably many values, so some radius $r$ would be missed. The sphere of radius $r$ is then empty, so the open ball of radius $r$ and the region outside it separate $X$. Connectedness forbids that.

Put differently, a metric lets you measure distances, and continuous real-valued functions on a connected space must fill whole intervals. Connectedness of $X$ is pushed forward into connectedness of a subset of $\mathbb{R}$, where it means "interval", and intervals are big.

---

## Formal Proof / Solution

**Setup.** Fix $x_0 \in X$ and some $y \in X$ with $y \neq x_0$. Put $\delta = d(x_0,y) > 0$. Define
$$f : X \to \mathbb{R}, \qquad f(x) = d(x_0, x).$$
By the triangle inequality, $|f(x) - f(x')| \le d(x,x')$. So $f$ is $1$-Lipschitz and in particular continuous.

**(b) first, since it implies (a).**

1. A continuous image of a connected space is connected, so $f(X) \subseteq \mathbb{R}$ is connected.
2. The connected subsets of $\mathbb{R}$ are exactly the intervals.
3. $f(X)$ contains $f(x_0) = 0$ and $f(y) = \delta$. Hence
$$[0,\delta] \subseteq f(X).$$
4. Each value $r \in [0,\delta]$ has at least one preimage. Choosing one preimage for each $r$ gives an injection $[0,\delta] \hookrightarrow X$. Therefore
$$|X| \ \ge\ |[0,\delta]| \ =\ |\mathbb{R}|.$$

**(a), directly and without quoting "connected subsets of $\mathbb{R}$ are intervals".**

1. Suppose $X$ is countable. Then $f(X)$ is a countable subset of $\mathbb{R}$.
2. The interval $(0,\delta)$ is uncountable, so there is some $r \in (0,\delta)$ with $r \notin f(X)$. That is, no point of $X$ lies at distance exactly $r$ from $x_0$.
3. Set
$$U = \{x : d(x_0,x) < r\}, \qquad V = \{x : d(x_0,x) > r\}.$$
   - Both are open, being preimages of open sets under the continuous map $f$.
   - They are disjoint.
   - $U \cup V = X$, because the "sphere" $\{d(x_0,x) = r\}$ is empty.
   - $x_0 \in U$ and $y \in V$, so both are nonempty.
4. This is a separation of $X$, contradicting connectedness. Hence $X$ is uncountable. $\blacksquare$

**(c) Hausdorff is not enough.**

There exist countably infinite connected Hausdorff spaces. A famous example is the **Golomb topology** on $\mathbb{N}_{>0}$. Its basis consists of the arithmetic progressions $\{a + nb : n \ge 0\}$ with $\gcd(a,b)=1$. This space is Hausdorff and connected, yet countable. (Bing also constructed a countable connected Hausdorff space.)

The proof above breaks down because in a general Hausdorff space there need not be enough continuous real-valued functions. Indeed, in such a countable connected space every continuous $X \to \mathbb{R}$ is constant. The metric hands us the non-constant function $d(x_0,\cdot)$ for free, and that is the whole trick.

What makes this function useful is a regularity property. Countable connected spaces exist that are even $T_2$, but none that are **Urysohn-regular enough**, in particular none that are completely regular. The same argument works verbatim for any connected Tychonoff space with two or more points.

---

**Corollaries worth savoring**

- $\mathbb{Q}$ is not connected. More strongly, $\mathbb{R}$ minus any countable set is still path-connected in $\mathbb{R}^2$-type arguments, but $\mathbb{Q}$ itself falls apart.
- Any nontrivial connected metric space, such as a curve, a manifold, or a Peano continuum, automatically has continuum many points.
