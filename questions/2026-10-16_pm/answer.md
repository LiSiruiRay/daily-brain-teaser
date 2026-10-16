# Answer: Three-Fold Closure Forces Two-Fold Closure

## Key Idea / Intuition

Suppose both $T$ and $U$ fail to be closed. Then some pair from $T$ "leaks" into $U$, and some pair from $U$ leaks into $T$. Multiply both leaky pairs together to get four numbers. The same product can be bracketed as "one element of $U$ times two elements of $U$" or as "two elements of $T$ times one element of $T$." The three-fold rule then forces this single number to lie in both $U$ and $T$, which is impossible because they are disjoint.

The whole proof is: **one product, two bracketings, two incompatible verdicts.**

---

## Formal Proof / Solution

**Step 1: Assume both fail.** Suppose, for contradiction, that neither $T$ nor $U$ is closed under multiplication. Then:

- there exist $t_1,t_2\in T$ with $t_1t_2\notin T$;
- there exist $u_1,u_2\in U$ with $u_1u_2\notin U$.

**Step 2: Locate the leaked products.** Since $S$ is closed under multiplication, $t_1t_2\in S$ and $u_1u_2\in S$. Since $S=T\sqcup U$, it follows that
$$t_1t_2\in U,\qquad u_1u_2\in T.$$

**Step 3: Bracket the same product two ways.** Consider
$$P = t_1t_2u_1u_2 .$$

- *First bracketing.* Write $P=(t_1t_2)\cdot u_1\cdot u_2$. Each of the three factors $t_1t_2,\;u_1,\;u_2$ lies in $U$. By the three-fold hypothesis for $U$, we get $P\in U$.
- *Second bracketing.* Write $P=t_1\cdot t_2\cdot(u_1u_2)$. Each of the three factors $t_1,\;t_2,\;u_1u_2$ lies in $T$. By the three-fold hypothesis for $T$, we get $P\in T$.

Both bracketings are legitimate because multiplication of real numbers is associative.

**Step 4: Contradiction.** We have found $P\in T\cap U$, but $T$ and $U$ are disjoint. Hence our assumption was false, and at least one of $T$, $U$ is closed under multiplication. $\blacksquare$

---

### Remarks

- **What was actually used.** We used only that multiplication is associative. Commutativity was not needed, and neither was the fact that we are working with real numbers. The same argument works in any semigroup $S=T\sqcup U$.
- **The model example.** Positives versus negatives is the prototype. There, $U$ behaves like the "odd" coset of a $\mathbb{Z}/2$-grading. Three-fold closure is exactly what an odd coset satisfies, since odd + odd + odd is odd. The theorem says that two such "odd-like" pieces cannot coexist.
- **The general lesson.** When a hypothesis is about $k$-fold products and the conclusion is about $2$-fold products, try building a single product that can be read as a $k$-fold product in two different ways.
