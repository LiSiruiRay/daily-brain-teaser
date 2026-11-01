---
name: "The Cross-Validation That Peeked: Screening Before the Folds"
type: "ML/Stats"
tags: ["cross-validation", "feature selection", "selection bias", "data leakage", "high-dimensional"]
date: "2026-11-01"
solved: false
comments: ""
related: []
redo: 0
difficulty: 2
source: "Hastie, Tibshirani & Friedman, The Elements of Statistical Learning (2nd ed.), Section 7.10.2 'The Wrong and Right Way to Do Cross-validation'"
---
# The Cross-Validation That Peeked: Screening Before the Folds

You have a binary classification problem with $N = 50$ samples and $p = 5000$ features. The data are **pure noise**:

- Labels $y_1,\dots,y_{50}$ are i.i.d. uniform on $\{-1,+1\}$.
- Features $x_{ij}$ are i.i.d. $\mathcal N(0,1)$ and independent of the labels.

An analyst runs **Procedure W**:

1. Using all 50 samples, compute the sample correlation between each feature and the label. Keep the 100 features with the largest $|\text{corr}|$.
2. Using only these 100 features, estimate the error of a 1-nearest-neighbour classifier with 5-fold cross-validation.

A colleague runs **Procedure R**: inside each CV fold, redo step 1 using **only the training folds**. Then fit 1-NN on the training folds and evaluate on the held-out fold.

**Questions.**

**(a)** What is the true test error of *any* classifier on this problem?

**(b)** Prove that the CV error estimate of Procedure R has expectation **exactly** $1/2$.

**(c)** Procedure W typically reports an error of only a few percent. Explain why, and give a back-of-the-envelope reason the effect is so large.

**(d)** Suppose instead that, before cross-validation, the analyst keeps the 100 features with the largest **sample variance** across all 50 samples. Does this pre-screening bias the CV estimate?
