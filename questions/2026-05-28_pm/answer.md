# Answer: Winding Number Is Always an Integer

## Key Idea / Intuition

The winding number counts how many times $\gamma$ loops around the origin. The cleanest proof avoids all topology and branch-cut gymnastics by constructing a "lifted" function that tracks the running phase of $\gamma(t)$. If we form $h(t) = e^{-\phi(t)}\gamma(t)$, where $\phi$ is the "log-derivative integral," then $h$ turns out to be **constant**. Since $\gamma$ is a closed curve, this forces $e^{\phi(1)} = 1$, which means $\phi(1)$ must be an integer multiple of $2\pi i$ — and that integer is exactly the winding number.

---

## Formal Proof / Solution

**Step 1: Define the "running logarithm" $\phi$.**

Set
$$\phi(t) = \int_0^t \frac{\gamma'(s)}{\gamma(s)}\, ds, \qquad t \in [0,1].$$

This is well-defined since $\gamma(s) \neq 0$ for all $s$, and $\gamma$ is (piecewise) $C^1$.

Note immediately that
$$\phi(1) = \int_0^1 \frac{\gamma'(s)}{\gamma(s)}\,ds = \int_\gamma \frac{dz}{z} = 2\pi i \cdot n(\gamma, 0).$$

**Step 2: Show $h(t) = e^{-\phi(t)}\gamma(t)$ is constant.**

Differentiate:
$$h'(t) = -\phi'(t)\, e^{-\phi(t)}\gamma(t) + e^{-\phi(t)}\gamma'(t).$$

But $\phi'(t) = \dfrac{\gamma'(t)}{\gamma(t)}$, so

$$h'(t) = e^{-\phi(t)}\!\left[-\frac{\gamma'(t)}{\gamma(t)}\cdot \gamma(t) + \gamma'(t)\right] = e^{-\phi(t)}\!\left[-\gamma'(t) + \gamma'(t)\right] = 0.$$

Hence $h(t)$ is **constant** on $[0,1]$.

**Step 3: Evaluate $h$ at the endpoints.**

Since $h$ is constant:
$$h(0) = e^{-\phi(0)}\gamma(0) = e^0 \cdot \gamma(0) = \gamma(0),$$
$$h(1) = e^{-\phi(1)}\gamma(1).$$

But $\gamma$ is closed: $\gamma(1) = \gamma(0)$. Therefore

$$\gamma(0) = e^{-\phi(1)}\gamma(0).$$

Since $\gamma(0) \neq 0$, we can cancel it:

$$e^{-\phi(1)} = 1 \implies e^{\phi(1)} = 1.$$

**Step 4: Conclude integrality.**

The equation $e^{w} = 1$ (for $w \in \mathbb{C}$) holds if and only if $w = 2\pi i k$ for some $k \in \mathbb{Z}$.

Therefore
$$\phi(1) = 2\pi i k \quad \text{for some } k \in \mathbb{Z},$$

and so
$$n(\gamma, 0) = \frac{\phi(1)}{2\pi i} = k \in \mathbb{Z}. \qquad \blacksquare$$

**Summary of the trick:** The auxiliary function $h(t) = e^{-\phi(t)}\gamma(t)$ is the "exponential integrating factor" that kills the $\phi'$ term, making $h' \equiv 0$. The closedness of $\gamma$ then forces $e^{\phi(1)}=1$, which is the algebraic reason the winding number is an integer.
