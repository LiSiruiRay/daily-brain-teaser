# Answer: An Entire Function with Non-Negative Real Part

## Geometric Intuition

Think about what the condition says about the *image* of $f$: the entire output of $f$ is confined to the right half-plane — a closed, convex half of $\mathbb{C}$.

Now recall **Liouville's theorem** needs boundedness. The right half-plane is not bounded, so we can't apply Liouville directly. But here's the key geometric picture:

> The right half-plane and the unit disk are **conformally equivalent** — one is just a "bent" version of the other.

The Möbius map $g(w) = (w-1)/(w+1)$ literally *folds* the right half-plane into the unit disk: points near the origin map near $-1$, points far out toward $+\infty$ map near $+1$, and the imaginary axis (boundary of the half-plane) wraps onto the unit circle. 

So if $f(\mathbb{C})$ is trapped in the right half-plane, then $g \circ f$ is trapped in the unit disk — and *that* is bounded. Liouville then says $g \circ f$ is constant, and unwrapping gives $f$ is constant.

The insight: **you don't need the image to be bounded, just conformal-equivalent to something bounded.**

---

## Solution

**Define** the Möbius transformation (https://www.youtube.com/watch?v=0z1fIsUNhO4&t=7s)

$$g(w) = \frac{w - 1}{w + 1}.$$

This map sends the right half-plane $\{w \in \mathbb{C} : \operatorname{Re}(w) \geq 0\}$ into the closed unit disk $\{|g| \leq 1\}$. Indeed, for $\operatorname{Re}(w) \geq 0$:

$$|w - 1|^2 = (\operatorname{Re}(w) - 1)^2 + \operatorname{Im}(w)^2,$$
$$|w + 1|^2 = (\operatorname{Re}(w) + 1)^2 + \operatorname{Im}(w)^2.$$

Their difference is $|w-1|^2 - |w+1|^2 = -4\operatorname{Re}(w) \leq 0$, so $|g(w)| \leq 1$.

**Now consider** the composition

$$h(z) = g(f(z)) = \frac{f(z) - 1}{f(z) + 1}.$$

- $h$ is entire: $f$ is entire, and $g$ is holomorphic away from $w = -1$. Since $\operatorname{Re}(f(z)) \geq 0$, we have $f(z) \neq -1$ for all $z$, so $h$ is holomorphic everywhere.
- $h$ is **bounded**: $|h(z)| = |g(f(z))| \leq 1$ for all $z \in \mathbb{C}$.

**By Liouville's theorem**, a bounded entire function is constant. So $h \equiv c$ for some $|c| \leq 1$.

**Inverting**, $f(z) = g^{-1}(c) = \frac{1+c}{1-c}$, which is a constant (assuming $c \neq 1$; but $c = 1$ would require $f(z) \to \infty$, impossible for an entire function).

Therefore $f$ is constant. $\blacksquare$

---

## Why the Trick Works

The Möbius map $g(w) = (w-1)/(w+1)$ is the unique (up to rotation) conformal map of the right half-plane to the unit disk fixing the real axis. Composing it with $f$ **converts a geometric constraint on the image** (image ⊂ right half-plane) into **analytic boundedness**, which is exactly what Liouville needs.

This composition trick is a template: whenever you know the image of an entire function avoids or is contained in some region, try to compose with a conformal map that compresses that region into a disk.

## Generalization

The same argument shows: if $f$ is entire and its image omits any open half-plane (or any disk, or any simply-connected proper open subset of $\mathbb{C}$), then $f$ is constant. This is essentially one direction of **Picard's little theorem** — an entire function that omits even *two* points must be constant.
