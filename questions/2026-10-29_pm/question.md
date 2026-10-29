---
name: "The Function Polynomials Cannot Reach"
type: "Complex Analysis"
tags: ["uniform approximation", "Cauchy's theorem", "Runge's theorem", "pole pushing", "maximum principle"]
date: "2026-10-29"
solved: false
comments: ""
related: []
redo: 0
difficulty: 2
source: "Stein & Shakarchi, Complex Analysis, Ch. 2 §5.4 (Runge approximation theorem)"
---
# The Function Polynomials Cannot Reach

Weierstrass tells us that every continuous function on $[-1,1]$ is a uniform limit of polynomials. Now move to the complex plane.

Let $\mathbb{T} = \{z \in \mathbb{C} : |z| = 1\}$ be the unit circle, and consider the continuous function $f(z) = \bar z$ on $\mathbb{T}$.

**(a)** Prove that there is **no** sequence of complex polynomials $p_n(z)$ with
$$
\sup_{|z|=1} |p_n(z) - \bar z| \longrightarrow 0.
$$

**(b) (Twist)** Now remove a small open arc from the circle. Let $K = \{e^{i\theta} : \delta \le \theta \le 2\pi - \delta\}$ for some $\delta > 0$. Show that on $K$, $\bar z$ **is** a uniform limit of polynomials in $z$.

What exactly changed?

---

**Field:** Complex Analysis (approximation theory)

**Why it's interesting:** Real intuition says "continuous functions on nice compact sets are uniform limits of polynomials." The complex plane says no. The obstruction is a *hole*: the circle encloses a region that polynomials "see," and the function $\bar z$ cannot be extended holomorphically into it. Cutting a tiny gap in the circle removes the obstruction. This is the simplest instance of **Runge's theorem**, and the proof of (a) is one line once you find the right test.

**Difficulty:** 2.5 / 5

**Tags:** uniform approximation, Cauchy's theorem, Runge's theorem, pole pushing
