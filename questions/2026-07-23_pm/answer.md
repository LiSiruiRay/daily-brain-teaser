# Answer: The Cauchy Integral That Evaluates Itself

## Key Idea / Intuition

The key insight is to convert the trigonometric integral over $[0, 2\pi]$ into a contour integral over the unit circle $|z| = 1$ by writing $z = e^{i\theta}$, so $\cos\theta = \frac{z + z^{-1}}{2}$ and $d\theta = \frac{dz}{iz}$. The resulting rational function of $z$ has poles that can be located explicitly, and then the residue theorem (a consequence of Cauchy's formula) does all the work. The answer turns out to be a clean expression involving $\sqrt{3}$, which is surprising from the integral's innocent appearance.

---

## Formal Proof / Solution

**Step 1: Substitution $z = e^{i\theta}$.**

On the unit circle $|z|=1$: 
$$\cos\theta = \frac{z + z^{-1}}{2}, \qquad d\theta = \frac{dz}{iz}.$$

So:
$$I = \oint_{|z|=1} \frac{\dfrac{z+z^{-1}}{2}}{2 - \dfrac{z+z^{-1}}{2}} \cdot \frac{dz}{iz}.$$

**Step 2: Simplify the integrand.**

Multiply numerator and denominator of the big fraction by $2z$:

$$\frac{z + z^{-1}}{2} = \frac{z^2+1}{2z}, \qquad 2 - \frac{z+z^{-1}}{2} = \frac{4z - z^2 - 1}{2z} = \frac{-(z^2 - 4z + 1)}{2z}.$$

So the integrand becomes:

$$\frac{(z^2+1)/(2z)}{-(z^2-4z+1)/(2z)} \cdot \frac{1}{iz} = \frac{z^2+1}{-(z^2-4z+1)} \cdot \frac{1}{iz}.$$

Thus:
$$I = \oint_{|z|=1} \frac{-(z^2+1)}{iz(z^2 - 4z + 1)}\, dz = \frac{i}{1} \oint_{|z|=1} \frac{z^2+1}{z(z^2-4z+1)}\, dz.$$

More carefully:
$$I = \frac{1}{i}\oint_{|z|=1} \frac{-(z^2+1)}{z(z^2-4z+1)}\,dz.$$

Let me redo cleanly. We have:

$$I = \oint_{|z|=1} \frac{z^2+1}{-(z^2-4z+1)} \cdot \frac{dz}{iz} = \frac{1}{i}\oint_{|z|=1} \frac{-(z^2+1)}{z(z^2-4z+1)}\,dz.$$

**Step 3: Factor the denominator.**

The roots of $z^2 - 4z + 1 = 0$ are:
$$z = \frac{4 \pm \sqrt{16-4}}{2} = 2 \pm \sqrt{3}.$$

So $z_1 = 2 - \sqrt{3} \approx 0.27$ (inside $|z|=1$) and $z_2 = 2+\sqrt{3} \approx 3.73$ (outside $|z|=1$).

**Step 4: Compute residues inside $|z|=1$.**

The poles inside are at $z=0$ and $z = z_1 = 2-\sqrt{3}$.

Define $g(z) = \dfrac{-(z^2+1)}{z(z^2-4z+1)}$.

**Residue at $z=0$:**
$$\text{Res}_{z=0}\, g(z) = \frac{-(0+1)}{0 \cdot \text{stuff}} \cdot \lim_{z\to 0} z \cdot g(z) = \frac{-1}{1 \cdot (0-0+1)} = -1.$$

More carefully: $\text{Res}_{z=0} = \lim_{z\to 0} z \cdot \frac{-(z^2+1)}{z(z^2-4z+1)} = \frac{-1}{1} = -1.$

**Residue at $z = 2-\sqrt{3}$:**

$$\text{Res}_{z=z_1} = \frac{-(z_1^2+1)}{z_1 \cdot (z_1 - z_2)} = \frac{-(z_1^2+1)}{z_1 \cdot (-2\sqrt{3})}.$$

Now $z_1 = 2-\sqrt{3}$, so $z_1^2 = 4 - 4\sqrt{3} + 3 = 7 - 4\sqrt{3}$, thus $z_1^2 + 1 = 8 - 4\sqrt{3} = 4(2-\sqrt{3})$.

$$\text{Res}_{z=z_1} = \frac{-4(2-\sqrt{3})}{(2-\sqrt{3})(-2\sqrt{3})} = \frac{-4}{-2\sqrt{3}} = \frac{2}{\sqrt{3}}.$$

**Step 5: Apply the residue theorem.**

$$\oint_{|z|=1} g(z)\, dz = 2\pi i \left(-1 + \frac{2}{\sqrt{3}}\right).$$

Therefore:
$$I = \frac{1}{i} \cdot 2\pi i \left(-1 + \frac{2}{\sqrt{3}}\right) = 2\pi\left(\frac{2}{\sqrt{3}} - 1\right).$$

**Simplifying:**

$$\boxed{I = 2\pi\!\left(\frac{2}{\sqrt{3}} - 1\right) = 2\pi\!\left(\frac{2\sqrt{3}}{3} - 1\right) \approx 2\pi(0.155) \approx 0.976.}$$

**Sanity check:** Since $\frac{\cos\theta}{2-\cos\theta}$ averages to a small positive number over $[0,2\pi]$, a value near $1$ makes sense. ✓

---

**The beauty:** A completely elementary-looking trigonometric integral, with no obvious closed form, yields an answer involving $\sqrt{3}$ — the signature of a quadratic residue computation hidden inside the unit circle substitution.
