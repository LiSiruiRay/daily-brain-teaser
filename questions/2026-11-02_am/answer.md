# Answer: Fekete's Subadditive Lemma

## Key Idea / Intuition

Subadditivity says that splitting a long block into shorter blocks can only increase the total cost. Fix a good block length $m$, one where $a_m/m$ is close to the infimum. Any large $n$ can be tiled by about $n/m$ copies of that block plus a short leftover piece. The average cost of the tiling is therefore close to $a_m/m$. The leftover piece is shorter than $m$, so it adds only a bounded amount, and that amount disappears after dividing by $n$. The whole proof is the division algorithm $n = qm + r$.

---

## Formal Proof / Solution

Let $L = \inf_{n\ge1} a_n/n \in [-\infty,\infty)$.

**Lower bound.** Every term satisfies $a_n/n \ge L$, so
$$\liminf_{n\to\infty}\frac{a_n}{n} \ge L.$$

**Upper bound.** Fix $m\ge 1$. For $n > m$, write $n = qm + r$ with $q\ge 1$ and $0\le r < m$. Applying subadditivity repeatedly gives
$$a_n \le q\,a_m + a_r,$$
with the convention that the term $a_r$ is absent when $r=0$. Set
$$C_m = \max\bigl(0, |a_1|,\dots,|a_{m-1}|\bigr),$$
which is a constant depending only on $m$. Then
$$\frac{a_n}{n} \le \frac{qm}{n}\cdot\frac{a_m}{m} + \frac{C_m}{n}.$$

Now let $n\to\infty$ with $m$ fixed:

- Since $n - m < qm \le n$, we have $qm/n \to 1$.
- Since $C_m$ is fixed, $C_m/n \to 0$.

Therefore
$$\limsup_{n\to\infty}\frac{a_n}{n} \le \frac{a_m}{m}.$$

This holds for every $m$, so we may take the infimum over $m$:
$$\limsup_{n\to\infty}\frac{a_n}{n} \le L.$$

If $L=-\infty$, this already says $a_n/n\to-\infty$. Otherwise, combining with the lower bound gives
$$\lim_{n\to\infty}\frac{a_n}{n} = L = \inf_n \frac{a_n}{n}. \qquad\blacksquare$$

**Follow-up.**

- If $A^k = 0$ for some $k$, then $\|A^n\|^{1/n} = 0$ for all $n\ge k$, so the limit is $0$.
- Otherwise $A^n \neq 0$ for every $n$. Indeed, $A^n=0$ would force $A^k = A^{k-n}A^n = 0$ for all $k\ge n$. So we may set $a_n = \log\|A^n\|$, which is finite. Submultiplicativity gives
$$\|A^{m+n}\| \le \|A^m\|\,\|A^n\|,$$
so $(a_n)$ is subadditive. By Fekete's lemma, $\frac1n\log\|A^n\|$ converges to $\inf_n \frac1n \log\|A^n\|$, where the value $-\infty$ is allowed. Exponentiating, $\|A^n\|^{1/n}$ converges to $\inf_n\|A^n\|^{1/n}$.

Gelfand's formula identifies this limit as the spectral radius $\rho(A)$. Fekete's lemma gives existence of the limit for free.

**Remarks.**

- The same argument shows that the connective constant $\mu = \lim c_n^{1/n}$ exists for self-avoiding walks, where $c_n$ counts walks of length $n$. The key inequality is $c_{m+n}\le c_m c_n$.
- The lemma is the deterministic seed of Kingman's subadditive ergodic theorem.
