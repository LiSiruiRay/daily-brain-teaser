# Answer: The Absent Ticket Inspector

## Key Idea / Intuition

The answer is exactly $\frac{1}{2}$, **independent of $n$**. This is shocking — with 100 or 1,000,000 passengers, the last person still has a 50/50 chance. The key insight is that throughout the entire process, the "fate" of the last seat is determined by a single competition: **at every displacement, the displaced passenger randomly chooses either seat 1 (your seat) or seat $n$ (their seat), or they pass the problem along**. The last seat is eventually "claimed" by one of these two outcomes, and by symmetry they are equally likely.

---

## Formal Proof / Solution

**Setup:** Label the seats $1, 2, \ldots, n$. You (passenger 1) sit randomly. Passenger $k$ sits in seat $k$ if free, otherwise picks randomly among free seats. We want $P(\text{passenger } n \text{ sits in seat } n)$.

**Key observation:** At any moment during boarding, the only "contested" seats are seat $1$ (yours, the one you stole) and seat $n$ (the last seat). All other seats will eventually be resolved.

**Elegant symmetry argument:**

Consider the following invariant: whenever a displaced passenger must choose a random free seat, **seat 1 and seat $n$ are always equally likely to be chosen** (since neither is ever "preferentially" occupied during the random choices).

More precisely, we prove by induction: the last passenger sits in seat $n$ with probability $\frac{1}{2}$.

**Base case $n = 2$:** You sit randomly in seat 1 or seat 2, each with probability $\frac{1}{2}$. If you sit in seat 1 (your own), passenger 2 gets seat 2. If you sit in seat 2, passenger 2 is displaced and gets seat 1. So $P(\text{last in own seat}) = \frac{1}{2}$. ✓

**Inductive step:** Suppose the result holds for $n-1$ passengers. With $n$ passengers:

- With probability $\frac{1}{n}$, you sit in seat 1 (your own) → everyone boards correctly → passenger $n$ gets seat $n$. ✓
- With probability $\frac{1}{n}$, you sit in seat $n$ → passenger $n$ is immediately displaced → passenger $n$ cannot sit in seat $n$. ✗
- With probability $\frac{k}{n}$ (for seats $2 \leq k \leq n-1$, i.e., probability $\frac{n-2}{n}$), you sit in seat $k$ for some $2 \leq k \leq n-1$.

In the last case, passengers $2, \ldots, k-1$ sit normally. Passenger $k$ is displaced and now faces the **same problem** with $n - k + 1$ remaining seats (including seat 1 and seat $n$). By the symmetry of the random choice, this sub-problem has exactly the same structure as the original with fewer passengers.

By summing over all $k$:

$$P_n = \frac{1}{n} \cdot 1 + \frac{1}{n} \cdot 0 + \sum_{k=2}^{n-1} \frac{1}{n} \cdot P_{n-k+1}$$

where $P_j$ is the probability for $j$ passengers. Using $P_2 = \frac{1}{2}$ and assuming $P_j = \frac{1}{2}$ for all $j < n$:

$$P_n = \frac{1}{n} + 0 + \sum_{k=2}^{n-1} \frac{1}{n} \cdot \frac{1}{2} = \frac{1}{n} + \frac{n-2}{n} \cdot \frac{1}{2} = \frac{1}{n} + \frac{n-2}{2n} = \frac{2 + n - 2}{2n} = \frac{n}{2n} = \frac{1}{2}.$$

**The cleanest way to see it:** The process terminates when either seat 1 or seat $n$ is chosen by a displaced passenger. At that moment, the choice is **uniform** between these two seats (both are always free until one is taken). So:

$$P(\text{seat } n \text{ chosen first}) = \frac{1}{2}.$$

**Answer:** $\boxed{\dfrac{1}{2}}$, for all $n \geq 2$.
