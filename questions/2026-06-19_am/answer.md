# Answer: Shanille's Free Throws: Pólya Urn Surprise

## Key Idea / Intuition

The key surprise is that **every outcome sequence of length 100 with exactly 50 hits is equally likely**. This is not obvious — you might expect sequences with "streaks" to have different probability from alternating ones. The probability rule creates a hidden symmetry: the rule is exactly the **Pólya urn** model, where all orderings are equally probable. Once you see this, the answer is just $1/99$ by a counting/symmetry argument.

---

## Formal Proof / Solution

**Setup.** She hits attempt 1, misses attempt 2. For $n \geq 3$, the probability of hitting attempt $n$ is $\frac{\text{(hits so far)}}{n-1}$.

**Step 1: Compute the probability of a specific sequence.**

Let's compute $P(\text{a specific sequence of 100 attempts with exactly } k \text{ hits})$.

Consider any fixed sequence $\omega$ of H's and M's of length 100 starting with H, M, and containing exactly $k$ hits total.

After the first two forced outcomes (H then M), we have 1 hit and 1 miss recorded. At step $n$ (for $n \geq 3$), if there have been $h$ hits and $m = n-1-h$ misses so far:
- $P(\text{hit}) = \frac{h}{n-1}$, $P(\text{miss}) = \frac{n-1-h}{n-1}$.

For a specific sequence with $k$ hits and $100-k$ misses, let's trace through the multiplicative contributions. At the moment of the $j$-th hit (for $j \geq 2$, since the first hit is forced), suppose there have been $j-1$ hits before — the contribution is $\frac{j-1}{\text{(step}-1)}$. Similarly each miss contributes a fraction.

More cleanly: the probability of **any specific sequence** of length $n$ starting H, M with exactly $k$ hits is:

$$P(\omega) = \frac{(k-1)!\,(n-k-1)!}{(n-1)!}$$

**Proof by induction or direct multiplication:**

At each step $t$ from 3 to $n$, the denominator is $t - 1$. So the product of all denominators is $(n-1)!/ 1! = (n-1)!/ (2-1)! $... let's be careful.

Steps 3 through $n$ give denominators $2, 3, \ldots, n-1$, whose product is $\frac{(n-1)!}{1}$.

The numerators: each hit at step $t$ contributes (current hit count before step $t$), and each miss contributes (current miss count before step $t$). 

- The hits after the first contribute numerators $1, 2, \ldots, k-1$ (the hit counts at the moment of each subsequent hit), giving $(k-1)!$.
- The misses after the second contribute numerators $1, 2, \ldots, (n-k)-1$, giving $(n-k-1)!$.

Therefore:
$$P(\omega) = \frac{(k-1)!\,(n-k-1)!}{(n-1)!}$$

**This is the same for every sequence with exactly $k$ hits!** The probability depends only on $k$, not on the order.

**Step 2: Count and compute.**

For $n = 100$, $k = 50$:

$$P(\text{exactly 50 hits in first 100}) = \binom{98}{49} \cdot \frac{49!\, 49!}{99!}$$

Wait — how many sequences are there? We must fix the first shot as H and second as M. The remaining 98 shots contain $49$ hits and $48$ misses... 

Actually: $k = 50$ hits total, $50$ misses total. The first shot is H (1 hit), second is M (1 miss). The remaining 98 shots have 49 hits and 49 misses, giving $\binom{98}{49}$ sequences.

So:

$$P(\text{exactly 50 of 100}) = \binom{98}{49} \cdot \frac{49!\, 49!}{99!} = \frac{98!}{49!\,49!} \cdot \frac{49!\,49!}{99!} = \frac{98!}{99!} = \frac{1}{99}.$$

**The beautiful answer: $\boxed{\dfrac{1}{99}}$.**

**Why it makes sense:** This is the Pólya urn model. In a Pólya urn starting with 1 red and 1 blue ball, after $n$ draws all compositions are equally likely. So among 100 draws, each value of $k$ from 1 to 99 is equally likely, giving probability $1/99$ each. ✓
