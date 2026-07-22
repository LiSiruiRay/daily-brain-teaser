# Answer: The Craps Shooter's Odds

## Key Idea / Intuition

The game splits into **independent cases** based on the first roll. For the "point" scenarios, only **two outcomes matter**: rolling the point again vs. rolling a 7. Once the point is established, all other outcomes are irrelevant — they just delay the resolution. So the conditional win probability given a point $p$ is simply the probability of rolling $p$ **divided by** the probability of rolling $p$ or $7$. Then we weight by the probability of each point occurring.

---

## Formal Proof / Solution

### Step 1: First-Roll Win/Loss

Count ways to roll each total with two dice (out of 36 equally likely outcomes):

| Total | Ways | Probability |
|-------|------|-------------|
| 2     | 1    | 1/36        |
| 3     | 2    | 2/36        |
| 7     | 6    | 6/36        |
| 11    | 2    | 2/36        |
| 12    | 1    | 1/36        |

**Immediate win** (7 or 11): $\frac{6+2}{36} = \frac{8}{36}$

**Immediate loss** (2, 3, or 12): $\frac{1+2+1}{36} = \frac{4}{36}$

---

### Step 2: Point Probabilities and Conditional Win

For a point $p$, all other rolls are irrelevant. By the **geometric trials argument**, the conditional probability of winning given point $p$ is:

$$P(\text{win} \mid \text{point is } p) = \frac{P(\text{roll } p)}{P(\text{roll } p) + P(\text{roll } 7)}$$

Compute for each possible point:

| Point $p$ | Ways to roll $p$ | $P(p)$ | $P(\text{win}\mid p) = \frac{P(p)}{P(p)+6/36}$ |
|-----------|-----------------|---------|----------------------------------------------|
| 4         | 3               | 3/36    | $\frac{3}{3+6} = \frac{1}{3}$               |
| 5         | 4               | 4/36    | $\frac{4}{4+6} = \frac{2}{5}$               |
| 6         | 5               | 5/36    | $\frac{5}{5+6} = \frac{5}{11}$              |
| 8         | 5               | 5/36    | $\frac{5}{5+6} = \frac{5}{11}$              |
| 9         | 4               | 4/36    | $\frac{4}{4+6} = \frac{2}{5}$               |
| 10        | 3               | 3/36    | $\frac{3}{3+6} = \frac{1}{3}$               |

---

### Step 3: Total Win Probability

$$P(\text{win}) = \frac{8}{36} + \sum_{\text{points}} P(\text{first roll} = p) \cdot P(\text{win}\mid p)$$

$$= \frac{8}{36} + 2\left[\frac{3}{36}\cdot\frac{1}{3} + \frac{4}{36}\cdot\frac{2}{5} + \frac{5}{36}\cdot\frac{5}{11}\right]$$

Compute each term:

$$\frac{3}{36}\cdot\frac{1}{3} = \frac{3}{108} = \frac{1}{36}$$

$$\frac{4}{36}\cdot\frac{2}{5} = \frac{8}{180} = \frac{2}{45}$$

$$\frac{5}{36}\cdot\frac{5}{11} = \frac{25}{396}$$

Multiply each by 2 (for symmetric pairs 4&10, 5&9, 6&8):

$$2\left[\frac{1}{36} + \frac{2}{45} + \frac{25}{396}\right]$$

Find common denominator (LCM of 36, 45, 396 = **1980**):

$$= 2\left[\frac{55}{1980} + \frac{88}{1980} + \frac{125}{1980}\right] = 2\cdot\frac{268}{1980} = \frac{536}{1980} = \frac{134}{495}$$

**Total:**

$$P(\text{win}) = \frac{8}{36} + \frac{134}{495} = \frac{440}{1980} + \frac{536}{1980} = \frac{976}{1980} = \boxed{\frac{244}{495} \approx 0.4929}$$

---

### The Surprise

The house edge is only about **1.41%** — craps is one of the **fairest casino games** in existence, with the player winning just barely under half the time. This elegant near-symmetry is why craps became so popular.
