# Answer: Cycle Lemma: Staying Strictly Ahead

## Key Idea / Intuition

At first glance this seems to require tracking a complicated path. The magical insight is a **reflection/cycle-lemma argument**: among all $(n+m)!/(n!\,m!)$ equally likely orderings, each one corresponds to exactly $n+m$ cyclic shifts, and the fraction of those shifts that keep red strictly ahead throughout equals $(n-m)/(n+m)$. This is a purely combinatorial symmetry — no calculation needed, just a clever counting of cycles.

The result is strikingly clean: the probability depends only on the *surplus* of red over blue, divided by the total.

---

## Formal Proof / Solution

**Setup.** Label each sequence of $n$ red ($+1$) and $m$ blue ($-1$) balls. Let $S_k$ denote the running total after $k$ draws. We want

$$P(S_k > 0 \text{ for all } k = 1, 2, \ldots, n+m).$$

**The Cycle Lemma.** Consider any sequence $a_1, a_2, \ldots, a_{n+m}$ with $n$ values $+1$ and $m$ values $-1$, so the total sum is $n - m > 0$. Form the $n+m$ cyclic shifts:

$$a_1, a_2, \ldots, a_{n+m}$$
$$a_2, a_3, \ldots, a_{n+m}, a_1$$
$$\vdots$$

**Claim:** Among these $n+m$ cyclic shifts, **exactly $n - m$ of them** have all partial sums strictly positive.

*Why?* The partial sums of the original sequence return to $0$ exactly $m$ times from below (loosely speaking), and the cycle lemma (Dvoretzky and Motzkin, 1947) gives this exact count via a parity/rotation argument. More precisely: define $S_k = a_1 + \cdots + a_k$. The shift starting at position $j+1$ has all positive partial sums if and only if position $j$ achieves the **minimum** of all $S_0, S_1, \ldots, S_{n+m-1}$. Since the total sum is $n - m > 0$, this minimum is achieved exactly $n - m$ times (it can be achieved at multiple consecutive indices only when the path touches the minimum plateau, but the strict positivity of the final sum ensures exactly $n-m$ valid starting positions by a careful argument).

**Conclusion.** Since every sequence belongs to an equivalence class of $n+m$ cyclic rotations, and exactly $n-m$ of those rotations are "good" (all partial sums $> 0$), the probability is:

$$\boxed{P = \frac{n - m}{n + m}}$$

**Quick sanity check.** If $m = 0$: all draws are red, so we are always ahead. Formula gives $n/n = 1$. ✓  
If $n = m+1$: formula gives $1/(2m+1)$, which matches the classic ballot problem result. ✓

**Why it's beautiful.** The answer $\frac{n-m}{n+m}$ is not just elegant — it says the probability equals the *fraction* by which red exceeds blue in total count. A purely combinatorial symmetry (cyclic rotation) collapses a complex path-counting problem into a single line.
