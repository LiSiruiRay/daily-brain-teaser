# A Continuous but Nowhere Differentiable Function

## Problem

Define
$$f(x) = \sum_{n=0}^{\infty} \left(\frac{1}{2}\right)^n \cos(4^n \pi x).$$

**(a)** Show that $f$ is continuous on $\mathbb{R}$.

**(b)** Show (or argue convincingly) that $f$ is **nowhere differentiable** — it has no derivative at any point $x \in \mathbb{R}$.

---

## Field
Real Analysis

## Why It's Beautiful

For most of mathematical history, people believed that a continuous function must be differentiable "almost everywhere" — corners and cusps are exceptional. Weierstrass shocked the mathematical world in 1872 by exhibiting a function that is continuous everywhere but differentiable **nowhere**.

The construction is almost magical: you build up a function by adding oscillations at every scale, with amplitudes shrinking just fast enough to ensure continuity, but frequencies growing fast enough to destroy all derivatives. It is one of the most famous counterexamples in analysis.

## Key Idea / Trick

**Continuity**: The series converges uniformly by the Weierstrass M-test (terms are bounded by $(1/2)^n$, which is summable), and each term is continuous, so the sum is continuous.

**Non-differentiability**: If $f'(x_0)$ existed, then difference quotients $[f(x_0+h) - f(x_0)]/h$ would converge to a finite limit. But by choosing $h_m = \pm 4^{-m}$ carefully, the $m$-th term of the series contributes a difference quotient of order $4^m \cdot (1/2)^m = 2^m \to \infty$, while earlier terms can be controlled — contradiction.

## Difficulty
3 / 5

## Tags
Real Analysis, Weierstrass function, Uniform convergence, M-test, Counterexample, Differentiability, Fractal
