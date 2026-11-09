---
name: "There Is No Slowest Divergent Series"
type: "analysis"
tags: ["infinite series", "Abel–Dini theorem", "Cauchy criterion", "telescoping", "comparison test"]
date: "2026-11-09"
solved: false
comments: ""
related: []
redo: 0
difficulty: 2
source: "Rudin, Principles of Mathematical Analysis, Ch. 3, Exercise 11 (Abel–Dini theorem); cited from memory, not from the materials folder"
---
# There Is No Slowest Divergent Series

Let $a_n > 0$ for all $n$, and suppose $\displaystyle\sum_{n=1}^\infty a_n$ **diverges**. Write
$$S_n = a_1 + a_2 + \cdots + a_n,$$
so that $S_n \uparrow \infty$.

**(a)** Prove that
$$\sum_{n=1}^\infty \frac{a_n}{S_n} \quad\text{also diverges.}$$

**(b)** Prove that
$$\sum_{n=1}^\infty \frac{a_n}{S_n^{2}} \quad\text{converges.}$$

**(c)** *(Philosophical punchline.)* Explain why (a) shows that **no divergent series diverges "most slowly"**. More precisely, for every divergent positive series $\sum a_n$ there is a divergent positive series $\sum b_n$ with $b_n/a_n \to 0$.

*Bonus:* Show more generally that $\sum a_n / S_n^{1+\varepsilon}$ converges for every $\varepsilon > 0$.

---

**Field:** Real analysis (infinite series)

**Why it's interesting:** Partial sums of a divergent series can grow arbitrarily slowly: like $\log n$, or $\log\log n$, or slower still. One might hope to find a "boundary" series sitting exactly at the edge between convergence and divergence, and use it as a universal comparison test. This problem shows that no such boundary exists. Dividing by $S_n$ always produces something that still diverges but does so more slowly. The proof needs only one line of Cauchy-criterion reasoning.

**Difficulty:** 2 / 5
