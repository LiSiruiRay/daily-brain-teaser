---
name: "Poisson's Log-Cosine Integral"
type: "Integration"
tags: ["mean value property", "roots of unity", "Riemann sums", "Jensen's formula", "harmonic functions"]
date: "2026-10-31"
solved: false
comments: ""
related: []
redo: 0
difficulty: 3
source: "Classical (Poisson's integral); folklore integration-bee staple"
---
# Poisson's Log-Cosine Integral

Let $a$ be a real number with $|a| \neq 1$. Evaluate

$$
I(a) \;=\; \int_0^{\pi} \ln\!\left(1 - 2a\cos x + a^2\right)\,dx .
$$

Your answer should depend on whether $|a|<1$ or $|a|>1$.

*Hint (try without it first):* Factor $1 - 2a\cos x + a^2$ over $\mathbb{C}$.

**Bonus:** What happens at $a = 1$, where the integrand has a logarithmic singularity at $x=0$?

---

**Field:** Integration / Complex analysis

**Why it's interesting:** Direct antidifferentiation gets nowhere. After one factorization, the integral turns out to be "secretly" an average of a harmonic function over a circle. The answer is then a striking dichotomy: exactly $0$ inside the unit disk and $2\pi\ln|a|$ outside it. It is the prototype of Jensen's formula. It also has a completely elementary second proof using roots of unity and Riemann sums.

**Difficulty:** 3 / 5
