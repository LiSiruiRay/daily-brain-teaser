---
name: "The Integrable Function Whose Integral Vanishes on Every Interval"
type: "analysis"
tags: ["Lebesgue differentiation theorem", "measure theory", "locally integrable", "vanishing integrals"]
date: "2026-07-27"
solved: false
comments: ""
related: []
redo: 0
difficulty: 2
---
# The Integrable Function Whose Integral Vanishes on Every Interval

Suppose $f: \mathbb{R} \to \mathbb{R}$ is locally integrable (i.e., integrable on every bounded interval), and satisfies

$$\int_a^b f(x)\, dx = 0 \quad \text{for every } a < b.$$

Must $f = 0$ almost everywhere?

Now suppose instead we only know that

$$\int_0^x f(t)\, dt = 0 \quad \text{for every } x \geq 0,$$

with $f$ locally integrable on $[0,\infty)$.

Does the same conclusion hold?

Finally: what if $f$ is merely assumed to be in $L^1_{\text{loc}}$ but the vanishing condition is changed to

$$\int_E f\, d\mu = 0 \quad \text{for every measurable set } E \subseteq [0,1]?$$

Prove the conclusion in each case, or give a counterexample.
