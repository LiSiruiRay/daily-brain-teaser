# Answer: Maximize I(f) − J(f): Pointwise Optimization

## Key Idea / Intuition

Write $I(f)-J(f)$ as a single integral $\int_0^1 \Phi\big(x,f(x)\big)\,dx$. The integrand at $x$ depends only on the number $f(x)$: there are no derivatives and no coupling between points. So choose $f(x)$ separately at each $x$ to make the integrand as large as possible. For fixed $x$, the integrand is a downward-opening parabola in $y=f(x)$, and its peak is found by completing the square. If the pointwise maximizers happen to form a continuous function, that function is the global maximizer.

---

## Formal Proof / Solution

**Step 1: Combine into one integral.**

$$
I(f)-J(f)=\int_0^1 \big(x^2 f(x) - x f(x)^2\big)\,dx=\int_0^1 x\big(x f(x)-f(x)^2\big)\,dx.
$$

**Step 2: Maximize pointwise.**

Fix $x\in[0,1]$ and treat $y=f(x)$ as a free real variable. Completing the square gives

$$
xy-y^2=\frac{x^2}{4}-\Big(y-\frac{x}{2}\Big)^2\le \frac{x^2}{4},
$$

with equality exactly when $y=x/2$. Since $x\ge 0$ on $[0,1]$, multiplying by $x$ keeps the inequality:

$$
x\big(x f(x)-f(x)^2\big)\le \frac{x^3}{4}\qquad\text{for every } x\in[0,1].
$$

**Step 3: Integrate the bound.**

$$
I(f)-J(f)\le \int_0^1 \frac{x^3}{4}\,dx=\frac{1}{16}.
$$

**Step 4: The bound is attained.**

The pointwise maximizer $f(x)=x/2$ is continuous, so it is an admissible function. Checking directly:

$$
I(f)=\int_0^1 \frac{x^3}{2}\,dx=\frac18,\qquad J(f)=\int_0^1 x\cdot\frac{x^2}{4}\,dx=\frac1{16},
$$

so $I(f)-J(f)=\tfrac18-\tfrac1{16}=\tfrac1{16}$.

$$
\boxed{\max_f\,\big(I(f)-J(f)\big)=\tfrac{1}{16},\quad \text{attained at } f(x)=\tfrac{x}{2}.}
$$

---

## Remarks

- **General principle.** For a functional $\int \Phi(x,f(x))\,dx$ with no derivatives, the following holds:
$$\sup_f \int\Phi(x,f(x))\,dx = \int \sup_y \Phi(x,y)\,dx.$$
This requires that a pointwise maximizer can be chosen in the admissible class, here the continuous functions.
- **When it can fail.** Suppose the pointwise maximizer jumped, for example if the coefficient of $f^2$ changed sign. Then the supremum could still equal the integral of pointwise suprema, but it might not be attained by any continuous $f$.
- **Contrast.** If the functional contained $f'(x)$, neighboring points would be coupled. You would then genuinely need the Euler–Lagrange equation. This problem is the "zeroth-order" case, where calculus of variations reduces to ordinary calculus.
