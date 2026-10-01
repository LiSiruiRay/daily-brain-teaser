# Answer: The Holomorphic Function That Knows Its Zeros Are Real

## Key Idea / Intuition

The answer is **no** in general — roots of the derivative need not stay on the unit circle. The key insight is the **Gauss–Lucas theorem**: the roots of $p'$ lie in the *convex hull* of the roots of $p$. For roots on the unit circle, the convex hull is the **closed unit disk** $|z| \leq 1$. So the correct statement is that all roots of $p'$ lie in $|z| \leq 1$, with equality (on the circle itself) only in degenerate cases. A single clean example demolishes the stronger claim, and then Gauss–Lucas clinches the sharp bound.

---

## Formal Proof / Solution

### Step 1: Counterexample showing $p'$ need not have roots on $|z|=1$

Take
$$p(z) = z^n - 1, \quad n \geq 3.$$
The roots of $p$ are the $n$-th roots of unity, all on $|z|=1$. ✓

Now $p'(z) = nz^{n-1}$, which has only the root $z = 0$ (with multiplicity $n-1$).

Since $|0| = 0 < 1$, the root of $p'$ is **strictly inside** the unit disk, not on the unit circle.

So the naive conjecture is **false**.

---

### Step 2: The correct statement via Gauss–Lucas

**Theorem (Gauss–Lucas).** If $p$ is a polynomial with roots $z_1, \ldots, z_n \in \mathbb{C}$, then every root of $p'$ lies in the convex hull $\operatorname{conv}(z_1, \ldots, z_n)$.

**Proof of Gauss–Lucas.** Write
$$\frac{p'(z)}{p(z)} = \sum_{k=1}^n \frac{1}{z - z_k}.$$
Suppose $p'(w) = 0$ but $p(w) \neq 0$. Then
$$\sum_{k=1}^n \frac{1}{w - z_k} = 0.$$
Taking complex conjugates and writing $\frac{1}{w-z_k} = \frac{\overline{w-z_k}}{|w-z_k|^2}$, we get
$$\sum_{k=1}^n \frac{\bar{w} - \bar{z}_k}{|w-z_k|^2} = 0 \implies \bar{w} = \frac{\sum_k \frac{\bar{z}_k}{|w-z_k|^2}}{\sum_k \frac{1}{|w-z_k|^2}}.$$
This says $\bar{w}$ (hence $w$) is a **weighted average** of the $\bar{z}_k$ (hence of the $z_k$) with positive weights $\lambda_k = \frac{1}{|w-z_k|^2}$. So $w \in \operatorname{conv}(z_1,\ldots,z_n)$. $\square$

---

### Step 3: Application to roots on $|z|=1$

If all roots of $p$ lie on $|z|=1$, then $\operatorname{conv}(z_1,\ldots,z_n) \subseteq \overline{\mathbb{D}}$ (the closed unit disk), since the unit disk is convex and contains the unit circle.

Therefore, **every root of $p'$ satisfies $|z| \leq 1$**.

The example $p(z)=z^n-1$ shows this bound is sharp: roots of $p'$ can be strictly inside $|z|<1$.

---

### Summary

| Claim | Truth |
|---|---|
| All roots of $p'$ lie on $\|z\|=1$ | ❌ False ($p(z)=z^n-1$ gives $p'$ vanishing only at $0$) |
| All roots of $p'$ lie in $\|z\|\leq 1$ | ✅ True by Gauss–Lucas |

The beautiful moral: **Gauss–Lucas is a convexity theorem in disguise**, and the "logarithmic derivative = weighted barycenter" identity is the one-line proof.
