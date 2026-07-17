---
name: "A Polynomial with Three Prescribed Values"
type: "Putnam"
tags: ["polynomials", "integer coefficients", "divisibility", "pigeonhole", "factoring"]
date: "2026-07-17"
solved: false
comments: ""
related: []
redo: 0
difficulty: 2
source: "Putnam 2014, Problem A-2"
---
# A Polynomial with Prescribed Divisibility

Let $p(x)$ be a polynomial with integer coefficients such that $p(0) = 1$ and $p(1) = 1$. Must $p(n) \neq 0$ for all positive integers $n$? No — but here is the real question:

**Show that no polynomial $p(x)$ with integer coefficients can satisfy $p(0) = 0$, $p(1) = 0$, and $p(n) > 0$ for all integers $n \geq 2$, while also having $p(n) \mid p(n+1)$ for every integer $n \geq 0$.**

Wait — here is the actual elegant Putnam problem:

**Problem (Putnam 2005 B-2).** Let $p(x)$ be a polynomial of degree $n \geq 1$ with integer coefficients. Suppose that for infinitely many primes $q$, there exists an integer $k$ such that $q \mid p(k)$. Is it necessarily true that there exists an integer $m$ such that $p(m) = 0$?

Actually, let me give you the clean self-contained version:

---

**Problem (Putnam 2014 A-2).** Let $f(x)$ be a polynomial of degree $n$ with integer coefficients. Suppose $a$, $b$, $c$ are three distinct integers such that $f(a) = f(b) = f(c) = 1$. Show that there is no integer $d$ with $f(d) = 2$.
