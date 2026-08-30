---
name: "The Softmax That Forgets Its Past: Invariance to Label Permutation vs. Feature Permutation"
type: "ML/Stats"
tags: ["softmax", "identifiability", "logistic regression", "multinomial", "non-identifiability", "Fisher information"]
date: "2026-08-30"
solved: false
comments: ""
related: []
redo: 0
difficulty: 2
source: "The Elements of Statistical Learning, Hastie, Tibshirani, Friedman (2nd ed.), Section 4.4"
---
# The Softmax That Forgets Its Past: Invariance to Label Permutation vs. Feature Permutation

Suppose you train a softmax classifier on a $K$-class problem. The model outputs

$$p(y = k \mid x) = \frac{e^{\beta_k^\top x}}{\sum_{j=1}^K e^{\beta_j^\top x}}, \quad k = 1, \ldots, K.$$

Now consider two operations:

**(A) Label permutation:** You relabel the training data by swapping class 1 and class 2 (and retrain from scratch).

**(B) Feature sign flip:** You replace every feature $x$ with $-x$ (and retrain from scratch).

**Question:** For each operation, describe precisely what happens to the learned coefficient vectors $\{\beta_k\}$. In particular:

- Under **(A)**, is the model equivalent to simply swapping $\beta_1$ and $\beta_2$?
- Under **(B)**, is the model equivalent to simply negating all $\beta_k$?

Now the punchline: the softmax loss function is

$$L = -\frac{1}{n}\sum_{i=1}^n \log p(y_i \mid x_i).$$

**True or False (and explain):** The softmax model has an *identifiability* problem — there exists a non-trivial transformation of $\{\beta_k\}$ that leaves *all* predicted probabilities unchanged for *every* input $x$.

Identify this transformation explicitly and explain why it is never resolved by more data.
