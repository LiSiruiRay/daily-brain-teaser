# Answer: The Integral That Loops Back Around

## Key Idea / Intuition

The trick is the **King's substitution**: replace $x$ with $\pi/2 - x$. Under this swap, $\tan x$ and $\cot x = 1/\tan x$ exchange roles, and the two resulting integrands are **complementary** — they add to 1 over the same interval. So $I + I = \pi/2$, giving $I = \pi/4$, regardless of the exponent $\sqrt{3}$ (or any positive exponent!).

---

## Formal Proof / Solution

**Step 1: Apply the substitution $x \mapsto \pi/2 - x$.**

Let $x = \pi/2 - u$, so $dx = -du$; when $x = 0$, $u = \pi/2$; when $x = \pi/2$, $u = 0$. Thus

$$I = \int_{\pi/2}^{0} \frac{1}{1 + \tan^{\sqrt{3}}(\pi/2 - u)}\,(-du) = \int_0^{\pi/2} \frac{1}{1 + \cot^{\sqrt{3}} u}\, du.$$

**Step 2: Simplify the new integrand.**

Since $\cot u = 1/\tan u$,

$$\frac{1}{1 + \cot^{\sqrt{3}} u} = \frac{1}{1 + \tan^{-\sqrt{3}} u} = \frac{\tan^{\sqrt{3}} u}{1 + \tan^{\sqrt{3}} u}.$$

So we have

$$I = \int_0^{\pi/2} \frac{\tan^{\sqrt{3}} x}{1 + \tan^{\sqrt{3}} x}\, dx.$$

**Step 3: Add the two expressions for $I$.**

$$2I = \int_0^{\pi/2} \frac{1}{1 + \tan^{\sqrt{3}} x}\, dx + \int_0^{\pi/2} \frac{\tan^{\sqrt{3}} x}{1 + \tan^{\sqrt{3}} x}\, dx = \int_0^{\pi/2} 1\, dx = \frac{\pi}{2}.$$

**Step 4: Conclude.**

$$\boxed{I = \frac{\pi}{4}.}$$

**Remark:** The exponent $\sqrt{3}$ is completely irrelevant. The same argument shows

$$\int_0^{\pi/2} \frac{1}{1 + \tan^{\alpha} x}\, dx = \frac{\pi}{4}$$

for any $\alpha \in \mathbb{R}$ (with $\alpha > 0$ to ensure the integrand is well-behaved). This is a beautiful example of how symmetry collapses an apparently difficult integral.
