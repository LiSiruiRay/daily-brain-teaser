---
name: "The Kernel Trick: Why Inner Products Are All You Need"
type: "ML/Stats"
tags: ["kernel trick", "feature maps", "SVM", "polynomial kernel", "dimensionality", "inner product"]
date: "2026-06-07"
solved: false
comments: ""
related: []
redo: 0
difficulty: 2
source: "The Elements of Statistical Learning, Hastie, Tibshirani, Friedman (2nd ed.), Ch. 12; also standard ML folklore"
---
# The Kernel Trick: Why Inner Products Are All You Need

You are building a classifier. You decide to map your input $x \in \mathbb{R}^d$ to a high-dimensional (even infinite-dimensional) feature space $\phi(x) \in \mathcal{H}$, then run a linear classifier there.

The prediction function takes the form:

$$f(x) = \sum_{i=1}^{n} \alpha_i \langle \phi(x_i), \phi(x) \rangle_{\mathcal{H}}$$

**The puzzle:** You never want to compute $\phi(x)$ explicitly. Instead you only ever evaluate a kernel function $k(x, x') = \langle \phi(x), \phi(x') \rangle_{\mathcal{H}}$.

Consider the polynomial kernel $k(x, x') = (1 + x \cdot x')^2$ on $\mathbb{R}^2$, where $x = (x_1, x_2)$.

**(a)** Find an explicit feature map $\phi: \mathbb{R}^2 \to \mathbb{R}^m$ such that $k(x,x') = \langle \phi(x), \phi(x') \rangle$.

**(b)** What is the dimension $m$ of the feature space? Now consider the more general kernel $k(x, x') = (1 + x \cdot x')^p$ on $\mathbb{R}^d$. What is the dimension of the induced feature space as a function of $d$ and $p$? What happens as $d$ and $p$ grow?

**(c) The conceptual punch line:** Suppose evaluating $k(x, x')$ costs $O(d)$ time. Evaluating $\langle \phi(x), \phi(x') \rangle$ explicitly costs $O(m)$ time, where $m$ grows polynomially in $d$ and $p$. What does this say about the power of the kernel trick?
