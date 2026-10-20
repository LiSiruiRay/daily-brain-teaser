# Answer: Furstenberg's Topological Proof of Infinitely Many Primes

## Key Idea / Intuition

Arithmetic progressions form a basis of a topology in which open sets are "fat": a nonempty open set always contains an entire infinite progression, so no finite nonempty set can be open. Each progression is also closed, because its complement is a finite union of other progressions, namely the remaining residue classes. Every integer except $\pm 1$ lies in some $N_{0,p}$. If there were only finitely many primes, $\bigcup_p N_{0,p}$ would be a *finite* union of closed sets, hence closed. Its complement $\{-1, 1\}$ would then be open, which contradicts fatness. The arithmetic content is just "every $n \ne \pm 1$ has a prime factor." The rest is the fact that finite unions of closed sets are closed.

---

## Formal Proof / Solution

**Step 1: It is a topology.**

- $\varnothing$ is open by definition. $\mathbb{Z}$ is open since $N_{a,1} = \mathbb{Z}$.
- *Arbitrary unions.* If $a \in \bigcup_i U_i$, then $a \in U_j$ for some $j$. So some $N_{a,b} \subseteq U_j \subseteq \bigcup_i U_i$.
- *Finite intersections.* Let $a \in U_1 \cap U_2$ with $N_{a,b_1} \subseteq U_1$ and $N_{a,b_2} \subseteq U_2$. Put $b = \operatorname{lcm}(b_1,b_2)$, or simply $b = b_1 b_2$. Then
$$N_{a,b} \subseteq N_{a,b_1} \cap N_{a,b_2} \subseteq U_1 \cap U_2.$$
Induction handles any finite intersection.

**Step 2: Two properties.**

- *(A) Nonempty open sets are infinite.* A nonempty open $U$ contains some $N_{a,b}$, which is infinite.
- *(B) $N_{a,b}$ is open and closed.*
  - It is open: for any $x \in N_{a,b}$, we have $N_{x,b} = N_{a,b}$.
  - It is closed: the integers split into the $b$ residue classes mod $b$, so
  $$\mathbb{Z} \setminus N_{a,b} = \bigcup_{i=1}^{b-1} N_{a+i,\,b}.$$
  This is a union of open sets, hence open.

**Step 3: Infinitely many primes.**

Every integer $n \ne \pm 1$ has a prime divisor $p$, which means $n \in N_{0,p}$. Conversely, no $N_{0,p}$ contains $\pm 1$. Therefore
$$\mathbb{Z} \setminus \{-1, 1\} = \bigcup_{p \text{ prime}} N_{0,p}.$$

Suppose there were only finitely many primes. Then the right-hand side is a finite union of closed sets, by (B), and so it is closed. Hence its complement $\{-1, 1\}$ is open. But $\{-1,1\}$ is nonempty and finite, which contradicts (A). $\blacksquare$

**Bonus remark.**

- The single place where finiteness of the set of primes enters is the axiom "finite unions of closed sets are closed." With infinitely many primes, the union is a union of infinitely many closed sets and need not be closed. Indeed, here it is not closed, since its complement $\{\pm 1\}$ is not open.
- This topology is the *profinite* (or "evenly spaced integer") topology. It is metrizable, Hausdorff, and has no isolated points.
- As Aigner–Ziegler note, the proof is essentially a repackaging of the inclusion–exclusion / Euclid idea in topological language. It is beautiful precisely because the topology does nothing but encode the residue classes.

*Reference:* M. Aigner & G. M. Ziegler, *Proofs from THE BOOK* (The_BOOK.pdf), Chapter 1 "Six proofs of the infinity of primes", Sixth proof (H. Furstenberg, 1955).
