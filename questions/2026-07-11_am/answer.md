# Answer: Integral of 1/(1+sin²x)

## Key Idea / Intuition

The integrand involves $\sin^2 x$, which mixes badly with direct antiderivatives. The trick is to **divide numerator and denominator by $\cos^2 x$**, turning the integral into one in terms of $\tan x$ only — a clean substitution $t = \tan x$ then reduces it to a standard arctangent integral over the entire positive real line.

---

## Formal Proof / Solution

**Step 1: Divide by $\cos^2 x$.**

On $(0, \pi/2)$, $\cos x \neq 0$, so we can write:

$$I = \int_0^{\pi/2} \frac{1}{1 + \sin^2 x} \cdot \frac{\sec^2 x}{\sec^2 x} \, dx = \int_0^{\pi/2} \frac{\sec^2 x}{\sec^2 x + \tan^2 x} \, dx.$$

Use $\sec^2 x = 1 + \tan^2 x$:

$$I = \int_0^{\pi/2} \frac{\sec^2 x}{1 + \tan^2 x + \tan^2 x} \, dx = \int_0^{\pi/2} \frac{\sec^2 x}{1 + 2\tan^2 x} \, dx.$$

**Step 2: Substitute $t = \tan x$.**

When $x: 0 \to \pi/2$, we have $t: 0 \to \infty$, and $dt = \sec^2 x \, dx$. So:

$$I = \int_0^{\infty} \frac{dt}{1 + 2t^2}.$$

**Step 3: Evaluate the standard integral.**

Factor out the $2$:

$$I = \int_0^{\infty} \frac{dt}{2\left(\frac{1}{2} + t^2\right)} = \frac{1}{2} \int_0^{\infty} \frac{dt}{t^2 + \frac{1}{2}}.$$

Using the standard formula $\displaystyle\int_0^\infty \frac{dt}{t^2 + a^2} = \frac{\pi}{2a}$ with $a = \frac{1}{\sqrt{2}}$:

$$I = \frac{1}{2} \cdot \frac{\pi}{2 \cdot \frac{1}{\sqrt{2}}} = \frac{1}{2} \cdot \frac{\pi\sqrt{2}}{2} = \frac{\pi\sqrt{2}}{4} = \frac{\pi}{2\sqrt{2}}.$$

**Result:**

$$\boxed{I = \dfrac{\pi}{2\sqrt{2}}.}$$

**Why is this beautiful?** The substitution $t = \tan x$ is a classical tool for integrals involving $\sin^2 x$ or $\cos^2 x$ in the denominator — it converts a bounded interval $[0, \pi/2]$ to $[0,\infty)$ and transforms a trigonometric integrand into a pure rational function, which is then immediately recognizable.
