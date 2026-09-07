# Answer: Surjective Map on Interval Has Two Fixed Points

## Key Idea / Intuition

The circle admits a rotation with no fixed point, so the answer to the first part is **no** — a simple rotation is a counterexample. For the second part, surjectivity is the key constraint: since $h$ maps onto all of $[0,1]$, the points $0$ and $1$ must each be "hit," and this forces the graph of $h$ to cross the diagonal $y = x$ at least twice. The argument is a clever two-application of IVT, exploiting the boundary behavior that surjectivity forces.

---

## Formal Proof / Solution

### Part 1: The Circle Has No Fixed-Point Property

The rotation $g : S^1 \to S^1$ defined by $g(e^{i\theta}) = e^{i(\theta + \pi)}$ (rotation by $180°$) is continuous and has **no fixed point**, since $g(z) = -z \neq z$ for all $z \in S^1$.

So the fixed-point property fails for $S^1$.

---

### Part 2: Surjective $h : [0,1] \to [0,1]$ Has At Least Two Fixed Points

**Setup.** Define $\varphi(x) = h(x) - x$. We want to show $\varphi$ has **at least two zeros** in $[0,1]$.

**Step 1: There is at least one fixed point.**

Since $h$ maps $[0,1]$ to $[0,1]$, we have $h(0) \geq 0$ so $\varphi(0) \geq 0$, and $h(1) \leq 1$ so $\varphi(1) \leq 0$. By IVT, there exists $c \in [0,1]$ with $\varphi(c) = 0$, i.e., $h(c) = c$.

**Step 2: Surjectivity forces $h$ to reach both endpoints, creating a second crossing.**

Since $h$ is surjective, there exist $a, b \in [0,1]$ with $h(a) = 0$ and $h(b) = 1$.

- At $x = a$: $\varphi(a) = h(a) - a = 0 - a = -a \leq 0$, with equality iff $a = 0$.
- At $x = b$: $\varphi(b) = h(b) - b = 1 - b \geq 0$, with equality iff $b = 1$.

**Step 3: Separate into cases.**

**Case A**: $a = 0$ and $b = 1$.

Then $h(0) = 0$ and $h(1) = 1$, so both endpoints are already fixed points. That gives **two** fixed points immediately.

**Case B**: $a > 0$ (so $\varphi(a) < 0$) or $b < 1$ (so $\varphi(b) > 0$).

Without loss of generality suppose $a > 0$, so $\varphi(a) < 0$.

- We have $\varphi(0) = h(0) \geq 0$.
- $\varphi(a) < 0$.

By IVT, there exists $c_1 \in [0, a)$ with $\varphi(c_1) = 0$ — a fixed point strictly before $a$.

Now consider what happens after $a$: since $h$ is surjective, there exists $b$ with $h(b) = 1$, so $\varphi(b) = 1 - b \geq 0$. If $b > a$, then:

- $\varphi(a) < 0$ and $\varphi(b) \geq 0$, so by IVT there exists $c_2 \in (a, b]$ with $\varphi(c_2) = 0$.

Since $c_1 < a \leq c_2$, we have **two distinct fixed points**.

If instead $b \leq a$, we can apply a symmetric argument using $\varphi(1) = h(1) - 1 \leq 0$ and $\varphi(b) \geq 0$ with $b < 1$, again obtaining two zeros.

**Conclusion.** In every case, $h$ has at least two fixed points. $\blacksquare$

---

**Remark.** The result is tight: $h(x) = x$ has infinitely many fixed points, and one can construct surjections with exactly two. The key is that surjectivity forces $h$ to "dip to $0$" and "reach $1$," creating two graph crossings with the diagonal.
