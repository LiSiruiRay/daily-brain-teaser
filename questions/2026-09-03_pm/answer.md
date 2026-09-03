# Answer: The Conformal Map That Straightens a Half-Strip

## Key Idea / Intuition

The key observation is that $\sin z$ maps the half-strip $S$ to the upper half-plane. Why? Because $\sin z = \sin(x+iy) = \sin x \cosh y + i \cos x \sinh y$. On the boundary of the strip ($x=0$, $x=\pi$, and the base $y=0$), $\sin$ maps to the real axis; inside the strip, the imaginary part is positive. So $\sin$ is the magic function — it "unfolds" the half-strip into a half-plane in one shot.

---

## Formal Proof / Solution

**Step 1: Write out $\sin z$ on the strip.**

For $z = x + iy$ with $0 < x < \pi$, $y > 0$:
$$\sin z = \sin x \cosh y + i \cos x \sinh y.$$

**Step 2: Check the imaginary part is positive inside $S$.**

- For $0 < x < \pi$: $\sin x > 0$.
- For $y > 0$: $\cosh y > 0$ and $\sinh y > 0$.

So $\operatorname{Im}(\sin z) = \cos x \sinh y$... wait, let me recheck the sign carefully.

Actually: $\operatorname{Im}(\sin(x+iy)) = \cos x \sinh y$. For $0 < x < \pi/2$ this is positive, but for $\pi/2 < x < \pi$, $\cos x < 0$. So $\sin$ alone does **not** map $S$ to $\mathbb{H}$.

**Step 3: The correct composition.**

The correct approach is a two-step map:

**Map 1:** $\zeta = e^{iz}$ maps the half-strip $S$ to the upper **semicircle** $D^+ = \{ |\zeta| < 1, \operatorname{Im}(\zeta) > 0 \}$.

*Why?* For $z = x+iy$ with $0 < x < \pi$, $y > 0$:
$$e^{iz} = e^{i(x+iy)} = e^{-y} e^{ix}.$$
- $|e^{iz}| = e^{-y} < 1$ since $y > 0$.
- $\arg(e^{iz}) = x \in (0,\pi)$, so $e^{iz}$ lies in the upper half of the disk.

This maps $S$ **bijectively** onto the upper semicircle $D^+$.

**Map 2:** The Möbius transformation
$$w = \frac{\zeta + 1}{\zeta - 1} \cdot (-1) = \frac{1 + \zeta}{1 - \zeta}$$

... actually let us use the standard map: the Möbius transformation
$$w = i\cdot\frac{1+\zeta}{1-\zeta}$$
maps the unit disk $|\zeta|<1$ to $\mathbb{H}$, and maps the upper semicircle $D^+$ to... the first quadrant. So we need to be more careful.

**Cleaner route:** Use $w = -\cos z$ directly.

For $z = x+iy$:
$$-\cos z = -\cos x \cosh y + i \sin x \sinh y.$$
- $\operatorname{Im}(-\cos z) = \sin x \sinh y > 0$ for $0 < x < \pi$, $y > 0$. ✓

**Step 4: Verify $f(z) = -\cos z$ maps $S \to \mathbb{H}$.**

- **Boundary $x = 0$, $y > 0$:** $-\cos(iy) = -\cosh y \in (-\infty, -1)$. ✓ (real axis)
- **Boundary $x = \pi$, $y > 0$:** $-\cos(\pi + iy) = \cosh y \in (1, \infty)$. ✓ (real axis)
- **Base $y = 0$, $0 < x < \pi$:** $-\cos x \in (-1, 1)$. ✓ (real axis, interval $(-1,1)$)
- **Interior:** $\operatorname{Im}(-\cos z) = \sin x \sinh y > 0$ since $\sin x > 0$ and $\sinh y > 0$. ✓

So $f(z) = -\cos z$ maps the boundary of $S$ to the real line and the interior to $\mathbb{H}$.

**Step 5: Injectivity.**

$-\cos z$ is injective on $S$: if $-\cos z_1 = -\cos z_2$, then $z_1 = \pm z_2 + 2\pi k$. In the half-strip, the only solution is $z_1 = z_2$.

**Step 6: Surjectivity.**

For any $w \in \mathbb{H}$, $\cos^{-1}(-w)$ has a branch landing in $S$ (since $\cos$ takes all complex values in appropriate strips). By the open mapping theorem and boundary behavior, $f(S) = \mathbb{H}$.

**Conclusion:**

$$\boxed{f(z) = -\cos z}$$

is a conformal bijection from the half-strip $S = \{0 < \operatorname{Re}(z) < \pi,\, \operatorname{Im}(z) > 0\}$ onto the upper half-plane $\mathbb{H}$.

**Summary of the picture:** $-\cos z$ "unfolds" the half-strip: the two vertical sides ($x=0$ and $x=\pi$) map to the two rays $(-\infty,-1)$ and $(1,\infty)$, and the bottom edge maps to the interval $(-1,1)$. Together these cover the entire real axis, and the interior opens up into the full upper half-plane.
