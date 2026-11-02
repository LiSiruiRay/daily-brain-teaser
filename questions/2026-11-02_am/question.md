---
name: "Fekete's Subadditive Lemma"
type: "analysis"
tags: ["sequences", "subadditivity", "division algorithm", "limits", "spectral radius"]
date: "2026-11-02"
solved: false
comments: ""
related: []
redo: 0
difficulty: 2
source: "Fekete (1923); classical folklore (e.g., Pólya–Szegő, Problems and Theorems in Analysis I, Part I, Problem 98)"
---
# Fekete's Subadditive Lemma

A real sequence $(a_n)_{n\ge 1}$ is called **subadditive** if
$$a_{m+n} \le a_m + a_n \qquad \text{for all } m,n\ge 1.$$

**Prove** that $\displaystyle \lim_{n\to\infty} \frac{a_n}{n}$ exists in $[-\infty,\infty)$ and that
$$\lim_{n\to\infty}\frac{a_n}{n} \;=\; \inf_{n\ge 1}\frac{a_n}{n}.$$

**Follow-up (one line, once you have the lemma):** For a square matrix $A$ and any submultiplicative norm $\|\cdot\|$, show that $\lim_{n\to\infty}\|A^n\|^{1/n}$ exists.
