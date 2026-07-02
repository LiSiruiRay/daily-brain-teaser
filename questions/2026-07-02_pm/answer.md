# Answer: Casorati–Weierstrass: Dense Image Near Essential Singularity

## Key Idea / Intuition

If the image of $f$ avoided a whole disk around some value $c$, then $1/(f(z)-c)$ would be bounded near $0$ — forcing $0$ to be either a removable singularity or a pole of $f$, contradicting the assumption that it's essential. So the image can never dodge an open set: it must be **dense**.

---

## Formal Proof / Solution

**Theorem (Casorati–Weierstrass):** If $f$ has an essential singularity at $z_0 = 0$, then for every punctured neighborhood $U = \{0 < |z| < r\}$, the image $f(U)$ is dense in $\mathbb{C}$.

---

**Proof by contradiction:**

Suppose $f(U)$ is *not* dense in $\mathbb{C}$. Then there exists $c \in \mathbb{C}$ and $\varepsilon > 0$ such that

$$|f(z) - c| \geq \varepsilon \quad \text{for all } z \in U.$$

Define

$$g(z) = \frac{1}{f(z) - c}, \quad z \in U.$$

Since $|f(z) - c| \geq \varepsilon > 0$, we have $g$ holomorphic on $U$ and

$$|g(z)| \leq \frac{1}{\varepsilon} \quad \text{for all } z \in U.$$

So $g$ is **bounded** on the punctured disk. By Riemann's removable singularity theorem, $g$ extends to a holomorphic function $\tilde{g}$ on the full disk $|z| < r$.

**Case 1: $\tilde{g}(0) \neq 0$.**

Then $f(z) = c + 1/\tilde{g}(z)$ extends holomorphically to $z = 0$. So $z = 0$ is a **removable singularity** of $f$ — contradiction.

**Case 2: $\tilde{g}(0) = 0$.**

Then $\tilde{g}(z) = z^m h(z)$ near $0$, where $h(0) \neq 0$ and $m \geq 1$. Thus

$$f(z) = c + \frac{1}{z^m h(z)},$$

which has a **pole of order $m$** at $z = 0$ — also a contradiction.

In both cases, we contradict the assumption that $z = 0$ is an essential singularity. $\blacksquare$

---

**Sanity check with $f(z) = e^{1/z}$:**

Write $z = r e^{i\theta}$. Then $1/z = \frac{1}{r}e^{-i\theta}$, so

$$e^{1/z} = e^{\cos\theta/r} \cdot e^{i\sin\theta/r}.$$

- The **modulus** $e^{\cos\theta/r}$ ranges over $(0, \infty)$ as $\theta, r$ vary.
- The **argument** $\sin\theta/r$ ranges over all of $\mathbb{R}$ (mod $2\pi$).

So $e^{1/z}$ takes all nonzero values and its image is indeed dense in $\mathbb{C}$ (actually all of $\mathbb{C} \setminus \{0\}$, by Picard's great theorem — a much stronger result).

---

**Remark:** Picard's Great Theorem strengthens this dramatically: near an essential singularity, $f$ takes **every** complex value with at most one exception, infinitely often. Casorati–Weierstrass is the elegant, accessible version of this idea.
