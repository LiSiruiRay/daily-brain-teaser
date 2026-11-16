---
name: "Barbalat's Lemma: When Does an Integrable Function Have to Die Out?"
type: "analysis"
tags: ["improper integrals", "uniform continuity", "counterexample", "Cauchy criterion", "Barbalat's lemma"]
date: "2026-11-16"
solved: false
comments: ""
related: []
redo: 0
difficulty: 2
---
# Barbalat's Lemma: When Does an Integrable Function Have to Die Out?

Let $f:[0,\infty)\to\mathbb{R}$ be continuous, and suppose the improper integral
$$\int_0^\infty f(x)\,dx = \lim_{T\to\infty}\int_0^T f(x)\,dx$$
exists and is finite.

**(a)** Show that this does **not** force $f(x)\to 0$. Find a continuous, **nonnegative** $f$ with $\int_0^\infty f<\infty$ but $\limsup_{x\to\infty} f(x) = \infty$.

**(b)** Prove that if $f$ is additionally **uniformly continuous** on $[0,\infty)$, then
$$\lim_{x\to\infty} f(x) = 0.$$

*(Bonus thought: $\int_0^\infty \sin(x^2)\,dx$ converges, yet $\sin(x^2)\not\to 0$. Which hypothesis of (b) fails?)*

---

**Field:** Real analysis

**Why it's interesting:** Everyone's first instinct is "if the area is finite, the function must go to zero," which is the continuous analogue of "if $\sum a_n$ converges then $a_n\to 0$." The analogue fails, because a function can hide arbitrarily tall spikes in arbitrarily thin intervals. Uniform continuity is exactly the hypothesis that forbids thin spikes. The result is known as **Barbalat's lemma**, and it is a workhorse in control theory: it is how one upgrades "a Lyapunov function has a finite limit" to "the state actually converges."

**Difficulty:** 2 / 5
