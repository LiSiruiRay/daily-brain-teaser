---
name: "Expected Fixed Points of a Random Permutation"
type: "Putnam"
tags: ["linearity of expectation", "permutations", "fixed points", "combinatorics", "elegant surprise"]
date: "2026-09-18"
solved: false
comments: ""
related: []
redo: 0
difficulty: 2
source: "Mathematical folklore / Putnam warmup"
---
# The Permutation That Avoids Its Own Position

Let $S_n$ be the set of all permutations of $\{1, 2, \ldots, n\}$. For a permutation $\sigma \in S_n$, say that $i$ is a **fixed point** if $\sigma(i) = i$.

Now consider all permutations $\sigma \in S_n$ and look at $\sum_{\sigma \in S_n} (\text{number of fixed points of } \sigma)$.

**Compute this sum.** Then use it to find the **expected number of fixed points** of a uniformly random permutation of $\{1, \ldots, n\}$.

Does the answer surprise you?
