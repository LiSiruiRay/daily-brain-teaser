# Answer: The Factorial That Unmasks e

## Key Idea / Intuition

Multiplying $e=\sum 1/k!$ by $n!$ turns every term with $k\le n$ into an integer. The sine has period $2\pi$, so it ignores that integer part. Only the tail $\sum_{k>n} n!/k!$ survives, and it is about $\tfrac{1}{n+1}$. So $e\,n!$ is "almost an integer, plus about $1/n$." Then $\sin(2\pi\cdot\text{small})\approx 2\pi\cdot\text{small}$, and multiplying by $n$ gives about $2\pi$. The factorial matters because $n!$ is divisible by every $k!$ with $k\le n$; a plain multiplier $n$ has no such property.

---

## Formal Proof / Solution

**Step 1: Split $e\,n!$ into an integer and a tail.**
Using $e=\sum_{k\ge 0}\frac{1}{k!}$,
$$e\,n! \;=\; \underbrace{\sum_{k=0}^{n}\frac{n!}{k!}}_{=:N_n\in\mathbb Z} \;+\; \underbrace{\sum_{k=n+1}^{\infty}\frac{n!}{k!}}_{=:r_n}.$$
Each $n!/k!$ with $k\le n$ is an integer, so $N_n\in\mathbb Z$. By $2\pi$-periodicity,
$$\sin(2\pi e\,n!) = \sin(2\pi r_n).$$

**Step 2: Squeeze the tail.**
Write the tail out term by term:
$$r_n = \frac{1}{n+1} + \frac{1}{(n+1)(n+2)} + \frac{1}{(n+1)(n+2)(n+3)} + \cdots$$
- Lower bound: keeping only the first term gives $r_n > \dfrac{1}{n+1}$.
- Upper bound: replace every factor $(n+j)$ by $(n+1)$. This gives the geometric series
$$r_n < \sum_{j\ge 1}\frac{1}{(n+1)^j} = \frac{1/(n+1)}{1-1/(n+1)} = \frac1n.$$

Hence
$$\frac{n}{n+1} < n\,r_n < 1, \qquad\text{so}\qquad n\,r_n \to 1 \quad\text{and}\quad r_n\to 0.$$

**Step 3: Linearize the sine.**
Since $2\pi r_n\to 0$ and $\frac{\sin x}{x}\to 1$ as $x\to 0$,
$$n\sin(2\pi e\,n!) = n\sin(2\pi r_n) = 2\pi\,(n r_n)\cdot\frac{\sin(2\pi r_n)}{2\pi r_n} \;\longrightarrow\; 2\pi\cdot 1\cdot 1 = 2\pi.$$

$$\boxed{\displaystyle\lim_{n\to\infty} n\sin(2\pi e\,n!) = 2\pi}$$

**Why the contrast with $\sin(2\pi e n)$:** The value of $\sin(2\pi e n)$ depends only on the fractional part $\{en\}$. Because $e$ is irrational, Weyl/Kronecker equidistribution makes $\{en\}$ dense in $[0,1)$, with no structure. With $n!$, the fractional part of $e\,n!$ is exactly $r_n$, which marches deterministically to $0$ like $1/n$. The factorials are tailored to the series of $e$.

**Bonus: $e$ is irrational.**
Suppose $e=p/q$. For any $n\ge q$, $e\,n! = p\cdot\frac{n!}{q}$ is an integer, so $r_n = e\,n!-N_n$ is an integer. But Step 2 gives $0<r_n<\frac1n\le 1$, and no integer lies strictly between $0$ and $1$. Contradiction. $\blacksquare$

(Equivalently: if $e$ were rational, $\sin(2\pi e\,n!)$ would be $0$ for all large $n$, and the limit would be $0$, not $2\pi$.)
