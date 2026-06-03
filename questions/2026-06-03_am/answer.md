# Answer: The Thick Coin

## Key Idea / Intuition

The beautiful insight is a classical theorem from solid geometry: **the surface area of a spherical zone depends only on its height**, not on where it sits on the sphere. So the probability of landing on edge equals the fraction of the sphere's surface covered by the "equatorial band" — which is simply proportional to the height of that band. Setting this fraction to $1/3$ is then a clean geometric calculation using the Pythagorean theorem.

---

## Formal Proof / Solution

**Setup.** Inscribe the coin (a cylinder of radius $r$, thickness $t$) in a sphere of radius $R$. The center of the sphere coincides with the center of the coin. A random point on the sphere is chosen uniformly; if the radius to that point hits the curved side of the cylinder, the coin lands on edge.

**Archimedes' Hat-Box Theorem (Zone Area).** For a sphere of radius $R$, the area of a spherical zone of height $h$ (the region between two parallel planes) is:
$$A_{\text{zone}} = 2\pi R h.$$
This is independent of where the zone sits — only the height matters.

**Geometry.** The edge band corresponds to the zone of height $h = t$ (the thickness). The total surface area of the sphere is $4\pi R^2$. So:
$$P(\text{edge}) = \frac{2\pi R t}{4\pi R^2} = \frac{t}{2R}.$$

**Finding $R$ in terms of $r$ and $t$.** The corners of the cylinder touch the inscribed sphere. By the Pythagorean theorem:
$$R^2 = r^2 + \left(\frac{t}{2}\right)^2.$$

**Setting $P(\text{edge}) = \frac{1}{3}$.** We need:
$$\frac{t}{2R} = \frac{1}{3} \implies t = \frac{2R}{3}.$$

Substituting into $R^2 = r^2 + (t/2)^2$:
$$R^2 = r^2 + \frac{R^2}{9} \implies \frac{8R^2}{9} = r^2 \implies R = \frac{3r}{2\sqrt{2}}.$$

Then:
$$t = \frac{2R}{3} = \frac{2}{3} \cdot \frac{3r}{2\sqrt{2}} = \frac{r}{\sqrt{2}}.$$

**The ratio of thickness to diameter:**
$$\frac{t}{2r} = \frac{1}{2\sqrt{2}} = \frac{\sqrt{2}}{4} \approx 0.354.$$

**Conclusion.** The coin should be about **35.4% as thick as its diameter** to have a $\frac{1}{3}$ chance of landing on edge. This is the answer von Neumann reportedly computed in his head in 20 seconds.

> **Sanity check:** If $t = 0$ (flat disk), $P(\text{edge}) = 0$. If $t \to \infty$ (long cylinder), $P(\text{edge}) \to 1$. The formula $t/2R = 1/3$ interpolates cleanly between these extremes. ✓
