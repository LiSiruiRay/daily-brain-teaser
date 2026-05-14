# Answer: Argument Principle: Zeros in an Annulus

## Key Idea / Intuition

The argument principle says that $\frac{1}{2\pi i}\oint \frac{f'}{f}\,dz$ counts **how many times $f(z)$ winds around the origin** as $z$ traverses $\gamma$ — each zero contributes $+1$ winding and each pole contributes $-1$. To count zeros in an annulus, simply apply Rouché on the outer circle $|z|=2$ and inner circle $|z|=1$ separately, then subtract. Rouché's theorem tells us: if one term dominates on the boundary, the total zero count equals the zero count of the dominant term.

---

## Formal Proof / Solution

### Step 1: Zeros inside $|z| < 2$

On $|z| = 2$, compare $f(z) = z^4 - 5z + 1$ by isolating the dominant term $z^4$:

$$|{-5z + 1}| \leq 5|z| + 1 = 5(2) + 1 = 11,$$
$$|z^4| = 16.$$

Since $16 > 11$, by **Rouché's theorem**, $f(z)$ has the same number of zeros inside $|z| < 2$ as $z^4$, which is $\mathbf{4}$ zeros (with multiplicity).

### Step 2: Zeros inside $|z| < 1$

On $|z| = 1$, compare $f(z) = z^4 - 5z + 1$ by isolating $-5z$ as the dominant term:

$$|z^4 + 1| \leq |z|^4 + 1 = 1 + 1 = 2,$$
$$|-5z| = 5.$$

Since $5 > 2$, by **Rouché's theorem**, $f(z)$ has the same number of zeros inside $|z| < 1$ as $-5z$, which is $\mathbf{1}$ zero (at the origin).

### Step 3: Zeros in the annulus

The number of zeros of $f$ in the open annulus $1 < |z| < 2$ is:

$$(\text{zeros inside } |z|<2) - (\text{zeros inside } |z| \leq 1).$$

We need to check: does $f$ have a zero **on** $|z|=1$? If $|z|=1$ and $f(z)=0$, then $z^4 + 1 = 5z$, so $|5z| = 5$ but $|z^4+1| \leq 2$, a contradiction. So no zeros lie on $|z|=1$.

Therefore:

$$\text{zeros in annulus} = 4 - 1 = \boxed{3}.$$

### Summary of the Argument Principle in action

The logarithmic derivative $\frac{f'}{f}$ has simple poles exactly at the zeros and poles of $f$, with residue $+\text{ord}$ at zeros and $-\text{ord}$ at poles. Integrating picks up exactly these residues via the residue theorem:

$$\frac{1}{2\pi i}\oint_\gamma \frac{f'(z)}{f(z)}\,dz = \sum_{\text{zeros}} \text{ord}(z_k) - \sum_{\text{poles}} \text{ord}(p_k) = N - P.$$

This geometric interpretation — counting **signed winding number** of the image curve $f(\gamma)$ around $0$ — is the heart of the argument principle.
