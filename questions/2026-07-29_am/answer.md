# Answer: The Coin That Remembers Its Past

## Key Idea / Intuition

The parity of the number of changes after $n$ flips depends only on whether the last coin equals the first coin — because each "change" flips the running parity, and the sequence of changes is just a record of when the coin differs from its predecessor. So instead of tracking the full sequence, track a single bit: **does the current coin match the first?** This turns the problem into a simple random walk on $\{0,1\}$, and the answer pops out cleanly.

---

## Formal Proof / Solution

**Setup.** Label the flips $X_1, X_2, \ldots, X_n \in \{H, T\}$. Define $C_i = \mathbf{1}[X_i \neq X_{i-1}]$ for $i = 2, \ldots, n$. We want

$$P\!\left(\sum_{i=2}^n C_i \equiv 0 \pmod{2}\right).$$

**Key observation.** The parity of the total number of changes equals the parity of $X_1 \oplus X_n$ (XOR), because each change flips the running "have we switched from the original value?" bit. More precisely:

$$\sum_{i=2}^n C_i \equiv X_1 \oplus X_n \pmod{2}$$

(where we encode $H=0, T=1$). This is a telescoping: each change toggles the value, and the cumulative parity of toggles is just whether the final value differs from the initial value.

**Reduction.** So we need:

$$P(X_1 = X_n).$$

**Computing $P(X_1 = X_n)$.** Since the coin is fair, by symmetry $X_n$ is uniform on $\{H, T\}$ regardless of $n$. But we need the *joint* distribution of $(X_1, X_n)$.

Let $p_n = P(X_n = X_1)$ (they match). Conditioning on $X_{n-1}$:

$$p_n = P(X_n = X_1) = P(X_n = X_{n-1}) \cdot P(X_{n-1} = X_1) + P(X_n \neq X_{n-1}) \cdot P(X_{n-1} \neq X_1).$$

Since the coin is fair, $P(X_n = X_{n-1}) = \tfrac{1}{2}$ always. So:

$$p_n = \tfrac{1}{2} \cdot p_{n-1} + \tfrac{1}{2} \cdot (1 - p_{n-1}) = \tfrac{1}{2}.$$

Wait — this gives $p_n = \frac{1}{2}$ for all $n \geq 2$, with $p_1 = 1$.

**Answer.**

$$P(\text{even number of changes after } n \text{ flips}) = \begin{cases} 1 & n = 1 \\ \dfrac{1}{2} & n \geq 2 \end{cases}$$

**The surprise revealed.** For $n \geq 2$, the answer *is* exactly $\frac{1}{2}$ — but the reason is subtle. It's not obvious from the raw definition, yet the telescoping XOR argument makes it crisp. The "memory" of the sequence collapses entirely into a single coin flip: does the last coin match the first?

**Sanity check for $n=2$:** Only one potential change. $P(\text{no change}) = P(X_2 = X_1) = \frac{1}{2}$. ✓

**Sanity check for $n=3$:** Two potential changes. $P(\text{0 changes}) = \frac{1}{4}$, $P(\text{2 changes}) = P(HHH) + P(TTT) + P(HTH) + P(THT) = \frac{1}{4}$. Total even $= \frac{1}{2}$. ✓
