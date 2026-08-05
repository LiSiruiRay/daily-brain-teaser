# Answer: The Sock Drawer Surprise

## Key Idea / Intuition

A matching pair appears on the **third draw at the latest** — by the pigeonhole principle, any three socks from two colors must contain two of the same color. So the game ends on draw 2 or draw 3. The first matching pair is red if and only if the **third sock** (when the game reaches draw 3) is red — but more cleanly, the answer reduces to a simple symmetry argument about the **first three socks drawn**.

The key insight: focus only on the **first three socks** drawn. A red match comes first if and only if among these three socks, draws 1 and 2 are *not* a matching pair (so draw 1 and 2 are different colors, one red one blue), and draw 3 **matches** draw 1 or 2 to make a red pair. But even cleaner: the game ends on draw 3 exactly when draws 1 and 2 differ, and then the **third sock's color** determines which color matches first.

---

## Formal Proof / Solution

**Step 1: When does the game end?**

- If draw 1 and draw 2 have the **same color**, the game ends on draw 2.
- If draw 1 and draw 2 have **different colors**, the game ends on draw 3 (draw 3 must match one of the first two).

**Step 2: Probability of a red match on draw 2.**

$$P(\text{red match on draw 2}) = \frac{r}{r+b} \cdot \frac{r-1}{r+b-1}$$

**Step 3: Probability of a red match on draw 3.**

This requires: draws 1,2 are different colors (one red, one blue), and draw 3 is red.

There are two orderings for "different colors" in draws 1–2: (Red, Blue) or (Blue, Red).

$$P(\text{RBR}) = \frac{r}{r+b}\cdot\frac{b}{r+b-1}\cdot\frac{r-1}{r+b-2}$$

$$P(\text{BRR}) = \frac{b}{r+b}\cdot\frac{r}{r+b-1}\cdot\frac{r-1}{r+b-2}$$

So:
$$P(\text{red match on draw 3}) = \frac{r \cdot b \cdot (r-1) + b \cdot r \cdot (r-1)}{(r+b)(r+b-1)(r+b-2)} = \frac{2rb(r-1)}{(r+b)(r+b-1)(r+b-2)}$$

**Step 4: Total probability of first match being red.**

$$\boxed{P(\text{first match is red}) = \frac{r(r-1)}{(r+b)(r+b-1)} + \frac{2rb(r-1)}{(r+b)(r+b-1)(r+b-2)}}$$

Factor out $\dfrac{r(r-1)}{(r+b)(r+b-1)}$:

$$= \frac{r(r-1)}{(r+b)(r+b-1)}\left(1 + \frac{2b}{r+b-2}\right) = \frac{r(r-1)}{(r+b)(r+b-1)}\cdot\frac{r+b-2+2b}{r+b-2}$$

$$= \frac{r(r-1)(r+3b-2)}{(r+b)(r+b-1)(r+b-2)}$$

**Step 5: Sanity check with symmetry.**

Let $r = b = 2$. Then total socks = 4.

$$P(\text{red first}) = \frac{2 \cdot 1 \cdot (2 + 6 - 2)}{4 \cdot 3 \cdot 2} = \frac{2 \cdot 6}{24} = \frac{12}{24} = \frac{1}{2}.$$

By symmetry ($r = b$), the answer must be $\tfrac{1}{2}$. ✓

**The beautiful surprise:** The answer does **not** simplify to just $r/(r+b)$ — the probability of a red match first is *not* simply proportional to $r$. The geometry of "first matching pair" introduces an asymmetry that favors the more numerous color *more strongly* than a naive guess suggests. For example, with $r=3, b=1$:

$$P = \frac{3 \cdot 2 \cdot (3+3-2)}{4 \cdot 3 \cdot 2} = \frac{6 \cdot 4}{24} = \frac{24}{24} = 1,$$

which makes sense: with only 1 blue sock, you can never get a blue matching pair!
