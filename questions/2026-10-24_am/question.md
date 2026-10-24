---
name: "The Integral That Only Cares About the Ratio"
type: "Integration"
tags: ["homogeneity", "tan substitution", "trigonometric integral", "Beta function", "integration bee"]
date: "2026-10-24"
solved: false
comments: ""
related: []
redo: 0
difficulty: 2
---
# The Integral That Only Cares About the Ratio

Evaluate

$$
I \;=\; \int_0^{\pi/2} \frac{dx}{\left(\sqrt{\sin x}+\sqrt{\cos x}\right)^4}.
$$

*Hint:* Count the "degree" of the integrand in $(\sin x,\cos x)$.

**Bonus.** For $p>0$, show that

$$
\int_0^{\pi/2} \frac{dx}{\left(\sin^p x+\cos^p x\right)^{2/p}} \;=\; \frac{1}{p}\,B\!\left(\tfrac1p,\tfrac1p\right),
$$

and check this against the cases $p=1$, $p=2$, and $p=\tfrac12$.

---

**Field:** Integration (integration bee)

**Why it's interesting:** The integrand looks unpleasant: square roots of trig functions raised to the fourth power. But it has a hidden structure. It is *homogeneous of degree $-2$* in $(\sin x,\cos x)$. Because $\sec^2 x\,dx = d(\tan x)$ also has degree $-2$, the whole integral depends only on the ratio $t=\tan x$. The square roots then disappear after a single substitution, and the integral reduces to a rational function.

**Key technique:** Use a homogeneity / ratio substitution. Divide by $\cos^2 x$, set $t=\tan x$, then set $u=\sqrt t$.

**Difficulty:** 2 / 5

**Tags:** trigonometric substitution, homogeneity, Weierstrass-free tan substitution, Beta function
