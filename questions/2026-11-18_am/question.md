---
name: "The Lost Boarding Pass"
type: "Probability"
tags: ["symmetry", "airplane seating", "harmonic numbers", "linearity of expectation", "folklore"]
date: "2026-11-18"
solved: false
comments: ""
related: []
redo: 0
difficulty: 2
source: "Mathematical folklore (the airplane seating / lost boarding pass puzzle)"
---
# The Lost Boarding Pass

A plane has $n$ seats, numbered $1,\dots,n$, and $n$ passengers, where passenger $i$ holds a ticket for seat $i$. They board in the order $1, 2, \dots, n$.

- Passenger $1$ has lost his boarding pass, so he sits in a seat chosen uniformly at random.
- Every later passenger $i \ge 2$ sits in seat $i$ if it is free. Otherwise, passenger $i$ picks a uniformly random seat among those still free.

**(a)** What is the probability that the last passenger, passenger $n$, sits in his own seat? Take $n = 100$ if you like.

**(b)** *(Bonus)* For $2 \le k \le n$, what is the probability that passenger $k$ finds his seat taken? Deduce the expected number of displaced passengers.

*Try (a) first. The answer has a one-line reason that needs no computation.*
