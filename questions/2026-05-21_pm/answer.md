# Answer: Open Mapping + Liouville: Dense Image of Entire Functions

## Key Idea / Intuition

The Open Mapping Theorem says that a non-constant holomorphic map sends open sets to open sets. But $\mathbb{C}$ is itself open — so the image $f(\mathbb{C})$ must be open. If the image also omits an open disk, you can build a bounded entire function, and Liouville kills it.

The beautiful engine here: **open image + missing open set → bounded entire function → Liouville → constant**. Three big theorems chained in two lines.

---

## Formal Proof / Solution

**Step 1: The image $f(\mathbb{C})$ is open.**

Since $f$ is non-constant and entire (hence holomorphic), the **Open Mapping Theorem** guarantees that $f$ maps open sets to open sets. Since $\mathbb{C}$ is open, $f(\mathbb{C})$ is an open subset of $\mathbb{C}$.

**Step 2: If $f(\mathbb{C})$ omits an open disk, construct a bounded entire function.**

Suppose $f(\mathbb{C}) \cap D(w_0, r) = \emptyset$ for some $w_0 \in \mathbb{C}$ and $r > 0$. This means:
$$|f(z) - w_0| \geq r \quad \text{for all } z \in \mathbb{C}.$$

Define:
$$g(z) = \frac{1}{f(z) - w_0}.$$

Since $f(z) - w_0$ is never zero (it has modulus $\geq r > 0$ everywhere), $g$ is entire. Moreover:
$$|g(z)| = \frac{1}{|f(z) - w_0|} \leq \frac{1}{r} \quad \text{for all } z \in \mathbb{C}.$$

So $g$ is a **bounded entire function**.

**Step 3: Apply Liouville's Theorem.**

By **Liouville's Theorem**, $g$ must be constant. But then $f(z) = w_0 + \frac{1}{g(z)}$ is also constant — contradicting our assumption that $f$ is non-constant. $\contradiction$

**Conclusion:** The image of a non-constant entire function $f(\mathbb{C})$ is dense in $\mathbb{C}$ — it cannot avoid any open set.

---

**Bonus: What about $e^z$?**

The function $e^z$ is non-constant and entire, so its image is dense. In fact $e^z$ omits exactly the point $0$ (since $e^z \neq 0$ for all $z$). This is consistent: omitting a *single point* is not enough to contradict Liouville (you can't build a bounded function from $\frac{1}{e^z - 0} = e^{-z}$, which is itself entire but unbounded). Little Picard sharpens this: a non-constant entire function omits **at most one** value — and $e^z$ shows the bound is tight.

---

**The chain of ideas:**

$$\text{Open Mapping} \implies f(\mathbb{C}) \text{ open} \implies \text{missing open disk} \implies \frac{1}{f-w_0} \text{ bounded entire} \xrightarrow{\text{Liouville}} \text{constant.}$$
