---
name: "Three-Fold Closure Forces Two-Fold Closure"
type: "Putnam"
tags: ["semigroups", "associativity", "proof by contradiction", "algebra", "Putnam 1995"]
date: "2026-10-16"
solved: false
comments: ""
related: []
redo: 0
difficulty: 2
source: "56th William Lowell Putnam Competition (1995), Problem A1; solutions by Kiran Kedlaya (materials/putnam/1995s.pdf)"
---
# Three-Fold Closure Forces Two-Fold Closure

**Field:** Algebra (semigroups) · Putnam 1995 A1

**Problem.** Let $S$ be a set of real numbers that is closed under multiplication: if $a,b\in S$, then $ab\in S$. Let $T$ and $U$ be disjoint subsets of $S$ whose union is $S$. Suppose:

- the product of any **three** elements of $T$ (not necessarily distinct) is in $T$, and
- the product of any **three** elements of $U$ (not necessarily distinct) is in $U$.

Show that at least one of $T$ and $U$ is closed under multiplication of **two** elements.

---

**Warm-up sanity check.** Take $S=\mathbb{R}\setminus\{0\}$, $T=(0,\infty)$ and $U=(-\infty,0)$.

- The product of three negatives is negative, so $U$ satisfies the hypothesis.
- The product of two negatives is positive, so $U$ is *not* closed under multiplication of two elements.
- $T$, however, is closed.

So the conclusion "at least one" cannot be strengthened to "both".

---

**Why it's interesting:** The statement sounds like it needs structure theory, such as sign characters or homomorphisms to $\mathbb{Z}/2$. In fact it falls to a single product of four elements that you are allowed to bracket in two different ways. It is a good example of using associativity as a weapon.

**Estimated difficulty:** 2 / 5

*Reference: 56th Putnam (1995), Problem A1; solution following Kiran Kedlaya's writeup (materials: `putnam/1995s.pdf`).*
