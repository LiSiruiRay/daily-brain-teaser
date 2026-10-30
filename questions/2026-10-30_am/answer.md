# Answer: The Fraction That Eventually Stops Simplifying

## Key Idea / Intuition

Track the **difference** $m_k - n_k$. Before reduction it simply doubles: $(2m+1)-(2n+1) = 2(m-n)$. The reduction then divides it by the common factor $d$, which is always odd.

So the powers of $2$ in the difference are just noise from the doubling. If we strip them off and look at the **odd part** of $|m_k - n_k|$, each step can only keep it the same or divide it by $d$. A positive integer cannot shrink forever, so cancellation ($d>1$) can happen only finitely often.

---

## Formal Proof / Solution

**Setup.** Let $d_k = \gcd(2m_k+1,\, 2n_k+1)$. Since $\frac{2m_k+1}{d_k}$ and $\frac{2n_k+1}{d_k}$ are coprime and have the right ratio, we get

$$m_{k+1} = \frac{2m_k+1}{d_k}, \qquad n_{k+1} = \frac{2n_k+1}{d_k}.$$

For a nonzero integer $r$, let $\operatorname{Odd}(r)$ denote the largest odd divisor of $|r|$.

**Step 1: The difference never vanishes.** The map $x \mapsto 2x+1$ is injective, and so is division by a common positive number. Hence $m_k \ne n_k$ implies $m_{k+1} \ne n_{k+1}$. Since $m_0 \ne n_0$, induction gives $m_k - n_k \neq 0$ for all $k$. Therefore $\operatorname{Odd}(m_k - n_k)$ is a well-defined positive integer.

**Step 2: $d_k$ is odd and divides $m_k - n_k$.**
- $d_k$ divides the odd number $2m_k+1$, so $d_k$ is odd.
- $d_k$ divides $(2m_k+1) - (2n_k+1) = 2(m_k - n_k)$.
- Since $\gcd(d_k, 2) = 1$, it follows that $d_k \mid m_k - n_k$.

**Step 3: The monovariant.** We have

$$m_{k+1} - n_{k+1} = \frac{(2m_k+1)-(2n_k+1)}{d_k} = 2\cdot\frac{m_k - n_k}{d_k}.$$

Multiplying by $2$ does not change the odd part. Dividing by the odd number $d_k$ divides the odd part by $d_k$. Hence

$$\operatorname{Odd}(m_{k+1} - n_{k+1}) = \frac{\operatorname{Odd}(m_k - n_k)}{d_k} \;\le\; \operatorname{Odd}(m_k - n_k),$$

with equality **if and only if** $d_k = 1$.

**Step 4: Descent.** The sequence $a_k = \operatorname{Odd}(m_k - n_k)$ is a nonincreasing sequence of positive integers. It strictly decreases (by a factor of at least $3$) exactly at the indices where $d_k > 1$.

A nonincreasing sequence of positive integers can strictly decrease only finitely many times; in fact at most $\log_3 a_0$ times. Hence $d_k = 1$ for all but finitely many $k$. That is, $2m_k+1$ and $2n_k+1$ are relatively prime for all sufficiently large $k$. $\blacksquare$

---

**Check with the example.** Start with $\frac14$: the difference is $-3$, with odd part $3$.
- Step 1: $\frac39$ has $d_0 = 3$, giving $\frac13$. The difference is $-2$, with odd part $1 = 3/3$. ✓
- From now on the odd part is $1$, so it cannot drop further. Indeed $\frac37, \frac7{15}, \frac{15}{31}, \dots$ never simplify.

**Takeaway.** When a process mixes a "growing" operation (doubling) with a "shrinking" one (cancellation), quotient out the growth. What remains, here the odd part, may be a quantity that only shrinks.
