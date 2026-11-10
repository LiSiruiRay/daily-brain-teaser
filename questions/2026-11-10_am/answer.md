# Answer: How Few Vertices Can a Torus Have?

## Key Idea / Intuition

The Euler characteristic fixes the ratio of vertices, edges and faces: on a closed triangulated surface, every edge borders exactly two triangles. For the torus this forces exactly $3$ edges per vertex on average ($E=3V$). A simplicial complex cannot have more than $\binom{V}{2}$ edges, because each pair of vertices spans at most one edge. Too few vertices cannot hold that many edges, and the inequality $3V \le \binom V2$ turns on exactly at $V=7$.

---

## Formal Proof / Solution

**Step 1: Counting relations.** Let a triangulation of $T^2$ have $V$ vertices, $E$ edges and $F$ triangles.

* **Euler characteristic.** Since $\chi(T^2)=0$, we have $V-E+F=0$.
* **Edge–face incidence.** In a triangulated closed surface, each edge lies in exactly two triangles. This is the surface condition: a neighborhood of an interior point of the edge is a disk, made of two half-disks. Each triangle has three edges, so double counting gives
$$3F = 2E.$$

Substituting $F=\tfrac23 E$ into $V-E+F=0$ gives $V=\tfrac13E$. Hence
$$E = 3V,\qquad F = 2V.$$

**Step 2: The simplicial constraint.** Distinct edges have distinct pairs of endpoints, so
$$E \le \binom{V}{2} = \frac{V(V-1)}{2}.$$
Combining this with $E=3V$:
$$3V \le \frac{V(V-1)}{2}\ \Longrightarrow\ 6 \le V-1\ \Longrightarrow\ V\ge 7.$$

**Step 3: Seven vertices suffice (the Möbius torus).** Take vertices $\mathbb{Z}/7$ and the $14$ triangles
$$\{i,\ i+1,\ i+3\},\qquad \{i,\ i+2,\ i+3\},\qquad i\in\mathbb{Z}/7.$$

* **All edges appear.** Each triangle has edges with differences $\{1,2,3\}$. Every pair of distinct elements of $\mathbb{Z}/7$ differs by $\pm1,\pm2$ or $\pm3$, so all $\binom72=21$ edges occur.
* **Each edge lies in exactly two triangles.**
  * The edge $\{j,j+1\}$ lies in $\{j,j+1,j+3\}$ and $\{j-2,j,j+1\}$.
  * The edge $\{j,j+2\}$ lies in $\{j-1,j,j+2\}$ and $\{j,j+2,j+3\}$.
  * The edge $\{j,j+3\}$ lies in $\{j,j+1,j+3\}$ and $\{j,j+2,j+3\}$.
* **Vertex links are circles.** Take vertex $0$. Its six triangles are $\{0,1,3\},\{0,2,3\},\{6,0,2\},\{5,6,1\},\{4,5,0\},\{4,6,0\}$. Their opposite edges are $13, 23, 62, 61, 45, 46$, which form the single 6-cycle $1\!-\!3\!-\!2\!-\!6\!-\!4\!-\!5\!-\!1$. By the $\mathbb{Z}/7$ symmetry, every vertex link is a hexagon.

So this complex is a closed surface with $\chi = 7-21+14=0$.

* **It is orientable.** Orient the triangles as $(i,i+1,i+3)$ and $(i,i+3,i+2)$. Each edge is then traversed in opposite directions by its two triangles. For example, $(j,j+3)$ appears in $(j,j+1,j+3)$ as $j+3\to j$ and in $(j,j+3,j+2)$ as $j\to j+3$.

By the classification of surfaces, an orientable closed surface with $\chi=0$ is the torus. Its 1-skeleton is $K_7$, so $K_7$ embeds in $T^2$. Császár (1949) even realized this torus as a polyhedron in $\mathbb{R}^3$ without self-intersections.

**Bonus.** In general $\chi = V - E + F$ with $3F=2E$ gives $E = 3(V-\chi)$. The condition $3(V-\chi)\le \binom V2$ then yields the following.

* **Sphere ($\chi=2$):** $3V-6\le V(V-1)/2$ gives $V^2-7V+12\ge 0$, i.e. $(V-3)(V-4)\ge 0$. A surface triangulation needs $V\ge 4$, which the tetrahedron boundary attains.
* **$\mathbb{RP}^2$ ($\chi=1$):** $3V-3\le V(V-1)/2$ gives $(V-1)(V-6)\ge0$, so $V\ge 6$. This is attained by the hemi-icosahedron (antipodal quotient of the icosahedron), whose 1-skeleton is $K_6$.
* **In general:** $V \ge \left\lceil \tfrac{7+\sqrt{49-24\chi}}{2}\right\rceil$. This is exactly the Heawood expression for the chromatic number of surfaces.
