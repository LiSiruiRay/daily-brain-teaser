# Answer: The Ordered Square: Connected but Not Path-Connected

## Key Idea / Intuition

In the dictionary order, the square looks like uncountably many copies of a vertical segment glued end to end. Moving along the order means climbing all of $\{0\}\times[0,1]$, then jumping to the bottom of the next column, and so on. That is why it is connected: there are no gaps and no missing suprema. A continuous path from the bottom-left corner to the top-right corner would have to pass through every column. The interior of each column is an open set, so the path would need to spend a nonempty open interval of time in each one. That would give uncountably many disjoint open time intervals, which is impossible because each contains a rational.

---

## Formal Proof / Solution

### Part 1: $I_o^2$ is connected

We use the standard fact that an ordered set is connected in the order topology if it is a **linear continuum**. That means it has the least upper bound property and is dense: between any two elements lies a third. (Munkres, Thm 24.1.)

**Least upper bound property.** Let $\emptyset\ne A\subseteq I_o^2$, and let $x_0=\sup\{a : (a,b)\in A\}$, computed in $[0,1]$.
- If some points of $A$ have first coordinate $x_0$, set $y_0=\sup\{b:(x_0,b)\in A\}$. Then $(x_0,y_0)$ is the least upper bound of $A$.
- If no point of $A$ has first coordinate $x_0$, then $(x_0,0)$ is an upper bound of $A$. It is also the least one. Any $(c,d)<(x_0,0)$ has $c<x_0$, so some $(a,b)\in A$ has $a>c$, which means $(c,d)$ is not an upper bound.

**Density.** Let $(a,b)<(c,d)$.
- If $a=c$, then $b<d$, and $\big(a,\tfrac{b+d}{2}\big)$ lies strictly between them.
- If $a<c$, then $\big(\tfrac{a+c}{2},\,0\big)$ lies strictly between them.

So $I_o^2$ is a linear continuum and hence connected.

### Part 2: $I_o^2$ is not path-connected

Suppose, for contradiction, that $f:[0,1]\to I_o^2$ is continuous with $f(0)=(0,0)$ and $f(1)=(1,1)$.

**Step 1: The image is convex, so $f$ is surjective.**
The image $f([0,1])$ is connected. Suppose some $p$ with $(0,0)<p<(1,1)$ were not in the image. Then
$$f([0,1]) \subseteq \{z : z<p\}\ \cup\ \{z : z>p\}.$$
These two sets are disjoint and open in the order topology. Each meets the image, since one contains $(0,0)$ and the other contains $(1,1)$. They would therefore separate the image, a contradiction. Hence $f([0,1])=I_o^2$.

**Step 2: The vertical fibers are open.**
For each $x\in[0,1]$, define
$$U_x=\{x\}\times(0,1)=\big((x,0),\,(x,1)\big).$$
This is an open interval in the order, so it is open in $I_o^2$. The sets $U_x$ are pairwise disjoint and each is nonempty.

**Step 3: Count.**
By continuity, each $V_x:=f^{-1}(U_x)$ is open in $[0,1]$. By surjectivity, each $V_x$ is nonempty. Since the $U_x$ are disjoint, the $V_x$ are pairwise disjoint as well.

Each nonempty open subset of $[0,1]$ contains a rational number, so choose $q_x\in V_x\cap\mathbb{Q}$. Disjointness makes $x\mapsto q_x$ injective. This gives an injection from the uncountable set $[0,1]$ into the countable set $\mathbb{Q}$, a contradiction.

Therefore no path joins $(0,0)$ to $(1,1)$, and $I_o^2$ is **not path-connected**. $\blacksquare$

### Remarks
- The argument never uses anything delicate about $f$. It only uses that $[0,1]$ is separable while $I_o^2$ contains uncountably many disjoint open sets, i.e., $I_o^2$ is not separable.
- **General principle:** a continuous image of a separable space is separable. A path-connected space with uncountably many disjoint nonempty open sets therefore cannot be swept out by a single path that hits all of them.
- The same argument shows that the only paths in $I_o^2$ stay inside a single vertical column $\{x\}\times[0,1]$. So the path components are exactly the columns, and there are uncountably many of them, even though the space is connected and compact.
