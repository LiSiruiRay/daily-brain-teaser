---
name: "The EM Algorithm That Overshoots: Why Hard Assignment Fails"
type: "ML/Stats"
tags: ["EM algorithm", "mixture models", "K-means", "ELBO", "KL divergence", "latent variables"]
date: "2026-10-04"
solved: false
comments: ""
related: []
redo: 0
difficulty: 3
source: "The Elements of Statistical Learning, Hastie, Tibshirani, Friedman, Chapter 8 & 14"
---
# The EM Algorithm That Overshoots: Why Hard Assignment Fails

Consider a simple Gaussian mixture model with two components:

$$p(x) = \pi \, \mathcal{N}(x;\mu_1,\sigma^2) + (1-\pi)\,\mathcal{N}(x;\mu_2,\sigma^2)$$

The **EM algorithm** iterates soft E-steps (computing posterior responsibilities) and M-steps (updating parameters). Suppose instead you replace the E-step with a **hard assignment**: each data point is assigned to whichever component has higher posterior probability.

**The question:** Hard-assignment EM (i.e., K-means style) maximizes the **same log-likelihood** as soft EM — true or false? If false, what objective does hard assignment actually optimize, and why does it tend to produce different (and generally worse) solutions?

Give a precise characterization of the two objectives and explain the conceptual gap between them.
