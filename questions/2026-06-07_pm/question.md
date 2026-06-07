---
name: "Optimism of Training Error and the LOO Shortcut"
type: "ML/Stats"
tags: ["optimism", "cross-validation", "hat matrix", "leverage", "bias", "generalization", "OLS"]
date: "2026-06-07"
solved: false
comments: ""
related: []
redo: 0
difficulty: 3
source: "The Elements of Statistical Learning, Chapter 7 (Hastie, Tibshirani, Friedman)"
---
# The Optimistic Scientist: Why Cross-Validation Beats Training Error, and When It Fails

You fit a model with $p$ parameters to $n$ training points using ordinary least squares. The training MSE is:

$$\widehat{\text{err}}_{\text{train}} = \frac{1}{n}\sum_{i=1}^n (y_i - \hat{f}(x_i))^2$$

and the true (expected) test MSE on a fresh draw is $\text{Err}$.

**(a)** Show that $\mathbb{E}[\widehat{\text{err}}_{\text{train}}] \leq \mathbb{E}[\text{Err}]$, i.e., training error is systematically optimistic. Give a clean formula for the gap.

**(b)** Now suppose $p = n$ (you fit as many parameters as data points). What happens to $\widehat{\text{err}}_{\text{train}}$? What does this mean for using training error as a model selection criterion?

**(c)** Leave-one-out cross-validation (LOO-CV) is proposed as a fix. For linear smoothers $\hat{y} = Hy$ (where $H$ is the hat matrix), LOO-CV has a remarkable shortcut formula:

$$\text{CV}_{(n)} = \frac{1}{n}\sum_{i=1}^n \left(\frac{y_i - \hat{y}_i}{1 - H_{ii}}\right)^2$$

Explain **intuitively** why the factor $(1 - H_{ii})$ appears in the denominator. What does $H_{ii}$ measure, and why does a large $H_{ii}$ make the correction large?
