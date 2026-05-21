# Answer: Logarithmic Derivative and Integrality of Winding

## Key Idea / Intuition

The idea is that $\log f(z)$, while not globally well-defined (since $\log$ is multi-valued), has a **perfectly well-defined derivative**: $(\log f)' = f'/f$. Integrating this derivative around a closed loop measures how much the argument of $f$ winds around, which must be an integer multiple of $2\pi$ — because $f$ returns to its starting value. The integral $\frac{1}{2\pi i}\oint f'/f\, dz$ is literally counting **how many times $f(\gamma)$ winds around the origin**.

---

## Formal Proof / Solution

### Step 1: The warm-up — $f(z) = z^n$

As $z = e^{i\theta}$ with $\theta$ going from $0$ to $2\pi$, we have $f(z) = e^{in\theta}$, so $\arg f = n\theta$. The total change in argument is:
$$\Delta \arg f = n \cdot 2\pi.$$

### Step 2: Setting up the integral

Suppose $f$ is analytic and nonvanishing on a closed curve $\gamma : [0,1] \to \mathbb{C}$. We want to compute:
$$I = \frac{1}{2\pi i} \oint_\gamma \frac{f'(z)}{f(z)}\, dz.$$

### Step 3: Local logarithm trick

Along the curve $\gamma$, since $f(\gamma(t)) \neq 0$ for all $t \in [0,1]$, we can define a **continuous branch** of the logarithm along the curve. That is, there exists a continuous function $L : [0,1] \to \mathbb{C}$ such that:
$$e^{L(t)} = f(\gamma(t)), \quad L(t) = \ln|f(\gamma(t))| + i\,\arg f(\gamma(t)).$$

(This is the **monodromy/path-lifting theorem** for the exponential map, or simply follows by continuity: locally, $\log f$ is analytic since $f \neq 0$.)

### Step 4: The integral reduces to boundary values

By the chain rule and the substitution $z = \gamma(t)$:
$$\oint_\gamma \frac{f'(z)}{f(z)}\, dz = \int_0^1 \frac{f'(\gamma(t))}{f(\gamma(t))}\, \gamma'(t)\, dt = \int_0^1 \frac{d}{dt} L(t)\, dt = L(1) - L(0).$$

### Step 5: Integrality

Since $\gamma$ is **closed**, $f(\gamma(1)) = f(\gamma(0))$, which means $e^{L(1)} = e^{L(0)}$. Therefore:
$$L(1) - L(0) = 2\pi i \cdot k$$
for some integer $k \in \mathbb{Z}$.

Thus:
$$\frac{1}{2\pi i} \oint_\gamma \frac{f'(z)}{f(z)}\, dz = k \in \mathbb{Z}.$$

### Step 6: Geometric meaning

The integer $k$ is the **winding number** of the image curve $f \circ \gamma$ around $0$. In the warm-up example $f(z) = z^n$ on the unit circle:
$$\frac{1}{2\pi i} \oint_{|z|=1} \frac{nz^{n-1}}{z^n}\, dz = \frac{1}{2\pi i} \cdot \frac{n}{z}\, dz = n.$$

This confirms the winding is exactly $n$.

### Bonus: Connection to the Argument Principle

When $f$ may have zeros and poles inside $\gamma$, the same reasoning gives the **Argument Principle**:
$$\frac{1}{2\pi i} \oint_\gamma \frac{f'(z)}{f(z)}\, dz = Z - P,$$
where $Z$ = number of zeros and $P$ = number of poles of $f$ inside $\gamma$ (counted with multiplicity). The integrality is automatic from the winding number perspective.
