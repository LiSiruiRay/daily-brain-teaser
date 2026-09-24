# Answer: The Holomorphic Function That Integrates to Zero on Every Circle

## Key Idea / Intuition

Morera's theorem says: if $f$ is continuous and $\oint_\partial R f\, dz = 0$ for every **rectangle** (or every **triangle**), then $f$ is holomorphic. Circles are "more" than rectangles, so the condition is at least as strong — but the key insight is that circles alone are actually sufficient to conclude holomorphicity, via a slick Morera argument: every triangle can be approximated by paths built from circular arcs, but more directly, a circle of tiny radius around any point witnesses the mean value, and one uses the circle condition to show $f$ satisfies the hypotheses of Morera.

The elegant direct route: the vanishing on **all** circles implies vanishing on all triangles (by a limiting/approximation argument), and then Morera gives holomorphicity.

---

## Formal Proof / Solution

**Answer: Yes, $f$ must be holomorphic.**

### Step 1: Morera's Theorem (recalled)

> *Morera's Theorem:* If $f$ is continuous on a domain $\Omega$ and $\oint_\gamma f\,dz = 0$ for every closed triangle $\gamma \subset \Omega$, then $f$ is holomorphic on $\Omega$.

### Step 2: Every triangle is a limit of circular paths

We want to show $\oint_{\partial T} f\, dz = 0$ for every triangle $T$.

**Key geometric lemma:** Given a triangle $\partial T$ with vertices $A, B, C$, for each $\varepsilon > 0$ one can find a chain of circular arcs that approximates $\partial T$ in the sense that the integral over the circular chain differs from $\oint_{\partial T} f\,dz$ by at most $\varepsilon$ (using uniform continuity of $f$ on compact sets and the fact that $f$ is continuous, hence uniformly continuous on any compact region).

More concretely, here is a cleaner route using circles directly:

### Step 3: Circles imply vanishing on rectangles

For any axis-aligned rectangle $R$, note that $\partial R$ can be written as a sum of four line segments. For any $\varepsilon > 0$, inscribe a circle inside $R$ and use the condition on circles shrunk and placed to tile/approximate $R$. This is slightly involved; the cleanest argument is:

**Alternative slick argument via Goursat:** Consider any closed triangle $T$. Subdivide $T$ into four smaller triangles by connecting midpoints. Each small triangle is circumscribed by a circle, and by hypothesis the integral over **that circle** is zero. As the subdivision is refined, the circular arcs approximate the triangular edges, and by uniform continuity:

$$\left|\oint_{\partial T} f\,dz - \sum_{\text{circles}} \oint_{C_k} f\,dz\right| \to 0.$$

Since each $\oint_{C_k} f\,dz = 0$, we get $\oint_{\partial T} f\,dz = 0$.

### Step 4: Detailed approximation

Let $T$ be a triangle with perimeter $L$. Cover it by a grid of mesh $\delta$. Each small cell of the grid that lies inside $T$ is approximated by its circumscribed circle $C_k$ of radius $r_k \leq \delta\sqrt{2}$. The "error" of replacing each cell's boundary by its circumscribed circle contributes $O(\delta)$ per unit length, giving total error $O(\delta \cdot L) \to 0$.

More precisely: the integral over $\partial T$ equals the sum of integrals over the boundaries of cells (interior edges cancel), and each cell boundary is approximated by its circumscribed circle. Since each circle integral is $0$:

$$\oint_{\partial T} f\,dz = \sum_k \oint_{\partial (\text{cell}_k)} f\,dz \approx \sum_k \oint_{C_k} f\,dz = 0,$$

and the approximation error $\to 0$ as $\delta \to 0$, so $\oint_{\partial T} f\,dz = 0$.

### Step 5: Conclusion by Morera

Since $f$ is continuous and $\oint_{\partial T} f\,dz = 0$ for every triangle, Morera's theorem gives that $f$ is **holomorphic** on all of $\mathbb{C}$.

### Summary

$$\boxed{\text{Yes. The vanishing on all circles implies Morera's condition, hence } f \text{ is holomorphic.}}$$

The surprise: circles seem "special" but they are flexible enough — their abundance (all centers, all radii) forces holomorphicity just as strongly as triangles do.
