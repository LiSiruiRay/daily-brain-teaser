# Answer: The Prisoner's Pardon: Three Boxes, One Clue

## Key Idea / Intuition

This problem is a clever mirror image of the Monty Hall problem — but with the opposite conclusion. In Monty Hall, a door being opened *shifts* probability away from you. Here, because **two out of three** prisoners are pardoned, the guard always has someone other than Alice to name (whether or not Alice is pardoned), so the guard's answer carries **no information** about Alice's fate. Her probability stays exactly $2/3$.

---

## Formal Proof / Solution

**Setup.** There are $\binom{3}{2} = 3$ equally likely scenarios, each with probability $1/3$:

| Scenario | Who is pardoned | Alice pardoned? |
|----------|----------------|-----------------|
| S1 | Alice, Bob | Yes |
| S2 | Alice, Carol | Yes |
| S3 | Bob, Carol | No |

Alice is pardoned in 2 out of 3 scenarios, so $P(\text{Alice pardoned}) = 2/3$.

**After the guard says "Bob."** We apply Bayes' theorem. The guard must name someone other than Alice who is pardoned. Let $G = \text{"guard names Bob"}$.

- **S1** (Alice, Bob pardoned): Guard can name Bob or Carol — wait, Carol is *not* pardoned. Guard must name Bob. So $P(G \mid S1) = 1$.
- **S2** (Alice, Carol pardoned): Guard can only name Carol (Bob is not pardoned). So $P(G \mid S2) = 0$.
- **S3** (Bob, Carol pardoned): Guard can name Bob or Carol. Assuming the guard picks uniformly at random, $P(G \mid S3) = 1/2$.

By the law of total probability:
$$P(G) = \frac{1}{3}\cdot 1 + \frac{1}{3}\cdot 0 + \frac{1}{3}\cdot\frac{1}{2} = \frac{1}{3} + \frac{1}{6} = \frac{1}{2}.$$

Now update:
$$P(S1 \mid G) = \frac{P(G\mid S1)\,P(S1)}{P(G)} = \frac{1 \cdot \frac{1}{3}}{\frac{1}{2}} = \frac{2}{3}.$$

$$P(S3 \mid G) = \frac{\frac{1}{2}\cdot\frac{1}{3}}{\frac{1}{2}} = \frac{1}{3}.$$

Alice is pardoned in scenario S1 (and not in S3), so:
$$P(\text{Alice pardoned} \mid G) = P(S1 \mid G) = \frac{2}{3}.$$

**Conclusion.** Alice's probability of being pardoned is still $\boxed{2/3}$, unchanged. The guard's information tells her *who else* is safe, but nothing about herself — because there were always at least two pardoned prisoners and the guard could always find someone to name.

**Contrast with Monty Hall.** In Monty Hall, only *one* prize exists and the host *must* open an empty door other than yours. Here, two pardons exist and the guard *must* name a pardoned prisoner other than you. The symmetry works out oppositely: in Monty Hall you should switch (probability goes from $1/3$ to $2/3$); here, there is nothing to switch and your probability stays put.
