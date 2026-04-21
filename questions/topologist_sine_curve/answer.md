# Answer: The Topologist's Sine Curve

---

## Intuition First

### Why is $\bar{S}$ connected?

Picture the sine curve $S$ wiggling forever as $x \to 0^+$, its oscillations getting compressed tighter and tighter. The vertical segment $\{0\} \times [-1,1]$ is the "ghost" of all those oscillations — every point on the segment is a limit of points on $S$. You can get arbitrarily close to any point on the vertical segment by walking along the sine curve far enough to the left.

So $\bar{S}$ cannot be split into two separated pieces: the vertical segment is glued to $S$ by proximity, even though it never actually "touches" $S$. The space is one piece — connected.

### Why is $\bar{S}$ not path-connected?

Now imagine trying to draw a continuous path from a point on the vertical segment $(0, 0)$ to a point on the sine curve. At some moment your path has to "make the jump" — it's on the segment ($x = 0$) and then, an instant later, it's on the sine curve ($x > 0$).

The moment your $x$-coordinate leaves zero and creeps toward $0^+$, your $y$-coordinate is forced to be $\sin(1/x)$, which oscillates infinitely between $-1$ and $+1$ as $x \to 0^+$. No matter how slowly you move, you can't control those oscillations — $y(t)$ will be thrashing wildly between $\pm 1$ even as $t$ is barely moving.

But a continuous path must have $y(t)$ settling down to a single value $y(t_0)$ as $t \to t_0$. That's a contradiction. The sine curve simply oscillates too fast near $x=0$ for any continuous path to "land" from the segment onto it.

**One-line summary:** the vertical segment is a limit point of $S$ but not reachable from $S$ by a continuous path — closeness in the limiting sense is weaker than closeness via a path.

---

## Formal Proof

### Part 1: $\bar{S}$ is Connected

$S$ is path-connected (hence connected): the map $t \mapsto (t, \sin(1/t))$ for $t > 0$ is a continuous parameterization of all of $S$.

**Lemma:** The closure of a connected set is connected.

*Proof.* Suppose $\bar{S} = U \cup V$ with $U, V$ open, disjoint, and nonempty. Since $S$ is connected, $S$ lies entirely in $U$ or $V$ — say $S \subset U$. Every point of $\bar{S} \setminus S = \{(0,y) : y \in [-1,1]\}$ is a limit point of $S \subset U$. Since $U$ is closed in $\bar{S}$ (complement of the open $V$), it contains all its limit points, so the vertical segment $\subset U$. Then $V = \emptyset$, a contradiction. $\blacksquare$

---

### Part 2: $\bar{S}$ is Not Path-Connected

Suppose for contradiction there is a continuous path:
$$\gamma: [0,1] \to \bar{S}, \qquad \gamma(0) = (0,0),\quad \gamma(1) \in S.$$

Write $\gamma(t) = (x(t), y(t))$ and define:
$$t_0 = \sup\{t \in [0,1] : x(t) = 0\}.$$

By continuity of $x$, we have $x(t_0) = 0$, so $\gamma(t_0)$ is on the vertical segment. For all $t > t_0$, we have $x(t) > 0$ (by definition of $t_0$), so:
$$y(t) = \sin\!\left(\tfrac{1}{x(t)}\right).$$

As $t \searrow t_0$, continuity of $x$ gives $x(t) \to 0^+$. Choose any $\delta > 0$. In $x \in (0, x(t_0 + \delta))$, the function $\sin(1/x)$ attains both $+1$ and $-1$, so by the intermediate value theorem applied to the continuous function $y(t)$, $y$ takes all values in $[-1, 1]$ on the interval $(t_0, t_0 + \delta)$.

This holds for every $\delta > 0$, so $y(t)$ does not converge as $t \to t_0^+$. But continuity of $\gamma$ requires $y(t) \to y(t_0)$. Contradiction. $\blacksquare$

---

## Summary

| Property | $S$ | $\bar{S}$ |
|----------|-----|-----------|
| Connected | Yes | Yes |
| Path-connected | Yes | **No** |

**Moral:** Connectedness is preserved by taking closures. Path-connectedness is not — a limit point can be "infinitely close" to a set without being reachable by any continuous path.
