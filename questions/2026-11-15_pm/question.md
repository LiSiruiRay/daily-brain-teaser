---
name: "Logistic Regression Secretly Balances Its Books"
type: "ML/Stats"
tags: ["logistic regression", "score equations", "canonical link", "calibration", "GLM", "moment matching"]
date: "2026-11-15"
solved: false
comments: ""
related: []
redo: 0
difficulty: 2
source: "Hastie, Tibshirani, Friedman — The Elements of Statistical Learning (2nd ed.), Section 4.4.1 (eq. 4.24) and Section 4.4.4 (eq. 4.32)"
---
# Logistic Regression Secretly Balances Its Books

You have training data $(x_i, y_i)_{i=1}^N$ with $y_i \in \{0,1\}$ and $x_i \in \mathbb{R}^p$. You fit a **logistic regression with an intercept** by maximum likelihood:

$$
\hat p_i = \sigma(\hat\beta_0 + x_i^T \hat\beta), \qquad \sigma(t) = \frac{1}{1+e^{-t}}.
$$

Assume the MLE exists, so the data are not separable.

**(a)** Show that, on the training set, the model predicts exactly the right total number of positives:
$$
\sum_{i=1}^N \hat p_i = \sum_{i=1}^N y_i .
$$

**(b)** Suppose one feature is a binary indicator, for example $x_{i1} = \mathbf 1[\text{patient } i \text{ is female}]$. Show that the average predicted probability among the women equals the observed rate among the women. Show the same for the men.

This holds even though the model may fit individual patients badly and contains many other continuous features.

**(c)** Now replace the logistic link with the **probit** link, $\hat p_i = \Phi(\hat\beta_0 + x_i^T\hat\beta)$, where $\Phi$ is the standard normal CDF. Does the identity in (a) still hold in general? What is special about the logit?

**(d)** *(Bonus)* Suppose you add a lasso penalty $\lambda\sum_{j\ge1}|\beta_j|$ and leave the intercept unpenalized. Which of the identities survive?
