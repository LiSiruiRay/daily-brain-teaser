---
name: "The Ballot Box Surprise: Two Candidates, One Mystery"
type: "Probability"
tags: ["ballot problem", "reflection principle", "cycle lemma", "combinatorics", "lattice paths", "sampling without replacement"]
date: "2026-07-08"
solved: false
comments: ""
related: []
redo: 0
difficulty: 3
source: "Fifty Challenging Problems in Probability with Solutions, Frederick Mosteller (related theme); Classical Ballot Theorem (Bertrand 1887)"
---
# The Ballot Box Surprise: Two Candidates, One Mystery

An urn contains $r$ red balls and $b$ blue balls, with $r > b$. You draw balls one at a time **without replacement**, noting the running total. At each step, let $R_k$ and $B_k$ denote the number of red and blue balls drawn after $k$ draws.

**Question:** What is the probability that red stays **strictly ahead** of blue (i.e., $R_k > B_k$ for every $k = 1, 2, \ldots, r+b$) throughout the entire drawing?

In other words: what fraction of orderings of the $r+b$ balls keep red strictly in the lead from start to finish?

**Hint:** Think about this combinatorially — you are asking about paths on a grid.
