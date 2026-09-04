# Answer: The Polynomial That Divides Its Own Composition

## Key Idea / Intuition

The magic here is a single observation: for any polynomial $f$ with integer coefficients and any integers $a, b$, we have $(a - b) \mid (f(a) - f(b))$. So if we let $a = f(n) + 1$ and $b = n$, then $(f(n) + 1 - n) \mid (f(f(n)+1) - f(n))$. This lets us control $f(f(n)+1)$ modulo $f(n)$. The "positive integer coefficients" condition then prevents accidental cancellation and pins down why only $n=1$ works.

---

## Formal Proof / Solution

**Setup and the key divisibility lemma.**

For any polynomial $f$ with integer coefficients and integers $a, b$:
$$(a - b) \mid (f(a) - f(b)).$$

This follows because $a^k - b^k = (a-b)(a^{k-1} + \cdots + b^{k-1})$, so each term of $f(a) - f(b)$ is divisible by $(a-b)$.

---

**Step 1: Reduce $f(f(n)+1)$ modulo $f(n)$.**

Apply the lemma with $a = f(n) + 1$ and $b = n$:

$$\bigl(f(n) + 1 - n\bigr) \mid \bigl(f(f(n)+1) - f(n)\bigr).$$

So:
$$f(f(n)+1) \equiv f(n) \pmod{f(n)+1-n}.$$

But we want to work modulo $f(n)$ itself. Apply the lemma differently: set $a = f(n)+1$, $b = 1$:

$$(f(n)) \mid (f(f(n)+1) - f(1)).$$

That is:
$$f(f(n)+1) \equiv f(1) \pmod{f(n)}.$$

---

**Step 2: Use this to analyze when $f(n) \mid f(f(n)+1)$.**

From Step 1:
$$f(n) \mid f(f(n)+1) \iff f(n) \mid f(1).$$

(Since $f(f(n)+1) \equiv f(1) \pmod{f(n)}$, divisibility of $f(f(n)+1)$ by $f(n)$ is equivalent to $f(n) \mid f(1)$.)

---

**Step 3: Since coefficients are positive integers, $f$ is strictly increasing on positive integers.**

Because $f$ has positive integer coefficients and is nonconstant, write $f(x) = a_d x^d + \cdots + a_1 x + a_0$ with $a_i \geq 0$, $a_d \geq 1$, $d \geq 1$. For positive integers $n \geq 1$:

$$f(n) \geq n \cdot a_1 + a_0 \geq 1,$$

and more importantly $f(n) \geq f(1) \geq 1$ with equality **only if $n = 1$** (since each term $a_i n^i \geq a_i \cdot 1^i$ for $n \geq 1$, and at least one term is strictly increasing).

Precisely: for $n \geq 2$, since $a_d \geq 1$ and $d \geq 1$:
$$f(n) \geq n^d \geq n \geq 2 > 1 = f(1) \text{ only if } f(1)=1,$$

but in general $f(n) > f(1)$ for $n > 1$ because all coefficients are positive:

$$f(n) - f(1) = \sum_{k=1}^{d} a_k(n^k - 1) \geq a_d(n^d - 1) \geq n^d - 1 \geq n - 1 \geq 1 > 0.$$

So for $n \geq 2$: $f(n) > f(1) \geq 1$, which means $f(n) \nmid f(1)$ (a larger positive integer cannot divide a smaller positive integer).

---

**Step 4: Conclusion.**

- If $n = 1$: $f(n) = f(1)$ and we need $f(1) \mid f(1)$, which is obviously true. ✓

- If $n \geq 2$: $f(n) > f(1) \geq 1$, so $f(n) \nmid f(1)$, hence $f(n) \nmid f(f(n)+1)$. ✗

Therefore, $f(n) \mid f(f(n)+1)$ **if and only if** $n = 1$. $\blacksquare$

---

**The elegant summary:**

$$f(f(n)+1) \equiv f(1) \pmod{f(n)},$$

and for $n \geq 2$, $f(n) > f(1)$ because all coefficients are positive, so no divisibility can occur.
