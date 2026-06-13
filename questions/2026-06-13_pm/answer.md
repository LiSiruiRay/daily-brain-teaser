# Answer: The King's Integral

## Key Idea / Intuition

The integrand doesn't simplify easily by substitution or antiderivatives. The trick is to pair the integral with its "mirror image" obtained by the substitution $x \mapsto \frac{\pi}{2} - x$, which swaps $\sin$ and $\cos$. When you add the original integral to its mirror, the integrand becomes exactly $1$, so the sum is trivial to compute.

---

## Formal Proof / Solution

**Step 1: Define the mirror integral.**

Let
$$I = \int_0^{\pi/2} \frac{\sin x}{\sin x + \cos x}\, dx.$$

Apply the substitution $x \mapsto \dfrac{\pi}{2} - x$. Since $\sin\!\left(\tfrac{\pi}{2}-x\right) = \cos x$ and $\cos\!\left(\tfrac{\pi}{2}-x\right) = \sin x$, and the limits stay $0 \to \pi/2$:

$$I = \int_0^{\pi/2} \frac{\cos x}{\cos x + \sin x}\, dx.$$

**Step 2: Add the two expressions.**

$$2I = \int_0^{\pi/2} \frac{\sin x}{\sin x + \cos x}\, dx + \int_0^{\pi/2} \frac{\cos x}{\cos x + \sin x}\, dx = \int_0^{\pi/2} \frac{\sin x + \cos x}{\sin x + \cos x}\, dx = \int_0^{\pi/2} 1\, dx = \frac{\pi}{2}.$$

**Step 3: Conclude.**

$$\boxed{I = \frac{\pi}{4}.}$$

---

**Why this is beautiful:** The integrand looks asymmetric and resistant to elementary antidifferentiation, yet the answer $\pi/4$ is perfectly clean. The "King's rule" (pairing with the complement substitution $x \mapsto a+b-x$ on $[a,b]$) is a universal trick that transforms a hard-looking rational-trigonometric integrand into $1$.
