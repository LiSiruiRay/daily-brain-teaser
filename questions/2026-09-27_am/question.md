---
name: "Fisher Information Curvature Identity"
type: "ML/Stats"
tags: ["Fisher information", "score function", "log-likelihood", "Cramér-Rao", "statistics"]
date: "2026-09-27"
solved: false
comments: ""
related: []
redo: 0
difficulty: 2
source: "The Elements of Statistical Learning (Hastie, Tibshirani, Friedman), standard statistical theory"
---
# The Fisher Information That Knows Its Own Curvature

Let $X \sim p_\theta(x)$ be a one-parameter family of distributions with score function $s(\theta) = \frac{\partial}{\partial \theta} \log p_\theta(X)$.

The **Fisher information** is defined as $I(\theta) = \mathbb{E}_\theta[s(\theta)^2]$.

Prove the following elegant identity:

$$I(\theta) = -\mathbb{E}_\theta\!\left[\frac{\partial^2}{\partial \theta^2} \log p_\theta(X)\right]$$

That is, Fisher information equals the **negative expected curvature** of the log-likelihood.

*Assume all regularity conditions hold so that differentiation and integration can be exchanged freely.*

After proving the identity, explain intuitively: why does **more curvature** (sharper log-likelihood) mean **more information** about $\theta$?
