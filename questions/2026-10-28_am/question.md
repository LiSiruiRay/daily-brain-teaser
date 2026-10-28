---
name: "Doubling Your Accuracy"
type: "Probability"
tags: ["variance", "experimental design", "Hadamard matrix", "unbiased estimation", "weighing design"]
date: "2026-10-28"
solved: false
comments: ""
related: []
redo: 0
difficulty: 2
source: "Frederick Mosteller, Fifty Challenging Problems in Probability with Solutions — 'Doubling Your Accuracy'"
---
# Doubling Your Accuracy

You have two rods with unknown lengths $a$ and $b$. You have a measuring instrument that is **unbiased but noisy**. Whenever you measure a length $\ell$, it reports

$$
\ell + \varepsilon,
$$

where $\mathbb{E}[\varepsilon]=0$ and $\operatorname{Var}(\varepsilon)=\sigma^2$. The size of the error does not depend on $\ell$, and errors from different measurements are independent.

You may use the instrument **exactly twice**. In each use you can measure any single length you can physically form with the rods. For example:

- one rod alone,
- the two rods laid **end to end**, which has length $a+b$,
- the two rods laid **side by side** with left ends aligned, where you measure the overhang, which has length $|a-b|$.

The obvious plan is to measure each rod once. That gives unbiased estimates of $a$ and $b$, each with variance $\sigma^2$.

1. Find a scheme that produces unbiased estimates of **both** $a$ and $b$, each with variance **strictly smaller** than $\sigma^2$.
2. *(Bonus)* Show that your scheme is optimal. No design using two measurements of signed combinations $\pm a \pm b$, $\pm a$, $\pm b$ can give either length an unbiased linear estimate with variance below $\sigma^2/2$.
3. *(Bonus)* With $n$ rods and $n$ measurements, how small can the variance be made?
