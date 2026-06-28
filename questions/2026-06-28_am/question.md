---
name: "The Wisdom of Crowds: When Does Averaging Hurt?"
type: "ML/Stats"
tags: ["ensemble methods", "majority vote", "correlation", "law of large numbers", "bias-variance"]
date: "2026-06-28"
solved: false
comments: ""
related: []
redo: 0
difficulty: 2
source: "The Elements of Statistical Learning, Ch. 8 (Hastie, Tibshirani, Friedman)"
---
# The Wisdom of Crowds: When Does Averaging Hurt?

You have $B$ independent classifiers, each achieving accuracy $p$ on a binary classification problem (labels $\{-1, +1\}$). You form a majority-vote ensemble.

**Part (a):** If $p > 1/2$, show that as $B \to \infty$ (odd), the ensemble accuracy approaches $1$.

**Part (b) (the twist):** Now suppose the $B$ classifiers are **not** independent, but instead all share a common "error core": with probability $\rho$, all classifiers are simultaneously wrong; with probability $1 - \rho$, each makes an independent error with probability $q < 1/2$.

For large $B$, what does the majority-vote accuracy converge to? 

In particular, show there is a **hard ceiling** on ensemble accuracy that averaging can never break, no matter how many classifiers you add. What is it?

*(Assume for simplicity that $q \to 0$ so individual errors outside the shared core vanish.)*
