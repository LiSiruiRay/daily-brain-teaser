# Answer: The Absolutely Continuous Function That Forgets Its Derivative

## Key Idea / Intuition

The key point is that absolute continuity lets us use the **Fundamental Theorem of Lebesgue integration**: $f(x) = \int_0^x f'(t)\,dt$. Once we have this, the condition $f' = f$ a.e. turns the functional equation $f(x) = \int_0^x f(t)\,dt$ into a Gronwall-type inequality. Gronwall's inequality (or a simple iteration argument) then forces $f \equiv 0$ — the function is "too small to be nonzero."

---

## Formal Proof / Solution

**Step 1: Use absolute continuity.**

Since $f$ is absolutely continuous and $f(0)=0$, by the Lebesgue FTC:
$$f(x) = \int_0^x f'(t)\,dt = \int_0^x f(t)\,dt \quad \text{for all } x \in [0,1].$$

**Step 2: Bound $|f|$.**

Let $M = \sup_{x \in [0,1]} |f(x)|$. Since $f$ is continuous (absolute continuity implies continuity) on a compact set, $M < \infty$. Then for all $x \in [0,1]$:
$$|f(x)| \leq \int_0^x |f(t)|\,dt \leq M \cdot x.$$

**Step 3: Iterate the estimate.**

Substitute this improved bound back:
$$|f(x)| \leq \int_0^x M \cdot t \,dt = M \cdot \frac{x^2}{2}.$$

Iterate $n$ times:
$$|f(x)| \leq M \cdot \frac{x^n}{n!}.$$

**Step 4: Conclude.**

For any fixed $x \in [0,1]$, taking $n \to \infty$:
$$|f(x)| \leq M \cdot \frac{1}{n!} \to 0.$$

Therefore $f(x) = 0$ for all $x \in [0,1]$. $\blacksquare$

---

**Remark (why AC is essential):** A function that is merely differentiable a.e. with $f' = f$ a.e. could potentially be pathological — for instance, the Cantor function has $f' = 0$ a.e. but is not identically zero, precisely because it is **not** absolutely continuous. Absolute continuity is exactly the condition that makes the Lebesgue FTC valid, tying $f$ to its derivative via an integral.
