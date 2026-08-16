---
name: ""
type: ""
tags: []
date: "2026-08-16"
solved: false
comments: ""
related: []
redo: 0
difficulty: 2
---
# The Overconfident Classifier: When More Data Hurts Calibration

You train a logistic regression model on a dataset with $p$ features and $n$ training examples, where $p$ is large relative to $n$. The model achieves near-zero training loss.

A colleague suggests: *"The model's predicted probabilities are well-calibrated — after all, we minimized cross-entropy, which directly targets the log-likelihood of probabilities."*

**Question:** Is this reasoning correct? Specifically:

1. When $p/n \to c > 0$ (i.e., the number of features is a constant fraction of the sample size), what happens to the maximum likelihood estimates $\hat{\beta}$ in logistic regression, and why does this make predicted probabilities systematically **overconfident** (pushed toward 0 and 1)?

2. Give a simple, clean argument for why minimizing training cross-entropy does **not** guarantee calibrated probabilities, even in principle — using just the concept of **overfitting** and the difference between training and test distributions.

3. **(Bonus conceptual punchline):** What simple post-hoc fix can partially restore calibration, and why does it work geometrically?
