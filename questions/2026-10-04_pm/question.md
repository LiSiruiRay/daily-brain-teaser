---
name: "Cross-Entropy Decomposition: Entropy + KL Divergence"
type: "ML/Stats"
tags: ["cross-entropy", "KL divergence", "calibration", "information theory", "binary entropy"]
date: "2026-10-04"
solved: false
comments: ""
related: []
redo: 0
difficulty: 2
source: "The Elements of Statistical Learning, Ch. 10; mathematical folklore in information theory"
---
# The Cross-Entropy Loss That Knows Its Own Calibration

Suppose you are training a binary classifier with outputs $\hat{p}_i \in (0,1)$ and true labels $y_i \in \{0,1\}$. The average cross-entropy loss on $n$ training examples is:

$$L = -\frac{1}{n}\sum_{i=1}^n \left[ y_i \log \hat{p}_i + (1-y_i)\log(1-\hat{p}_i) \right].$$

Now suppose the model is **perfectly calibrated** on the training set, meaning the predicted probability equals the empirical class frequency within every "bucket." In the simplest case: suppose all $n$ examples share the same predicted score $\hat{p}$, and the fraction of positives among them is $\bar{y} = \frac{1}{n}\sum_i y_i$.

**Question:** Show that the cross-entropy loss satisfies

$$L \geq H(\bar{y}),$$

where $H(p) = -p\log p - (1-p)\log(1-p)$ is the binary entropy, with equality if and only if $\hat{p} = \bar{y}$.

In other words: among all constant predictions $\hat{p}$, the **calibrated prediction** $\hat{p} = \bar{y}$ minimizes the cross-entropy loss, and the minimum value is exactly the irreducible entropy of the label distribution.
