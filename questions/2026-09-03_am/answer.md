# Answer: The Holomorphic Function That Misses Two Points

## Key Idea / Intuition

If $f$ avoids two values $a$ and $b$, we can normalize so that $f$ avoids $0$ and $1$. Then $\log f$ can be defined globally (since $f$ never hits $0$), giving an entire function $g = \log f$ that avoids all real multiples of $2\pi i$. One more layer of cleverness — a classical trick using $\sin$ or the exponential — produces a **bounded entire function**, which by Liouville must be constant.

The cleanest route: use the fact that $\mathbb{C} \setminus \{0,1\}$ has the upper half-plane as its **universal cover**, combined with the monodromy theorem, to lift $f$ to a bounded holomorphic function.

---

## Formal Proof / Solution

**Step 1: Normalize.**

Since $a \neq b$, consider $h(z) = \frac{f(z) - a}{b - a}$. Then $h$ is entire, and $h$ omits both $0$ and $1$. So without loss of generality, assume $f$ itself is entire and satisfies $f(z) \notin \{0, 1\}$ for all $z$.

**Step 2: Define a global logarithm.**

Since $f$ is entire and never zero, $f$ has a global holomorphic logarithm:
$$g(z) = \log f(z),$$
which is entire. Here we use that $\mathbb{C}$ is simply connected, so the logarithm can be defined without branch cuts. Thus $e^{g(z)} = f(z)$ and $g$ is entire.

**Step 3: The image constraint on $g$.**

Since $f(z) \neq 1$, we have $e^{g(z)} \neq 1$, which means:
$$g(z) \notin 2\pi i \mathbb{Z} \quad \text{for all } z.$$

**Step 4: Use the universal covering of $\mathbb{C} \setminus \{0,1\}$.**

Here is the key classical fact: **the upper half-plane $\mathbb{H}$ is the universal cover of $\mathbb{C} \setminus \{0,1\}$**, via the modular lambda function $\lambda : \mathbb{H} \to \mathbb{C} \setminus \{0,1\}$.

Since $f : \mathbb{C} \to \mathbb{C} \setminus \{0,1\}$ and $\mathbb{C}$ is simply connected, by the **monodromy theorem** (lifting criterion for covering spaces), $f$ lifts to a holomorphic map:
$$\tilde{f} : \mathbb{C} \to \mathbb{H}$$
satisfying $\lambda \circ \tilde{f} = f$.

**Step 5: Apply Liouville's theorem.**

The upper half-plane $\mathbb{H}$ is conformally equivalent to the open unit disk $\mathbb{D}$ via the Möbius transformation:
$$\phi(w) = \frac{w - i}{w + i}.$$

Define $F = \phi \circ \tilde{f} : \mathbb{C} \to \mathbb{D}$. Then $F$ is an **entire function** with $|F(z)| < 1$ for all $z$.

By **Liouville's theorem**, $F$ is constant. Hence $\tilde{f}$ is constant, and therefore:
$$f = \lambda \circ \tilde{f}$$
is constant. $\blacksquare$

---

## Why This Is Surprising

The result is sharp: an entire function can omit **one** value (e.g., $e^z$ omits $0$). Omitting two values is too much — the function is forced to be constant. The proof is conceptually beautiful: the "two missing values" rigidify the target space so much that its universal cover becomes the disk, and any entire map into the disk must be constant by Liouville.
