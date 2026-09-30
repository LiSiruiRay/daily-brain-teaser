# Answer: The Gambler's Ruin on a Circle

## Key Idea / Intuition

This is a **biased random walk** on the integers $\{1, 2, \ldots, 7\}$, absorbed at the two endpoints. The "circle" framing is just colorful dressing — once you see that the token walks along a line segment between two absorbing barriers, the classic Gambler's Ruin formula applies immediately. The key is that for a biased walk with $P(\text{right}) = p$ and $P(\text{left}) = q = 1-p$, the probability of reaching the right barrier before the left barrier from position $k$ is given by a clean geometric formula involving $r = q/p$.

---

## Formal Proof / Solution

**Setup.** Label positions $1, 2, \ldots, 7$ with absorbing barriers at $1$ (loss) and $7$ (win). The token starts at position $4$. At each step:
$$p = P(\text{move right}) = \tfrac{2}{3}, \quad q = P(\text{move left}) = \tfrac{1}{3}.$$

**Classic Gambler's Ruin Formula.** Let $P_k$ = probability of reaching position $N = 7$ before position $1$, starting from $k$. The standard result for a biased walk absorbed at $\{1, N\}$ is:

$$P_k = \frac{1 - r^{k-1}}{1 - r^{N-1}}, \quad \text{where } r = \frac{q}{p}.$$

Here $r = \tfrac{1/3}{2/3} = \tfrac{1}{2}$, and $N - 1 = 6$.

**Derivation sketch.** The recurrence $P_k = p \cdot P_{k+1} + q \cdot P_{k-1}$ with $P_1 = 0$, $P_7 = 1$ has the general solution $P_k = A + B \cdot r^{k-1}$. Applying boundary conditions:
- $P_1 = 0 \Rightarrow A + B = 0 \Rightarrow A = -B$
- $P_7 = 1 \Rightarrow A + B \cdot r^6 = 1 \Rightarrow B(r^6 - 1) = 1$

So $B = \tfrac{1}{r^6 - 1}$, $A = \tfrac{-1}{r^6 - 1}$, giving:
$$P_k = \frac{r^{k-1} - 1}{r^6 - 1} = \frac{1 - r^{k-1}}{1 - r^6}.$$

**Computation.** With $k = 4$ and $r = 1/2$:

$$P_4 = \frac{1 - (1/2)^3}{1 - (1/2)^6} = \frac{1 - 1/8}{1 - 1/64} = \frac{7/8}{63/64} = \frac{7}{8} \cdot \frac{64}{63} = \frac{7 \cdot 64}{8 \cdot 63} = \frac{448}{504} = \frac{8}{9}.$$

**Answer:**
$$\boxed{P_4 = \dfrac{8}{9}.}$$

**Sanity check.** The walk strongly favors moving right ($p = 2/3$), and the token starts exactly in the middle. So a probability well above $\tfrac{1}{2}$ of reaching the right barrier makes sense. Indeed $\tfrac{8}{9} \approx 0.889$.
