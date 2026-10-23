---
name: "Zeros Hidden Before the Beginning"
type: "Putnam"
tags: ["recurrence", "periodicity mod N", "pigeonhole", "invertible dynamics", "running backwards"]
date: "2026-10-23"
solved: false
comments: ""
related: []
redo: 0
difficulty: 3
source: "Putnam 2006 A3; solutions by Kiran Kedlaya and Lenny Ng (materials/putnam/2006s.pdf)"
---
# Zeros Hidden Before the Beginning

Define a sequence of integers by

$$x_k = k \quad \text{for } k = 1, 2, \dots, 2006,$$

and, for $k \ge 2006$,

$$x_{k+1} = x_k + x_{k-2005}.$$

So the sequence begins

$$1, 2, 3, \dots, 2005, 2006, 2007, 2009, 2012, 2016, \dots$$

**Prove that the sequence contains 2005 consecutive terms, each divisible by $2006$.**

*(Hint-free version: try it first. If stuck, ask yourself where the sequence came from, not where it is going.)*
