# Answer: Collapsing Square Boundary Gives Sphere

## Key Idea / Intuition

The square is homeomorphic to the closed disk $D^2$ (just round the corners). When you collapse the boundary circle of a disk to a single point, you are essentially "pinching" the boundary to create a bubble — which is exactly a sphere. The formal argument finds an explicit homeomorphism, or uses the universal property of quotient maps together with a compactness argument.

There are two clean approaches:
1. **Via the disk:** First show $I^2 \cong D^2$, then show $D^2/S^1 \cong S^2$ via a geometric map.
2. **Direct map:** Write down an explicit surjection $I^2 \to S^2$ that collapses $\partial I^2$ to one point, then invoke the closed-map lemma.

We'll use approach 2 since it's the most illuminating.

---

## Formal Proof / Solution

**Step 1: The closed-map lemma (key tool).**

> If $f: X \to Y$ is a continuous bijection and $X$ is compact and $Y$ is Hausdorff, then $f$ is a homeomorphism.

**Step 2: Set up the quotient.**

Let $q: I^2 \to X = I^2/\partial I^2$ be the quotient map. The space $X$ has one special point $* = q(\partial I^2)$ and otherwise $q$ is injective on the interior $\text{int}(I^2)$.

**Step 3: Describe the explicit map $I^2 \to S^2$.**

Identify $S^2 \subset \mathbb{R}^3$ as the unit sphere. Use *spherical coordinates*: parametrize $S^2$ minus the north pole $N = (0,0,1)$ and south pole $S=(0,0,-1)$ via latitude $\phi \in (0,\pi)$ and longitude $\theta \in [0, 2\pi)$.

Define $f: I^2 \to S^2$ by mapping $(s,t) \mapsto (\sin(\pi t)\cos(2\pi s),\, \sin(\pi t)\sin(2\pi s),\, \cos(\pi t))$.

That is, set $\theta = 2\pi s$ and $\phi = \pi t$:

$$f(s,t) = \bigl(\sin(\pi t)\cos(2\pi s),\; \sin(\pi t)\sin(2\pi s),\; \cos(\pi t)\bigr).$$

**Step 4: Verify $f$ collapses exactly $\partial I^2$.**

- At $t = 0$ (bottom edge): $f(s,0) = (0,0,1) = N$ for all $s$. ✓
- At $t = 1$ (top edge): $f(s,1) = (0,0,-1) = S$ for all $s$. ✓
- At $s = 0$ and $s = 1$ (left/right edges): $\cos(0) = \cos(2\pi) = 1$, $\sin(0)=\sin(2\pi)=0$, so both vertical edges map to the same curve — they agree since $\theta = 0$ and $\theta = 2\pi$ are the same angle. ✓

So the entire boundary $\partial I^2$ maps to either $N$, $S$, or the same meridian $(\theta=0)$... wait — actually, $N$ and $S$ are two distinct points! We need $f$ to collapse **all** of $\partial I^2$ to **one** point. Let us reconsider.

**Corrected cleaner approach — via the disk:**

**Step 3' (better):** First note that $I^2 \cong D^2$ (the closed unit disk) via any homeomorphism $\psi: D^2 \to I^2$ (e.g., radial rescaling to a square). So:

$$X = I^2/\partial I^2 \cong D^2 / S^1.$$

Now define $g: D^2 \to S^2$ by the formula: for $z = (x,y) \in D^2$ with $r = \|z\| \le 1$,

$$g(x,y) = \bigl(2x\sqrt{1-r^2},\; 2y\sqrt{1-r^2},\; 2r^2 - 1\bigr).$$

**Verify $g$ is well-defined and continuous:** clear from the formula.

**Verify $g$ is surjective:** For any $(a,b,c) \in S^2$, set $r^2 = \tfrac{1+c}{2}$, so $r = \sqrt{\tfrac{1+c}{2}} \in [0,1]$, and $(x,y) = \tfrac{(a,b)}{2\sqrt{1-r^2}}$ when $r < 1$ (the south pole $c=-1$ gives $r=0$; the north pole $c=1$ collapses the boundary). One checks surjectivity.

**Verify $g$ collapses exactly $S^1 = \partial D^2$:** On $r = 1$ (the boundary), $\sqrt{1-r^2} = 0$, so:

$$g(x,y)\big|_{r=1} = (0,\, 0,\, 1) = N,$$

a single point — the north pole. Interior points $r < 1$ are mapped injectively (distinct $(x,y)$ give distinct $(a,b,c)$). ✓

**Step 4': Apply the universal property.**

Since $g: D^2 \to S^2$ is continuous and collapses $S^1$ to a single point, it factors through the quotient:

$$\tilde{g}: D^2/S^1 \to S^2, \qquad \tilde{g} \circ q = g,$$

and $\tilde{g}$ is a continuous bijection.

**Step 5': Invoke the closed-map lemma.**

- $D^2/S^1$ is compact (quotient of a compact space).
- $S^2$ is Hausdorff.
- $\tilde{g}$ is a continuous bijection.

Therefore $\tilde{g}$ is a **homeomorphism**. $\blacksquare$

**Conclusion:**

$$I^2/\partial I^2 \cong D^2/S^1 \cong S^2.$$

The beautiful idea is that collapsing the boundary of a disk to a point is the topological operation of "inflating a balloon" — and the closed-map lemma turns a geometric intuition into a rigorous proof with minimal work.
