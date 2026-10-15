# Answer: Successive Wins: Father or Champion in the Middle?

## Key Idea / Intuition

To win two sets **in a row** out of three, Elmer *must* win the middle set, because both consecutive pairs, (1,2) and (2,3), contain it. The middle set is a bottleneck, so it should be the easiest one, against his father. The outer sets only need one success between them, so facing the champion twice there costs less than it seems. Hence C–F–C is better, even though Elmer plays the champion twice. When the consecutiveness requirement is removed, the bottleneck disappears and the naive intuition (play the weaker opponent more often) is correct again.

---

## Formal Proof / Solution

### (a) Two wins in a row

Label the sets 1, 2, 3 with win probabilities $p_1, p_2, p_3$. The event "two consecutive wins" is
$$
(W_1 \cap W_2) \cup (W_2 \cap W_3) = W_2 \cap (W_1 \cup W_3).
$$
This factorization is the whole trick. By independence,
$$
P = p_2\,\bigl[1 - (1-p_1)(1-p_3)\bigr].
$$

**Order F–C–F** ($p_1 = p_3 = f,\ p_2 = c$):
$$
P_{FCF} = c\,\bigl[1-(1-f)^2\bigr] = cf(2-f).
$$

**Order C–F–C** ($p_1 = p_3 = c,\ p_2 = f$):
$$
P_{CFC} = f\,\bigl[1-(1-c)^2\bigr] = fc(2-c).
$$

**Comparison:**
$$
P_{CFC} - P_{FCF} = fc\,\bigl[(2-c) - (2-f)\bigr] = fc\,(f - c) > 0.
$$

So **Champion–Father–Champion is strictly better.**

*Numerical example:* with $f = 0.8$ and $c = 0.4$,
$$
P_{CFC} = 0.8 \cdot 0.4 \cdot 1.6 = 0.512, \qquad P_{FCF} = 0.4 \cdot 0.8 \cdot 1.2 = 0.384.
$$

### (b) At least two wins out of three

Now order is irrelevant except for *how many* sets are played against each opponent. "At least two of three" means all three wins, or exactly two.

**F–C–F** (two sets vs. father, one vs. champion):
$$
P'_{FCF} = f^2 c + f^2(1-c) + 2f(1-f)c = f^2 + 2fc - 2f^2c.
$$

**C–F–C** (two vs. champion, one vs. father):
$$
P'_{CFC} = c^2 + 2fc - 2fc^2.
$$

**Comparison:**
$$
P'_{FCF} - P'_{CFC} = (f^2 - c^2) - 2fc(f - c) = (f-c)\bigl(f + c - 2fc\bigr) = (f-c)\bigl[f(1-c) + c(1-f)\bigr] > 0.
$$

So under the relaxed rule, **Father–Champion–Father is better**, which matches the naive intuition.

### Moral

The answer flips because the structure of the winning event changes:

- **"Two in a row"** $= W_2 \cap (W_1 \cup W_3)$. Set 2 is a required "series" component, while sets 1 and 3 are redundant "parallel" components. Put the strongest link (the weaker opponent) where failure is fatal.
- **"Two of three"** is symmetric in the sets. Only the multiset of probabilities matters, so you want more easy sets.

The same reliability principle applies in engineering: in a system made of series and parallel parts, put your most reliable component on the series bottleneck.

---

**Source:** F. Mosteller, *Fifty Challenging Problems in Probability with Solutions*, Problem 2 ("Successive Wins"). Part (b) is an added contrast.
