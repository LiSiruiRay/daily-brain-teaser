# Answer: The Cliff-Hanger

## Key Idea / Intuition

**Self-similarity.** To fall from distance 2, the man must first get from 2 to 1, and then fall from 1. The walk is translation-invariant, so "getting from 2 to 1" is an exact copy of "getting from 1 to 0". The two stages are also independent. So if $P$ is the probability of ever falling from distance 1, the probability of ever falling from distance 2 is $P^2$.

**One-step equation.** Conditioning on the first step then gives a quadratic for $P$. Its roots are $1$ and $p/q$.

**Choosing the root.** The quadratic does not say which root is right. We pin it down by showing that the true probability lies below **every** nonnegative root. The true probability is built up from below, as the probability of falling within $n$ steps for larger and larger $n$. So it lands on the smallest root, not the largest.

**Answer.** For $p = \tfrac13$, the probability of falling is $\tfrac12$. In general it is $\min(1, p/q)$.

---

## Formal Proof / Solution

**Setup.** Let $P_k$ be the probability of ever reaching $0$ when starting from position $k \ge 1$.

**Step 1: $P_2 = P_1^2$.**
Any path from $2$ to $0$ moves by $\pm 1$, so it must pass through $1$.
- Let $T$ be the first time the walk hits $1$. Then $\Pr(T<\infty)$ is the probability of ever moving one unit closer. By translation invariance, this equals $P_1$.
- By the strong Markov property, the walk after time $T$ is a fresh walk started at $1$, independent of the past. It reaches $0$ with probability $P_1$.

Hence $P_2 = P_1 \cdot P_1 = P_1^2$. The same argument gives $P_k = P_1^k$ for every $k \ge 1$.

**Step 2: First-step analysis.**
From position $1$, he falls immediately with probability $p$. Otherwise, with probability $q$, he moves to position $2$. Therefore
$$P_1 = p + q\,P_1^2 \quad\Longleftrightarrow\quad qx^2 - x + p = 0 \quad (x = P_1).$$
Factor using $p + q = 1$:
$$qx^2 - x + p = (x-1)(qx - p),$$
so the roots are
$$x = 1 \qquad\text{and}\qquad x = \frac{p}{q}.$$

**Step 3: Which root?**
Let $x \ge 0$ be **any** nonnegative solution of $x = p + qx^2$. We claim $P_1 \le x$.

Define $u_n(k)$ as the probability of hitting $0$ within $n$ steps, starting from $k$. Set $u_n(0) = 1$ for all $n$.

We prove $u_n(k) \le x^k$ for all $n \ge 0$ and $k \ge 0$, by induction on $n$.
- **Base case $n = 0$.** We have $u_0(0) = 1 = x^0$, and $u_0(k) = 0 \le x^k$ for $k \ge 1$.
- **Inductive step.** For $k \ge 1$, condition on the first step:
$$u_{n+1}(k) = p\,u_n(k-1) + q\,u_n(k+1) \le p\,x^{k-1} + q\,x^{k+1} = x^{k-1}\bigl(p + qx^2\bigr) = x^{k-1}\cdot x = x^k.$$
For $k = 0$ the bound $u_{n+1}(0) = 1 = x^0$ holds trivially.

The events "fall within $n$ steps" increase with $n$, and their union is "eventually fall". So by continuity of probability,
$$P_1 = \lim_{n\to\infty} u_n(1) \le x.$$

**Step 4: Conclusion.**
By Step 2, $P_1$ is itself a root. By Step 3, it is at most every nonnegative root. So $P_1$ is the **smallest** nonnegative root:
$$\boxed{P_1 = \min\!\left(1, \frac{p}{q}\right)}$$

- **Part 1.** For $p = \tfrac13$ we get $q = \tfrac23$, so $P_1 = \dfrac{1/3}{2/3} = \tfrac12$.
- **Drift toward the cliff or fair walk ($p \ge \tfrac12$).** Then $p/q \ge 1$, so the smallest root is $1$ and he falls with certainty.
- **Drift away from the cliff ($p < \tfrac12$).** He falls with probability $p/q$. Starting $k$ steps away, the probability is $(p/q)^k$.

**Remarks.**
- At $p = \tfrac12$ the fall is certain, but the expected time until falling is infinite. This is the classic null-recurrent behaviour of the simple symmetric random walk.
- The equation $x = p + qx^2$ is exactly the extinction equation of a branching process in which each individual has either $0$ children (probability $p$) or $2$ children (probability $q$). In both settings, the correct answer is the smallest fixed point, and for the same monotone-iteration reason.
