---
name: "Weierstrass Series: Continuity via Abel Summation"
type: "analysis"
tags: ["uniform convergence", "Dirichlet test", "Abel summation", "Weierstrass function", "continuity"]
date: "2026-05-18"
solved: false
comments: ""
related: []
redo: 0
difficulty: 4
---
# The Weierstrass M-Test and a Tricky Series

Define the function

$$f(x) = \sum_{n=1}^{\infty} \frac{\sin(n^2 x)}{n^2}$$

**(a)** Prove that $f$ is continuous on $\mathbb{R}$.

**(b)** Prove that $f$ is differentiable **nowhere**.

Wait — actually, part (b) is false! The series $\sum \frac{\sin(n^2 x)}{n^2}$ *is* differentiable (in fact $C^\infty$) everywhere.

Here is the real question:

> **True or False, and prove it:** The function
> $$g(x) = \sum_{n=1}^{\infty} \frac{\sin(n^2 x)}{n^{1/2}}$$
> is continuous on $\mathbb{R}$.

And the follow-up:

> Can you construct a series $\sum a_n \sin(n^2 x)$ that is continuous but **not** differentiable anywhere? What is the threshold on the decay rate of $a_n$?

Focus on: **Is $g$ well-defined and continuous?** Prove your answer carefully.
