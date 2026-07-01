---
name: "The Secretary Who Knows the Distribution"
type: "Probability"
tags: ["optimal stopping", "secretary problem", "threshold strategy", "uniform distribution", "1/e"]
date: "2026-07-01"
solved: false
comments: ""
related: []
redo: 0
difficulty: 3
source: "Fifty Challenging Problems in Probability with Solutions, Frederick Mosteller, Problem 48"
---
# The Secretary Who Knows the Distribution

You interview candidates one by one. Their quality scores are drawn independently and uniformly from $[0,1]$. You must accept or reject each candidate immediately and irrevocably. You know the distribution (uniform on $[0,1]$) and want to **maximize the probability of hiring the best candidate** out of $n = 2$.

**With only 2 candidates**, what is the optimal strategy, and what is your probability of success?

Now generalize: with $n$ candidates, the optimal threshold strategy (accept candidate $k$ if their score exceeds some threshold $t_k$) gives a success probability that approaches what limit as $n \to \infty$?
