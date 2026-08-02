---
name: "Naive Bayes Independence Violation: Wrong Probabilities, Right Decisions"
type: "ML/Stats"
tags: ["naive bayes", "classification", "log-odds", "independence assumption", "calibration"]
date: "2026-08-02"
solved: false
comments: ""
related: []
redo: 0
difficulty: 2
source: "The Elements of Statistical Learning, Hastie, Tibshirani, Friedman (2nd ed.), Chapter 6 / general ML folklore"
---
# The Naive Bayes Independence Assumption: When Does It Hurt?

Suppose you are classifying emails as spam or not spam using **Naive Bayes**, which assumes that all features $X_1, X_2, \ldots, X_p$ are conditionally independent given the class label $Y \in \{0, 1\}$.

Now consider just two binary features: $X_1$ = "contains the word 'free'" and $X_2$ = "contains the word 'prize'". In spam emails, these two words are **highly positively correlated**: if one appears, the other almost certainly does too.

**The puzzle:** Despite this blatant violation of the independence assumption, Naive Bayes classifiers often still produce the **correct classification decision** (even if the probability estimates are badly wrong). 

Explain precisely and concisely:

1. *Why* does the independence violation corrupt the probability estimates?
2. *Why* does the classifier often still get the decision right?

As a concrete sanity check: suppose

$$P(X_1=1, X_2=1 \mid Y=1) = 0.8, \quad P(X_1=1, X_2=1 \mid Y=0) = 0.05$$

but Naive Bayes computes (incorrectly assuming independence):

$$\hat{P}(X_1=1 \mid Y=1)^2 = 0.64, \quad \hat{P}(X_1=1 \mid Y=0)^2 = 0.0025.$$

Both the true and naive likelihood ratios favor $Y=1$ enormously. What does this tell you about Naive Bayes?
