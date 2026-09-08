# Answer: The Quotient Square That Becomes a Disk

## Key Idea / Intuition

When you pinch the top edge of a square to a single point, you are doing exactly what a cone does: taking a space $A$ (the bottom edge, together with the sides), collapsing one end of $A \times [0,1]$ to a point. The result is a **triangle**, which is homeomorphic to a **disk** $D^2$ — or equivalently, to the cone over an interval. The key insight is to write down an explicit homeomorphism and use the **closed map lemma**: a continuous bijection from a compact space to a Hausdorff space is automatically a homeomorphism.

---

## Formal Proof / Solution

**Step 1: Identify the quotient.**

Let $q : [0,1]^2 \to X/{\sim}$ be the quotient map. The equivalence relation collapses $\{(x,1) : x \in [0,1]\}$ to a single point $*$, while all other points are identified only with themselves.

**Step 2: Define a candidate homeomorphism.**

Consider the closed triangle
$$T = \{(u, v) \in \mathbb{R}^2 : u \geq 0,\; v \geq 0,\; u + v \leq 1\},$$
which is homeomorphic to $D^2$ (it is a compact convex set with nonempty interior).

Define a map $f : [0,1]^2 \to T$ by
$$f(x, t) = \bigl((1-t)\,x,\; (1-t)(1-x)\bigr).$$

**Step 3: Check that $f$ is continuous and respects $\sim$.**

- $f$ is clearly continuous (polynomial in $x$ and $t$).
- When $t = 1$: $f(x, 1) = (0, 0)$ for all $x$. So all top-edge points map to the apex $(0,0)$ of the triangle — the identification $\sim$ is respected.
- Thus $f$ descends to a continuous map $\bar{f} : X/{\sim} \to T$.

**Step 4: Check that $\bar{f}$ is a bijection.**

*Surjectivity:* Given any $(u,v) \in T$, let $s = u+v$. If $s = 0$, then $t = 1$ and any $x$ maps there (this is the apex). If $s > 0$, set $t = 1-s$ and $x = u/s$; then $f(x,t) = (u,v)$.

*Injectivity:* Suppose $f(x,t) = f(x', t')$, i.e.,
$$(1-t)x = (1-t')x', \qquad (1-t)(1-x) = (1-t')(1-x').$$
Adding: $(1-t) = (1-t')$, so $t = t'$. If $t < 1$, then $1-t > 0$ and we get $x = x'$. If $t = t' = 1$, both points are in the collapsed class $[(x,1)]_\sim$, so they represent the same point in $X/\sim$.

**Step 5: Apply the closed map lemma.**

$X/\sim$ is compact (continuous image of the compact square $[0,1]^2$), and $T$ is Hausdorff (it is a subspace of $\mathbb{R}^2$). A continuous bijection from a compact space to a Hausdorff space is a homeomorphism.

**Conclusion:**

$$X/{\sim} \;\cong\; T \;\cong\; D^2.$$

Collapsing the top edge of the unit square to a point yields a space homeomorphic to the **closed disk** (equivalently, a triangle/cone over an interval). $\blacksquare$

---

**Remark:** This is a special case of the general fact that the **cone** $CX = X \times [0,1] / (X \times \{1\})$ over a contractible compact space $X$ is contractible and, when $X$ is an arc, yields a disk.
