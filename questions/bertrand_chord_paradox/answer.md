# Bertrand's Chord Paradox — Answer

## Setup

The side length of an equilateral triangle inscribed in a unit circle is √3. A chord is longer than √3 if and only if its **midpoint lies within distance 1/2 from the center** (since a chord of half-length h satisfies h² + d² = 1, so the chord length = 2h > √3 iff d < 1/2).

---

## Three Natural Methods

### Method 1: Random Endpoints
Choose two points A and B independently and uniformly on the circle. WLOG fix A. The chord AB is longer than √3 iff B lies in the arc "opposite" A — specifically the arc subtending an angle of 120° centered at the antipodal point of A. That arc is 1/3 of the circle.

**P = 1/3**

---

### Method 2: Random Midpoint
Every chord is uniquely determined by its midpoint (inside the disk). Choose a midpoint uniformly at random in the disk. The chord is longer than √3 iff the midpoint is within distance 1/2 from the center (the "favorable" disk of radius 1/2).

$$P = \frac{\pi (1/2)^2}{\pi (1)^2} = \frac{1}{4}$$

**P = 1/4**

---

### Method 3: Random Radius + Position
Fix a radius (say, vertical). Choose a point uniformly at random on this radius. The chord perpendicular to the radius at that point is longer than √3 iff the point is in the middle half of the radius (distance from center < 1/2), which is half the radius.

**P = 1/2**

---

## The Paradox

All three methods are geometrically natural and internally consistent. They give different answers because they correspond to different probability measures on the space of chords. The phrase "random chord" is ill-defined.

This was Bertrand's (1889) original observation, and it motivated Poincaré and later Kolmogorov to insist that a probability problem must specify its sample space and measure explicitly.

**Modern resolution:** Jaynes (1973) argued that Method 3 is the "correct" one under a physical symmetry argument (the answer should be invariant under scaling and translation of the circle). This gives **P = 1/2** and is related to the principle of maximum entropy / geometric invariance. But this remains debated.

---

## Key Takeaway

> Probability is not just about "symmetry" — it depends on how you parameterize the space of outcomes. Different natural parameterizations can give different answers.

## Reference
Bertrand, J. (1889). *Calcul des Probabilités*. The problem appears in Section I as an example of geometric probability.

Check out this video: https://www.youtube.com/watch?v=mZBwsm6B280

some related leetcode question (surprise!!): https://leetcode.com/problems/generate-random-point-in-a-circle/description/ 

why is the following solution not working?

```
class Solution:

    def __init__(self, radius: float, x_center: float, y_center: float):
        self.radius = radius
        self.x_center = x_center
        self.y_center = y_center
    
    def rescale(self, x, a, b, c, d):
        return c + (x - a) * ((d - c) / (b - a))

    def randPoint(self) -> List[float]:
        radius = self.radius
        x_center = self.x_center
        y_center = self.y_center

        ran_theta = random.random()
        ran_r = random.random()

        theta = self.rescale(ran_theta, 0, 1, 0, 2 * math.pi)
        r = self.rescale(ran_r, 0, 1, 0, radius)

        ran_y = r * math.sin(theta)
        ran_x = r * math.cos(theta)
        ret_x = x_center + ran_x
        ret_y = y_center + ran_y

        return [ret_x, ret_y]


        


# Your Solution object will be instantiated and called as such:
# obj = Solution(radius, x_center, y_center)
# param_1 = obj.randPoint()
```