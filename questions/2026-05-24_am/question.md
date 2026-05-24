---
name: "The Double Descent Puzzle"
type: "ML/Stats"
tags: ["double descent", "overparameterization", "minimum norm", "implicit regularization", "bias-variance", "pseudoinverse"]
date: "2026-05-24"
solved: false
comments: ""
related: []
redo: 0
difficulty: 3
source: "The Elements of Statistical Learning, Ch. 7; Hastie et al. 2022"
---
# The Double Descent Puzzle

You are training a linear regression model with $p$ parameters on $n$ training points, using ordinary least squares (OLS). Assume the features are in "general position" (no perfect multicollinearity).

**(a)** What happens to the **training error** as $p$ increases from $1$ to $n-1$? What happens at $p = n$? What about $p > n$?

**(b)** Classical statistical wisdom says: "more parameters → more overfitting → worse test error." Yet modern deep learning routinely uses models with $p \gg n$ and achieves *excellent* test performance. How can this be reconciled?

In particular: in the **overparameterized regime** $p > n$, there are infinitely many zero-training-error solutions. Which one does gradient descent (or the pseudoinverse) select, and why does that choice matter for generalization?
