---
name: "Cover's Counting Theorem: Capacity of a Hyperplane"
type: "ML/Stats"
tags: ["linear separability", "perceptron capacity", "Pascal recursion", "high-dimensional statistics", "p >> N"]
date: "2026-11-08"
solved: false
comments: ""
related: []
redo: 0
difficulty: 3
source: "T. M. Cover (1965), 'Geometrical and Statistical Properties of Systems of Linear Inequalities'; context: Hastie–Tibshirani–Friedman, The Elements of Statistical Learning, 2nd ed., Ch. 18 (p ≫ N problems)"
---
# Cover's Counting Theorem: How Many Labelings Can a Hyperplane Shatter?

Let $x_1,\dots,x_N\in\mathbb{R}^d$ be in **general position**: every subset of at most $d$ of the points is linearly independent. A *dichotomy* is a labeling $y\in\{\pm1\}^N$. It is *realizable* if some $w\in\mathbb{R}^d$ gives
$$
\operatorname{sign}(w\cdot x_i)=y_i\quad\text{for all } i,
$$
with $w\cdot x_i\neq 0$ for every $i$. This is a homogeneous linear classifier: its hyperplane passes through the origin.

Let $C(N,d)$ be the number of realizable dichotomies.

**(a)** Show that $C(N,d)$ depends only on $N$ and $d$, and that
$$
C(N,d)\;=\;2\sum_{k=0}^{d-1}\binom{N-1}{k}.
$$

**(b)** Suppose the labels are assigned by independent fair coin flips. Show that the probability the data are linearly separable equals $1/2$ **exactly** when $N=2d$. Show also that this probability equals $1$ whenever $N\le d$.

*(Hint for (a): add points one at a time. When a new point arrives, which old dichotomies split into two new ones?)*
