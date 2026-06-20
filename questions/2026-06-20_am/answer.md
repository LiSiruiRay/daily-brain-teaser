# Answer: The Beta-Flavored Integral

## Key Idea / Intuition

The Beta function $B(a,b) = \int_0^1 x^{a-1}(1-x)^{b-1}\,dx = \frac{(a-1)!(b-1)!}{(a+b-1)!}$ (for positive integers) turns both integrals into pure combinatorics. The second integral looks harder, but writing $1+10x = 11x + (1-x)$ is a magical decomposition that instantly reduces $J$ to a linear combination of two Beta values — no expansion needed.

---

## Formal Proof / Solution

### Step 1: Recall the Beta function formula

For positive integers $m, n$:

$$B(m,n) = \int_0^1 x^{m-1}(1-x)^{n-1}\,dx = \frac{(m-1)!\,(n-1)!}{(m+n-1)!}.$$

### Step 2: Compute $I$

$$I = \int_0^1 x^3(1-x)^4\,dx = B(4,5) = \frac{3!\cdot 4!}{8!} = \frac{6 \cdot 24}{40320} = \frac{144}{40320} = \frac{1}{280}.$$

### Step 3: The trick for $J$

Write the factor $1+10x$ as:

$$1 + 10x = 11x + (1-x).$$

This is the key move — it splits into terms where one power of $x$ shifts up and the other power of $(1-x)$ shifts up:

$$J = \int_0^1 x^3(1-x)^4\bigl[11x + (1-x)\bigr]\,dx = 11\int_0^1 x^4(1-x)^4\,dx + \int_0^1 x^3(1-x)^5\,dx.$$

### Step 4: Evaluate each piece

$$\int_0^1 x^4(1-x)^4\,dx = B(5,5) = \frac{4!\cdot 4!}{9!} = \frac{576}{362880} = \frac{1}{630}.$$

$$\int_0^1 x^3(1-x)^5\,dx = B(4,6) = \frac{3!\cdot 5!}{9!} = \frac{720}{362880} = \frac{1}{504}.$$

### Step 5: Combine

$$J = \frac{11}{630} + \frac{1}{504}.$$

Find a common denominator. $\text{lcm}(630, 504) = 2520$:

$$J = \frac{44}{2520} + \frac{5}{2520} = \frac{49}{2520} = \frac{7}{360}.$$

### Summary

$$\boxed{I = \frac{1}{280}, \qquad J = \frac{7}{360}.}$$

The beauty is that $1+10x = 11x+(1-x)$ avoids any polynomial expansion, keeping the computation a one-line Beta reduction.
