---
name: "Integral of (x-1)²/(2eˣ+x²+1)"
type: "Integration"
tags: ["Logarithmic derivative", "Integration bee", "Algebraic manipulation"]
date: "2026-04-04"
solved: false
comments: ""
related: []
redo: 0
---
# Integral of $(x-1)^2 / (2e^x + x^2 + 1)$

## Problem

Compute:
$$\int \frac{(x-1)^2}{2e^x + x^2 + 1}\, dx$$

---

## Field
Integration / Calculus

## Why It's Beautiful

The integrand looks completely intractable — an ugly mix of $e^x$ and a polynomial in both numerator and denominator. There's no obvious substitution and no standard form. Yet the answer is a clean closed form, found by a single algebraic observation.

The trick reveals that the "ugly" denominator was specifically crafted so its derivative nearly matches the numerator. This is a hallmark of integration bee problems: disguise a logarithmic derivative behind an intimidating face.

## Key Idea / Trick

Let $D = 2e^x + x^2 + 1$. Compute $D' = 2e^x + 2x$.

Then observe:
$$\frac{(x-1)^2}{D} = \frac{x^2 - 2x + 1}{D} = \frac{(2e^x + x^2 + 1) - (2e^x + 2x)}{D} = 1 - \frac{D'}{D}$$

The integrand is just $1 - D'/D$, which integrates immediately to $x - \ln D + C$.

## Difficulty
2 / 5

## Tags
Integration, Logarithmic derivative, Integration bee, Algebraic manipulation, Recognition trick
