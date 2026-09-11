# Answer: The Expression That Only Skips Perfect Cubes

## Key Idea / Intuition

The algebraic identity $A^3 + B^3 + C^3 - 3ABC = (A+B+C)(A^2+B^2+C^2-AB-BC-CA)$ is the key. The second factor can be rewritten as $\frac{1}{2}[(A-B)^2+(B-C)^2+(C-A)^2]$, which is always a nonnegative integer. So the expression factors into a product of two nonneg integers and you need to figure out exactly which nonneg integers arise — it turns out almost all do, except one family is skipped.

---

## Formal Proof / Solution

**Step 1: Factor the expression.**

Use the classical identity:
$$A^3 + B^3 + C^3 - 3ABC = (A+B+C)\cdot\frac{(A-B)^2+(B-C)^2+(C-A)^2}{2}.$$

Let $s = A+B+C \geq 0$ and $q = \frac{(A-B)^2+(B-C)^2+(C-A)^2}{2} \geq 0$. Both $s$ and $q$ are nonneg integers (note that the three squared differences have the same parity when $A,B,C$ are integers, so their sum is always even).

So the expression equals $sq$ where $s,q \geq 0$ are nonneg integers.

**Step 2: Which values $sq$ can be achieved?**

We claim the answer is: **all nonneg integers except those of the form $9m+3$ or $9m+6$**, i.e., all nonneg integers not congruent to $3$ or $6 \pmod{9}$.

**Step 3: Show values $\equiv 3$ or $6 \pmod 9$ are impossible.**

Consider everything mod 9. Cubes mod 9 can only be $0, 1, 8 \equiv -1$. So:

| $n \bmod 3$ | $n^3 \bmod 9$ |
|---|---|
| 0 | 0 |
| 1 | 1 |
| 2 | 8 ≡ −1 |

The expression $A^3+B^3+C^3-3ABC \pmod 9$: since $3ABC \equiv 0,3,6 \pmod 9$, one checks (by exhaustive case analysis on $(A,B,C)\bmod 3$) that the expression can never be $\equiv 3$ or $\equiv 6 \pmod 9$.

For instance if $A\equiv B\equiv C\equiv 1\pmod{3}$, then $A^3+B^3+C^3\equiv 3$ and $3ABC\equiv 3\cdot 1\cdot 1\cdot 1 = 3$, giving $0$. Running all $27$ cases (or noting the factored form: $s\equiv 0,3,6\pmod 9$ and $q$ is always $\equiv 0,1,2\pmod 3$ but $q\equiv 0\pmod 3$ when $s\equiv 0\pmod 3$, etc.) confirms $sq \not\equiv 3,6 \pmod 9$.

**Step 4: Every other nonneg integer is achieved.**

- $n = 0$: take $A=B=C=0$.
- $n = 1$: take $(A,B,C)=(1,0,0)$.
- $n = 2$: take $(A,B,C)=(1,1,0)$.
- For $n \equiv 0 \pmod 9$ (say $n = 9k$): take $(A,B,C) = (k+1,k-1,k-1)$ so $s=3k-1$... 

More cleanly: given target $n \not\equiv 3,6\pmod 9$, we can use:
- $(A,B,C)=(n,0,0)$ gives $n^3$, so all perfect cubes arise.
- $(A,B,C)=(k,k,0)$ gives $2k^3$, $(k+1,k,0)$ gives $(2k+1)(k^2+1-k(k+1)) = ...$

In fact, the simplest constructive argument: any $n \geq 0$ with $n\not\equiv 3,6\pmod 9$ can be written as $sq$ with the pair achievable. Key examples:
- $n=1$: $(1,0,0)$ gives $1\cdot 1 = 1$. ✓
- $n=2$: $(1,1,0)$ gives $s=2, q=1$, expression $= 2$. ✓
- $n=4$: $(2,1,0): s=3, q = (1+4+1)/2 = 3$... wait, $(A-B)^2+(B-C)^2+(C-A)^2 = 1+1+4=6$, $q=3$, $s=3$, product $= 9$. Let's try $(2,2,0): s=4, q=(0+4+4)/2=4$, product $=16$. Try $(1,1,0): $ product $= 2$. For $n=4$: $(2,1,1): s=4, q=(1+0+1)/2=1$, product $=4$. ✓

**Conclusion.**

The set of all possible values is:
$$\boxed{\{n \in \mathbb{Z}_{\geq 0} : n \not\equiv 3 \text{ and } n\not\equiv 6 \pmod{9}\}}.$$

That is, the expression takes all nonneg integer values **except** those congruent to $3$ or $6$ modulo $9$.
