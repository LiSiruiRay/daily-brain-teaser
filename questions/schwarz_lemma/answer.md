# The Schwarz Lemma — Answer

---

## First: Clarifying the Terminology

These three words get conflated, but they mean different things.

### Holomorphic (= Complex Differentiable)

$f$ is **holomorphic** on an open set $U$ if it is complex differentiable at every point of $U$.

Complex differentiable means the limit

$$f'(z) = \lim_{h \to 0} \frac{f(z+h) - f(z)}{h}$$

exists, where $h \in \mathbb{C}$ can approach 0 from **any direction** in the complex plane.

This is much stronger than real differentiability — requiring the limit to be the same from all directions forces $f$ to satisfy the **Cauchy-Riemann equations**.

### Analytic

$f$ is **analytic** at $z_0$ if it has a convergent **power series** expansion near $z_0$:

$$f(z) = \sum_{n=0}^{\infty} a_n (z - z_0)^n$$

In **real** analysis: analytic is strictly stronger than smooth (e.g. $e^{-1/x^2}$ is smooth but not analytic at 0).

In **complex** analysis: **holomorphic $\iff$ analytic**. This is a deep theorem — complex differentiability alone forces a power series to exist. So in complex analysis the two words are used interchangeably.

### Harmonic

A real-valued function $u(x, y)$ is **harmonic** if it satisfies Laplace's equation:

$$\Delta u = \frac{\partial^2 u}{\partial x^2} + \frac{\partial^2 u}{\partial y^2} = 0$$

The connection to holomorphic functions: if $f = u + iv$ is holomorphic, then **both $u$ and $v$ are harmonic**. This follows directly from the Cauchy-Riemann equations.

Conversely, every harmonic function is locally the real part of some holomorphic function.

### Summary Table

| Word | Meaning | Context |
|------|---------|---------|
| Holomorphic | Complex differentiable | Complex analysis |
| Analytic | Has a power series | Real or complex |
| Harmonic | Satisfies $\Delta u = 0$ | Real-valued functions |

In complex analysis: **holomorphic $\iff$ analytic**, and holomorphic $\Rightarrow$ real/imaginary parts are harmonic.

---

## Solution to the Schwarz Lemma

**Goal:** $f: \mathbb{D} \to \mathbb{D}$ holomorphic, $f(0) = 0$. Prove $|f(z)| \leq |z|$.

### Step 1: Define a helper function

Let

$$g(z) = \frac{f(z)}{z} \quad \text{for } z \neq 0$$

The problem: $g$ seems undefined at $z = 0$. But since $f(0) = 0$, near $z = 0$:

$$f(z) = f(0) + f'(0)z + \cdots = f'(0)z + O(z^2)$$

So $g(z) = f(z)/z \to f'(0)$ as $z \to 0$.

This means $z = 0$ is a **removable singularity** — $g$ extends to a holomorphic function on all of $\mathbb{D}$ by defining $g(0) = f'(0)$.

### Step 2: Bound $g$ on a circle

Fix any radius $0 < r < 1$. On the circle $|z| = r$:

$$|g(z)| = \frac{|f(z)|}{|z|} = \frac{|f(z)|}{r}$$

Since $f$ maps into $\mathbb{D}$, we have $|f(z)| < 1$, so:

$$|g(z)| < \frac{1}{r} \quad \text{on } |z| = r$$

### Step 3: Apply the Maximum Modulus Principle

The **Maximum Modulus Principle** says: a holomorphic function on a closed disk attains its maximum modulus **on the boundary**, not the interior (unless it is constant).

So for all $z$ inside the disk $|z| \leq r$:

$$|g(z)| \leq \max_{|z|=r} |g(z)| < \frac{1}{r}$$

### Step 4: Let $r \to 1$

The bound $|g(z)| < 1/r$ holds for every $r < 1$. Sending $r \to 1$:

$$|g(z)| \leq 1 \quad \text{for all } z \in \mathbb{D}$$

This means $|f(z)/z| \leq 1$, i.e.

$$\boxed{|f(z)| \leq |z|}$$

---

## Bonus: When does equality hold?

If $|g(z_0)| = 1$ for some interior point $z_0 \in \mathbb{D}$, then $|g|$ attains its maximum **in the interior** of the disk. The Maximum Modulus Principle then forces $g$ to be **constant**:

$$g(z) = e^{i\theta} \quad \text{for some } \theta \in \mathbb{R}$$

Therefore $f(z) = e^{i\theta} z$ — a rotation. $\square$

---

## The Big Picture

The one trick is: **divide by $z$ to turn $f$ into $g$**, then use the Maximum Modulus Principle. The condition $f(0) = 0$ is exactly what makes $z = 0$ a removable singularity rather than a pole.

The result says: fixing the origin forces $f$ to be a contraction. The only way to preserve distances is to rotate.
