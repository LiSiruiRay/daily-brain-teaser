# Answer: Feynman's Trick: arctan(x)/x and Catalan's Constant

## Key Idea / Intuition

The integral $I(\alpha) = \int_0^1 \frac{\arctan(\alpha x)}{x}\,dx$ looks hard to attack directly because $\arctan(\alpha x)/x$ has no elementary antiderivative. The trick is **Feynman's trick**: differentiate with respect to the parameter $\alpha$. The derivative $I'(\alpha)$ involves $1/(1+\alpha^2 x^2)$, which integrates cleanly in $x$. We recover $I(\alpha)$ by integrating back in $\alpha$, using the initial condition $I(0) = 0$.

---

## Formal Proof / Solution

**Step 1: Differentiate under the integral sign.**

Define
$$I(\alpha) = \int_0^1 \frac{\arctan(\alpha x)}{x}\,dx, \qquad \alpha \geq 0.$$

Differentiate with respect to $\alpha$:
$$I'(\alpha) = \int_0^1 \frac{\partial}{\partial \alpha}\frac{\arctan(\alpha x)}{x}\,dx = \int_0^1 \frac{1}{1+\alpha^2 x^2}\,dx.$$

**Step 2: Evaluate $I'(\alpha)$.**

$$I'(\alpha) = \int_0^1 \frac{dx}{1+\alpha^2 x^2}.$$

Substitute $u = \alpha x$, $du = \alpha\,dx$:
$$I'(\alpha) = \frac{1}{\alpha}\int_0^{\alpha} \frac{du}{1+u^2} = \frac{1}{\alpha}\arctan(\alpha).$$

So
$$I'(\alpha) = \frac{\arctan(\alpha)}{\alpha}.$$

**Step 3: Integrate back.**

$$I(\alpha) = \int_0^\alpha \frac{\arctan(t)}{t}\,dt + C.$$

The initial condition $I(0) = 0$ gives $C = 0$, so

$$I(\alpha) = \int_0^\alpha \frac{\arctan(t)}{t}\,dt.$$

Wait — this is circular if we just want $I(1)$! Let's instead use a second differentiation approach. We need a closed form.

**Alternative: integrate $I'(\alpha) = \arctan(\alpha)/\alpha$ directly via integration by parts.**

Actually, let us integrate $I'(\alpha)$ from $0$ to $1$:
$$I(1) = \int_0^1 I'(\alpha)\,d\alpha = \int_0^1 \frac{\arctan \alpha}{\alpha}\,d\alpha = I(1).$$

This is indeed consistent but circular for a closed form. Let's go one level deeper and use **Leibniz again** on $I'(\alpha)$.

**Better approach: compute $I(1)$ via a double integral.**

$$I(1) = \int_0^1 \frac{\arctan x}{x}\,dx = \int_0^1 \frac{1}{x}\int_0^x \frac{dt}{1+t^2}\,dx = \int_0^1 \int_t^1 \frac{1}{x(1+t^2)}\,dx\,dt$$

(swapping order: $0 \le t \le x \le 1$)

$$= \int_0^1 \frac{1}{1+t^2}\ln\!\left(\frac{1}{t}\right)dt = \int_0^1 \frac{-\ln t}{1+t^2}\,dt.$$

**Step 4: Evaluate $\int_0^1 \frac{-\ln t}{1+t^2}\,dt$.**

Expand the geometric series:
$$\frac{1}{1+t^2} = \sum_{n=0}^\infty (-1)^n t^{2n}.$$

$$\int_0^1 \frac{-\ln t}{1+t^2}\,dt = \sum_{n=0}^\infty (-1)^n \int_0^1 (-\ln t)\, t^{2n}\,dt.$$

Use the standard formula $\int_0^1 (-\ln t)\,t^k\,dt = \frac{1}{(k+1)^2}$:

$$= \sum_{n=0}^\infty (-1)^n \frac{1}{(2n+1)^2} = 1 - \frac{1}{9} + \frac{1}{25} - \cdots = G,$$

where $G$ is **Catalan's constant** $\approx 0.9159656$.

**Result:**

$$\boxed{\int_0^1 \frac{\arctan x}{x}\,dx = G \approx 0.9159\ldots}$$

where $G = \sum_{n=0}^\infty \frac{(-1)^n}{(2n+1)^2}$ is Catalan's constant.

The Feynman trick converts an $\arctan/x$ integrand into $1/(1+\alpha^2 x^2)$, and swapping the order of integration then connects the answer to the classic Leibniz-type series defining $G$.
