# Answer: Integral of ln(1+x²)/(1+x²)

## Key Idea / Intuition

The integrand $\frac{\ln(1+x^2)}{1+x^2}$ looks intimidating, but the substitution $x = \tan\theta$ turns $1+x^2$ into $\sec^2\theta$ and reveals a clean trigonometric integral. The $\ln(1+x^2)$ becomes $\ln(\sec^2\theta) = 2\ln(\sec\theta) = -2\ln(\cos\theta)$, and suddenly we're integrating $-2\ln(\cos\theta)$ over $[0,\pi/4]$, which can be handled by a classic symmetry/duplication trick.

---

## Formal Proof / Solution

**Step 1: Substitution $x = \tan\theta$.**

Let $x = \tan\theta$, so $dx = \sec^2\theta\, d\theta$ and $1+x^2 = \sec^2\theta$.

When $x=0$: $\theta=0$. When $x=1$: $\theta=\pi/4$.

$$I = \int_0^{\pi/4} \frac{\ln(\sec^2\theta)}{\sec^2\theta}\cdot \sec^2\theta\, d\theta = \int_0^{\pi/4} \ln(\sec^2\theta)\, d\theta = -2\int_0^{\pi/4} \ln(\cos\theta)\, d\theta.$$

**Step 2: Evaluate $J = \int_0^{\pi/4} \ln(\cos\theta)\, d\theta$.**

Use the known result (derivable via the Fourier series for $\ln(\cos\theta)$ or the standard Clausen integral):

$$\int_0^{\pi/2} \ln(\cos\theta)\, d\theta = -\frac{\pi}{2}\ln 2.$$

Split this into two pieces:

$$\int_0^{\pi/2} \ln(\cos\theta)\, d\theta = \int_0^{\pi/4} \ln(\cos\theta)\, d\theta + \int_{\pi/4}^{\pi/2} \ln(\cos\theta)\, d\theta.$$

In the second integral, substitute $\theta \to \frac{\pi}{2}-\phi$, so $\cos\theta = \sin\phi$:

$$\int_{\pi/4}^{\pi/2} \ln(\cos\theta)\, d\theta = \int_0^{\pi/4} \ln(\sin\phi)\, d\phi.$$

So:

$$-\frac{\pi}{2}\ln 2 = \int_0^{\pi/4} \ln(\cos\theta)\, d\theta + \int_0^{\pi/4} \ln(\sin\theta)\, d\theta = \int_0^{\pi/4} \ln(\sin\theta\cos\theta)\, d\theta.$$

Now use $\sin\theta\cos\theta = \frac{1}{2}\sin(2\theta)$:

$$\int_0^{\pi/4} \ln\!\left(\tfrac{1}{2}\sin 2\theta\right)d\theta = \int_0^{\pi/4}\!\ln(\sin 2\theta)\,d\theta - \frac{\pi}{4}\ln 2.$$

Substitute $u = 2\theta$ in the first part:

$$\int_0^{\pi/4}\ln(\sin 2\theta)\,d\theta = \frac{1}{2}\int_0^{\pi/2}\ln(\sin u)\,du = \frac{1}{2}\cdot\left(-\frac{\pi}{2}\ln 2\right) = -\frac{\pi}{4}\ln 2.$$

So:

$$-\frac{\pi}{2}\ln 2 = -\frac{\pi}{4}\ln 2 - \frac{\pi}{4}\ln 2 = -\frac{\pi}{2}\ln 2. \checkmark$$

This is consistent but doesn't separate $J$ directly. Instead, use the **Clausen-type result** directly:

$$\int_0^{\pi/4}\ln(\cos\theta)\,d\theta = \frac{G}{2} - \frac{\pi}{4}\ln 2,$$

where $G = \sum_{n=0}^\infty \frac{(-1)^n}{(2n+1)^2} \approx 0.9159...$ is **Catalan's constant**.

This follows from the Fourier series $-\ln(2\cos\theta) = \sum_{k=1}^\infty \frac{(-1)^k}{k}\cos(2k\theta)$, integrated term by term over $[0,\pi/4]$.

**Step 3: Final answer.**

$$I = -2J = -2\left(\frac{G}{2} - \frac{\pi}{4}\ln 2\right) = -G + \frac{\pi}{2}\ln 2.$$

$$\boxed{I = \int_0^1 \frac{\ln(1+x^2)}{1+x^2}\,dx = \frac{\pi \ln 2}{2} - G}$$

where $G$ is Catalan's constant. Numerically: $\frac{\pi\ln 2}{2} \approx 1.089$, $G \approx 0.916$, so $I \approx 0.173$.

**The surprise:** a clean-looking rational-times-log integrand over $[0,1]$ secretly encodes Catalan's constant — one of the most mysterious constants in mathematics, whose irrationality is still unknown.

Written to: [questions/2025-07-14_PM_integral_ln_1_plus_x2.md](questions/2025-07-14_PM_integral_ln_1_plus_x2.md)
