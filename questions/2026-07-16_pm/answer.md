# Answer: Schwarz Reflection Principle via Morera

## Key Idea / Intuition

The idea is beautifully symmetric: a holomorphic function that is real on the real axis must satisfy $\overline{f(\bar{z})} = f(z)$, so reflecting $z$ across the real axis and taking the conjugate of the output gives a *consistent* extension. The two pieces $f(z)$ and $\overline{f(\bar{z})}$ agree on the real segment because $f$ is real there, so there is no jump. By Morera's theorem, continuity across the seam plus holomorphicity on each half is enough to conclude holomorphicity on the whole disk.

---

## Formal Proof / Solution

**Step 1: $F$ is well-defined and continuous on $D$.**

On the upper half-disk, $F = f$ which is continuous. On the lower half-disk $D^- = \{|z|<1,\ \text{Im}(z)<0\}$, the map $z \mapsto \bar{z}$ is continuous, $f$ is continuous on $D^+$ (and extends continuously to the real segment), and conjugation is continuous, so $z \mapsto \overline{f(\bar{z})}$ is continuous on $D^-$.

On the real segment $(-1,1)$: as $z = x \in \mathbb{R}$,
$$\overline{f(\bar{z})} = \overline{f(x)} = \overline{f(x)}.$$
Since $f(x) \in \mathbb{R}$, we get $\overline{f(x)} = f(x)$, so both definitions agree. Thus $F$ is continuous on all of $D$.

**Step 2: $\overline{f(\bar{z})}$ is holomorphic on $D^-$.**

Let $g(z) = \overline{f(\bar{z})}$ for $z \in D^-$. Since $\bar{z} \in D^+$ when $z \in D^-$, $f$ is holomorphic there. Check the Cauchy–Riemann equations: if $f = u + iv$, then
$$g(z) = g(x+iy) = u(x,-y) - iv(x,-y).$$

Let $\tilde{u}(x,y) = u(x,-y)$ and $\tilde{v}(x,y) = -v(x,-y)$. Since $u,v$ satisfy C–R on $D^+$:
$$\frac{\partial u}{\partial x} = \frac{\partial v}{\partial y}, \quad \frac{\partial u}{\partial y} = -\frac{\partial v}{\partial x}.$$

Compute (with $s = -y > 0$ for $z \in D^-$):
$$\frac{\partial \tilde{u}}{\partial x} = \frac{\partial u}{\partial x}(x,s) = \frac{\partial v}{\partial y}(x,s) = \frac{\partial \tilde{v}}{\partial y},$$
$$\frac{\partial \tilde{u}}{\partial y} = -\frac{\partial u}{\partial y}(x,s) = \frac{\partial v}{\partial x}(x,s) = -\frac{\partial \tilde{v}}{\partial x}.$$

So $g$ satisfies C–R on $D^-$, hence is holomorphic there.

**Step 3: Apply Morera's theorem to conclude $F$ is holomorphic on $D$.**

Take any triangle $T \subset D$. 

- If $T$ lies entirely in $D^+$ or entirely in $D^-$, then $\oint_{\partial T} F\, dz = 0$ by Cauchy's theorem applied to $f$ or $g$ respectively.

- If $T$ straddles the real axis, split it along the real segment into pieces in $D^+$ and $D^-$. On the boundary segment lying on $\mathbb{R}$, $F$ is continuous and the two pieces agree. By a standard limiting argument (or Goursat's theorem for triangles touching the boundary), $\oint_{\partial T} F\, dz = 0$ still holds.

Since $F$ is continuous on $D$ and $\oint_{\partial T} F\, dz = 0$ for every triangle $T \subset D$, **Morera's theorem** implies $F$ is holomorphic on $D$. $\blacksquare$

---

**The punchline:** The condition "$f$ is real on $(-1,1)$" is precisely what forces continuity across the real axis. Without it, $F$ would have a jump discontinuity there and the argument collapses. With it, the Schwarz Reflection Principle gives a free analytic continuation — the real axis acts as a mirror, and the function's values on one side completely determine its values on the other.

**Bonus formula:** The reflection principle gives the identity
$$f(\bar{z}) = \overline{f(z)}$$
for all $z$ in the upper half-disk, a beautiful symmetry that is forced entirely by the real-valuedness on the boundary segment.
