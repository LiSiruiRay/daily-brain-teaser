# Answer: The Unfair Subway

## Key Idea / Intuition

Marvin's arrival time is uniform, so what matters is not how often each train comes, but how much of the timeline "belongs" to each train. A train captures Marvin exactly when he arrives in the gap just before it.

If every uptown train arrives only 1 minute after a downtown train, the uptown train owns a 1-minute window. The downtown train owns the remaining 9 minutes. Equal frequency does not mean equal waiting-gap length. Probabilities follow **gap length**, not **train count**. This is the same length-biased sampling behind the waiting-time (inspection) paradox.

---

## Formal Proof / Solution

**Setup.** The schedule repeats with period $T$. Place a downtown train at time $0$ and the uptown train at time $d$, so the next downtown train comes at time $T$. Because Marvin's arrival time is uniform over a long window compared with $T$, its position within the cycle is (essentially exactly) uniform on $[0, T)$. Call this position $U$.

**Part 1 and Part 2a: which train he takes.**

- If $U \in (0, d]$, the next train is the uptown one at time $d$.
- If $U \in (d, T]$, the next train is the downtown one at time $T$.

Therefore
$$
P(\text{uptown}) = \frac{d}{T}, \qquad P(\text{downtown}) = \frac{T-d}{T}.
$$

With $T = 10$ and $d = 1$, Marvin goes uptown with probability $1/10$. The mother's observation is explained without any bias on Marvin's part. The timetable alone does it.

More generally, *any* split $p \in (0,1)$ can be achieved with identical frequencies by choosing $d = pT$.

**Part 2b: expected wait.** If $U$ lands in a gap of length $g$, his wait is uniform on $[0, g]$, with mean $g/2$. The gap has length $d$ with probability $d/T$ and length $T - d$ with probability $(T-d)/T$. Hence
$$
\mathbb{E}[\text{wait}] = \frac{d}{T}\cdot\frac{d}{2} + \frac{T-d}{T}\cdot\frac{T-d}{2} = \frac{d^2 + (T-d)^2}{2T}.
$$

**Part 3: optimal offset.** The numerator $d^2 + (T-d)^2$ is a convex function of $d$, symmetric about $T/2$. So it is minimized at $d = T/2$, giving
$$
\mathbb{E}[\text{wait}]_{\min} = \frac{2\,(T/2)^2}{2T} = \frac{T}{4}.
$$

Interleaving the trains evenly gives a combined service every $T/2$ minutes, and the mean wait is half of that.

In Marvin's case ($T = 10$, $d = 1$):
$$
\mathbb{E}[\text{wait}] = \frac{1 + 81}{20} = 4.1 \text{ minutes},
$$
compared with the optimal $2.5$ minutes. The lopsided schedule is unfair to his mother and also wastes his time.

**Bonus: the hidden assumption.** "Each direction has equal frequency, so each is equally likely" silently assumes the train events are **symmetric in time relative to each other**. One instance is an offset of $d = T/2$. Another is an offset that is itself random and uniform on $[0, T)$: then averaging $d/T$ over $d$ gives $1/2$.

The general principle is that a uniformly random observer lands in a gap with probability proportional to its length. Size-biased sampling therefore favours long gaps. The same mechanism gives the classical waiting-time formula
$$
\mathbb{E}[\text{wait}] = \frac{\mathbb{E}[G^2]}{2\,\mathbb{E}[G]}
$$
for gaps $G$. This is why, with irregular buses, you wait longer on average than half the mean gap.
