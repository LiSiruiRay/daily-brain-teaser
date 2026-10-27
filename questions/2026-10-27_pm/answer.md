# Answer: Exactly Twice Is Impossible

## Key Idea / Intuition

If $f(a)=f(b)$, then on $[a,b]$ the graph is a "hill" (or a "valley"). The top of the hill, at height $M$, must be hit exactly twice. Values just below $M$ are then hit too often:
- Each side of the hill crosses those values once.
- The second preimage of $M$ forces at least one more crossing.

So you get at least $3$ preimages. That breaks "exactly twice."

---

## Formal Proof / Solution

Suppose, for contradiction, that $f$ is continuous and every value has exactly two preimages.

**Step 1: Set up a hill.**
Pick any $c$ and let $a<b$ be its two preimages, so $f(a)=f(b)=c$. On $(a,b)$, $f\neq c$. Since $(a,b)$ is connected, by the IVT either $f>c$ throughout $(a,b)$ or $f<c$ throughout. Replacing $f$ by $-f$ if necessary (which preserves the hypothesis), assume
$$
f(x)>c \quad\text{for all } x\in(a,b).
$$

**Step 2: Take the top of the hill.**
By compactness, $f$ attains its maximum $M$ on $[a,b]$ at some point $p$. Since $f>c$ inside, we have $M>c$ and $p\in(a,b)$. The value $M$ has exactly one other preimage $q\neq p$. There are two cases.

**Case A: $q\in[a,b]$.**
Then $q\in(a,b)$, because $f(a)=f(b)=c<M$. Say $p<q$; the case $q<p$ is symmetric.
- $f$ is not constant on $[p,q]$, since otherwise $M$ would have infinitely many preimages.
- So $m:=\min_{[p,q]}f<M$, attained at some $s\in(p,q)$.

Choose any $y$ with $\max(c,m)<y<M$. By the IVT, $y$ is attained:
- on $(a,p)$, since $f(a)=c<y<M=f(p)$;
- on $(p,s)$, since $f(p)=M>y>m=f(s)$;
- on $(s,q)$, since $f(s)=m<y<M=f(q)$;
- on $(q,b)$, since $f(q)=M>y>c=f(b)$.

These intervals are disjoint, so $y$ has at least $4$ preimages. Contradiction.

**Case B: $q\notin[a,b]$.**
Say $q>b$; the case $q<a$ is symmetric. Take any $y\in(c,M)$. By the IVT, $y$ is attained:
- on $(a,p)$, since $f(a)=c<y<M=f(p)$;
- on $(p,b)$, since $f(p)=M>y>c=f(b)$;
- on $(b,q)$, since $f(b)=c<y<M=f(q)$.

That gives at least $3$ preimages. Contradiction.

Both cases are impossible, so no such $f$ exists. $\blacksquare$

---

## Remarks on the Bonus

**Exactly three times is possible.** Take a "rising zigzag" built from piecewise-linear pieces:
- On $[0,1]$, go from $0$ up to $2$.
- On $[1,2]$, go from $2$ down to $1$.
- On $[2,3]$, go from $1$ up to $3$.

Then extend so that $f(x+3)=f(x)+3$. Each unit band of values is crossed by three consecutive monotone pieces. With care at the corner points (the "turning" values), every $y$ is hit exactly three times.

**General parity theorem.** A continuous $f:\mathbb{R}\to\mathbb{R}$ taking each value exactly $n$ times exists if and only if $n$ is odd. Here is the idea for even $n$:
- For large $|x|$, $f$ must tend to $\pm\infty$ in a consistent way.
- If both ends go to the same infinity, a large value $y$ is crossed an even number of times. If the ends go to opposite infinities, it is crossed an odd number of times.
- A local-extremum counting argument, generalizing the hill argument above, then rules out the even case.

The proof above is the cleanest instance of this: **local extrema create excess preimages.**
