# Answer: The Comb Space Is Not Locally Connected

## Key Idea / Intuition

The comb space is connected — you can "travel" from any tooth to any other via the base. But local connectivity at $(0,1)$ fails for a subtle reason: every small neighborhood of $p = (0,1)$ on the left spine contains points that can only be reached from the rest of the comb by going all the way down to the base and back up — so no small connected open neighborhood of $p$ exists. The infinitely many teeth "pinch off" the left spine from its nearby environment.

---

## Formal Proof / Solution

### Step 1: $X$ is connected.

Note that each vertical segment $\{\frac{1}{n}\} \times [0,1]$ is connected and intersects the base $[0,1] \times \{0\}$, which is also connected. So

$$B = \left([0,1] \times \{0\}\right) \cup \bigcup_{n=1}^{\infty} \left(\left\{\tfrac{1}{n}\right\} \times [0,1]\right)$$

is connected (a union of connected sets sharing a common point or intersecting the base). The left spine $\{0\} \times [0,1]$ is connected, and its point $(0,0)$ lies in the closure of $B$ (since $(\frac{1}{n}, 0) \to (0,0)$). 

More precisely: $(0,0) \in B$ (it lies on the base), so the left spine meets $B$ at $(0,0)$, hence $X = B \cup (\{0\}\times[0,1])$ is connected as a union of two connected sets with a point in common. $\checkmark$

---

### Step 2: $X$ is **not** locally connected at $p = (0,1)$.

Recall: a space is **locally connected** at $p$ if every open neighborhood of $p$ contains a connected open neighborhood of $p$.

**Pick any open neighborhood $U$ of $p = (0,1)$ in $X$.** We may assume $U = X \cap B_\varepsilon(p)$ for some small $\varepsilon > 0$. Choose $\varepsilon < 1$ so that $U$ does not reach the base.

Explicitly, for $\varepsilon < 1$, the open ball $B_\varepsilon((0,1))$ intersects $X$ in:
- A segment of the left spine: $\{0\} \times (1-\varepsilon, 1]$,
- Portions of the teeth $\{\frac{1}{n}\} \times (1-\varepsilon, 1]$ for all $n$ large enough that $\frac{1}{n} < \varepsilon$.

Since $\varepsilon < 1$, none of these tooth portions reach the base $y = 0$, so **they are not connected to each other** (each tooth piece $\{\frac{1}{n}\} \times (1-\varepsilon, 1]$ is a separate isolated arc, disconnected from the left spine and from each other within $U$).

**Formally:** The component of $p = (0,1)$ in $U$ is exactly the segment $\{0\} \times (1-\varepsilon, 1]$, because:
- The left spine piece $\{0\} \times (1-\varepsilon, 1]$ is connected and contains $p$.
- Each tooth piece $\{\frac{1}{n}\} \times (1-\varepsilon, 1]$ (for $\frac{1}{n} < \varepsilon$) is disjoint from the left spine in $U$ (since $\frac{1}{n} \neq 0$) and does not connect to it within $U$.

So the connected component of $p$ in $U$ is $\{0\} \times (1-\varepsilon, 1]$, which is **not open in $X$**: any open set in $X$ containing $(0, 1-\varepsilon/2)$ must contain points of the form $(\frac{1}{n}, 1-\varepsilon/2)$ for large $n$, which lie outside this component.

Since the connected component of $p$ in $U$ is not open, $U$ contains **no** connected open neighborhood of $p$. Since $U$ was arbitrary, $X$ is **not locally connected at $p$**. $\blacksquare$

---

### Summary

| Property | Answer |
|---|---|
| Connected | **Yes** — teeth and base form a connected set; left spine shares a point |
| Locally connected at $(0,1)$ | **No** — the infinitely many nearby teeth are isolated from the left spine in any small neighborhood |

This example beautifully illustrates that **connectedness and local connectedness are independent**: a space can be connected everywhere yet fail to be locally connected at a single point.
