# Answer: Collapsing Disk Boundary Gives Sphere

## Key Idea / Intuition

Think of inflating the disk like a balloon: pinch the entire boundary circle together into one point. As you do this, the flat disk "puffs up" and closes on itself — giving you a sphere $S^2$. The key is to write down an explicit homeomorphism (or use the universal property of quotient maps), mapping the interior of $D^2$ bijectively onto the sphere minus the north pole, then checking the boundary collapses exactly onto the north pole.

---

## Formal Proof / Solution

**Claim:** $D^2 / S^1 \cong S^2$.

### Step 1: Write Down a Continuous Surjection $D^2 \to S^2$

Consider $S^2 \subset \mathbb{R}^3$. We define a map $f: D^2 \to S^2$ that:
- sends every point of $S^1 = \partial D^2$ to the north pole $N = (0,0,1)$,
- is a homeomorphism from the open disk $\mathrm{int}(D^2)$ to $S^2 \setminus \{N\}$.

Concretely, use the following construction. For a point $p = (x, y) \in D^2$ with $r = \|(x,y)\|$, define:

$$f(x, y) = \begin{cases} \text{(explicit formula below)} & r < 1 \\ (0, 0, 1) & r = 1 \end{cases}$$

One explicit formula: map using the inverse of stereographic projection composed with a radial stretch. Specifically, first map $r \in [0,1)$ bijectively to $[0, \infty)$ via $t = \tan\!\left(\frac{\pi r}{2}\right)$, yielding the point $\left(\frac{x}{r} \cdot t,\, \frac{y}{r} \cdot t\right) \in \mathbb{R}^2$, then apply inverse stereographic projection from the north pole:

$$f(x,y) = \left(\frac{2u}{1+u^2+v^2},\; \frac{2v}{1+u^2+v^2},\; \frac{u^2+v^2-1}{u^2+v^2+1}\right)$$

where $(u,v) = \frac{\tan(\pi r/2)}{r}(x,y)$ for $r > 0$ and $f(0,0) = (0,0,-1)$ (south pole).

As $r \to 1^-$, we have $t = \tan(\pi r/2) \to \infty$, so $u^2 + v^2 \to \infty$, and:
$$f(x,y) \to (0, 0, 1) = N.$$

So $f$ is continuous on all of $D^2$ (including the boundary), maps $\partial D^2$ to $N$, and maps $\mathrm{int}(D^2)$ homeomorphically onto $S^2 \setminus \{N\}$.

### Step 2: Apply the Quotient Map Theorem

The map $f: D^2 \to S^2$ is:
1. **Continuous** (verified above),
2. **Surjective** (every point of $S^2$ is hit),
3. **Constant on equivalence classes**: $f(p) = f(q)$ iff $p \sim q$ (since the only identifications are on $\partial D^2$, all sent to $N$).

By the **universal property of quotient spaces**, $f$ induces a continuous bijection:
$$\tilde{f}: D^2/S^1 \longrightarrow S^2.$$

### Step 3: It's a Homeomorphism

Since $D^2$ is **compact** and $S^2$ is **Hausdorff**, and $\tilde{f}$ is a continuous bijection from the compact space $D^2/S^1$ (which inherits compactness from $D^2$) to the Hausdorff space $S^2$, it follows that:

$$\tilde{f} \text{ is a homeomorphism.}$$

(A continuous bijection from a compact space to a Hausdorff space is always a homeomorphism, since closed sets map to closed sets, hence the inverse is continuous.)

### Conclusion

$$D^2 / S^1 \cong S^2. \qquad \blacksquare$$

**Why this is beautiful:** The argument is a template that works far more generally — any time you quotient a compact space by collapsing a subspace to a point, you can identify the result by finding an explicit surjection and invoking compact-Hausdorff. The same idea shows $I/\partial I \cong S^1$, $D^n/S^{n-1} \cong S^n$ for all $n$.
