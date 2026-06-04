# Answer: A Holomorphic Function That Is Its Own Derivative

## Key Idea / Intuition

The condition $f' = f$ forces the Taylor coefficients of $f$ to be completely determined: they must be $a_n = 1/n!$. Once you know the power series, the functional equation $f(z+w) = f(z)f(w)$ is **not** proved by plugging in the series naively — instead, the elegant trick is to fix $w$ and consider $g(z) = f(z+w) / f(w)$. Because $f$ has no zeros (shown from the functional equation, or by noting $f(z)f(-z) = f(0) = 1$), the ratio is well-defined and entire, satisfies $g' = g$, $g(0) = 1$ — so uniqueness from the power series argument forces $g(z) = f(z)$.

---

## Formal Proof / Solution

### Step 1: The power series of $f$ is uniquely determined

Since $f$ is entire, write $f(z) = \sum_{n=0}^\infty a_n z^n$. The condition $f'(z) = f(z)$ gives

$$\sum_{n=1}^\infty n\, a_n\, z^{n-1} = \sum_{n=0}^\infty a_n\, z^n.$$

Matching coefficients: $(n+1)a_{n+1} = a_n$ for all $n \geq 0$, so

$$a_n = \frac{a_0}{n!}.$$

With $f(0) = a_0 = 1$, we get $f(z) = \sum_{n=0}^\infty \frac{z^n}{n!}$.

**Uniqueness:** Any entire solution with $f(0) = 1$ and $f' = f$ must have this series — the recurrence determines all coefficients.

---

### Step 2: $f$ has no zeros

From the series, $f(z) \cdot f(-z) = f(0) = 1$ (which we will prove momentarily from the functional equation, but can also be seen directly: $f(z)f(-z)$ is entire, its derivative is $f'(z)f(-z) - f(z)f'(-z) = f(z)f(-z) - f(z)f(-z) = 0$, so $f(z)f(-z) = f(0)\cdot f(0) = 1$). Hence $f(z) \neq 0$ for all $z$.

---

### Step 3: Proving the functional equation

Fix any $w \in \mathbb{C}$. Define

$$g(z) = \frac{f(z + w)}{f(w)}.$$

Since $f(w) \neq 0$, $g$ is entire. Compute:

- $g'(z) = \dfrac{f'(z+w)}{f(w)} = \dfrac{f(z+w)}{f(w)} = g(z)$.
- $g(0) = \dfrac{f(w)}{f(w)} = 1$.

So $g$ satisfies the same ODE and initial condition as $f$. By **Step 1**, any entire function satisfying $h' = h$, $h(0) = 1$ must equal $\sum z^n/n!$. Therefore $g(z) = f(z)$, i.e.,

$$f(z + w) = f(z)\,f(w). \qquad \square$$

---

### Step 4: Conclusion

The unique entire function with $f' = f$ and $f(0) = 1$ is

$$\boxed{f(z) = e^z = \sum_{n=0}^\infty \frac{z^n}{n!}}.$$

The functional equation $f(z+w) = f(z)f(w)$ is the **defining algebraic property** of the exponential — derived here purely from complex analysis, without any reference to real exponentials or ODEs.

---

### Why This Is Beautiful

The proof is a perfect loop: the power series forces uniqueness, uniqueness forces the functional equation, and the functional equation reveals the object is $e^z$. The key trick — **fixing $w$ and forming $f(z+w)/f(w)$** — is a clean, one-line idea that replaces any computation.
