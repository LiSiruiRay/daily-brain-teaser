# Answer: Pigeonhole on an Icosahedron

## Key Idea / Intuition

The icosahedron has 12 vertices, and every vertex is surrounded by exactly 5 faces. If we assume for contradiction that no two face-sharing faces have the same label, then at every vertex the 5 surrounding faces all carry **distinct** nonneg integers — meaning they are at least $0,1,2,3,4$, summing to at least $10$. Summing over all 12 vertices overcounts each face exactly 3 times (since every face has 3 vertices). This gives a lower bound on the total sum that exceeds 39 — contradiction.

---

## Formal Proof / Solution

**Setup.**  
A regular icosahedron has:
- 20 faces, each an equilateral triangle,
- 12 vertices,
- each vertex shared by exactly **5** faces,
- each face having exactly **3** vertices.

Denote the label on face $i$ by $a_i \geq 0$, with $\sum_{i=1}^{20} a_i = 39$.

**Assume for contradiction** that no two faces sharing a vertex carry the same label.

**Local constraint at each vertex.**  
Fix any vertex $v$. The 5 faces meeting at $v$ form a "fan," and any two consecutive faces in this fan share an edge (hence share $v$ itself). In fact every pair among these 5 faces shares the vertex $v$, so by assumption they must all have **distinct** labels.

Since they are distinct nonneg integers, the 5 labels at vertex $v$ are at least $0, 1, 2, 3, 4$ in some order, giving:

$$\sum_{\text{faces } f \ni v} a_f \;\geq\; 0 + 1 + 2 + 3 + 4 = 10.$$

**Global count.**  
Sum this inequality over all 12 vertices:

$$\sum_{v} \sum_{\text{faces } f \ni v} a_f \;\geq\; 12 \times 10 = 120.$$

The left side counts each face $f$ once per vertex of $f$, and since every face is a triangle it has exactly **3** vertices:

$$\sum_{v} \sum_{f \ni v} a_f = \sum_{f} 3\, a_f = 3 \sum_{f} a_f = 3 \times 39 = 117.$$

**Contradiction.**  
We have derived $117 \geq 120$, which is false.

Therefore the assumption was wrong: **there exist two faces sharing a vertex with the same label.** $\blacksquare$

---

**Why the bound is tight.**  
The number 39 is carefully chosen: $3 \times 39 = 117 < 120 = 12 \times 10$. If the total were 40, the argument would fail (117 would become 120, matching the bound with no contradiction). This shows the problem is tight — a beautiful instance of pigeonhole / double counting.
