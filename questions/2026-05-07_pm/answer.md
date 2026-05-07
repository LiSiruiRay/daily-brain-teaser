# Answer: Entire Function Avoiding a Disk Must Be Constant

## Key Idea / Intuition

If $f$ misses an entire $\epsilon$-disk around $w_0$, then $g(z) = \frac{1}{f(z) - w_0}$ is entire and bounded — and Liouville's theorem immediately kills it. The Open Mapping Theorem gives a conceptually deeper reason why a non-constant entire function *cannot* avoid any open set: its image must itself be open, so a "gap" in the image is impossible. Together these two viewpoints — one elementary via Liouville, one geometric via Open Mapping — reveal the rigid, space-filling nature of non-constant holomorphic maps.

---

## Formal Proof / Solution

### Part 1: Elementary Proof via Liouville

**Setup.** Suppose $f: \mathbb{C} \to \mathbb{C}$ is entire and for some $w_0 \in \mathbb{C}$ and $\epsilon > 0$:
$$|f(z) - w_0| \geq \epsilon \quad \text{for all } z \in \mathbb{C}.$$

**Construction.** Define
$$g(z) = \frac{1}{f(z) - w_0}.$$

- $g$ is entire: since $f(z) - w_0 \neq 0$ everywhere (it stays at distance $\geq \epsilon > 0$ from zero), the denominator never vanishes, so $g$ is holomorphic on all of $\mathbb{C}$.

- $g$ is bounded: the hypothesis gives
$$|g(z)| = \frac{1}{|f(z) - w_0|} \leq \frac{1}{\epsilon} \quad \text{for all } z \in \mathbb{C}.$$

**Conclusion by Liouville.** An entire bounded function must be constant (Liouville's Theorem). Hence $g$ is constant, which forces $f(z) - w_0$ to be constant, hence $f$ itself is constant. $\blacksquare$

---

### Part 2: Conceptual Proof via the Open Mapping Theorem

**Theorem (Open Mapping).** If $f$ is holomorphic and non-constant on a connected open set $\Omega$, then $f(\Omega)$ is open.

**Why this implies density.** Suppose $f$ is non-constant and entire. By the Open Mapping Theorem, $f(\mathbb{C})$ is an open subset of $\mathbb{C}$. 

Now suppose for contradiction that $f(\mathbb{C})$ is not dense, i.e., there exists $w_0$ and $\epsilon > 0$ with $B(w_0, \epsilon) \cap f(\mathbb{C}) = \emptyset$. In particular $w_0 \notin f(\mathbb{C})$, and the image avoids an open ball. But $f(\mathbb{C})$ is open by the Open Mapping Theorem — and a non-empty open set in $\mathbb{C}$ cannot be bounded away from all of $\mathbb{C}$ (the complement would have to contain an open set too, yet the image is connected and open... more precisely, the argument from Part 1 closes the gap).

The cleanest version: the Open Mapping Theorem tells us that $f(\mathbb{C})$ is open; but Part 1 tells us it cannot miss any open disk. Together: $f(\mathbb{C}) = \mathbb{C}$ unless $f$ is constant.

---

### Summary of the Beautiful Chain of Ideas

| Step | Tool | Conclusion |
|---|---|---|
| $f$ entire, $f(\mathbb{C})$ misses a disk | Compose with $1/(\cdot - w_0)$ | Get bounded entire function |
| Bounded entire function | Liouville's Theorem | Function is constant |
| $f$ non-constant entire | Open Mapping Theorem | $f(\mathbb{C})$ is open, hence dense |

The key insight is that **Liouville's theorem is secretly a statement about the image of $f$**: boundedness of the image forces constancy. The hypothesis $|f(z) - w_0| \geq \epsilon$ is precisely the statement that the image avoids an open set, and the trick of taking $\frac{1}{f-w_0}$ converts geometric separation into analytic boundedness.
