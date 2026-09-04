# Answer: The Checkerboard Walk: Can the Knight Return Home?

## Key Idea / Intuition

The key observation is that a knight **always moves from a white square to a black square and vice versa** — it is a parity-reversing move on the two-color chessboard. This means a knight's tour is secretly just a path (or cycle) that alternates colors. Any closed tour must therefore visit equally many black and white squares, but removing two squares of the same color destroys this balance, making a closed tour impossible — but part (b) is even stronger: even an *open* tour is impossible for the same parity reason!

---

## Formal Proof / Solution

### Setup: The Parity Constraint

Label all 64 squares as Black (B) or White (W) in the standard alternating pattern. There are exactly **32 black** and **32 white** squares.

**Key lemma:** Every knight move goes from a square of one color to a square of the other color. (This is because a knight moves $(±1, ±2)$ or $(±2, ±1)$; in either case the sum of coordinate changes is odd, flipping parity.)

---

### Part (a): No Closed Knight's Tour Starting at a Corner

A corner square — say $a1$ — is **black** (say). In a closed tour visiting all 64 squares and returning to $a1$, the knight makes exactly **64 moves**.

Since each move alternates color, after an *even* number of moves the knight is on the same color as the start. After 64 moves it returns to $a1$ (black). ✓ — so parity does **not** immediately obstruct this.

Indeed, closed knight's tours **do exist** on an $8\times 8$ board; they have been explicitly constructed. So the answer to (a) is: **Yes, a closed knight's tour exists.**

*(The Putnam spirit here is that one might expect parity to kill it — but it doesn't for part (a), because 64 is even. The elegant parity argument is really the story of part (b).)*

---

### Part (b): No Knight's Tour After Removing Two Squares of the Same Color

Remove two squares, both of the same color — say both **black**. The remaining 62 squares consist of **30 black** and **32 white** squares.

**Claim:** No Hamiltonian path (open knight's tour) exists on these 62 squares.

**Proof:** Since every knight move alternates color, any path of $k$ moves visits squares whose colors alternate: $B, W, B, W, \ldots$ or $W, B, W, B, \ldots$

A path visiting all 62 squares makes exactly **61 moves** and visits 62 squares alternating in color. In a 62-square alternating path, there are either:
- 31 Black and 31 White squares visited (if the path starts and ends on the same color), or  
- 31 of one color and 31 of the other (always 31 each, since 62 = 31 + 31).

Wait — more carefully: in any path of 62 squares alternating B/W, the count is either $31B + 31W$ (if start and end are different colors) or... actually in an alternating sequence of length 62 (even), we always get exactly **31 of each color**.

But our board has **30 black** and **32 white** squares. A Hamiltonian path on 62 squares would require visiting all of them: 30 black and 32 white — which is NOT 31 and 31.

This is a **contradiction**: an alternating path of even length 62 must use equal numbers of each color, but $30 \neq 32$.

**Therefore, no knight's tour exists on the 62 remaining squares.** $\blacksquare$

---

### Summary

| Part | Answer | Reason |
|------|--------|--------|
| (a) | **Yes**, closed tours exist | Parity is consistent (64 even, 32 = 32) |
| (b) | **No** open tour possible | Parity fails: 30 ≠ 32, but alternating path of even length needs equal counts |

The beautiful takeaway: the **graph-coloring / bipartite parity argument** is a one-line obstruction that kills part (b) instantly, while part (a) shows that when parity is satisfied, existence is genuinely nontrivial (and true!).
