---
name: "The Vanishing Gradient Plateau: Why Sigmoid Networks Saturate"
type: "ML/Stats"
tags: ["neural networks", "sigmoid", "vanishing gradient", "backpropagation", "activation functions"]
date: "2026-07-26"
solved: false
comments: ""
related: []
redo: 0
difficulty: 2
source: "The Elements of Statistical Learning, Ch. 11 (Hastie, Tibshirani, Friedman)"
---
# The Vanishing Gradient Plateau: Why Sigmoid Networks Saturate

Consider a single neuron with sigmoid activation $\sigma(z) = \frac{1}{1+e^{-z}}$, where $z = w x + b$.

Training uses gradient descent on the squared loss $L = \frac{1}{2}(y - \sigma(z))^2$ for a single training example $(x, y)$.

**(a)** Show that the gradient $\frac{\partial L}{\partial w}$ contains the factor $\sigma(z)(1-\sigma(z))$.

**(b)** Now suppose the network is initialized with a large weight $|w| \gg 1$ and $x = 1$, $y = 0$. Argue clearly: even though the network is making a **large error** (since $\sigma(z) \approx 1$ but $y = 0$), learning is **extremely slow**. What is the maximum possible value of $\sigma(z)(1-\sigma(z))$, and where is it achieved?

**(c)** This is the **vanishing gradient** / **saturation** phenomenon. Give a one-sentence intuition for *why* the sigmoid's shape causes this, and name one architectural change that mitigates it.
