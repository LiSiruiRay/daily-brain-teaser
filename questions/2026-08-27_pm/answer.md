# Answer: The Entire Function Bounded on a Line

## Key Idea / Intuition

The conditions on the real and imaginary axes secretly force $f(z) + f(-z)$ to vanish everywhere. Define $g(z) = f(z) + f(-z)$: this is entire, and the two axis conditions together imply $g$ vanishes on *both* coordinate axes. Since the zeros of $g$ accumulate along these lines, the identity theorem kills $g$ entirely.

---

## Formal Proof / Solution

**Step 1: Set up the auxiliary function.**

Define
$$g(z) = f(z) + f(-z).$$
Since $f$ is entire, so is $g$.

**Step 2: Use the real-axis condition.**

For $x \in \mathbb{R}$, we are told $f(x) \in \mathbb{R}$, so $\overline{f(x)} = f(x)$. Also $-x \in \mathbb{R}$, so $f(-x) \in \mathbb{R}$. Thus
$$g(x) = f(x) + f(-x) \in \mathbb{R}.$$

But wait — we need $g$ to *vanish* on the real axis, not just be real. Let us use the imaginary-axis condition first.

**Step 3: Use the imaginary-axis condition.**

For $t \in \mathbb{R}$, let $z = it$. We are told $f(it)$ is purely imaginary, so $f(it) = i\,c(t)$ for some $c(t) \in \mathbb{R}$. Then $-z = -it$, and $f(-it)$ is also purely imaginary (since $-it$ lies on the imaginary axis), say $f(-it) = i\,d(t)$. Thus
$$g(it) = f(it) + f(-it) = i\bigl(c(t) + d(t)\bigr) \in i\mathbb{R}.$$

**Step 4: Combine both conditions for $g$.**

From Step 2: for real $x$, $g(x) = f(x) + f(-x)$ is real.

Now use the **Schwarz reflection principle** perspective. Because $f$ takes real values on $\mathbb{R}$, the power series of $f$ centered at $0$ has **real coefficients**. Write
$$f(z) = \sum_{n=0}^\infty a_n z^n, \quad a_n \in \mathbb{R}.$$

*Why real coefficients?* The Taylor coefficients satisfy $a_n = f^{(n)}(0)/n!$. Since all derivatives of $f$ at $0$ are real (by differentiating the condition $f(x)\in\mathbb{R}$ for $x\in\mathbb{R}$ and taking the limit $x\to 0$), we get $a_n \in \mathbb{R}$.

**Step 5: Apply the imaginary-axis condition to the series.**

For $z = it$ with $t \in \mathbb{R}$:
$$f(it) = \sum_{n=0}^\infty a_n (it)^n = \sum_{k=0}^\infty a_{2k}(-1)^k t^{2k} + i \sum_{k=0}^\infty a_{2k+1}(-1)^k t^{2k+1}.$$

The real part is $\sum_{k} a_{2k}(-1)^k t^{2k}$ and the imaginary part is $\sum_{k} a_{2k+1}(-1)^k t^{2k+1}$.

Since $f(it)$ must be **purely imaginary** for all $t \in \mathbb{R}$, the real part must vanish:
$$\sum_{k=0}^\infty a_{2k}(-1)^k t^{2k} = 0 \quad \text{for all } t \in \mathbb{R}.$$

This is a power series in $t$ that is identically zero, so every coefficient vanishes:
$$a_{2k} = 0 \quad \text{for all } k \geq 0.$$

**Step 6: Conclude $f$ is odd.**

Since all even-degree Taylor coefficients vanish, we have
$$f(z) = \sum_{k=0}^\infty a_{2k+1} z^{2k+1},$$
which is an odd function. Therefore
$$f(-z) = -f(z) \quad \text{for all } z \in \mathbb{C}. \qquad \blacksquare$$

---

**Remark:** The two conditions — real on $\mathbb{R}$, imaginary on $i\mathbb{R}$ — together do exactly the right amount of work: real coefficients from the first, vanishing even coefficients from the second. Each condition alone is not enough.
