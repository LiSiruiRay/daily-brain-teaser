---
name: "The Gaussian Mixture Whose Likelihood Explodes"
type: "ML/Stats"
tags: ["maximum likelihood", "Gaussian mixture", "EM algorithm", "degeneracy", "regularization"]
date: "2026-11-15"
solved: false
comments: ""
related: []
redo: 0
difficulty: 2
source: "Hastie, Tibshirani, Friedman — The Elements of Statistical Learning (2nd ed.), §8.5.1 (EM for two-component mixtures)"
---
# The Gaussian Mixture Whose Likelihood Explodes

Let $x_1,\dots,x_n\in\mathbb R$ be **distinct** data points with $n\ge 2$. Write $\varphi_\sigma(t)=\frac{1}{\sqrt{2\pi}\,\sigma}e^{-t^2/(2\sigma^2)}$.

**(a) A single Gaussian.** Show that the likelihood
$$L(\mu,\sigma)=\prod_{i=1}^n \varphi_\sigma(x_i-\mu)$$
is bounded above on $\mathbb R\times(0,\infty)$. This is why the usual MLE $(\bar x, \hat\sigma^2)$ exists.

**(b) Two Gaussians.** Consider the two-component mixture
$$f(x)=\pi\,\varphi_{\sigma_1}(x-\mu_1)+(1-\pi)\,\varphi_{\sigma_2}(x-\mu_2),\qquad \pi\in(0,1),$$
with likelihood $L=\prod_i f(x_i)$. Show that
$$\sup_{\pi,\mu_1,\mu_2,\sigma_1,\sigma_2} L=+\infty .$$
So the "maximum likelihood estimate" of a Gaussian mixture does not exist.

**(c) A cure.** Suppose $n\ge 3$ and we force a common variance, $\sigma_1=\sigma_2=\sigma$. Show that the likelihood is now bounded again.

*Hint:* Ask how much each data point can contribute when one variance becomes tiny. In (a), what happens to the other points? In (b), who keeps them alive?
