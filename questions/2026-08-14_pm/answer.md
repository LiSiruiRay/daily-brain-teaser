# Answer: The Derivative That Divides 2016

## Key Idea / Intuition

The key is to think about what $j$-th derivatives of integer-coefficient polynomials look like at integers. The natural basis for integer-valued polynomials is not $\{1, x, x^2, \ldots\}$ but the **binomial coefficients** $\binom{x}{n}$. Taking $j$ derivatives of $x^n$ produces $n(n-1)\cdots(n-j+1) x^{n-j}$, and at integers this must be divisible by $2016$ for all valid $n \geq j$. So we need $j!$ to be divisible by $2016$, and we want the smallest such $j$.

More precisely: the $j$-th derivative of $x^n$ at $x = k$ is $n(n-1)\cdots(n-j+1)k^{n-j}$, a product of $j$ consecutive integers times $k^{n-j}$. The "worst case" is $n = j$, giving $j!$. So we need $2016 \mid j!$.

---

## Formal Proof / Solution

**Step 1: Factor 2016.**

$$2016 = 2^5 \cdot 3^2 \cdot 7$$

**Step 2: Reduce to divisibility of $j!$.**

Every polynomial with integer coefficients can be written uniquely in the basis of falling factorials / binomial coefficients. It suffices to check the monomials $p(x) = x^n$ for $n \geq j$ (since lower-degree polynomials have zero $j$-th derivative). The $j$-th derivative of $x^n$ is

$$\frac{d^j}{dx^j} x^n = n(n-1)\cdots(n-j+1)\, x^{n-j}.$$

At an integer $k$, this equals $\frac{n!}{(n-j)!} \cdot k^{n-j}$.

The hardest case to make divisible by $2016$ is $n = j$, $k = 1$ (or any $k$ coprime to $2016$), giving:

$$p^{(j)}(1) = j! \cdot 1^0 = j!.$$

So we **need** $2016 \mid j!$.

**Step 3: Conversely, if $2016 \mid j!$, does it always work?**

For general $n \geq j$ and integer $k$:
$$\frac{n!}{(n-j)!} \cdot k^{n-j} = j! \cdot \binom{n}{j} \cdot k^{n-j}.$$

If $2016 \mid j!$, then $2016$ divides $j! \cdot \binom{n}{j} \cdot k^{n-j}$ for all integers $k$ and all $n \geq j$. So divisibility of $j!$ by $2016$ is both **necessary and sufficient**.

**Step 4: Find the smallest $j$ with $2016 \mid j!$.**

We need $2^5 \cdot 3^2 \cdot 7 \mid j!$.

- The factor $7$ requires $j \geq 7$ (since $7! = 5040$ contains one factor of 7).
- Check $j = 7$: $7! = 5040 = 2^4 \cdot 3^2 \cdot 5 \cdot 7$. This gives only $2^4$, but we need $2^5$. So $7 \nmid$ our requirement — wait, actually the issue is the power of 2: $7!$ contributes $\lfloor 7/2 \rfloor + \lfloor 7/4 \rfloor = 3 + 1 = 4$ factors of 2. We need 5.
- Check $j = 8$: $8! = 40320$. Powers of 2 in $8!$: $\lfloor 8/2\rfloor + \lfloor 8/4\rfloor + \lfloor 8/8\rfloor = 4 + 2 + 1 = 7 \geq 5$. ✓  
  Powers of 3: $\lfloor 8/3\rfloor + \lfloor 8/9\rfloor = 2 + 0 = 2 \geq 2$. ✓  
  Powers of 7: $\lfloor 8/7\rfloor = 1 \geq 1$. ✓

So $2016 \mid 8!$ but $2016 \nmid 7!$ (since $7!$ only has $2^4$, missing one factor of 2).

**Conclusion:**

$$\boxed{j = 8}$$
