# Answer: A Polynomial with Three Prescribed Values

## Key Idea / Intuition

The key insight is that for any polynomial $f$ with integer coefficients, the integer $m - n$ always divides $f(m) - f(n)$. So if $f(a) = f(b) = f(c) = 1$, then $(d - a)(d - b)(d - c)$ must divide $f(d) - 1$. With three distinct integers $a, b, c$, the product $(d-a)(d-b)(d-c)$ is a product of three distinct integers, whose absolute value is already too large to equal $1$ — which is what $f(d) - 1 = 1$ would require.

---

## Formal Proof / Solution

**Setup:** Let $f(x)$ have integer coefficients, with $f(a) = f(b) = f(c) = 1$ for distinct integers $a, b, c$.

**Key divisibility fact:** For any polynomial with integer coefficients and any integers $m, n$:
$$(m - n) \mid f(m) - f(n).$$
This follows because $m^k - n^k$ is divisible by $m - n$ for every non-negative integer $k$.

**Factoring out the roots of $f(x) - 1$:** Since $f(a) = f(b) = f(c) = 1$, the polynomial $f(x) - 1$ has $a, b, c$ as roots. We can write:
$$f(x) - 1 = (x - a)(x - b)(x - c) \cdot g(x)$$
for some polynomial $g(x)$ with integer coefficients (since $f(x) - 1$ has leading integer coefficients and $a, b, c$ are integer roots).

**Suppose for contradiction** that $f(d) = 2$ for some integer $d$. Then:
$$f(d) - 1 = 1 = (d - a)(d - b)(d - c) \cdot g(d).$$

So $(d - a)(d - b)(d - c)$ must be an integer that divides $1$, meaning:
$$(d - a)(d - b)(d - c) \in \{1, -1\}.$$

**But this is impossible.** The three quantities $d - a$, $d - b$, $d - c$ are three **distinct** integers (since $a, b, c$ are distinct). Their product can equal $\pm 1$ only if all three factors are in $\{-1, +1\}$. However, there are only two elements in $\{-1, +1\}$, so by the pigeonhole principle, at least two of $d-a, d-b, d-c$ must be equal — contradicting that $a, b, c$ are distinct.

**Conclusion:** No such integer $d$ with $f(d) = 2$ exists. $\blacksquare$

---

**Remark:** The argument shows more generally that if $f$ has integer coefficients and takes the value $v$ at $k$ distinct integers, then $f(d) = v + 1$ is impossible for any integer $d$ whenever $k \geq 3$ (or even $k = 2$ if you want the product of two distinct integers to equal $\pm 1$, which fails unless they are $\{-1, 1\}$, but adding a third kills it completely). The beauty is that the geometry of "three distinct points" collides with arithmetic of small numbers.
