# Answer: The Lost Boarding Pass

## Key Idea / Intuition

Ignore the messy chain of displaced passengers and ask which seat is left over at the end. By the time passenger $n$ boards, seats $2,\dots,n-1$ are all occupied, so the leftover seat is either seat $1$ or seat $n$, never anything else.

Every random chooser treats seat $1$ and seat $n$ identically: neither seat has an "owner" who will reclaim it before the end. So the first of these two seats to be taken is equally likely to be either one, and the answer is $\tfrac12$ for every $n \ge 2$. The same symmetry, applied to a larger set of "equivalent" seats, answers part (b).

---

## Formal Proof / Solution

**Setup: the chain of random choices.**

Call a passenger a *random chooser* if he picks a seat at random. That means passenger $1$, plus every displaced passenger. The choices happen at boarding times $t_0 = 1 < t_1 < t_2 < \cdots$, where each new random chooser is the owner of the seat just picked.

- If the pick at time $t_m$ is seat $1$, the chain stops: everyone afterwards finds his seat free.
- If the pick at time $t_m$ is seat $j \ne 1$, then $j > t_m$, because the seats of passengers $2,\dots,t_m$ are already occupied. Passenger $j$ is displaced, so $t_{m+1} = j$.

Thus the chain is strictly increasing in time.

**A uniformity lemma.**

Fix $k$ with $2 \le k \le n$ and let
$$S_k = \{1\} \cup \{k, k+1, \dots, n\}, \qquad |S_k| = n-k+2.$$

Before any random chooser picks a seat in $S_k$, every seat of $S_k$ is free:

- Seat $1$ has no owner left to claim it.
- Seats $k,\dots,n$ belong to passengers who have not boarded yet, since the chain has only reached times $< k$.

Let $T$ be the first random pick that lands in $S_k$. Then:

- **$T$ happens before passenger $k$ boards.** A pick in $\{2,\dots,k-1\}$ creates another random chooser who boards before time $k$. The increasing chain therefore cannot stall below $k$ without first landing in $S_k$.
- **The seat chosen at $T$ is uniform on $S_k$.** At every step before $T$, all seats of $S_k$ are free and the pick is uniform over the free seats. So, conditional on the pick lying in $S_k$, it is uniform on $S_k$.

**(b) Passenger $k$ is displaced exactly when the pick at $T$ is seat $k$.** Check the three possible outcomes:

- If the pick at $T$ is seat $1$, the chain stops and passenger $k$ finds his seat free.
- If the pick at $T$ is seat $j > k$, the next random chooser boards at time $j > k$. No one touches seat $k$ before passenger $k$ arrives, so it is free.
- If the pick at $T$ is seat $k$, passenger $k$ is displaced.

Therefore
$$\boxed{\;\Pr(\text{passenger } k \text{ finds his seat taken}) = \frac{1}{n-k+2}\;}$$

**(a)** Setting $k = n$ gives $S_n = \{1, n\}$, so
$$\Pr(\text{passenger } n \text{ gets his own seat}) = 1 - \frac12 = \boxed{\tfrac12},$$
independently of $n$ (for $n \ge 2$).

**Expected number of displaced passengers.** By linearity of expectation,
$$\mathbb{E}[\#\text{displaced}] = \sum_{k=2}^{n} \frac{1}{n-k+2} = \sum_{m=2}^{n}\frac1m = H_n - 1 \approx \ln n + \gamma - 1.$$
For $n = 100$ this is about $4.19$. Even on a large plane, only a handful of people are inconvenienced.

**Remark.** The answer $\tfrac12$ is surprising because the process looks complicated: a cascade of random displacements of unpredictable length. The insight is to stop tracking the dynamics and look only at the *terminal configuration*. The only seats that matter are those whose fate is decided purely by random choosers, and among those, symmetry makes every seat equally likely to be taken first.
