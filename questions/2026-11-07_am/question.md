---
name: "The Integral That Only Sees the Tangent"
type: "Integration"
tags: ["homogeneity", "tangent substitution", "trigonometric integral", "Beta function", "integration bee"]
date: "2026-11-07"
solved: false
comments: ""
related: []
redo: 0
difficulty: 2
---
# The Integral That Only Sees the Tangent

Evaluate

$$
I \;=\; \int_0^{\pi/2} \frac{dx}{\left(\sqrt{\sin x}+\sqrt{\cos x}\right)^{4}} .
$$

*Warm-up variant:* for $a,b>0$, show that

$$
\int_0^{\pi/2} \frac{dx}{(a\sin x + b\cos x)^2} = \frac{1}{ab}.
$$

---

**Field:** Integration (integration bee)

**Why it's interesting:**
The integrand looks unfriendly because of the square roots of $\sin$ and $\cos$. It is also symmetric under $x \mapsto \tfrac{\pi}{2}-x$, so King's rule leaves it unchanged and gives nothing. The integral becomes easy once you notice one structural fact. The denominator is homogeneous of degree $2$ in the pair $(\sin x,\cos x)$. Any such integrand depends on $x$ only through $\tan x$, apart from a factor $\sec^2 x$, and $\sec^2 x\,dx$ is exactly $d(\tan x)$. After that substitution the answer is a small rational number.

**Key trick (brief):** Divide the numerator and denominator by $\cos^2 x$, then substitute $u=\tan x$ and $u=t^2$.

**Difficulty:** 2 / 5

**Tags:** homogeneity, tangent substitution, trigonometric integrals, Beta function
