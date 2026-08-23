---
name: "The Logistic Regression Coefficient That Goes to Infinity"
type: "ML/Stats"
tags: ["logistic regression", "MLE", "separability", "optimization", "implicit bias", "regularization"]
date: "2026-08-23"
solved: false
comments: ""
related: []
redo: 0
difficulty: 2
source: "The Elements of Statistical Learning, Hastie, Tibshirani, Friedman — Chapter 4 (Linear Methods for Classification)"
---
# The Logistic Regression Coefficient That Goes to Infinity

Suppose you are fitting a logistic regression model to a binary classification dataset in $\mathbb{R}^p$ using maximum likelihood estimation (via gradient ascent or Newton's method). The dataset is **linearly separable**: there exists a hyperplane $w^\top x = 0$ such that all class-1 points satisfy $w^\top x > 0$ and all class-0 points satisfy $w^\top x < 0$.

**Question:** What happens to the maximum likelihood estimate $\hat{\beta}$ as training proceeds? Does the MLE exist? What does the log-likelihood surface look like, and what does this imply about convergence of the algorithm?
