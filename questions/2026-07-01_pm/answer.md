# Answer: The Gambler Who Can't Lose... Until He Does

## Key Idea / Intuition

For a biased game ($p > 1/2$), there is a genuine chance of escaping ruin forever — the random walk drifts upward, so with positive probability it never returns to 0. The probability of eventual ruin from fortune $k$ is $(q/p)^k$, so starting from \$1, ruin probability is exactly $q/p < 1$, meaning survival probability is $1 - q/p > 0$.

For the **fair game**, the shocking answer is: the gambler is **ruined with probability 1**. Despite having no negative drift, a simple random walk on $\mathbb{Z}$ is recurrent — it visits every state infinitely often, so it will inevitably hit 0. The survival probability is exactly **0**.

This contrast is the heart of the problem: a tiny positive drift makes all the difference between certain doom and genuine hope.

---

## Formal Proof / Solution

### Setup: Gambler's Ruin

Let $p_k$ = probability of eventual ruin starting from fortune $k \geq 1$.

The ruin probability satisfies the recurrence:
$$p_k = p \cdot p_{k+1} + q \cdot p_k \cdot p_1 \cdot \ldots$$

More cleanly: let $r$ = probability of ruin starting from \$1. By the Markov property and independence of games, the probability of ruin from fortune $k$ is $r^k$ (to be ruined from $k$, you must be ruined $k$ times in a row from fortune 1 — or more precisely, ruin from $k$ requires first hitting $k-1$, then $k-2$, ..., then $0$, each with probability $r$).

So ruin from \$1 satisfies:
$$r = p \cdot r^2 + q \cdot 1$$

(from \$1: win with prob $p$ → now at \$2, need $r^2$ to reach 0; lose with prob $q$ → immediately at \$0.)

This gives the quadratic:
$$p r^2 - r + q = 0$$

Dividing by $p$:
$$r^2 - \frac{1}{p}r + \frac{q}{p} = 0$$

Factor: $(r - 1)\!\left(r - \frac{q}{p}\right) = 0$

So the two solutions are $r = 1$ and $r = q/p$.

**Which root do we take?**

We need the **smallest non-negative solution** (this is the standard theory of branching processes / random walk — take the root in $[0,1]$).

- If $p > 1/2$: then $q/p < 1$, so the two roots are $q/p$ and $1$. The smallest non-negative root is $r = q/p$.
- If $p = 1/2$: then $q/p = 1$, so both roots coincide at $r = 1$.
- If $p < 1/2$: then $q/p > 1$, so the only root in $[0,1]$ is $r = 1$.

### Results

**Biased game ($p > 1/2$), starting from \$1:**
$$\Pr(\text{ruin}) = \frac{q}{p} < 1$$
$$\boxed{\Pr(\text{never ruined}) = 1 - \frac{q}{p} = \frac{p - q}{p} > 0}$$

For example, if $p = 2/3$: survival probability $= 1 - (1/3)/(2/3) = 1/2$.

**Fair game ($p = 1/2$), starting from \$1:**
$$\Pr(\text{ruin}) = 1 \implies \boxed{\Pr(\text{never ruined}) = 0}$$

### Why Is the Fair Game Result Surprising?

The gambler has **no expected loss** per round — his expected fortune grows linearly at rate $0$. Yet he is **certain to be ruined**. 

The deeper reason: simple symmetric random walk in 1D is **recurrent** — it returns to every state with probability 1. In particular, it returns to 0. There is no escape.

In contrast, simple random walk in 3D is **transient** — it escapes to infinity with positive probability. Dimensionality (or drift) is what separates hope from doom.

The moral: **zero expected loss does not mean zero risk of ruin.** The gambler needs a strict positive edge ($p > 1/2$) just to have a fighting chance of surviving forever.
