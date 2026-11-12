---
name: "How Many Zeros Can a Bounded Function Afford?"
type: "Complex Analysis"
tags: ["Blaschke factors", "maximum modulus principle", "Jensen's formula", "zero counting", "unit disk"]
date: "2026-11-12"
solved: false
comments: ""
related: []
redo: 0
difficulty: 3
source: "Inspired by Stein & Shakarchi, Complex Analysis, Ch. 5 §1 (Jensen's formula)"
---
# How Many Zeros Can a Bounded Function Afford?

Let $f$ be holomorphic on the open unit disk $\mathbb{D}=\{|z|<1\}$ with

$$|f(z)| \le 2 \quad \text{for all } z\in\mathbb{D}, \qquad f(0)=1.$$

**(a)** Prove that $f$ has **at most one zero**, counted with multiplicity, in the closed disk $\{|z|\le \tfrac12\}$.

**(b)** Show that the bound is sharp. That is, exhibit such an $f$ with exactly one zero in $\{|z|\le\tfrac12\}$.

**(c) Bonus.** Suppose instead $|f|\le M$ on $\mathbb{D}$, $|f(0)|=1$, and $0<r<1$. Show that the number of zeros in $\{|z|\le r\}$ is at most
$$\frac{\log M}{\log(1/r)}.$$

*Hint-free version:* try it before reading further. One well-chosen division does all the work.
