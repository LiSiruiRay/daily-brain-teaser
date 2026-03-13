# Parallel Transport on a Sphere — Answer

**The vector rotates by $2\pi(1 - \cos\theta)$.**

---

## Step 1: What does "parallel transport" mean?

On a flat plane, moving a vector along a path while keeping it pointing the same direction is obvious. On a curved surface, there is no global "same direction." Instead, **parallel transport** means: move the vector along the curve, and at each moment, only allow changes in the direction *along* the surface that are forced by the curve turning — never rotate the vector within the tangent plane.

Concretely: a vector $V$ is parallel transported along a curve $\gamma$ if its **covariant derivative** along $\gamma$ is zero:

$$\nabla_{\dot\gamma} V = 0$$

This is the "straightest possible" way to carry a vector along a curve on a curved surface.

---

## Step 2: The key tool — Gauss-Bonnet Theorem

For a smooth closed curve $\gamma$ on a surface bounding a region $\Omega$:

$$\int_\gamma \kappa_g \, ds + \iint_\Omega K \, dA = 2\pi$$

where:
- $\kappa_g$ = **geodesic curvature** of $\gamma$ (how much the curve bends within the surface)
- $K$ = **Gaussian curvature** of the surface

**The holonomy angle** (rotation of a parallel-transported vector around $\gamma$) is:

$$\alpha = \iint_\Omega K \, dA$$

Intuition: on a flat plane $K = 0$ everywhere, so $\alpha = 0$ — a vector always comes back unchanged. On a sphere, $K > 0$, so enclosed curvature causes rotation.

---

## Step 3: Gaussian curvature of the unit sphere

For the unit sphere $S^2$, the Gaussian curvature is constant:

$$K = 1 \quad \text{everywhere}$$

---

## Step 4: Area of the spherical cap

The region enclosed by the latitude circle at colatitude $\theta$ is a **spherical cap** — the "polar cap" from the north pole down to angle $\theta$.

Using the standard area element $dA = \sin\theta' \, d\theta' \, d\phi$:

$$\text{Area} = \int_0^{2\pi} \int_0^\theta \sin\theta' \, d\theta' \, d\phi = 2\pi \Big[-\cos\theta'\Big]_0^\theta = 2\pi(1 - \cos\theta)$$

---

## Step 5: Compute the holonomy

$$\alpha = \iint_\Omega K \, dA = 1 \cdot 2\pi(1 - \cos\theta) = \boxed{2\pi(1 - \cos\theta)}$$

---

## Sanity checks

| $\theta$ | Situation | $\alpha$ | Makes sense? |
|---------|-----------|----------|--------------|
| $\theta \to 0$ | Tiny circle near north pole | $\approx \pi\theta^2 \to 0$ | Small loop, small curvature enclosed → tiny rotation ✓ |
| $\theta = \pi/2$ | Equator | $2\pi(1-0) = 2\pi \equiv 0$ | Equator is a geodesic → parallel transport has no holonomy ✓ |
| $\theta = \pi/3$ | 60° from north pole | $2\pi(1 - \tfrac{1}{2}) = \pi$ | Vector completely flips direction! |
| $\theta = \pi$ | Full sphere (south pole) | $2\pi(1-(-1)) = 4\pi \equiv 0$ | Closed surface, total curvature $4\pi$ → back to start ✓ |

---

## Why is this beautiful?

On a flat surface, carrying a vector around any loop always returns it unchanged. On a sphere, **the curvature leaves a fingerprint**: the vector rotates by exactly the area of the spherical cap (since $K=1$). The rotation is a direct geometric measurement of the enclosed curvature.

This is the concept of **holonomy** — the failure of parallel transport to return a vector to its original orientation. It is the geometric heart of gauge theory in physics, and explains why a Foucault pendulum rotates: the Earth's surface is curved, and as the Earth rotates, the pendulum parallel transports itself around a latitude circle, accumulating a holonomy angle of $2\pi(1-\cos\theta)$ per day.
