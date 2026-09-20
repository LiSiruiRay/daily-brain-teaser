---
name: ""
type: ""
tags: []
date: "2026-09-20"
solved: false
comments: ""
related: []
redo: 0
difficulty: 2
---
# The Posterior That Remembers Too Little: Jeffreys Prior Invariance

Suppose you observe $X \sim \text{Binomial}(n, \theta)$ and want to place a prior on $\theta \in [0,1]$.

A colleague suggests using the **uniform prior** $\pi(\theta) = 1$, arguing it is "non-informative." But then you reparametrize: let $\phi = \sin^{-1}(\sqrt{\theta})$, the arcsine transform. Your colleague applies the uniform prior to $\phi$ instead.

**(a)** Show that the two priors — uniform on $\theta$ vs. uniform on $\phi$ — are **not the same** (i.e., a uniform prior on $\theta$ does not correspond to a uniform prior on $\phi$).

**(b)** The **Jeffreys prior** is defined as $\pi(\theta) \propto \sqrt{I(\theta)}$, where $I(\theta)$ is the Fisher information. Compute the Jeffreys prior for $\theta$ in the binomial model, and show it is $\text{Beta}(1/2, 1/2)$.

**(c)** Show that the Jeffreys prior is **reparametrization invariant**: if $\phi = g(\theta)$ is a smooth bijection and $\pi_J(\theta) \propto \sqrt{I(\theta)}$, then the induced prior on $\phi$ is also the Jeffreys prior for $\phi$.

*Why does this matter?* It means Jeffreys prior gives the same "non-informative" answer regardless of how you parametrize the problem — something the flat prior catastrophically fails to do.
