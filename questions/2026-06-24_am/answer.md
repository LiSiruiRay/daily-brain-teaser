# Answer: Expected Runs of Heads

## Key Idea / Intuition

Rather than trying to count runs directly — which requires tracking complex consecutive structure — we use **indicator random variables**. A run of heads *starts* at position $i$ if and only if position $i$ is heads AND either $i=1$ or position $i-1$ is tails. This decouples the problem beautifully: we just count the expected number of "run starts."

---

## Formal Proof / Solution

**Setup:** Let $X_1, X_2, \ldots, X_n$ be i.i.d. fair coin flips ($H$ or $T$, each with probability $\frac{1}{2}$).

**Define indicator variables:** Let $I_i$ be the indicator that a run of heads *begins* at position $i$. Then:

$$\text{(number of runs of heads)} = \sum_{i=1}^{n} I_i$$

**When does a run of heads begin at position $i$?**

- **Case $i = 1$:** A run starts at position 1 iff $X_1 = H$. So:
$$P(I_1 = 1) = \frac{1}{2}$$

- **Case $i \geq 2$:** A run starts at position $i$ iff $X_{i-1} = T$ and $X_i = H$ (tails followed by heads, meaning a new run begins). Since flips are independent:
$$P(I_i = 1) = P(X_{i-1} = T) \cdot P(X_i = H) = \frac{1}{2} \cdot \frac{1}{2} = \frac{1}{4}$$

**Expected number of runs of heads:**

$$E\left[\sum_{i=1}^{n} I_i\right] = E[I_1] + \sum_{i=2}^{n} E[I_i] = \frac{1}{2} + (n-1) \cdot \frac{1}{4}$$

$$\boxed{E[\text{runs of heads}] = \frac{n+1}{4}}$$

**Sanity check:** For $n=1$: the formula gives $\frac{2}{4} = \frac{1}{2}$, which is correct (one run of heads with probability $\frac{1}{2}$). For $n=2$: formula gives $\frac{3}{4}$. Direct check: sequences $HH, HT, TH, TT$ have $1, 1, 1, 0$ runs of heads respectively, giving expected value $\frac{3}{4}$. ✓

**Why this is beautiful:** The linearity of expectation transforms a problem about complex consecutive structure into a simple sum over independent pairs of coin flips. No need to track run lengths or use generating functions — just ask "where does a new run begin?"

**Note:** By symmetry, the expected number of runs of *tails* is also $\frac{n+1}{4}$, and the expected *total* number of runs (heads or tails) is $\frac{n+1}{2}$, a clean result.
