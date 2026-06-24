---
name: "The Matching Birthdays: Expected Collisions"
type: "Probability"
tags: ["linearity of expectation", "birthday problem", "Poisson approximation", "indicator variables"]
date: "2026-06-24"
solved: false
comments: ""
related: []
redo: 0
difficulty: 2
source: "Fifty Challenging Problems in Probability with Solutions (Frederick Mosteller), Problem 45 (matching), classical birthday variant"
---
# The Matching Birthdays: Expected Collisions

A room has $n$ people. Each person's birthday is chosen uniformly at random from 365 days (independently). Let $X$ be the number of **pairs** of people who share a birthday.

1. Find $E[X]$.
2. Use your answer to show that if $n \geq 28$, then $E[X] \geq 1$, meaning we *expect* at least one shared birthday pair.
3. (**The surprise**) The well-known birthday problem says the probability of *at least one* collision first exceeds $\frac{1}{2}$ around $n = 23$. How can $E[X] \geq 1$ require $n \approx 28$ yet a collision becomes *likely* at $n \approx 23$? Reconcile this apparent contradiction.
