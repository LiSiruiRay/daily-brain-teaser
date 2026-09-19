---
name: "Sophomore's Dream: Integral of x^x"
type: "Integration"
tags: ["power series", "integration by substitution", "Bernoulli", "closed form", "sophomore's dream"]
date: "2026-09-19"
solved: false
comments: ""
related: []
redo: 0
difficulty: 3
source: "Johann Bernoulli (1697); mathematical folklore"
---
# The Integral That Splits at a Threshold

Evaluate the definite integral

$$I = \int_0^1 x^x \, dx + \int_0^1 x^{-x} \, dx.$$

Wait — that's not quite it. Instead, evaluate:

$$I = \int_0^1 \left(x^x + x^{-x}\right) dx - 2\int_0^1 dx$$

...

Actually, let's state the real gem cleanly. Compute:

$$I = \int_0^1 x^x \, dx$$

and show it equals

$$I = \sum_{n=1}^{\infty} \frac{(-1)^{n+1}}{n^n} = 1 - \frac{1}{2^2} + \frac{1}{3^3} - \frac{1}{4^4} + \cdots$$
