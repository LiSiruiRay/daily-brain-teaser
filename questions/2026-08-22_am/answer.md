# Answer: The Integral That Reflects Twice

## Key Idea / Intuition

The integral $\int_0^1 \frac{\ln(1+x)}{1+x^2}\,dx$ looks hard because the logarithm and rational function don't obviously interact. The trick is to use the substitution $x = \tan\theta$ to convert it into a trigonometric integral over $[0,\pi/4]$, then exploit the reflection $\theta \mapsto \pi/4 - \theta$ (a symmetry of the integration interval) to collapse $\ln(1+\tan\theta)$ into something whose average is a pure constant — revealing $I$ in terms of $\ln\sqrt{2}$ and $\pi$.

---

## Formal Proof / Solution

**Step 1: Substitute $x = \tan\theta$.**

Set $x = \tan\theta$, so $dx = \sec^2\theta\,d\theta$ and $1+x^2 = \sec^2\theta$. When $x=0$, $\theta=0$; when $x=1$, $\theta = \pi/4$. Then:

$$I = \int_0^{\pi/4} \frac{\ln(1+\tan\theta)}{\sec^2\theta}\cdot \sec^2\theta\,d\theta = \int_0^{\pi/4} \ln(1+\tan\theta)\,d\theta.$$

**Step 2: Apply the reflection $\theta \mapsto \pi/4 - \theta$.**

Let $J = \int_0^{\pi/4} \ln(1+\tan\theta)\,d\theta$. Substitute $\theta \to \pi/4 - \theta$:

$$J = \int_0^{\pi/4} \ln\!\left(1 + \tan\!\left(\tfrac{\pi}{4}-\theta\right)\right)d\theta.$$

Use the addition formula:

$$\tan\!\left(\tfrac{\pi}{4}-\theta\right) = \frac{1-\tan\theta}{1+\tan\theta}.$$

So:

$$1 + \tan\!\left(\tfrac{\pi}{4}-\theta\right) = 1 + \frac{1-\tan\theta}{1+\tan\theta} = \frac{(1+\tan\theta)+(1-\tan\theta)}{1+\tan\theta} = \frac{2}{1+\tan\theta}.$$

Therefore:

$$J = \int_0^{\pi/4} \ln\!\left(\frac{2}{1+\tan\theta}\right)d\theta = \int_0^{\pi/4} \left[\ln 2 - \ln(1+\tan\theta)\right]d\theta.$$

**Step 3: Solve for $J$.**

Adding $J$ to itself (original + reflected):

$$2J = \int_0^{\pi/4}\ln(1+\tan\theta)\,d\theta + \int_0^{\pi/4}\left[\ln 2 - \ln(1+\tan\theta)\right]d\theta = \int_0^{\pi/4}\ln 2\,d\theta = \frac{\pi}{4}\ln 2.$$

Thus:

$$J = \frac{\pi}{8}\ln 2.$$

**Conclusion:**

$$\boxed{I = \frac{\pi}{8}\ln 2.}$$

The beautiful punchline: the reflection $\theta \mapsto \pi/4-\theta$ causes $\ln(1+\tan\theta)$ and $\ln(2/(1+\tan\theta))$ to be *mirror images* of each other, so their sum is just the constant $\ln 2$ — and the integral of a constant over $[0,\pi/4]$ is trivial.
