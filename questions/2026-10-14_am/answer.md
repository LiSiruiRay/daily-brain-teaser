# Answer: The Ballot Box Surprise: Early Leader Locks In

## Key Idea / Intuition

The condition "never tied after the start" means the path either stays entirely positive or entirely negative the whole time. By symmetry, exactly half of such paths stay positive and half stay negative. So the answer is simply $\frac{1}{2}$ — no calculation needed, just symmetry.

But the deeper surprise is: the number of such "never-returning" paths is itself elegant to compute, and the reflection principle makes the whole story click.

---

## Formal Proof / Solution

**Setup.** Consider sequences of $n$ heads (steps $+1$) and $n$ tails (steps $-1$). Let $S_k = H_k - T_k$ be the running difference after $k$ flips, with $S_0 = 0$. We want paths where $S_k \neq 0$ for all $k = 1, \ldots, 2n$.

**Step 1: Classify "non-returning" paths.**

Such a path must have $S_1 = +1$ (heads first) or $S_1 = -1$ (tails first), and then never return to $0$. By symmetry (flip all heads and tails), the number of paths with $S_k > 0$ for all $k \geq 1$ equals the number with $S_k < 0$ for all $k \geq 1$.

**Step 2: Count paths that stay strictly positive.**

A path stays strictly positive if and only if:
- $S_1 = +1$ (must start with a head), and
- $S_k \geq 1$ for all $k = 1, \ldots, 2n$, and $S_{2n} = 0$.

By the **Cycle Lemma** (or the reflection principle / ballot problem), the number of paths from $0$ to $0$ in $2n$ steps that stay **strictly positive** after time $0$ is:

$$\frac{1}{2n}\binom{2n}{n}$$

Wait — let's use the ballot problem directly. The number of paths of length $2n$ with $n$ steps $+1$ and $n$ steps $-1$ that satisfy $S_k > 0$ for all $k = 1, \ldots, 2n$ equals:

$$\frac{1}{2n}\binom{2n}{n}$$

This is a classical result: among all $2n$ cyclic rotations of such a balanced sequence, exactly $1$ has all partial sums positive (by the cycle lemma).

**Step 3: Total non-returning paths.**

By symmetry, the number of paths with $S_k < 0$ for all $k \geq 1$ also equals $\frac{1}{2n}\binom{2n}{n}$.

So the total number of non-returning paths is:

$$\frac{1}{2n}\binom{2n}{n} + \frac{1}{2n}\binom{2n}{n} = \frac{1}{n}\binom{2n}{n}$$

**Step 4: Answer the conditional probability.**

Among all non-returning paths, the ones that stay **strictly positive** are exactly half:

$$P(\text{always ahead} \mid \text{never tied after start}) = \frac{\frac{1}{2n}\binom{2n}{n}}{\frac{1}{n}\binom{2n}{n}} = \frac{\frac{1}{2n}}{\frac{1}{n}} = \boxed{\frac{1}{2}}$$

**The Surprise.** The answer $\frac{1}{2}$ is immediate from symmetry, yet many people expect it to be something more exotic. The elegant hidden content is the *count* of non-returning paths: it equals $\frac{1}{n}\binom{2n}{n}$, which is twice the Catalan-adjacent number $\frac{1}{2n}\binom{2n}{n}$. The cycle lemma — that among all $2n$ cyclic rotations of a balanced $\pm 1$ sequence, exactly one keeps all partial sums positive — is the beautiful combinatorial engine underneath.
