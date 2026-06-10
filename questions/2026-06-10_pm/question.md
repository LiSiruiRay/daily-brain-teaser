---
name: "Second-Best Runner-Up"
type: "Probability"
tags: ["tournament", "combinatorics", "indicator trick", "bracket"]
date: "2026-06-10"
solved: false
comments: ""
related: []
redo: 0
difficulty: 2
source: "Fifty Challenging Problems in Probability with Solutions, Frederick Mosteller, Problem 16"
---
# The Second-Best Player Problem

A tennis tournament has **8 players**. They are seeded into a standard single-elimination bracket (as shown below) by drawing positions from a hat at random.

```
1 ─┐
   ├─┐
2 ─┘ │
     ├─┐
3 ─┐ │ │
   ├─┘ │
4 ─┘   ├─── Winner
5 ─┐   │
   ├─┐ │
6 ─┘ │ │
     ├─┘
7 ─┐ │
   ├─┘
8 ─┘
```

Assume the **best player always beats everyone**, and the **second-best player always beats everyone except the best player**.

The **runner-up cup** goes to the loser of the final match.

**What is the probability that the second-best player wins the runner-up cup?**

More generally, what is this probability for a tournament of $2^n$ players?
