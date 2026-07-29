---
name: "The Lazy Drunk: Random Walk Returns in 2D vs 3D"
type: "Probability"
tags: ["random walk", "recurrence", "Polya theorem", "dimension", "generating functions"]
date: "2026-07-29"
solved: false
comments: ""
related: []
redo: 0
difficulty: 3
source: "Fifty Challenging Problems in Probability with Solutions (Frederick Mosteller), Problem 51; classical result of Pólya (1921)"
---
# The Lazy Drunk: Random Walk Returns in 2D vs 3D

A particle starts at the origin and takes steps in the following way:

- **In 2D:** at each step, it moves one unit **North, South, East, or West**, each with probability $\frac{1}{4}$.
- **In 3D:** at each step, it moves one unit along one of the **6 axis directions** ($\pm x, \pm y, \pm z$), each with probability $\frac{1}{6}$.

**In 2D**, it is a classical fact that the particle returns to the origin with probability **1** (the walk is recurrent).

**Question:** In 3D, does the particle return to the origin with probability 1, or is there a positive probability of escaping to infinity forever? If it escapes, roughly what is the probability of **never** returning?

*You don't need to compute the exact value — reasoning about why the answer differs between 2D and 3D is the heart of the problem. But if you can, the exact escape probability is approximately $\mathbf{0.3405}$.*
