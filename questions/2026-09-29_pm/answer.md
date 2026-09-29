# Answer: Disk Boundary Reflection Gives Sphere

## Key Idea / Intuition

The identification glues the upper semicircle to the lower semicircle by reflecting across the real axis — so the boundary circle $S^1$ gets folded in half, turning it into a closed arc (a copy of $[0,1]$, topologically). The interior of the disk stays untouched. So we end up gluing a disk along its boundary to a line segment — which collapses the boundary to an arc, producing something that looks like a sphere $S^2$.

More precisely: after the identification, the boundary circle becomes a closed interval (its two endpoints $1$ and $-1$ are fixed, and each pair $\{e^{i\theta}, e^{-i\theta}\}$ becomes a single point). This means we have a disk whose boundary has been "pinched" to an arc. Topologically, that is exactly a sphere.

---

## Formal Proof / Solution

**Step 1: Understand what the identification does to $S^1$.**

The boundary $S^1$ consists of points $e^{i\theta}$ for $\theta \in [0, 2\pi)$. The identification glues $e^{i\theta} \sim e^{-i\theta}$, i.e., it folds the circle by reflection across the real axis.

The quotient of $S^1$ under the antipodal-reflection $e^{i\theta} \mapsto e^{-i\theta}$ is homeomorphic to a **closed interval** $[0, \pi]$ (parametrized by $\theta \in [0,\pi]$, where each pair $\{e^{i\theta}, e^{-i\theta}\}$ is a single point, and the endpoints $\theta = 0$ and $\theta = \pi$ (i.e., $1$ and $-1$) are fixed).

So $S^1/{\sim} \cong [0,1]$.

**Step 2: Decompose the disk.**

Write $D^2 = \text{int}(D^2) \cup S^1$. The interior is untouched. We are forming:

$$D^2/{\sim} = D^2 \text{ with the boundary folded to an interval.}$$

**Step 3: Use a concrete homeomorphism.**

Consider the map $f: D^2 \to S^2$ defined by thinking of $S^2 \subset \mathbb{R}^3$. Write $z = x + iy \in D^2$ with $x^2 + y^2 \leq 1$. Map:

$$f(x, y) = (2x\sqrt{1-x^2-y^2},\ 2|y|\sqrt{1-x^2-y^2},\ 1 - 2(x^2+y^2))$$

or more elegantly, observe the following:

Take the upper hemisphere $S^2_+ = \{(a,b,c) \in S^2 : b \geq 0\}$. There is a homeomorphism $D^2 \to S^2_+$ sending the boundary $S^1$ to the equator $\{b=0\} \cap S^2$.

Now, the equator of $S^2$ under the reflection $(a,0,c) \mapsto (a,0,c)$ is already identified with itself (it's the boundary of both hemispheres). This means:

$$D^2/{\sim} \cong S^2_+ \cup_{\text{equator}} S^2_- \cong S^2$$

where we are gluing the upper and lower hemispheres along the equator — but since the identification on $S^1$ exactly matches how the equator is shared, we recover the full sphere.

**Step 4: Direct argument via CW structure.**

- The quotient $S^1/{\sim}$ gives an arc $A \cong [0,1]$ with two endpoints $p = [1]$ and $q = [-1]$.
- The disk $D^2/{\sim}$ is obtained from $A$ by attaching a 2-cell (the interior of $D^2$) whose attaching map wraps $S^1$ around $A$ exactly **twice** — once for the upper semicircle, once for the lower semicircle.
- A 2-cell attached to an arc $[0,1]$ by a map $\partial D^2 \to [0,1]$ that traverses the arc back and forth gives a quotient homeomorphic to $S^2$.

(Alternatively: fold the disk in half along the real diameter — the two halves are two disks, glued along their shared semicircle boundary, which is precisely $S^2$.)

**Conclusion:**

$$D^2/{\sim} \;\cong\; S^2$$

The key surprise: identifying boundary points by reflection — a seemingly mild relation — doubles the disk into a sphere.
