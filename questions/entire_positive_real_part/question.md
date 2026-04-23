# Problem: An Entire Function with Non-Negative Real Part

## Problem Statement

Suppose $f : \mathbb{C} \to \mathbb{C}$ is entire (holomorphic on all of $\mathbb{C}$) and satisfies

$$\operatorname{Re}(f(z)) \geq 0 \quad \text{for all } z \in \mathbb{C}.$$

Prove that $f$ must be **constant**.

---

## Metadata

| Field | Details |
|---|---|
| **Field** | Complex Analysis |
| **Tags** | Entire functions, Liouville's theorem, Möbius transformation, Bounded functions |
| **Difficulty** | 2 / 5 |
| **Date** | 2026-04-23 |

## Why It's Interesting

At first glance, having non-negative real part seems like a very *mild* geometric constraint — it just says the image of $f$ lands in the closed right half-plane. Yet this alone forces $f$ to be constant. The surprising punch comes from a one-line composition trick that converts a geometric condition on the *image* into boundedness, then Liouville does the rest.

The key technique — composing with a Möbius transformation to "compress" an unbounded region into the unit disk — is a genuinely powerful and reusable idea in complex analysis.

## Key Idea / Hint

Consider composing $f$ with a carefully chosen Möbius transformation that maps the right half-plane $\{\operatorname{Re}(w) \geq 0\}$ into the closed unit disk $\{|w| \leq 1\}$. What happens to the composition?

## Answer

See [answer.md](answer.md)
