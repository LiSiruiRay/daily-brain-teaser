# Truncated Exponential Has No Repeated Roots

## Problem

Define the **truncated exponential polynomial**:
$$p_n(x) = 1 + x + \frac{x^2}{2!} + \frac{x^3}{3!} + \cdots + \frac{x^n}{n!}$$

Prove that $p_n(x)$ has **no repeated real roots** for any $n \geq 1$.

---

## Field
Putnam / Analysis / Polynomials

## Why It's Beautiful

The truncated exponentials are the partial sums of $e^x$. They look complicated — their roots spread out in the complex plane and have no closed form. Yet the statement that they have no repeated real roots admits a **3-line proof** from a single elegant observation.

The key identity $p_n(x) = p_{n-1}(x) + x^n/n!$ is obvious once written down, but using it to kill repeated roots requires a small, satisfying twist.

## Key Idea / Trick

A repeated root $r$ of $p_n$ satisfies both $p_n(r) = 0$ and $p_n'(r) = 0$.

Note that $p_n'(x) = p_{n-1}(x)$, so $p_{n-1}(r) = 0$.

But $p_n(x) = p_{n-1}(x) + \dfrac{x^n}{n!}$, so $0 = 0 + \dfrac{r^n}{n!}$, giving $r = 0$.

Yet $p_n(0) = 1 \neq 0$. Contradiction.

## Difficulty
2 / 5

## Tags
Putnam, Polynomials, Repeated roots, Derivatives, Truncated exponential, Elegant identity
