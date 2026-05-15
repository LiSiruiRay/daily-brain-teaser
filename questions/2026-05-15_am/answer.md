# Answer: A Polynomial That Takes the Value 1 Too Often

## Key Idea / Intuition

If a polynomial takes the value $1$ at four distinct integer points, we can **factor out** those roots explicitly. The leftover polynomial has integer coefficients, so when we evaluate at any integer $b$, the product of four distinct integer factors must multiply to $-2$. But a product of four distinct integers cannot equal $-2$, since $-2$ cannot be written as a product of four distinct integers — there simply aren't enough small integers to make this work.

---

## Formal Proof / Solution

**Setup.** Since $p(a_i) = 1$ for $i = 1, 2, 3, 4$, the polynomial $q(x) = p(x) - 1$ has roots at $a_1, a_2, a_3, a_4$. Therefore:

$$q(x) = p(x) - 1 = (x - a_1)(x - a_2)(x - a_3)(x - a_4) \cdot r(x)$$

for some polynomial $r(x)$ with integer coefficients (since $p$ has integer coefficients).

**Evaluate at $b$.** Suppose for contradiction that $p(b) = -1$ for some integer $b$. Then $q(b) = -2$, so:

$$(b - a_1)(b - a_2)(b - a_3)(b - a_4) \cdot r(b) = -2.$$

Since all quantities here are integers, we need:

$$(b - a_1)(b - a_2)(b - a_3)(b - a_4) \mid -2.$$

**Key observation.** The four values $b - a_1,\, b - a_2,\, b - a_3,\, b - a_4$ are **four distinct integers** (since $a_1, a_2, a_3, a_4$ are distinct). Their product must divide $-2$, so their product is one of $\pm 1, \pm 2$.

But a product of **four distinct integers** must have absolute value at least $|{-3} \cdot {-1} \cdot 1 \cdot 2| = 6$ if we try to make them small — or more carefully: four distinct integers include at least two with $|n| \geq 1$ and $|n| \geq 2$, and in fact the minimum absolute product of four distinct integers occurs at $\{-1, 0, 1, 2\}$ (or similar), giving product $0$. But the product cannot be $0$ (that would give $p(b) = 1$, not $-1$).

Let's be precise. Suppose the four distinct integers $c_1 < c_2 < c_3 < c_4$ satisfy $|c_1 c_2 c_3 c_4| \leq 2$. Since they are distinct, at least two of them are nonzero. If all four are nonzero, then $|c_1 c_2 c_3 c_4| \geq 1 \cdot 1 \cdot 2 \cdot 3 = 6 > 2$, contradiction. So at least one is zero, but then the product is $0$, not $\pm 2$. 

Wait — if one is zero: then product = 0 ≠ ±2. If none is zero: four distinct nonzero integers have $|$product$| \geq 1 \cdot 2 \cdot 3 \cdot \ldots$? No, they can be negative. The **smallest** absolute product of four distinct nonzero integers is achieved by $\{-2, -1, 1, 2\}$:

$$(-2)(-1)(1)(2) = 4 > 2.$$

Any other set of four distinct nonzero integers has an even larger absolute product. So in every case, either the product is $0$ (impossible, since we need $\pm 2$), or the absolute value is at least $4 > 2$ (impossible).

**Conclusion.** In all cases, the product $(b-a_1)(b-a_2)(b-a_3)(b-a_4)$ cannot equal $\pm 1$ or $\pm 2$, so the equation cannot hold. This contradicts the assumption that $p(b) = -1$, completing the proof. $\blacksquare$

---

**Summary of the key bound:**
- Four distinct integers, all zero → product 0 ✗  
- One zero among them → product 0 ✗  
- All nonzero, four distinct integers → $|\text{product}| \geq 4$ ✗  

None of these can equal $\pm 2$, so $p(b) = -1$ is impossible.
