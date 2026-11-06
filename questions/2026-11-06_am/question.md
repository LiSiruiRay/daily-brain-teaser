---
name: "Averaging a Matrix Group Gives a Projection"
type: "Putnam"
tags: ["linear algebra", "group averaging", "idempotent", "trace equals rank", "representation theory"]
date: "2026-11-06"
solved: false
comments: ""
related: []
redo: 0
difficulty: 2
source: "Putnam 1985, Problem B-6 (materials/putnam/1985.pdf)"
---
# Averaging a Matrix Group Gives a Projection

Let $G = \{M_1, M_2, \dots, M_r\}$ be a finite set of real $n\times n$ matrices that forms a group under matrix multiplication. Suppose that

$$\sum_{i=1}^{r} \operatorname{tr}(M_i) = 0.$$

Prove that

$$\sum_{i=1}^{r} M_i = 0,$$

the $n \times n$ zero matrix.

*Remark.* The identity element of $G$ need not be $I_n$. For example, $G$ could consist of singular matrices that form a group among themselves.

---

**Field:** Linear algebra / group theory (representation theory in disguise)

**Why it is interesting:** The hypothesis gives only one number, the sum of the traces, and asks you to conclude that an entire matrix vanishes. That looks far too weak, until you see that the averaged matrix is forced to have a very rigid structure. This is the seed of character theory. In representation theory, the average of the characters of a representation counts the copies of the trivial representation.

**Difficulty:** 2 / 5

**Source:** 46th William Lowell Putnam Competition (1985), Problem B–6.
