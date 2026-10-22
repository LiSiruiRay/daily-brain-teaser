# Answer: A Polynomial That Lives on the Unit Circle

## Key Idea / Intuition

On the unit circle, conjugation is inversion: $\bar z = 1/z$. So the condition $p\,\bar p = 1$ is really the *algebraic* identity $p(z)\,p^*(1/z) = 1$, where $p^*$ is $p$ with conjugated coefficients. An identity between holomorphic functions on a circle holds everywhere on $\mathbb{C}\setminus\{0\}$. A zero $z_0 \neq 0$ of $p$ would make the left side vanish, which is impossible. So every zero of $p$ sits at the origin, and $p$ is a monomial.

Equivalently, one can view it through reflection symmetry. A function of modulus $1$ on the circle must have its zeros at $z_0$ "mirrored" by poles at $1/\bar z_0$. A polynomial has no poles to spare, so its zeros cannot be anywhere except $0$, whose mirror point is $\infty$.

---

## Formal Proof / Solution

**Setup.** Write $p(z) = \sum_{k=0}^{n} a_k z^k$ with $a_n \neq 0$. The polynomial is not identically zero, since $|p|=1$ on the circle. Define the "conjugate polynomial"

$$p^*(w) = \sum_{k=0}^{n} \overline{a_k}\, w^k, \qquad\text{so that}\qquad \overline{p(z)} = p^*(\bar z).$$

**Step 1: Turn the modulus condition into an analytic identity.**
For $|z| = 1$ we have $\bar z = 1/z$. Hence

$$1 = |p(z)|^2 = p(z)\,\overline{p(z)} = p(z)\,p^*(\bar z) = p(z)\,p^*(1/z).$$

**Step 2: Extend off the circle.**
The function $F(z) = p(z)\,p^*(1/z) - 1$ is holomorphic on the connected domain $\mathbb{C}\setminus\{0\}$. It vanishes on the unit circle, a set with accumulation points. By the identity theorem, $F \equiv 0$:

$$p(z)\,p^*(1/z) = 1 \qquad \text{for all } z \neq 0.$$

**Step 3: Locate the zeros.**
Suppose $p(z_0) = 0$ for some $z_0 \neq 0$. Plugging $z_0$ into the identity gives $0 \cdot p^*(1/z_0) = 1$, where $p^*(1/z_0)$ is a finite number. This is a contradiction. Therefore every zero of $p$ is at $0$.

**Step 4: Conclude.**
By the fundamental theorem of algebra, $p(z) = a_n \prod_{i=1}^{n}(z - z_i)$. Step 3 shows all $z_i = 0$, so $p(z) = a_n z^n$. Evaluating at $z=1$ gives $|a_n| = 1$. $\blacksquare$

---

### Alternative proof (maximum modulus + Blaschke factors)

$p$ has no zeros on $|z|=1$, so its zeros $z_1,\dots,z_m$ (with multiplicity) in the closed disk all lie in the open disk. Form the Blaschke product

$$B(z) = \prod_{i=1}^{m} \frac{z - z_i}{1 - \overline{z_i}\, z}.$$

Each factor has modulus $1$ on $|z|=1$. The quotient $g = p/B$ is holomorphic and zero-free on a neighborhood of the closed disk, with $|g| = 1$ on the boundary.

- The maximum modulus principle applied to $g$ gives $|g| \le 1$ inside.
- The maximum modulus principle applied to $1/g$ gives $|g| \ge 1$ inside.

So $|g| \equiv 1$, and an open mapping argument shows $g \equiv c$ is constant. Hence $p = cB$.

$B$ has a pole at $1/\overline{z_i}$ for every $z_i \neq 0$, while $p$ has no poles. Therefore all $z_i = 0$, giving $B(z) = z^m$ and $p = c z^m$.

---

### Bonus: rational functions

The same reasoning shows that a rational function $R$ with $|R| = 1$ on $|z| = 1$ satisfies $R(z)\,\overline{R(1/\bar z)} = 1$. Zeros at $a$ must therefore be paired with poles at $1/\bar a$. Consequently

$$R(z) = c\, z^{k} \prod_{i} \frac{z - a_i}{1 - \overline{a_i}\, z}, \qquad |c| = 1,\ k \in \mathbb{Z},\ a_i \neq 0.$$

So $R$ is a unimodular constant times a power of $z$ times a finite Blaschke product. Taking $|a_i| < 1$ for all $i$ is exactly the condition that $R$ map the unit disk into itself. These are precisely the proper holomorphic self-maps of the disk.
