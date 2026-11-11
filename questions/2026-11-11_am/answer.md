# Answer: Rolling for a Six, Seeing Only Evens

## Key Idea / Intuition

Conditioning on "no odd number before the first 6" is a survival condition. Long sequences have many chances to hit an odd number, so they are very unlikely to survive. The condition therefore strongly favors short sequences.

The clean way to see this is to ignore the rolls that don't matter. Rolls of $2$ or $4$ change nothing, so only the first roll landing in $\{1,3,5,6\}$ decides the outcome. The time of that first "decisive" roll is independent of which decisive face appears. So conditioning on that face being $6$ does not change the time.

The answer is $\tfrac32$, not $3$. The "3-sided die" picture is wrong because the condition does more than delete odd faces. It also deletes every long sequence in which an odd face would have appeared.

---

## Formal Proof / Solution

**Step 1: Reduce to the first decisive roll.**
Call a roll *decisive* if it lands in $D=\{1,3,5,6\}$. Let $T$ be the index of the first decisive roll. Each roll is decisive with probability $4/6 = 2/3$, independently, so
$$
T \sim \text{Geometric}(2/3), \qquad \mathbb{E}[T] = \tfrac{3}{2}.
$$

**Step 2: The event in question is "the first decisive roll is a 6".**
Let $A = \{\text{all rolls up to and including the first 6 are even}\}$. Before time $T$, every roll is $2$ or $4$.

- If roll $T$ shows $6$, then the first $6$ occurs at time $T$ and no odd number came before it. So $A$ occurs and $N=T$.
- If roll $T$ shows an odd number, then an odd number appears before any $6$, so $A$ fails.

Hence $A = \{X_T = 6\}$, and on $A$ we have $N = T$.

**Step 3: Independence of the time and the face.**
Given that a roll is decisive, its face is uniform on $D$, regardless of how many non-decisive rolls came before. Formally,
$$
\Pr(T=n,\ X_T=6) = \left(\tfrac13\right)^{n-1}\cdot\tfrac16 = \left[\left(\tfrac13\right)^{n-1}\tfrac23\right]\cdot\tfrac14 = \Pr(T=n)\cdot\Pr(X_T=6).
$$
So $T$ is independent of $X_T$, and $\Pr(A)=\tfrac14$.

**Step 4: Conclude.**
$$
\mathbb{E}[N\mid A] = \mathbb{E}[T \mid X_T=6] = \mathbb{E}[T] = \frac{3}{2}.
$$

**Sanity check by direct computation.**
$$
\mathbb{E}[N\mid A] = \frac{\sum_{n\ge1} n\left(\tfrac13\right)^{n-1}\tfrac16}{1/4} = \frac{2}{3}\sum_{n\ge1} n\left(\tfrac13\right)^{n-1} = \frac23\cdot\frac{1}{(1-\tfrac13)^2} = \frac23\cdot\frac94 = \frac32.
$$

**Where the "answer 3" goes wrong.**
That reasoning computes $\mathbb{E}[N]$ for a die whose faces are $\{2,4,6\}$. It assumes conditioning on $A$ only changes the per-roll distribution. In fact it reweights entire sequences: a sequence of length $n$ survives with probability proportional to $(1/3)^{n-1}$, not $(2/3)^{n-1}$. Equivalently, $\{N=n\}\cap A$ requires $n-1$ rolls from $\{2,4\}$. That is much rarer than $n-1$ rolls from $\{1,2,3,4,5\}\setminus\{1,3,5\}$ in a world where odd faces have simply been removed.

**Moral.** Conditioning on an event that becomes harder to satisfy as time goes on biases the waiting time downward. This selection effect is the same mechanism behind many survivorship paradoxes in statistics.
