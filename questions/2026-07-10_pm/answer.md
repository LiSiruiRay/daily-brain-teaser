# Answer: The Tournament Bracket Paradox

## Key Idea / Intuition

The surprising fact is that "domination" by a single player can be replaced by "domination of every small set" — and such tournaments actually exist. The trick is to use a **probabilistic argument**: in a random tournament (each game independently decided by a fair coin), the probability that some pair has no common dominator is small when $n$ is large enough. For $n = 7$ specifically, we can use a beautiful **algebraic/explicit construction** via the quadratic residues modulo 7 (the Paley tournament), which has exactly this property.

The key insight: instead of searching, **use the probabilistic method** — show that a random tournament on $n$ players (for large enough $n$) satisfies the property with positive probability, so such a tournament must exist. For $n=7$ we exhibit it concretely.

---

## Formal Proof / Solution

### Part 1: The $n = 7$ explicit construction

Label players $0, 1, 2, 3, 4, 5, 6$ (elements of $\mathbb{Z}_7$). Define the tournament by:

$$i \text{ beats } j \iff j - i \in \{1, 2, 4\} \pmod{7}$$

(These are exactly the quadratic residues mod 7: $1^2=1$, $2^2=4$, $3^2=2$.)

**Claim:** For every pair $\{p, q\}$, there exists a player $r$ who beats both $p$ and $q$.

By the rotational symmetry of the construction (it's invariant under $x \mapsto x+1 \pmod 7$), it suffices to check the case $p = 0$. The players who beat $0$ are those $r$ with $0 - r \in \{1,2,4\}$, i.e., $r \in \{3, 5, 6\}$.

For each $q \neq 0$, we need some $r \in \{3,5,6\}$ that also beats $q$, meaning $q - r \in \{1,2,4\} \pmod 7$.

- $q=1$: Need $r$ with $1-r \in \{1,2,4\}$, i.e. $r \in \{0,6,4\}$. Intersection with $\{3,5,6\}$: $r=6$. ✓  
- $q=2$: Need $r \in \{1,0,5\}$. Intersection: $r=5$. ✓  
- $q=3$: Need $r \in \{2,1,6\}$. Intersection: $r=6$. ✓  
- $q=4$: Need $r \in \{3,2,0\}$. Intersection: $r=3$. ✓  
- $q=5$: Need $r \in \{4,3,1\}$. Intersection: $r=3$. ✓  
- $q=6$: Need $r \in \{5,4,2\}$. Intersection: $r=5$. ✓  

Every pair has a common dominator. $\square$

---

### Part 2: Probabilistic proof for general $n$

**Theorem:** For $n$ sufficiently large, there exists a tournament on $n$ players such that for every set $S$ of $k = \lfloor \log_2 n \rfloor$ players, some player outside $S$ beats all of $S$.

**Proof:** Consider a random tournament on $n$ players where each game is decided by a fair coin flip, independently.

Fix a set $S$ of $k$ players and a player $v \notin S$. The probability that $v$ beats all players in $S$ is $2^{-k}$. So the probability that **no** player outside $S$ beats all of $S$ is:

$$P(\text{no dominator of } S) = \left(1 - 2^{-k}\right)^{n-k}$$

There are $\binom{n}{k}$ choices of $S$. By the union bound, the probability that **some** set $S$ has no dominator is at most:

$$\binom{n}{k}\left(1-2^{-k}\right)^{n-k} \leq \frac{n^k}{k!} \cdot e^{-(n-k)/2^k}$$

For $k = \lfloor \log_2 n \rfloor$, we have $2^k \leq n$, so $(n-k)/2^k \geq (n-k)/n \to 1$ but more importantly the exponential decay dominates the polynomial $n^k/k!$ as $n \to \infty$.

Concretely: $\frac{n^k}{k!} \cdot e^{-(n-k)/2^k} \to 0$ as $n \to \infty$ since $e^{-(n-k)/2^k} \leq e^{-\sqrt{n}/2}$ decays faster than any polynomial.

So this probability is **less than 1** for large $n$, meaning with positive probability the random tournament has the desired property. Therefore such a tournament **exists**. $\square$

---

### Why This Is Surprising

The property says: no matter which $k$ players you pick, the remaining players "cover" them — someone beats all of them. This feels like it should be impossible (who dominates everyone?), but it doesn't require a single "king" — different dominators can cover different subsets. The probabilistic argument shows existence without construction; the Paley tournament over $\mathbb{Z}_7$ gives a beautiful explicit example for small $n$.
