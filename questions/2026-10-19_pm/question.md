---
name: "The Derivative That Drags Its Function Along"
type: "analysis"
tags: ["integrating factor", "L'Hopital's rule", "asymptotics", "ODE stability", "limits"]
date: "2026-10-19"
solved: false
comments: ""
related: []
redo: 0
difficulty: 2
source: "G. H. Hardy, A Course of Pure Mathematics (classic exercise); cf. W. Rudin, Principles of Mathematical Analysis, Thm 5.13"
---
# The Derivative That Drags Its Function Along

Let $f:\mathbb{R}\to\mathbb{R}$ be differentiable, and suppose

$$\lim_{x\to\infty}\big(f(x)+f'(x)\big)=L \qquad (L\in\mathbb{R}).$$

**Prove** that

$$\lim_{x\to\infty} f(x)=L \qquad\text{and}\qquad \lim_{x\to\infty} f'(x)=0.$$

**Follow-up (think for 30 seconds each):**
1. Does the same conclusion hold if $f(x)+f''(x)\to 0$?
2. Does it hold if $f(x)-f'(x)\to 0$?
3. What about $f(x)+2f'(x)\to L$?

---

**Field:** Real analysis (differentiation, limits)

**Why it's interesting / classic:**
The hypothesis controls only a *combination* of $f$ and $f'$. Neither $f$ nor $f'$ is assumed to converge, and one could imagine them oscillating against each other. They cannot. The equation $y+y'=g$ is a damped first-order system, and the damping forces $f$ to settle. This is a well-known exercise from G. H. Hardy's *A Course of Pure Mathematics*. It is a model example of the **integrating factor** idea in a pure-analysis setting, and it shows a sharp version of L'Hôpital's rule at work.

**Difficulty:** 2 / 5

**Tags:** integrating factor, L'Hôpital's rule, asymptotics, Hardy
