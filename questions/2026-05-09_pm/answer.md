# Answer: Integral of ln(sin x)

## Key Idea / Intuition

The trick is a beautiful **symmetry + duplication** argument. Write $I$ using the substitution $x \mapsto \pi/2 - x$ to get $I = \int_0^{\pi/2} \ln(\cos x)\,dx$ as well. Then add the two copies of $I$ together and use the product-to-sum identity $\sin x \cos x = \frac{1}{2}\sin(2x)$. A single substitution then reduces the resulting integral back to $I$ itself, giving a clean equation to solve.

---

## Formal Proof / Solution

**Step 1: Symmetry.**

By the substitution $x \mapsto \tfrac{\pi}{2} - x$,

$$I = \int_0^{\pi/2} \ln(\cos x)\, dx.$$

**Step 2: Add the two copies.**

$$2I = \int_0^{\pi/2} \ln(\sin x)\, dx + \int_0^{\pi/2} \ln(\cos x)\, dx = \int_0^{\pi/2} \ln(\sin x \cos x)\, dx.$$

Use the identity $\sin x \cos x = \dfrac{\sin 2x}{2}$:

$$2I = \int_0^{\pi/2} \ln\!\left(\frac{\sin 2x}{2}\right) dx = \int_0^{\pi/2} \ln(\sin 2x)\, dx - \int_0^{\pi/2} \ln 2\, dx.$$

**Step 3: Substitute $u = 2x$ in the first piece.**

$$\int_0^{\pi/2} \ln(\sin 2x)\, dx = \frac{1}{2}\int_0^{\pi} \ln(\sin u)\, du.$$

Now use the symmetry of $\sin$ about $\pi/2$:

$$\int_0^{\pi} \ln(\sin u)\, du = 2\int_0^{\pi/2} \ln(\sin u)\, du = 2I.$$

So $\displaystyle\int_0^{\pi/2} \ln(\sin 2x)\,dx = \frac{1}{2}\cdot 2I = I$.

**Step 4: Solve for $I$.**

$$2I = I - \frac{\pi}{2}\ln 2$$

$$I = -\frac{\pi}{2}\ln 2.$$

**Result:**

$$\boxed{\int_0^{\pi/2} \ln(\sin x)\, dx = -\frac{\pi}{2}\ln 2.}$$

**Why it's surprising:** The integral of a function that diverges to $-\infty$ at the endpoint $x=0$ gives a clean closed form involving $\pi$ and $\ln 2$ — two of the most fundamental constants in mathematics, linked here by a symmetry argument rather than any residue or special-function machinery.

---

Written to: [questions/2025-07-18-PM.md](questions/2025-07-18-PM.md) | Answer: [questions/2025-07-18-PM-answer.md](questions/2025-07-18-PM-answer.md)
