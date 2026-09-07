# Answer: Uniform Limit of Derivatives via Integration

## Key Idea / Intuition

Uniform convergence alone is not enough to swap limits and derivatives — differentiability is a *local* property that requires controlling difference quotients, and uniform convergence only controls function values. However, integration is much more forgiving: uniform convergence *does* pass through integrals, and since a function is recovered from its derivative by the Fundamental Theorem of Calculus, we can bootstrap this to conclude differentiability when the *derivatives* also converge uniformly.

---

## Formal Proof / Solution

### Part (a): Counterexample

Uniform convergence does **not** preserve differentiability.

**Counterexample:** Let
$$f_n(x) = \sqrt{x^2 + \tfrac{1}{n}}.$$
Each $f_n$ is smooth on $[0,1]$, and
$$|f_n(x) - |x|| = \sqrt{x^2 + \tfrac{1}{n}} - |x| = \frac{1/n}{\sqrt{x^2+1/n}+|x|} \leq \frac{1/n}{\sqrt{1/n}} = \frac{1}{\sqrt{n}} \to 0$$
uniformly. So $f_n \to f = |\cdot|$ uniformly on $[0,1]$, but $f(x) = x$ is not differentiable at $x = 0$.

---

### Part (b): Uniform convergence of derivatives implies differentiability of the limit

**Setup.** We know:
- $f_n \rightrightarrows f$ uniformly on $[0,1]$,
- $f_n' \rightrightarrows g$ uniformly on $[0,1]$.

**Step 1: Integrate $f_n'$.**

By the Fundamental Theorem of Calculus, for each $n$ and each $x \in [0,1]$:
$$f_n(x) - f_n(0) = \int_0^x f_n'(t)\, dt.$$

**Step 2: Pass to the limit using uniform convergence.**

Since $f_n' \rightrightarrows g$ uniformly, we can pass the limit inside the integral:
$$\int_0^x f_n'(t)\, dt \to \int_0^x g(t)\, dt \quad \text{uniformly in } x.$$

Since $f_n(x) \to f(x)$ and $f_n(0) \to f(0)$, taking $n \to \infty$ gives:
$$f(x) - f(0) = \int_0^x g(t)\, dt.$$

**Step 3: Conclude differentiability.**

The right-hand side is the integral of a continuous function $g$ (uniform limit of continuous functions is continuous). By the Fundamental Theorem of Calculus:
$$f'(x) = g(x) \quad \text{for all } x \in [0,1].$$

Thus $f$ is (continuously) differentiable and $f' = g$. $\blacksquare$

---

### Summary of the Trick

| Question | Answer |
|---|---|
| $f_n \rightrightarrows f$ implies $f$ differentiable? | **No** — counterexample: $\sqrt{x^2+1/n} \to |x|$ |
| $f_n \rightrightarrows f$ and $f_n' \rightrightarrows g$ implies $f' = g$? | **Yes** — integrate $f_n'$, swap limit and integral, differentiate |

The moral: **to prove a derivative statement, integrate first, then differentiate.** This is a recurring theme in analysis — integration is the robust operation that tolerates limit-swapping, while differentiation is fragile.
