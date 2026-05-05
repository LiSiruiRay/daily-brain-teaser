---
name: "The Comb Space Is Not Locally Connected"
type: "topology"
tags: ["local connectedness", "connectedness", "counterexample", "comb space", "point-set topology"]
date: "2026-05-05"
solved: false
comments: ""
related: []
redo: 0
difficulty: 3
source: "Topology, Munkres — Chapter 3 (Connectedness); also mathematical folklore"
---
# The Comb Space Is Not Locally Connected

Let the **comb space** $X \subset \mathbb{R}^2$ be defined as:

$$X = \left(\{0\} \times [0,1]\right) \cup \left([0,1] \times \{0\}\right) \cup \left(\bigcup_{n=1}^{\infty} \left\{\tfrac{1}{n}\right\} \times [0,1]\right)$$

That is, $X$ consists of:
- The segment $\{0\} \times [0,1]$ (the "left spine"),
- The segment $[0,1] \times \{0\}$ (the "base"),
- Vertical unit segments at $x = 1, \tfrac{1}{2}, \tfrac{1}{3}, \tfrac{1}{4}, \ldots$

**Question:** Is $X$ connected? Is $X$ locally connected at the point $p = (0, 1)$?

Prove your answers.
