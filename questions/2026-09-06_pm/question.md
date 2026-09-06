---
name: "The Calibration Trap: Perfect Accuracy vs Probability Estimation"
type: "ML/Stats"
tags: ["calibration", "naive Bayes", "classification", "probability estimation", "conditional independence"]
date: "2026-09-06"
solved: false
comments: ""
related: []
redo: 0
difficulty: 2
source: "The Elements of Statistical Learning, Hastie, Tibshirani, Friedman (2nd ed.), Section 6.6.3 and folklore"
---
# The Calibration Trap: When a Perfect Classifier Fails Probability Estimation

Suppose you train a binary classifier that achieves **100% training accuracy** — it correctly labels every training point. A colleague claims: "Since our classifier is perfect on the training set, we can read off class probabilities directly from its output scores. If the model outputs a score of 0.9 for class 1, the true probability of class 1 is 0.9."

Now consider a specific case. You train a **naive Bayes classifier** on two features $X_1$ and $X_2$ that are **strongly positively correlated** (say $\rho = 0.95$) given the class label. The model achieves near-perfect classification accuracy.

**Question:** Even if the classifier achieves perfect (or near-perfect) classification accuracy, explain precisely why its output scores **cannot** be trusted as calibrated probabilities. What goes wrong in the naive Bayes case specifically, and what is the general principle?

As a concrete sanity check: if the true posterior is $P(Y=1 \mid X) = 0.6$, can a perfectly-accurate classifier output a score of $0.99$ for the same input? Is this consistent or contradictory?
