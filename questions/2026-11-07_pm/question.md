---
name: "The Exponential That Hides a Product Rule"
type: "Integration"
tags: ["product rule in reverse", "e^x(f+f') trick", "ansatz", "integration bee"]
date: "2026-11-07"
solved: false
comments: ""
related: []
redo: 0
difficulty: 2
---
# The Exponential That Hides a Product Rule

Evaluate

$$
I \;=\; \int_0^1 e^x\,\frac{x^2+1}{(x+1)^2}\,dx .
$$

*(No series and no numerical approximation. The answer is a small integer.)*

**Field:** Integration (calculus)

**Why it's interesting:** This is a standard integration-bee trap. Integration by parts or partial fractions turns into a mess involving the exponential integral $\operatorname{Ei}$. The integrand is in fact an exact derivative in disguise, and once you see that, the problem takes one line. The trick is the identity $\frac{d}{dx}\big(e^x f(x)\big)=e^x\big(f(x)+f'(x)\big)$. It shows up often in contests and has a neat interpretation in terms of operators.

**Difficulty:** 2 / 5

**Tags:** product rule in reverse, $e^x(f+f')$ trick, ansatz, integration bee
