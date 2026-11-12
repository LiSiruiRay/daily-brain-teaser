---
name: "A Univalent Map Cannot Shrink the Disk"
type: "Complex Analysis"
tags: ["area formula", "orthogonality", "univalent functions", "Parseval", "geometric function theory"]
date: "2026-11-12"
solved: false
comments: ""
related: []
redo: 0
difficulty: 2
source: "Classic (area method of Gronwall–Bieberbach; folklore)"
---
# A Univalent Map Cannot Shrink the Disk

Let $\mathbb{D}=\{z\in\mathbb{C}: |z|<1\}$ and let $f:\mathbb{D}\to\mathbb{C}$ be holomorphic and **injective**, normalized so that

$$
f(0)=0,\qquad f'(0)=1 .
$$

**Prove** that

$$
\operatorname{Area}\big(f(\mathbb{D})\big)\;\ge\;\pi,
$$

with equality **if and only if** $f(z)=z$.

In words: if a univalent map has unit derivative at the origin, its image has at least the area of the disk, and only the identity achieves exactly that area.

*(Try it for 5 minutes before reading on.)*

---

**Field:** Complex Analysis (geometric function theory)

**Why it's interesting:** Schwarz's lemma says a holomorphic map *into* the disk with $f(0)=0$ satisfies $|f'(0)|\le 1$, so it can only shrink. This result is a partial converse in terms of area. Fix $f'(0)=1$ and ask how small the image can be. The answer is that it can't be smaller than the disk. The proof uses no estimates. It is just Parseval's identity in disguise: the monomials $z^n$ are orthogonal on the disk, so higher-order terms can only *add* area and never cancel it. This "area method" is the seed of Gronwall's area theorem and Bieberbach's proof that $|a_2|\le 2$, the first case of the Bieberbach conjecture.

**Difficulty:** 2 / 5

**Tags:** area formula, orthogonality, univalent functions, Parseval
