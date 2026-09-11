# Answer: The Coloring That Cannot Avoid Arithmetic

## Key Idea / Intuition

This is a finite combinatorial trap: you only need to check what happens to the numbers $\{1, 2, 3, 4, 5\}$ or even simpler — just trace where $1$ lands and watch the forced cascade. If $1$ is red, then consider $2 = 1+1$: if $2$ is red, we're done ($1+1=2$). If $2$ is blue, consider $4 = 2+2$: if $4$ is blue, we're done. If $4$ is red, then $1+4=5$ forces a check on $3$… The point is that the structure of arithmetic progressions within a small finite set is so rigid that one of two colors must contain a solution.

---

## Formal Proof / Solution

We use a **finite case analysis** on the coloring of just the numbers $\{1, 2, 3, 4, 5\}$.

Call the two colors **R** (red) and **B** (blue). Consider the number $1$; by symmetry assume $1$ is **R**.

**Case 1: $2$ is R.**
Then $1 + 1 = 2$ with $1, 1, 2$ all red. ✓

**Case 2: $2$ is B.**

Now consider $4 = 2 + 2$.

- **Subcase 2a: $4$ is B.**
  Then $2 + 2 = 4$ with $2, 2, 4$ all blue. ✓

- **Subcase 2b: $4$ is R.**
  Now consider $3$.

  - **Subsubcase 2b-i: $3$ is R.**
    Then $1 + 3 = 4$, all three ($1, 3, 4$) are red. ✓

  - **Subsubcase 2b-ii: $3$ is B.**
    Now consider $5$.

    - **If $5$ is B:** then $2 + 3 = 5$, all three ($2, 3, 5$) are blue. ✓

    - **If $5$ is R:** then $1 + 4 = 5$, all three ($1, 4, 5$) are red. ✓

In every case, we find $x, y, z$ of the same color with $x + y = z$. $\blacksquare$

---

## Remarks

- This is a special case of **Schur's theorem** (1916), which states: for any $r$-coloring of $\{1, \ldots, N\}$ with $N$ sufficiently large, there exist same-colored $x, y, z$ with $x + y = z$. The **Schur number** $S(2) = 4$ tells us $\{1,2,3,4\}$ can be 2-colored avoiding monochromatic solutions — but $\{1,\ldots,5\}$ cannot. (Check: $\{1,4\}$ red, $\{2,3\}$ blue works for $n=4$.)

- The proof above is essentially the verification that $S(2) = 4$, so $5$ numbers suffice.

- The argument is also **Ramsey-theoretic in spirit**: arithmetic structure inevitably creates monochromatic configurations under any finite coloring.
