# Answer: The Integral That Sums to an Arcsine

## Key Idea / Intuition

The weight $1/\sqrt{x(1-x)}$ is the arclength element of the Beta distribution, and the substitution $x = \sin^2\theta$ transforms the integral into one involving $\ln(\sin^2\theta)$ against a flat measure on $[0,\pi/2]$ — which is precisely twice the classical log-sine integral $\int_0^{\pi/2}\ln(\sin\theta)\,d\theta = -\frac{\pi}{2}\ln 2$. The answer turns out to be a clean multiple of $\pi\ln 2$.

---

## Formal Proof / Solution

**Step 1: Substitution $x = \sin^2\theta$.**

Let $x = \sin^2\theta$, so $dx = 2\sin\theta\cos\theta\,d\theta$, and:
$$\sqrt{x(1-x)} = \sqrt{\sin^2\theta\cos^2\theta} = \sin\theta\cos\theta.$$

When $x=0$, $\theta=0$; when $x=1$, $\theta=\pi/2$. Thus:

$$I = \int_0^{\pi/2} \frac{\ln(\sin^2\theta)}{\sin\theta\cos\theta}\cdot 2\sin\theta\cos\theta\,d\theta = 2\int_0^{\pi/2}\ln(\sin^2\theta)\,d\theta.$$

**Step 2: Simplify.**

$$I = 2\int_0^{\pi/2} 2\ln(\sin\theta)\,d\theta = 4\int_0^{\pi/2}\ln(\sin\theta)\,d\theta.$$

**Step 3: Use the classical log-sine integral.**

The classical result (provable by the reflection symmetry $\theta \mapsto \pi/2 - \theta$ and Wallis's product) states:
$$\int_0^{\pi/2}\ln(\sin\theta)\,d\theta = -\frac{\pi}{2}\ln 2.$$

**Step 4: Conclude.**

$$I = 4\cdot\left(-\frac{\pi}{2}\ln 2\right) = -2\pi\ln 2.$$

---

**Quick verification of the classical log-sine integral** (for completeness):

Let $L = \int_0^{\pi/2}\ln(\sin\theta)\,d\theta$. By $\theta\mapsto\pi/2-\theta$, also $L = \int_0^{\pi/2}\ln(\cos\theta)\,d\theta$. Thus:
$$2L = \int_0^{\pi/2}\ln(\sin\theta\cos\theta)\,d\theta = \int_0^{\pi/2}\ln\!\left(\tfrac{\sin 2\theta}{2}\right)d\theta.$$

Substituting $\phi = 2\theta$ and using the $\pi/2$-periodicity:
$$2L = \tfrac{1}{2}\int_0^{\pi}\ln(\sin\phi)\,d\phi - \tfrac{\pi}{2}\ln 2 = L - \tfrac{\pi}{2}\ln 2,$$

so $L = -\tfrac{\pi}{2}\ln 2$. $\checkmark$

---

**Final answer:**

$$\boxed{I = -2\pi\ln 2.}$$
