---
name: "A Sequence That Always Hits a Perfect Square"
type: "Putnam"
tags: ["sequences", "perfect squares", "number theory", "fixed points", "parity argument"]
date: "2026-06-12"
solved: false
comments: ""
related: []
redo: 0
difficulty: 2
source: "Putnam 1991, Problem B-1"
---
# A Sequence That Always Hits a Perfect Square

Define a sequence $(a_k)_{k=0}^{\infty}$ as follows. Let $S(n) = n - m^2$, where $m$ is the greatest integer with $m^2 \leq n$. (So $S(n)$ is the "remainder" when you subtract the largest perfect square $\leq n$.)

Set $a_0 = A$ (a positive integer), and

$$a_{k+1} = a_k + S(a_k), \quad k \geq 0.$$

**For which positive integers $A$ does this sequence eventually become constant?**

*(The sequence is constant once it reaches some value and stays there forever.)*
