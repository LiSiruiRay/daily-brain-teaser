# Answer: Integral of arctan(x)/(1+x²)

## Key Idea / Intuition

The integrand $\frac{\arctan x}{1+x^2}$ is almost screaming at you: notice that $\frac{d}{dx}\arctan x = \frac{1}{1+x^2}$. So the integrand is exactly $u\,du$ in disguise, where $u = \arctan x$. This is a pure substitution — no clever symmetry, no Feynman, just recognizing that you're integrating a function against its own derivative.

---

## Formal Proof / Solution

**Substitution.** Let

$$u = \arctan x, \quad du = \frac{dx}{1+x^2}.$$

**Change of limits:**
- When $x = 0$: $u = \arctan 0 = 0$.
- When $x \to \infty$: $u = \arctan(\infty) = \dfrac{\pi}{2}$.

**Rewrite the integral:**

$$I = \int_0^\infty \frac{\arctan x}{1+x^2}\,dx = \int_0^{\pi/2} u\,du.$$

**Evaluate:**

$$I = \left[\frac{u^2}{2}\right]_0^{\pi/2} = \frac{1}{2}\cdot\frac{\pi^2}{4} = \boxed{\dfrac{\pi^2}{8}}.$$

**Why is this satisfying?** The answer $\pi^2/8$ is a "Basel cousin" — it's half of $\pi^2/4$, and it arises from the simplest possible self-referential substitution. The function $\arctan$ integrates against its own derivative perfectly over the natural domain $[0,\infty)$ imposed by $\arctan$'s range $[0, \pi/2)$.
