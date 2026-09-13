---
name: "Naive Bayes Beats Its Own Assumptions"
type: "ML/Stats"
tags: ["Naive Bayes", "decision boundary", "calibration", "log-odds", "model misspecification"]
date: "2026-09-13"
solved: false
comments: ""
related: []
redo: 0
difficulty: 2
source: "Domingos & Pazzani (1997), 'On the Optimality of the Simple Bayesian Classifier under Zero-One Loss'; ESL Ch. 6"
---
# The Naive Bayes That Beats Its Own Assumptions

Suppose you want to classify emails as spam or not-spam. You train a **Naive Bayes classifier**, which assumes all features (words) are conditionally independent given the class. You know for a fact that many words are highly correlated — "free" and "prize" almost always appear together.

Despite this blatant violation of the independence assumption, your colleague claims:

> "Even though Naive Bayes gives wildly wrong probability estimates, its **decision boundary** (i.e., which class it predicts) can still be optimal."

Is your colleague correct? Give a concrete argument for why this can happen, and explain what structural property of the decision rule makes it robust to miscalibration of probabilities.
