# Answer: An Impossible Integer Polynomial

## A Natural but Failed Attempt

Write $P(x) = a_0 + a_1 x + a_2 x^2 + \cdots + a_n x^n$ with $a_i \in \mathbb{Z}$.

**The attempt**: Factor out $x$ from the non-constant terms:

$$P(7) = a_0 + 7\underbrace{(a_1 + 7a_2 + \cdots + 7^{n-1}a_n)}_{=:\, K \,\in\, \mathbb{Z}} = 11$$

$$P(11) = a_0 + 11\underbrace{(a_1 + 11a_2 + \cdots + 11^{n-1}a_n)}_{=:\, M \,\in\, \mathbb{Z}} = 13$$

So we need integers $a_0, K, M$ satisfying:
$$7K = 11 - a_0, \quad 11M = 13 - a_0.$$

Subtracting: $11M - 7K = 2$. The attempt was to show this linear Diophantine equation has **no integer solution**.

**Why it fails**: By Bezout's lemma, $11m - 7k = c$ has integer solutions if and only if $\gcd(7, 11) \mid c$. Since $\gcd(7, 11) = 1$, it divides every integer — so solutions always exist. In fact, $m = 4,\, k = 6$ gives $11(4) - 7(6) = 44 - 42 = 2$. The equation is perfectly satisfiable.

**The deeper issue**: Even if you continued to constrain $a_0$ — from $7K = 11 - a_0$ and $11M = 13 - a_0$ you get $a_0 \equiv 4 \pmod{7}$ and $a_0 \equiv 2 \pmod{11}$, and by CRT (since $\gcd(7,11)=1$) there is always an integer $a_0$ satisfying both. So the approach of constraining $a_0$ alone can never produce a contradiction.

**What goes wrong structurally**: The quantities $K$ and $M$ are *not* independent integers. They both depend on the same coefficients $a_1, \ldots, a_n$:
$$K = a_1 + 7a_2 + \cdots, \quad M = a_1 + 11a_2 + \cdots$$
So fixing $(a_0, K, M)$ doesn't mean you can freely choose coefficients — $K$ and $M$ are correlated through $a_1, \ldots, a_n$. The approach discards this coupling and loses all the information.

The correct approach instead looks at $P(11) - P(7)$ *directly*, without decomposing by $a_0$.

This actaully gave me an interesting thought: when you are trying to solve a problem like this, you tend to reduce it (not in the theory of computation sense), but the direction is important. Which information you chose to lose is important.

For example this attempt chose to lose the inner connection between $M$ and $K$, and reduced the problem to "show the linear Diophantine equation has **no integer solution**". That is clearly the wrong direction.


---

## Intuition First

Integer-coefficient polynomials are "rigid" with respect to integer inputs. If you know $P(a)$ and $P(b)$ for two integers $a, b$, their difference $P(a) - P(b)$ cannot be arbitrary — it is always divisible by $a - b$. This is because each monomial $x^n$ already has this property (since $a^n - b^n$ is divisible by $a - b$), and the whole polynomial inherits it by linearity.

So knowing $P(7)$ and $P(11)$ forces $4 \mid (P(11) - P(7))$. But $13 - 11 = 2$, and $4 \nmid 2$. Done.

---

## Key Lemma

**Lemma**: For any polynomial $P(x)$ with integer coefficients and any integers $a, b$:
$$(a - b) \mid (P(a) - P(b)).$$

**Proof**: It suffices to prove it for monomials $x^n$, since $P(a) - P(b)$ is a linear combination (with integer coefficients) of terms $a^n - b^n$.

The factorization
$$a^n - b^n = (a - b)(a^{n-1} + a^{n-2}b + \cdots + b^{n-1})$$
shows $(a-b) \mid (a^n - b^n)$ for all integers $a, b$ and $n \geq 1$. $\square$

---

## Proof of the Main Result

Suppose for contradiction that such a $P$ exists. By the lemma with $a = 11$, $b = 7$:

$$(11 - 7) \mid (P(11) - P(7))$$
$$4 \mid (13 - 11)$$
$$4 \mid 2.$$

This is a contradiction. Therefore no such polynomial exists. $\blacksquare$

---

## Why This Matters

The lemma $(a-b) \mid (P(a) - P(b))$ is a fundamental and reusable fact. It immediately gives:

- **Integer root test**: if $P(r) = 0$ for integer $r$, then $(r - a) \mid P(a)$ for any integer $a$, i.e., every integer root of $P$ divides the constant term (when leading coeff is 1).
- **Mod $p$ constraints**: if $P(a) \equiv P(b) \pmod{p}$ is required, you know $(a-b)$ must be divisible by $p$ — or the values themselves must conspire to cancel mod $p$.

The one-line proof is a perfect example of a Putnam technique: find a single invariant (here, divisibility) that rules out the entire family of candidates at once.
