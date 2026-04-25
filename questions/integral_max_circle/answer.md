# Answer: Integral of a Max with a Circle

$$\boxed{\dfrac{\pi}{3} - \dfrac{\sqrt{3}}{4}}$$

---

## Intuition First

The function $y = \sqrt{1-x^2}$ is the **upper unit semicircle**. The integrand $\max(0,\, \sqrt{1-x^2} - \tfrac{1}{2})$ is zero wherever the circle dips below the horizontal line $y = \tfrac{1}{2}$, and equals the height above that line wherever the circle is above it.

So the integral is simply the **area of the circular segment** of the unit disk that lies above the line $y = \tfrac{1}{2}$.

$$\text{(integral)} = \text{(sector area)} - \text{(triangle area)}$$

---

## Geometric Solution

**Step 1 — Find where the circle crosses $y = \tfrac{1}{2}$.**

$$\sqrt{1-x^2} = \frac{1}{2} \implies x = \pm\frac{\sqrt{3}}{2}$$

In polar terms, these are the points at angles $\theta = \tfrac{\pi}{6}$ and $\theta = \tfrac{5\pi}{6}$. The arc above $y = \tfrac{1}{2}$ subtends an angle of $\tfrac{5\pi}{6} - \tfrac{\pi}{6} = \tfrac{2\pi}{3}$.

**Step 2 — Sector area.**

$$A_{\text{sector}} = \frac{1}{2} r^2 \cdot \theta = \frac{1}{2}(1)^2 \cdot \frac{2\pi}{3} = \frac{\pi}{3}$$

**Step 3 — Triangle area.**

The sector contains a triangle with vertices at the origin and the two intersection points $\bigl(\pm\tfrac{\sqrt{3}}{2},\, \tfrac{1}{2}\bigr)$.

- Base: distance between the two points $= \sqrt{3}$
- Height: distance from origin to the chord $y = \tfrac{1}{2}$ is $\tfrac{1}{2}$

$$A_{\text{triangle}} = \frac{1}{2} \cdot \sqrt{3} \cdot \frac{1}{2} = \frac{\sqrt{3}}{4}$$

**Step 4 — Circular segment area.**

$$\int_{-1}^{1} \max\!\left(0, \sqrt{1-x^2} - \frac{1}{2}\right)dx = A_{\text{sector}} - A_{\text{triangle}} = \frac{\pi}{3} - \frac{\sqrt{3}}{4}$$

---

## Verification via Calculus

The integrand is nonzero only where $\sqrt{1-x^2} \geq \tfrac{1}{2}$, i.e. $|x| \leq \tfrac{\sqrt{3}}{2}$.

$$\int_{-\sqrt{3}/2}^{\sqrt{3}/2} \!\left(\sqrt{1-x^2} - \frac{1}{2}\right)dx$$

Using $\displaystyle\int \sqrt{1-x^2}\,dx = \frac{x\sqrt{1-x^2}}{2} + \frac{\arcsin x}{2} + C$:

$$\left[\frac{x\sqrt{1-x^2}}{2} + \frac{\arcsin x}{2}\right]_{-\sqrt{3}/2}^{\sqrt{3}/2} - \frac{1}{2}\cdot\sqrt{3}$$

$$= 2\!\left(\frac{\frac{\sqrt{3}}{2}\cdot\frac{1}{2}}{2} + \frac{1}{2}\cdot\frac{\pi}{3}\right) - \frac{\sqrt{3}}{2} = \frac{\sqrt{3}}{4} + \frac{\pi}{3} - \frac{\sqrt{3}}{2} = \frac{\pi}{3} - \frac{\sqrt{3}}{4} \checkmark$$
