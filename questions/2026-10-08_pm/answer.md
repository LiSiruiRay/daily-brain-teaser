# Answer: The Conformal Map That Unfolds a Wedge

## Key Idea / Intuition

A wedge of angle $\alpha$ is "too narrow" — it subtends only a fraction $\alpha/\pi$ of a half-plane. The fix is to **raise $z$ to the power $\pi/\alpha$**: this is the one holomorphic map that rotates and stretches angles, turning the wedge boundary rays (at angles $0$ and $\alpha$) into the real axis. Once you have the upper half-plane, the classical Cayley map $w \mapsto \frac{w-i}{w+i}$ converts it to the disk. Composing these two steps solves both parts.

---

## Formal Proof / Solution

### Part (a): Wedge $W_\alpha \to \mathbb{H}$

The wedge $W_\alpha$ has boundary rays at argument $0$ and $\alpha$.

**Define**
$$f(z) = z^{\pi/\alpha}.$$

Taking the principal branch with $\arg(z) \in (0, \alpha)$, we get
$$\arg(f(z)) = \frac{\pi}{\alpha} \arg(z) \in \left(0, \frac{\pi}{\alpha}\cdot\alpha\right) = (0, \pi).$$

So $f$ maps $W_\alpha$ into $\{ w : 0 < \arg(w) < \pi \} = \mathbb{H}$. Since $f$ is holomorphic and injective on $W_\alpha$ (it's a bijection onto $\mathbb{H}$), this is the desired conformal map:

$$\boxed{f(z) = z^{\pi/\alpha} : W_\alpha \xrightarrow{\;\sim\;} \mathbb{H}.}$$

---

### Part (b): Quarter-plane $\to$ Unit disk $\mathbb{D}$

The quarter-plane is $W_{\pi/2} = \{x > 0,\, y > 0\}$, so $\alpha = \pi/2$.

**Step 1.** Map quarter-plane to upper half-plane:
$$g(z) = z^{\pi/(\pi/2)} = z^2.$$

Check: if $z = x + iy$ with $x,y > 0$, then $z^2 = x^2 - y^2 + 2ixy$, and $\operatorname{Im}(z^2) = 2xy > 0$. ✓

**Step 2.** Map upper half-plane to unit disk via the **Cayley map**:
$$\varphi(w) = \frac{w - i}{w + i}.$$

This is the standard conformal bijection $\mathbb{H} \to \mathbb{D}$.

**Composition:** The conformal map from the quarter-plane to $\mathbb{D}$ is
$$\Phi(z) = \varphi(g(z)) = \frac{z^2 - i}{z^2 + i}.$$

**Verification at boundary:**
- The ray $\{y=0, x>0\}$: $z^2 \in \mathbb{R}_{>0}$, so $\frac{z^2 - i}{z^2+i}$ has modulus 1. ✓  
- The ray $\{x=0, y>0\}$: $z = iy$, $z^2 = -y^2 \in \mathbb{R}_{<0}$, again $|w - i| = |w + i|$ when $w$ is real. ✓

So the boundary maps to the unit circle, confirming $\Phi$ maps the quarter-plane conformally onto $\mathbb{D}$:

$$\boxed{\Phi(z) = \frac{z^2 - i}{z^2 + i}.}$$

---

### Summary Table

| Map | Source | Target |
|---|---|---|
| $z^{\pi/\alpha}$ | Wedge $W_\alpha$ | $\mathbb{H}$ |
| $z^2$ | Quarter-plane $W_{\pi/2}$ | $\mathbb{H}$ |
| $\frac{w-i}{w+i}$ | $\mathbb{H}$ | $\mathbb{D}$ |
| $\frac{z^2-i}{z^2+i}$ | Quarter-plane | $\mathbb{D}$ |

The beautiful structure: **angle-scaling power maps** + **Cayley transform** are the two universal building blocks of conformal mappings to canonical domains.
