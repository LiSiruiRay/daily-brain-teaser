# Answer: Zero-Mean Functions: A Closed Hyperplane in C([0,1])

## Key Idea / Intuition

The set $A$ is a **closed proper subspace** of $C([0,1])$, not a dense set. The obstruction is the integral functional: if $f_n \to f$ uniformly, then $\int_0^1 f_n \to \int_0^1 f$, so the limit of any sequence in $A$ must also integrate to zero. Thus $A$ is already closed, and you can only uniformly approximate functions whose integral is **exactly** zero. The punchline is surprisingly clean: the closure of $A$ is $A$ itself, and the "reachable" functions are precisely those with zero mean.

---

## Formal Proof / Solution

**Step 1: $A$ is closed.**

Define the linear functional $L : C([0,1]) \to \mathbb{R}$ by $L(f) = \int_0^1 f(x)\,dx$.

This functional is **continuous** in the uniform norm, since

$$|L(f)| = \left|\int_0^1 f(x)\,dx\right| \leq \|f\|_\infty \cdot 1 = \|f\|_\infty.$$

Since $A = L^{-1}(\{0\})$ is the preimage of the closed set $\{0\}$ under a continuous map, $A$ is **closed** in $C([0,1])$.

**Step 2: $A$ is not dense.**

The constant function $g \equiv 1$ has $L(g) = 1 \neq 0$, so $g \notin A$.

If $A$ were dense, there would exist $f_n \in A$ with $\|f_n - g\|_\infty \to 0$. But then

$$|L(f_n) - L(g)| \leq \|f_n - g\|_\infty \to 0,$$

which forces $L(g) = \lim L(f_n) = 0$, a contradiction.

**Step 3: Characterization of $\overline{A}$.**

Since $A$ is already closed, $\overline{A} = A$ itself. Therefore:

$$\overline{A} = A = \left\{f \in C([0,1]) : \int_0^1 f(x)\,dx = 0\right\}.$$

A function $g \in C([0,1])$ can be uniformly approximated by elements of $A$ **if and only if** $\int_0^1 g(x)\,dx = 0$.

**Step 4: The geometric picture (codimension-1 hyperplane).**

$A$ is a closed **hyperplane** in the Banach space $C([0,1])$: it is the kernel of the bounded linear functional $L$. Its codimension is exactly 1. The full space decomposes as

$$C([0,1]) = A \oplus \mathbb{R} \cdot \mathbf{1},$$

where $\mathbf{1}$ is the constant function $1$. Any $f$ decomposes as

$$f = \underbrace{\left(f - \int_0^1 f\,dx\right)}_{\in A} + \underbrace{\int_0^1 f\,dx}_{\text{scalar}} \cdot \mathbf{1}.$$

The distance from any $f$ to $A$ is exactly $\left|\int_0^1 f(x)\,dx\right|$, which is zero if and only if $f \in A$.

**Conclusion:** $A$ is a closed, proper, dense-in-itself subspace of codimension 1. The only functions uniformly approximable by zero-mean continuous functions are the zero-mean continuous functions themselves.
