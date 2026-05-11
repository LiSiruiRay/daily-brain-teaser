---
name: "Dirichlet Function and Lebesgue Measure Zero"
type: "analysis"
tags: ["Lebesgue integration", "measure zero", "Riemann vs Lebesgue", "Monotone Convergence Theorem", "Dirichlet function"]
date: "2026-05-11"
solved: false
comments: ""
related: []
redo: 0
difficulty: 2
source: "Rudin - Real and Complex Analysis, Chapter 1; mathematical folklore"
---
# The Lebesgue Integral of a Suspicious Function

Define $f : [0,1] \to \mathbb{R}$ by

$$f(x) = \begin{cases} 1 & \text{if } x \in \mathbb{Q} \\ 0 & \text{if } x \notin \mathbb{Q}. \end{cases}$$

(This is the **Dirichlet function**.)

1. Show that $f$ is **not Riemann integrable** on $[0,1]$.
2. Compute the **Lebesgue integral** $\int_{[0,1]} f \, d\mu$.
3. Now consider the sequence of functions $f_n : [0,1] \to \mathbb{R}$ defined as follows: enumerate the rationals in $[0,1]$ as $q_1, q_2, q_3, \ldots$ and set

$$f_n(x) = \begin{cases} 1 & \text{if } x \in \{q_1, q_2, \ldots, q_n\} \\ 0 & \text{otherwise.} \end{cases}$$

Show that $f_n \to f$ pointwise, compute $\int_{[0,1]} f_n \, d\mu$ for each $n$, and verify the Monotone Convergence Theorem in this example.
