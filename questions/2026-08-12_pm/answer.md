# Answer: The Envelope Paradox

## Key Idea / Intuition

The argument secretly assumes that both scenarios — "the other envelope has $50" and "the other envelope has $200" — are equally likely **given that you saw \$100**. But this is a claim about a posterior probability, not a prior. For a fixed prior distribution on the smaller amount, these two events cannot both have probability $1/2$ for every possible observed value simultaneously. The flaw is that no valid prior probability distribution makes the switching calculation uniformly correct for all observed values.

---

## Formal Proof / Solution

### Setting Up the Framework

Let $X$ be the smaller of the two amounts. The two envelopes contain $X$ and $2X$.

You open an envelope and see some value $v$. There are two cases:
- **Case A:** You picked the smaller envelope, so $v = X$ and the other has $2v$. This happens with probability $1/2$.
- **Case B:** You picked the larger envelope, so $v = 2X$ and the other has $v/2$. This happens with probability $1/2$ (unconditionally, before knowing $v$).

The friend's argument implicitly claims: **given that you saw $v = 100$**, both cases A and B occur with probability $1/2$.

### Why This Fails

Using Bayes' theorem, the conditional probability of Case A given you saw $v$ is:

$$P(\text{Case A} \mid v) = \frac{P(v \mid \text{Case A}) \cdot P(\text{Case A})}{P(v \mid \text{Case A}) \cdot P(\text{Case A}) + P(v \mid \text{Case B}) \cdot P(\text{Case B})}$$

For this to equal $1/2$ for a specific $v = 100$, we need:

$$P(v = 100 \mid \text{Case A}) = P(v = 100 \mid \text{Case B})$$

i.e., the prior probability that the smaller amount equals \$100 must equal the prior probability that the smaller amount equals \$50.

For this to hold for **every** possible observed value $v$, we would need the prior on $X$ to satisfy:
$$f(v) = f(v/2) \quad \text{for all } v > 0$$

where $f$ is the density of $X$. This means $f(v) = f(v/2) = f(v/4) = \cdots \to f(0^+)$ and similarly $f(v) = f(2v) = f(4v) = \cdots \to f(\infty)$. No proper probability distribution can satisfy this — such a prior does not exist.

### The Resolution

The argument is only valid for a **specific** observed value $v$ if the prior happens to assign equal probability to "smaller amount $= v$" and "smaller amount $= v/2$". For any fixed proper prior, this holds for at most a measure-zero set of values of $v$.

In fact, for any proper prior $f$ on $X$:
- If $v$ is large, it's more likely you're in Case B (you picked the larger), so the other envelope probably has $v/2 < v$. You should **not** switch.
- If $v$ is small, Case A is more likely, and you probably should switch.

The symmetry argument "you should always switch" fails because the **act of opening the envelope and seeing $v$** gives you Bayesian information about which envelope you hold — but only relative to a prior. Without a prior, the calculation is simply undefined.

### Punchline

The paradox arises from treating the conditional probabilities $P(\text{other} = 2v \mid v) = P(\text{other} = v/2 \mid v) = 1/2$ as a prior-free fact, when in reality these are posterior probabilities that depend on the underlying distribution of envelope amounts. **The error is using a posterior calculation without a prior.**
