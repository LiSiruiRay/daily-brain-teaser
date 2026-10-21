# Answer: Buffon's Needle and the Noodle Trick

## Key Idea / Intuition

Count *crossings* instead of computing a probability. The expected number of crossings is additive: cut a wire into pieces and the expectations add, even though the pieces are highly dependent. So the expected count must be $c \cdot (\text{length})$ for some universal constant $c$, whatever the shape. Now drop a circle of diameter $d$. It always meets the lines in exactly 2 points, and its length is $\pi d$. That forces $c = 2/(\pi d)$. A short needle crosses at most once, so its expected crossing count equals its crossing probability.

---

## Formal Proof / Solution

**Setup.** A rigid wire is "dropped at random" when it receives a uniform rotation and, independently, a translation whose component perpendicular to the lines is uniform modulo $d$. For a straight needle, this is exactly the model in the problem. Let $N$ be the number of intersection points of the wire with the lines. Tangencies and other degenerate positions have probability $0$, so we ignore them.

**Step 1: Segments give a linear function.** Let $f(\ell) = \mathbb{E}[N]$ for a straight segment of length $\ell$. By rotation invariance, $f$ depends only on $\ell$.

- **Additivity.** Split a segment of length $a+b$ into pieces of lengths $a$ and $b$. The crossings of the whole segment are the crossings of piece 1 plus the crossings of piece 2 (almost surely). Each piece, viewed on its own, is a uniformly rotated and uniformly translated segment of its length. The two pieces are strongly dependent, but linearity of expectation does not care. Hence
$$f(a+b) = f(a) + f(b).$$
- **Monotonicity.** A longer segment contains a shorter one, so $f$ is nondecreasing.

A monotone solution of Cauchy's equation is linear. Therefore $f(\ell) = c\,\ell$ for some constant $c$.

**Step 2: Polygons.** Take any polygonal wire with edges of lengths $\ell_1,\dots,\ell_k$. Each edge, viewed on its own, is a randomly dropped segment. By linearity,
$$\mathbb{E}[N] = c(\ell_1 + \dots + \ell_k) = c \cdot \text{(perimeter)}.$$

**Step 3: The circle pins down $c$.** Consider a circle of diameter $d$. Its vertical extent is exactly $d$. So almost surely it meets exactly one line, and it meets that line in exactly $2$ points: $N_{\text{circle}} = 2$ a.s.

Now sandwich the circle between an inscribed regular $n$-gon $P_n$ and a circumscribed regular $n$-gon $Q_n$, all rigidly attached and dropped together. All three curves are convex. A line crosses a convex closed curve in $2$ points if it meets the interior, and in $0$ points otherwise. Every line meeting the interior of $P_n$ also meets the disk, and every line meeting the disk also meets the interior of $Q_n$. So, pointwise,
$$N_{P_n} \le N_{\text{circle}} = 2 \le N_{Q_n}.$$
Taking expectations gives
$$c\cdot \operatorname{per}(P_n) \;\le\; 2 \;\le\; c \cdot \operatorname{per}(Q_n).$$
As $n\to\infty$, both perimeters tend to $\pi d$. Hence
$$c = \frac{2}{\pi d}.$$

**Step 4: Answer to (a) and (b).** If $\ell \le d$, the needle can cross at most one line, apart from probability-zero events. So $N \in \{0,1\}$ and
$$P(\text{cross}) = \mathbb{E}[N] = \frac{2\ell}{\pi d}.$$

**Step 5: Answer to (c).** For a long needle ($\ell > d$), Step 1 still applies, giving
$$\mathbb{E}[N] = \frac{2\ell}{\pi d}.$$
For any rigid noodle of length $L$, first take a polygonal noodle; Step 2 gives $\mathbb{E}[N] = \frac{2L}{\pi d}$. For a smooth noodle, approximate it by polygons. The answer is independent of the shape:
$$\boxed{\ \mathbb{E}[N] = \frac{2L}{\pi d}\ }$$

**Sanity check via calculus.** Fix the angle $\theta$ between the needle and the lines. The needle crosses a line exactly when its midpoint lies within $\tfrac{\ell}{2}\sin\theta$ of a line. Given $\theta$, this happens with probability $\ell\sin\theta/d$. Averaging over the angle,
$$P = \frac{1}{\pi}\int_0^\pi \frac{\ell \sin\theta}{d}\,d\theta = \frac{2\ell}{\pi d}.$$

**Moral.** Linearity of expectation holds for dependent pieces. This turns a geometric integral into a symmetry argument: find one shape whose crossing count is deterministic, and the constant is forced.
