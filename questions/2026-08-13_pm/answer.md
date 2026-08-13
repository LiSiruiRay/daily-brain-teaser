# Answer: The Möbius Transformation That Sends the Real Line to Itself

## Key Idea / Intuition

A Möbius transformation is completely determined by its values at **three points**. The real line contains infinitely many real points, so if $f$ maps $\mathbb{R}$ to itself, we can read off the coefficients by evaluating at three convenient real inputs — and the constraints force the coefficients to be (proportionally) real. Conversely, if the coefficients are real, then $f$ maps reals to reals by direct inspection. The elegance is that the "three-point determination" of Möbius transformations does all the heavy lifting.

---

## Formal Proof / Solution

### ($\Leftarrow$) Real coefficients $\Rightarrow$ real line maps to itself

If $a, b, c, d \in \mathbb{R}$ and $x \in \mathbb{R}$, then

$$f(x) = \frac{ax+b}{cx+d} \in \mathbb{R} \cup \{\infty\}$$

since the numerator and denominator are both real. Also $f(\infty) = a/c \in \mathbb{R} \cup \{\infty\}$. So $f(\mathbb{R} \cup \{\infty\}) \subseteq \mathbb{R} \cup \{\infty\}$. Since $f$ is a bijection of the Riemann sphere, equality holds. $\checkmark$

---

### ($\Rightarrow$) Real line maps to itself $\Rightarrow$ coefficients are proportionally real

Assume $f(\mathbb{R} \cup \{\infty\}) = \mathbb{R} \cup \{\infty\}$.

**Step 1: Extract three real values.**

Evaluate $f$ at $0, 1, \infty$:

$$f(0) = \frac{b}{d} =: \alpha \in \mathbb{R}, \qquad f(\infty) = \frac{a}{c} =: \beta \in \mathbb{R}, \qquad f(1) = \frac{a+b}{c+d} =: \gamma \in \mathbb{R}.$$

(We treat the case where some of these are $\infty$ separately; it only simplifies the argument.)

**Step 2: Solve for ratios.**

From $b/d = \alpha$ we get $b = \alpha d$.

From $a/c = \beta$ we get $a = \beta c$.

From $(a+b)/(c+d) = \gamma$:

$$a + b = \gamma(c + d) \implies \beta c + \alpha d = \gamma c + \gamma d.$$

Rearranging:

$$(\beta - \gamma)c = (\gamma - \alpha)d.$$

If $\beta \neq \gamma$ (i.e., $c \neq 0$), we may set $c = 1$ and obtain

$$d = \frac{\beta - \gamma}{\gamma - \alpha} \in \mathbb{R} \quad (\text{since } \alpha, \beta, \gamma \in \mathbb{R}).$$

Then $a = \beta c = \beta \in \mathbb{R}$ and $b = \alpha d \in \mathbb{R}$.

If $\beta = \gamma$, then either $\alpha = \gamma$ (all three values equal, impossible for a Möbius transformation) or $d = 0$, in which case $b = \alpha d = 0$ and we can set $c = 1$, getting $a = \beta \in \mathbb{R}$, $b = 0$, $d = 0$, $c = 1$ — all real. $\checkmark$

**Step 3: Conclusion.**

In all cases we find $a, b, c, d \in \mathbb{R}$ representing the same transformation (possibly after rescaling by $\lambda = 1/d$ or $1/c$). $\blacksquare$

---

### Remark: A slicker reformulation

A Möbius transformation preserves $\mathbb{R} \cup \{\infty\}$ if and only if it preserves the **cross-ratio** of real quadruples, which happens precisely when the transformation matrix $\begin{pmatrix} a & b \\ c & d \end{pmatrix}$ lies in $GL_2(\mathbb{R})$ (up to complex scalar). This is the group-theoretic way to say the same thing: the stabilizer of $\mathbb{R} \cup \{\infty\}$ inside $PGL_2(\mathbb{C})$ is exactly $PGL_2(\mathbb{R})$.
