# Parallel Transport on a Sphere

**Type:** Differential Geometry
**Tags:** Parallel transport, Holonomy, Gauss-Bonnet, Geodesics, Curvature
**Date:** 2026-03-12
**Difficulty:** 3/5

**Why it's beautiful:**
This problem makes curvature *visible*. On a flat plane, if you carry a vector around any closed loop keeping it "straight" the whole time, it comes back unchanged. On a sphere, it doesn't — and the angle it rotates by is a direct measurement of the curvature enclosed. The answer connects to the Gauss-Bonnet theorem and explains a real-world phenomenon: the Foucault pendulum.

---

## Setup

On the unit sphere $S^2$, a **latitude circle** at **colatitude** $\theta$ (measured from the north pole) is the circle:

$$\{ (\sin\theta \cos\phi,\ \sin\theta \sin\phi,\ \cos\theta) : \phi \in [0, 2\pi) \}$$

So $\theta = 0$ is the north pole, $\theta = \pi/2$ is the equator, $\theta = \pi$ is the south pole.

## Problem

Take a unit tangent vector at a point on the latitude circle at colatitude $\theta$. **Parallel transport** it all the way around the circle (keeping it as "straight" as possible along the surface). When the vector returns to its starting point, **by what angle has it rotated?**

---

*Hint: Use the Gauss-Bonnet theorem. The holonomy around a closed curve equals the integral of Gaussian curvature over the enclosed region.*
