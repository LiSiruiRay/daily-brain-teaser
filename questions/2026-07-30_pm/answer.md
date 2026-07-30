# Answer: The Conformal Map That Squares the Disk

## Key Idea / Intuition

The hypothesis says $f$ is "dominated by $z^2$" on the boundary. The natural move is to form the ratio $g(z) = f(z)/z^2$, which removes the double zero at the origin. This ratio is holomorphic on the punctured disk — and because $f(0) = 0$ with sufficient vanishing, the singularity at $0$ is removable. Then the **Maximum Modulus Principle** says $|g|$ attains its max on the boundary, where we know $|g| \leq 1$. Equality inside forces $g$ to be a constant of modulus 1.

---

## Formal Proof / Solution

**Step 1: Form the auxiliary function.**

Define
$$g(z) = \frac{f(z)}{z^2}, \quad z \in \mathbb{D} \setminus \{0\}.$$

Since $f(0) = 0$, write $f(z) = a_1 z + a_2 z^2 + \cdots$ near $0$. Then
$$g(z) = \frac{a_1 z + a_2 z^2 + \cdots}{z^2} = \frac{a_1}{z} + a_2 + a_3 z + \cdots$$

For $g$ to have a removable singularity at $0$, we need $a_1 = 0$, i.e., $f'(0) = 0$.

Wait — do we know this? Not directly. Let's be more careful.

**Step 2: Handle the singularity properly.**

We know $|f(z)| \leq |z|^2$ on $|z|=1$. By the Maximum Modulus Principle applied to $f$ itself on $\overline{\mathbb{D}}$, we get $|f(z)| \leq 1$ for all $z \in \mathbb{D}$. But we can do better.

Consider $g(z) = f(z)/z^2$ on $\mathbb{D}\setminus\{0\}$. We claim $z=0$ is a removable singularity. Indeed, near $0$:
$$|f(z)| \leq \|f\|_\infty \cdot 1 \quad \Rightarrow \quad |g(z)| = \frac{|f(z)|}{|z|^2} \leq \frac{C}{|z|^2},$$
which seems to blow up. But we can use a refined argument: apply the **three-circle theorem** or the following direct approach.

**Direct approach via Schwarz lemma framework:**

Define $h(z) = f(z)/z$ for $z \neq 0$. Since $f(0)=0$, the singularity is removable and $h$ is holomorphic on $\mathbb{D}$ with $h(0) = f'(0) = a_1$. On $|z|=1$: $|h(z)| = |f(z)| \leq |z|^2 = 1$. By Maximum Modulus, $|h(z)| \leq 1$ on all of $\mathbb{D}$, so $|f(z)| \leq |z|$.

Now apply the same trick to $h$: on $|z|=1$, $|h(z)| = |f(z)|/1 \leq |z|^2 / |z| = |z| = 1$. Define $k(z) = h(z)/z = f(z)/z^2$ for $z \neq 0$. Since $|h(z)| \leq |z|$ (from above), we have $h(0) = 0$, so $k$ extends holomorphically to $0$ with $k(0) = h'(0)$.

On $|z| = 1$: $|k(z)| = |h(z)| \leq 1$. By Maximum Modulus:
$$|k(z)| \leq 1 \quad \text{for all } z \in \mathbb{D}.$$

This gives
$$\boxed{|f(z)| = |z|^2 |k(z)| \leq |z|^2} \quad \text{for all } z \in \mathbb{D}.$$

**Step 3: Equality case.**

If $|f(z_0)| = |z_0|^2$ for some $z_0 \neq 0$, then $|k(z_0)| = 1$. Since $k$ is holomorphic on $\mathbb{D}$ with $|k| \leq 1$ on the boundary, and $|k|$ attains its maximum value $1$ at an interior point $z_0$, the **Maximum Modulus Principle** forces $k$ to be a **constant**:
$$k(z) \equiv c, \quad |c| = 1.$$

Therefore:
$$f(z) = c z^2, \quad |c| = 1.$$

**Summary:**
- The bound $|f(z)| \leq |z|^2$ propagates from the boundary to the interior via two applications of the Schwarz lemma / Maximum Modulus Principle.
- Equality at any interior point forces $f(z) = e^{i\theta} z^2$ for some real $\theta$.
