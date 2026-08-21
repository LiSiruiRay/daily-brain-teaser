# Answer: Central Binomial Coefficient mod Prime

## Key Idea / Intuition

The central binomial coefficient $\binom{2p}{p} = \frac{(2p)!}{(p!)^2}$ looks complicated, but modulo $p$ almost everything cancels. The numerator $(2p)!$ and denominator $(p!)^2$ share many factors, and Wilson's theorem (or a direct product argument) reveals that all factors except two copies of "$p$" cancel, leaving exactly $2$ mod $p$.

---

## Formal Proof / Solution

**Step 1: Write out the binomial coefficient.**

$$\binom{2p}{p} = \frac{(2p)!}{p! \cdot p!} = \frac{(2p)(2p-1)\cdots(p+1)}{p!}.$$

So we can write:

$$\binom{2p}{p} = \frac{\prod_{k=1}^{p}(p+k)}{\prod_{k=1}^{p} k}.$$

**Step 2: Analyze the numerator factor by factor mod $p$.**

For each $k \in \{1, 2, \ldots, p\}$:

$$p + k \equiv k \pmod{p}.$$

Therefore:

$$\prod_{k=1}^{p}(p+k) \equiv \prod_{k=1}^{p} k = p! \pmod{p \cdot p!}$$

Wait — let's be more careful and work directly.

**Step 3: Direct computation via the product formula.**

$$\binom{2p}{p} = \prod_{k=1}^{p} \frac{p+k}{k}.$$

For $k = p$: the factor is $\frac{2p}{p} = 2$.

For $k = 1, 2, \ldots, p-1$: the factor is $\frac{p+k}{k} = 1 + \frac{p}{k}$.

So:

$$\binom{2p}{p} = 2 \cdot \prod_{k=1}^{p-1}\left(1 + \frac{p}{k}\right).$$

**Step 4: Reduce modulo $p$.**

Each factor $\left(1 + \frac{p}{k}\right)$ — we want to think of this inside $\mathbb{Z}$. Since $\gcd(k, p) = 1$ for $k = 1, \ldots, p-1$ (as $p$ is prime), each $\frac{p}{k}$ is an integer multiple of $p$ divided by $k$, but $\binom{2p}{p}$ is an integer so the full product is an integer.

More cleanly: write

$$\binom{2p}{p} = \frac{(2p)!}{(p!)^2}.$$

By **Lucas' theorem**: for a prime $p$, and writing $2p$ and $p$ in base $p$:

$$2p = 2 \cdot p + 0, \quad p = 1 \cdot p + 0.$$

Lucas' theorem states:

$$\binom{2p}{p} \equiv \binom{2}{1}\binom{0}{0} = 2 \cdot 1 = 2 \pmod{p}.$$

**Alternatively (elementary):** Factor out the $k=p$ term:

$$\binom{2p}{p} = \frac{(2p)(2p-1)\cdots(p+1)}{p!} = 2 \cdot \frac{(2p-1)(2p-2)\cdots(p+1)}{(p-1)!}.$$

Now look at $S := \frac{(2p-1)(2p-2)\cdots(p+1)}{(p-1)!}$. The numerator is the product of integers $p+1, p+2, \ldots, 2p-1$ (that's $p-1$ terms), and the denominator is $(p-1)!$, so $S = \binom{2p-1}{p-1}$ is an integer. Modulo $p$:

$$\prod_{j=1}^{p-1}(p+j) \equiv \prod_{j=1}^{p-1} j = (p-1)! \pmod{p},$$

so

$$S = \frac{\prod_{j=1}^{p-1}(p+j)}{(p-1)!} \equiv \frac{(p-1)!}{(p-1)!} = 1 \pmod{p}.$$

Therefore:

$$\binom{2p}{p} = 2 \cdot S \equiv 2 \cdot 1 = 2 \pmod{p}. \qquad \blacksquare$$

**Remark.** This is actually the heart of why $\frac{1}{p}\binom{2p}{p}$ — which arises in Catalan number territory — is always an integer that is $\equiv \frac{2}{p}$... but $2/p$ only makes sense mod $p$, hinting at deeper divisibility in the Catalan numbers.
