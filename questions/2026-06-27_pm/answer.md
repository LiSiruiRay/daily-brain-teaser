# Answer: Wallis-Type Product Integral

## Key Idea / Intuition

The key trick is to rewrite $\sin x + \cos x$ as a single sinusoidal function using the amplitude-phase form: $\sin x + \cos x = \sqrt{2}\sin(x + \pi/4)$. This converts the integral into a known form involving $\ln(\sin)$ over a shifted interval — and the classic result $\int_0^{\pi/2} \ln(\sin x)\,dx = -\frac{\pi}{2}\ln 2$ does all the heavy lifting. The shift of the interval can be handled by symmetry and periodicity.

---

## Formal Proof / Solution

**Step 1: Rewrite the argument.**

Use the identity:
$$\sin x + \cos x = \sqrt{2}\,\sin\!\left(x + \frac{\pi}{4}\right).$$

So:
$$I = \int_0^{\pi/2} \ln\!\left(\sqrt{2}\,\sin\!\left(x + \frac{\pi}{4}\right)\right) dx = \int_0^{\pi/2} \frac{1}{2}\ln 2\, dx + \int_0^{\pi/2} \ln\!\left(\sin\!\left(x + \frac{\pi}{4}\right)\right) dx.$$

The first part gives:
$$\frac{1}{2}\ln 2 \cdot \frac{\pi}{2} = \frac{\pi \ln 2}{4}.$$

**Step 2: Evaluate the shifted integral.**

Let $u = x + \pi/4$, so $du = dx$ and $x \in [0, \pi/2]$ maps to $u \in [\pi/4, \, 3\pi/4]$:

$$\int_0^{\pi/2} \ln\!\left(\sin\!\left(x + \frac{\pi}{4}\right)\right) dx = \int_{\pi/4}^{3\pi/4} \ln(\sin u)\, du.$$

**Step 3: Use the symmetry of $\ln(\sin u)$.**

Since $\ln(\sin u)$ is symmetric about $u = \pi/2$ (i.e., $\sin(\pi - u) = \sin u$), the integral over $[\pi/4, 3\pi/4]$ can be related to the full integral over $[0, \pi]$.

The full interval symmetry gives:
$$\int_0^{\pi} \ln(\sin u)\, du = 2\int_0^{\pi/2} \ln(\sin u)\, du = 2 \cdot \left(-\frac{\pi}{2}\ln 2\right) = -\pi \ln 2.$$

Now split:
$$\int_0^{\pi} \ln(\sin u)\,du = \int_0^{\pi/4} \ln(\sin u)\,du + \int_{\pi/4}^{3\pi/4} \ln(\sin u)\,du + \int_{3\pi/4}^{\pi} \ln(\sin u)\,du.$$

By the substitution $u \mapsto \pi - u$, the first and last pieces are equal:
$$\int_{3\pi/4}^{\pi} \ln(\sin u)\,du = \int_0^{\pi/4} \ln(\sin u)\,du.$$

So:
$$\int_{\pi/4}^{3\pi/4} \ln(\sin u)\,du = -\pi\ln 2 - 2\int_0^{\pi/4} \ln(\sin u)\,du.$$

**Step 4: Evaluate $\int_0^{\pi/4} \ln(\sin u)\,du$.**

Use the known result (derivable from the reflection formula or the Fourier series of $\ln \sin$):
$$\int_0^{\pi/4} \ln(\sin u)\,du = -\frac{\pi}{4}\ln 2 - \frac{G}{2},$$
where $G = \sum_{n=0}^\infty \frac{(-1)^n}{(2n+1)^2}$ is Catalan's constant.

Therefore:
$$\int_{\pi/4}^{3\pi/4} \ln(\sin u)\,du = -\pi\ln 2 - 2\!\left(-\frac{\pi}{4}\ln 2 - \frac{G}{2}\right) = -\pi\ln 2 + \frac{\pi}{2}\ln 2 + G = -\frac{\pi}{2}\ln 2 + G.$$

**Step 5: Combine.**

$$I = \frac{\pi\ln 2}{4} + \left(-\frac{\pi}{2}\ln 2 + G\right) = \frac{\pi\ln 2}{4} - \frac{\pi\ln 2}{2} + G = -\frac{\pi \ln 2}{4} + G.$$

$$\boxed{I = G - \frac{\pi}{4}\ln 2,}$$

where $G \approx 0.9159\ldots$ is Catalan's constant.

**Sanity check:** Numerically, $G - \frac{\pi}{4}\ln 2 \approx 0.9159 - 0.5440 = 0.3719$, and direct numerical integration of $\int_0^{\pi/2}\ln(\sin x + \cos x)\,dx \approx 0.3719$. ✓
