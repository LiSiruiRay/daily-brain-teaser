# Answer: The Entire Function That Squares to Another

## Key Idea / Intuition

The function $z^2 - 1$ has two zeros, at $z = 1$ and $z = -1$. If $f^2 = z^2 - 1$, then $f$ must vanish at these points. But near each zero of $z^2 - 1$ (which is a simple zero), $f$ would have to be a "half-zero" — a zero of order $1/2$ — which cannot be holomorphic. More precisely, the issue is topological: the function $z^2 - 1$ changes sign as you loop around one of its zeros, so there is no consistent holomorphic square root globally on $\mathbb{C}$.

---

## Formal Proof / Solution

**Suppose for contradiction** that such an entire $f$ exists with $f(z)^2 = z^2 - 1$.

**Step 1: Zeros of $f$.**

At $z = 1$: we have $f(1)^2 = 0$, so $f(1) = 0$. Similarly $f(-1) = 0$.

Write $z^2 - 1 = (z-1)(z+1)$. Both zeros are simple (order 1). Since $f^2 = z^2-1$, the order of vanishing satisfies $2\,\mathrm{ord}_{z=1}(f) = 1$, which is impossible for a holomorphic function (orders must be non-negative integers).

**Conclusion from Step 1:** No entire $f$ can satisfy $f^2 = z^2-1$.

---

**Alternative (topological) argument:** Suppose such $f$ is entire (hence continuous). Consider the loop $\gamma(t) = e^{it}$ for $t \in [0, 2\pi]$, which winds once around both $z = 1$ and $z = -1$ together. Actually, let us use a smaller loop.

Consider $\gamma(t) = 1 + \epsilon e^{it}$ winding once around $z = 1$ (with $\epsilon$ small enough to exclude $z = -1$). Along $\gamma$,

$$f(\gamma(t))^2 = \gamma(t)^2 - 1 = (\gamma(t)-1)(\gamma(t)+1).$$

Near $z = 1$, we have $(\gamma(t) - 1) = \epsilon e^{it}$ (winds once around 0) while $(\gamma(t)+1) \approx 2$ (nonzero, winds zero times). So $f(\gamma(t))^2$ winds **once** around 0.

But $f(\gamma(t))^2$ winds an **even** number of times around 0 for any closed curve (since winding number of $w^2$ is twice the winding number of $w$). Contradiction.

**More precisely:** The winding number of $f \circ \gamma$ around 0 equals $\frac{1}{2}\cdot(\text{winding number of } f^2 \circ \gamma \text{ around } 0) = \frac{1}{2}\cdot 1 = \frac{1}{2}$, which is not an integer — impossible for a continuous closed curve.

---

**Summary:** No entire function $f$ satisfies $f(z)^2 = z^2 - 1$.

The obstruction is that $z^2 - 1$ has **simple zeros**, so its square root would require a branch cut; there is no single-valued holomorphic square root of $z^2-1$ on any domain that includes both $\pm 1$. (By contrast, $z^2+1$ restricted to the right half-plane does admit a holomorphic square root, since you can avoid the branch cut.)

**Remark:** If instead the equation were $f(z)^2 = (z^2-1)^2$, then $f(z) = \pm(z^2-1)$ works (an entire function). The key difference is that **even-order** zeros allow holomorphic square roots, but **odd-order** zeros do not.
