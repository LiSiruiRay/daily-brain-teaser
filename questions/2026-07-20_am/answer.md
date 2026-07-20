# Answer: The Integral That Oscillates Into Submission

## Key Idea / Intuition

The factor $1/x$ is awkward to integrate directly, but it has a beautiful integral representation: $\frac{1}{x} = \int_0^\infty e^{-xt}\, dt$. Inserting this under the integral sign (Feynman's trick / Laplace transform) converts the problem into computing a family of standard Gaussian-exponential integrals, then integrating the result over a parameter. The answer turns out to be $\frac{\pi}{4}$, a genuinely surprising outcome from a wildly oscillating integrand.

---

## Formal Proof / Solution

**Step 1: Represent $1/x$ as a Laplace transform.**

Use the identity
$$\frac{1}{x} = \int_0^\infty e^{-xt}\, dt, \quad x > 0.$$

So
$$I = \int_0^\infty e^{-x}\sin(x)\left(\int_0^\infty e^{-xt}\, dt\right) dx = \int_0^\infty \left(\int_0^\infty e^{-x(1+t)}\sin(x)\, dx\right) dt.$$

(Fubini is justified since the double integral of the absolute value converges.)

**Step 2: Evaluate the inner integral.**

For fixed $t > 0$, let $a = 1+t > 1$. Then

$$\int_0^\infty e^{-ax}\sin(x)\, dx = \operatorname{Im}\int_0^\infty e^{-ax} e^{ix}\, dx = \operatorname{Im}\frac{1}{a - i} = \operatorname{Im}\frac{a+i}{a^2+1} = \frac{1}{a^2+1}.$$

So the inner integral equals $\dfrac{1}{(1+t)^2 + 1}$.

**Step 3: Integrate over $t$.**

$$I = \int_0^\infty \frac{dt}{(1+t)^2 + 1}.$$

Substitute $u = 1+t$, $du = dt$:

$$I = \int_1^\infty \frac{du}{u^2+1} = \left[\arctan(u)\right]_1^\infty = \frac{\pi}{2} - \frac{\pi}{4} = \boxed{\frac{\pi}{4}}.$$

**Summary of the trick:**

The key move is replacing $\frac{1}{x}$ by $\int_0^\infty e^{-xt}\,dt$, which promotes the oscillatory integral to a one-parameter family of pure exponential integrals, each of which is elementary via $\int_0^\infty e^{-ax}\sin x\,dx = \frac{1}{a^2+1}$. The final integral over the parameter is just an arctangent.
