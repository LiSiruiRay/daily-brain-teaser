---
name: "LDA Is Secretly Logistic Regression"
type: "ML/Stats"
tags: ["logistic regression", "LDA", "Gaussian generative model", "Bayes theorem", "bias-variance", "discriminative vs generative"]
date: "2026-08-16"
solved: false
comments: ""
related: []
redo: 0
difficulty: 2
source: "The Elements of Statistical Learning, Hastie, Tibshirani, Friedman, 2nd ed., Section 4.3"
---
# The Softmax That Forgets Its Past: Logistic Regression and Sufficient Statistics

Suppose you have binary labels $y \in \{0, 1\}$ and a feature vector $x \in \mathbb{R}^p$. You fit logistic regression, which models:

$$P(y = 1 \mid x) = \sigma(\beta^T x) = \frac{1}{1 + e^{-\beta^T x}}.$$

Now consider a different scenario: you are told that within each class, the features are Gaussian with a **shared covariance matrix**:

$$x \mid y = k \sim \mathcal{N}(\mu_k, \Sigma), \quad k = 0, 1,$$

with class priors $\pi_k = P(y = k)$.

**The question:** Using Bayes' theorem, compute $P(y=1 \mid x)$ under this generative (LDA) model. What do you notice? What does this say about the relationship between logistic regression and Linear Discriminant Analysis (LDA)?

*Follow-up to ponder:* LDA has more parameters than logistic regression. Does fitting more parameters make LDA better? When would LDA beat logistic regression, and when would it lose?
