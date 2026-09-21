# Answer: Stone–Weierstrass: Even vs Odd Power Subalgebras

## Key Idea / Intuition

The Stone–Weierstrass theorem says a subalgebra of $C(K)$ is dense if and only if it **separates points** and **contains a nonzero constant**. The algebra $A$ (even powers) contains the constant function $1$ (take $k=0$, $a_0 = 1$) and separates points on $[0,1]$, so it is dense. The algebra $B$ (odd powers only) contains **no nonzero constants** — every function in $B$ vanishes at $x=0$ — and therefore cannot approximate, say, $f \equiv 1$.

---

## Formal Proof / Solution

### $A$ is dense in $C([0,1])$

$A$ consists of all polynomials in the variable $u = x^2$. Since $x \in [0,1]$, we have $u \in [0,1]$ as well, and the map $x \mapsto x^2$ is a **bijection** from $[0,1]$ onto $[0,1]$.

More precisely, define $\varphi : [0,1] \to [0,1]$ by $\varphi(x) = x^2$. Any $f \in C([0,1])$ defines $g = f \circ \varphi^{-1} \in C([0,1])$ (since $\varphi^{-1}(u) = \sqrt{u}$ is continuous on $[0,1]$). By the classical **Weierstrass approximation theorem**, polynomials in $u$ are dense in $C([0,1])$, so $g$ can be approximated by some $p(u) = \sum a_k u^k$. Then

$$f(x) = g(x^2) \approx p(x^2) = \sum a_k x^{2k} \in A.$$

Hence $A$ is dense. Equivalently, by the **Stone–Weierstrass theorem**: $A$ is a subalgebra of $C([0,1])$ that

1. **contains constants**: $f \equiv 1 \in A$ (set $a_0 = 1$, $N=0$),
2. **separates points**: for $x \neq y$ in $[0,1]$, $x^2 \neq y^2$ (since both are nonnegative and distinct implies their squares are distinct on $[0,1]$).

So $A$ is dense by Stone–Weierstrass. $\checkmark$

---

### $B$ is **not** dense in $C([0,1])$

Every function $f \in B$ has the form $f(x) = a_1 x + a_3 x^3 + \cdots + a_{2N+1} x^{2N+1}$, so in particular

$$f(0) = 0 \quad \text{for every } f \in B.$$

The **closure** of $B$ in the sup-norm therefore satisfies: every $g \in \overline{B}$ must also satisfy $g(0) = 0$ (since uniform limits preserve pointwise values). But the constant function $f \equiv 1$ satisfies $f(0) = 1 \neq 0$, so

$$1 \notin \overline{B}.$$

Hence $B$ is **not** dense in $C([0,1])$.

**The precise obstruction:** $B$ is contained in the proper closed subspace

$$\{ f \in C([0,1]) : f(0) = 0 \},$$

so its closure can be at most this proper subspace—far from all of $C([0,1])$.

---

### Summary

| Algebra | Contains constants? | Separates points? | Dense in $C([0,1])$? |
|---------|-------------------|-------------------|----------------------|
| $A$ (even powers $x^{2k}$) | ✓ (constant 1) | ✓ | **Yes** |
| $B$ (odd powers $x^{2k+1}$) | ✗ (all vanish at 0) | ✓ | **No** |

The Stone–Weierstrass theorem makes the failure of $B$ structural and inevitable: lacking constants is a fatal obstruction when the base point is in the domain.
