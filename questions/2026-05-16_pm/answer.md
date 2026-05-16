# Answer: Sophomore's Dream Integral

## Key Idea / Intuition

The trick is to expand $x^x = e^{x \ln x}$ as a power series in $x \ln x$, then integrate term by term. Each resulting integral $\int_0^1 x^n (\ln x)^n \, dx$ can be evaluated by the substitution $x = e^{-t}$, turning it into a Gamma integral. The two integrals $\int_0^1 x^x dx$ and $\int_0^1 x^{-x} dx$ combine beautifully into a sum known as the **Sophomore's Dream**, named after Johann Bernoulli (1697).

---

## Formal Proof / Solution

### Step 1: Expand $x^x$ as a series

$$x^x = e^{x \ln x} = \sum_{n=0}^\infty \frac{(x \ln x)^n}{n!}$$

So:
$$\int_0^1 x^x \, dx = \sum_{n=0}^\infty \frac{1}{n!} \int_0^1 x^n (\ln x)^n \, dx.$$

### Step 2: Evaluate $\int_0^1 x^n (\ln x)^n \, dx$

Substitute $x = e^{-t}$, so $\ln x = -t$, $dx = -e^{-t} dt$, and the limits go from $t = \infty$ to $t = 0$:

$$\int_0^1 x^n (\ln x)^n \, dx = \int_\infty^0 e^{-nt}(-t)^n (-e^{-t}) \, dt = (-1)^n \int_0^\infty t^n e^{-(n+1)t} \, dt.$$

Now substitute $u = (n+1)t$:

$$= (-1)^n \cdot \frac{1}{(n+1)^{n+1}} \int_0^\infty u^n e^{-u} \, du = (-1)^n \cdot \frac{n!}{(n+1)^{n+1}}.$$

### Step 3: Sum the series for $\int_0^1 x^x \, dx$

$$\int_0^1 x^x \, dx = \sum_{n=0}^\infty \frac{1}{n!} \cdot (-1)^n \cdot \frac{n!}{(n+1)^{n+1}} = \sum_{n=0}^\infty \frac{(-1)^n}{(n+1)^{n+1}} = \sum_{n=1}^\infty \frac{(-1)^{n-1}}{n^n}.$$

That is:

$$\int_0^1 x^x \, dx = 1 - \frac{1}{2^2} + \frac{1}{3^3} - \frac{1}{4^4} + \cdots$$

### Step 4: Handle $\int_0^1 x^{-x} \, dx$

Similarly, $x^{-x} = e^{-x \ln x}$, so:

$$\int_0^1 x^{-x} \, dx = \sum_{n=0}^\infty \frac{(-1)^n}{n!} \int_0^1 x^n (\ln x)^n \, dx = \sum_{n=0}^\infty \frac{(-1)^n}{n!} \cdot (-1)^n \cdot \frac{n!}{(n+1)^{n+1}} = \sum_{n=0}^\infty \frac{1}{(n+1)^{n+1}}.$$

So:

$$\int_0^1 x^{-x} \, dx = \sum_{n=1}^\infty \frac{1}{n^n} = 1 + \frac{1}{2^2} + \frac{1}{3^3} + \frac{1}{4^4} + \cdots$$

### Step 5: Final Answer

$$\boxed{I = \int_0^1 x^x \, dx + \int_0^1 x^{-x} \, dx = \sum_{n=1}^\infty \frac{(-1)^{n-1}}{n^n} + \sum_{n=1}^\infty \frac{1}{n^n}}$$

Each piece individually is already a beautiful result. Numerically:
- $\int_0^1 x^{-x} \, dx \approx 1.2913$
- $\int_0^1 x^x \, dx \approx 0.7834$
- Their sum $\approx 2.0747$

These two identities together are called **Sophomore's Dream** — a playful name because they look too clean to be true, yet follow from a surprisingly elementary calculation.
