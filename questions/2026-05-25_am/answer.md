# Answer: Lebesgue Differentiation: Failure Everywhere?

## Key Idea / Intuition

The Lebesgue Differentiation Theorem is rock-solid: for **any** $L^1_{\mathrm{loc}}$ function, the averaging limit equals $f(x)$ at *almost every* point — no measurable function can escape this. The most extreme example of "failure everywhere" is simply impossible. However, the theorem leaves open a **measure-zero** set of exceptional points, and with a clever construction you can make the limit exist but differ from $f$ on a measure-zero set (e.g., at a jump discontinuity, the limit is the average of left and right limits). The bonus reveals a genuine subtlety: non-symmetric intervals can break the theorem even at Lebesgue points.

---

## Formal Proof / Solution

### Part 1: Cannot Fail Everywhere

**Claim:** No bounded measurable $f$ can have its Lebesgue averages disagree with $f(x)$ at *every* $x$.

**Proof:** By the Lebesgue Differentiation Theorem, for any $f \in L^1_{\mathrm{loc}}(\mathbb{R})$,

$$\frac{1}{2r}\int_{x-r}^{x+r} f(t)\,dt \to f(x) \quad \text{for a.e. } x.$$

Since "almost every" means the exceptional set has Lebesgue measure zero, and $\mathbb{R}$ has infinite measure, the set where the limit equals $f(x)$ is **co-null** (complement has measure zero). In particular, it is **dense** (in fact full measure). So failure at *every* point is impossible. $\blacksquare$

---

### Part 2: The Extremal Example — Failure on a Measure-Zero Set

Consider $f = \mathbf{1}_{[0,\infty)}$, the Heaviside step function. Then:

- For $x > 0$: the average over $[x-r, x+r]$ is $1$ for small $r$, and $f(x) = 1$. ✓  
- For $x < 0$: the average is $0$ for small $r$, and $f(x) = 0$. ✓  
- For $x = 0$: 

$$\frac{1}{2r}\int_{-r}^{r} \mathbf{1}_{[0,\infty)}(t)\,dt = \frac{1}{2r} \cdot r = \frac{1}{2} \neq f(0) = 1.$$

So the limit **exists** at $x = 0$ but equals $\tfrac{1}{2} \neq f(0)$. This is the classic example: at a **jump discontinuity**, the symmetric averaging limit gives the *midpoint* of the jump, not the function value.

The takeaway: the Lebesgue Differentiation Theorem guarantees correctness a.e., but the function's value at a single point (a measure-zero set) is invisible to the integral — you can freely redefine $f$ on a null set without changing any integral. The theorem recovers the *equivalence class representative* in a canonical sense.

---

### Bonus: Non-Symmetric Intervals Can Fail at Lebesgue Points

Replace $[x-r, x+r]$ with $[x, x+r]$ (one-sided average). Then the one-sided derivative

$$\lim_{r\to 0} \frac{1}{r}\int_x^{x+r} f(t)\,dt$$

still equals $f(x)$ at a.e. $x$ (by the same theorem applied to one-sided balls).

But consider a **genuinely non-symmetric** family of intervals, e.g., $[x - r^2, x + r]$. The ratio of left-to-right length tends to $0$, so effectively this is a one-sided limit. For the Heaviside function at $x = 0$:

$$\frac{1}{r^2 + r}\int_{-r^2}^{r} \mathbf{1}_{[0,\infty)}\,dt = \frac{r}{r^2 + r} = \frac{1}{1+r} \to 1 = f(0^+),$$

which now recovers the **right-hand limit**, not the symmetric average $\tfrac{1}{2}$.

More dramatically, using the **Busemann–Feller–Morse theorem**, there exist *differentiation bases* (families of sets shrinking to a point) for which the differentiation theorem **fails** even for continuous functions — the geometry of the sets matters deeply. This is why the theorem is stated for **balls** (or nicely shaped sets with bounded eccentricity).

---

### Summary Table

| Scenario | Does limit $= f(x)$ a.e.? |
|---|---|
| Symmetric intervals $[x-r,x+r]$ | ✓ Yes (LDT) |
| One-sided intervals $[x, x+r]$ | ✓ Yes (LDT) |
| Badly shaped/non-symmetric basis | ✗ Can fail |
| Failure at **every** point | ✗ Impossible |
