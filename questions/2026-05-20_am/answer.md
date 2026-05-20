# Answer: The First Ace

## Key Idea / Intuition

Rather than computing a messy sum over geometric-like probabilities, use a beautiful symmetry argument: the 4 aces and 48 non-aces divide the deck into **5 gaps**. By symmetry, each gap has the same expected size. The cards before the first ace form one of these five gaps, so on average there are $48/5$ non-ace cards before the first ace — plus the ace itself gives $48/5 + 1 = 53/5$.

---

## Formal Proof / Solution

**Setup.** Place 52 cards in a random order. The 4 aces land in 4 of the 52 positions, splitting the deck into 5 segments:

$$[\underbrace{\text{non-aces}}_{\text{before 1st ace}}] \; \text{ACE}_1 \; [\cdots] \; \text{ACE}_2 \; [\cdots] \; \text{ACE}_3 \; [\cdots] \; \text{ACE}_4 \; [\underbrace{\text{non-aces}}_{\text{after 4th ace}}]$$

**Symmetry argument.** The 48 non-ace cards are distributed among **5 gaps** (before ace 1, between aces 1–2, 2–3, 3–4, and after ace 4). By symmetry — since all $\binom{52}{4}$ placements of the four aces are equally likely — each gap has the same expected number of non-ace cards:

$$\mathbb{E}[\text{non-aces in any one gap}] = \frac{48}{5}.$$

**Answer.** The number of cards turned up to reach the first ace equals:

$$(\text{non-aces before first ace}) + 1 \quad \Longrightarrow \quad \mathbb{E} = \frac{48}{5} + 1 = \frac{53}{5} = \boxed{10.6}.$$

**Sanity check via direct formula.** Let $X$ be the position of the first ace. Then:

$$\mathbb{E}[X] = \sum_{k=1}^{49} k \cdot P(X = k),$$

where $P(X = k) = \dfrac{\binom{k-1}{0}\binom{52-k}{3}}{\binom{52}{4}} \cdot \frac{4}{52-k+1}$... this sum is messy. The symmetry argument gives the answer in one line — that's what makes it beautiful.

**General formula.** For a deck of $n$ cards with $a$ aces:

$$\mathbb{E}[\text{position of first ace}] = \frac{n+1}{a+1}.$$

Here: $\dfrac{52+1}{4+1} = \dfrac{53}{5} = 10.6$. ✓

This formula has a clean combinatorial proof: by symmetry, the $a$ aces divide $n$ cards into $a+1$ equally-treated gaps, and the expected position of the first ace is $\frac{n-a}{a+1} + 1 = \frac{n+1}{a+1}$.
