# Answer: The SVM That Saw Only Dot Products

## Key Idea / Intuition

The SVM's geometry — margins, distances, projections — depends on $\beta$ only through inner products of training points. When you write the dual, $\beta$ itself disappears and is replaced entirely by pairwise dot products $\langle x_i, x_j \rangle$. Swapping in $k(x_i, x_j) = \langle \phi(x_i), \phi(x_j) \rangle$ is therefore a completely seamless substitution: the dual and the decision function never needed $\phi$ explicitly, only the Gram matrix. This is the **kernel trick** — you implicitly work in $\mathcal{H}$ without ever touching it.

---

## Formal Proof / Solution

### Step 1: The Dual Objective Depends Only on Dot Products

From the excerpt (ESL eq. 12.13), the Wolfe dual of the soft-margin SVM is

$$\max_{\alpha}\ L_D = \sum_{i=1}^N \alpha_i - \frac{1}{2}\sum_{i=1}^N\sum_{j=1}^N \alpha_i \alpha_j y_i y_j \langle x_i, x_j \rangle$$

subject to $0 \leq \alpha_i \leq C$ and $\sum_i \alpha_i y_i = 0$.

The primal variable $\beta$ appears nowhere. Every occurrence of feature vectors is mediated by **inner products** $\langle x_i, x_j \rangle$.

### Step 2: Kernelized Dual

Replace $\langle x_i, x_j \rangle \mapsto k(x_i, x_j)$:

$$\max_{\alpha}\ \sum_{i=1}^N \alpha_i - \frac{1}{2}\sum_{i,j} \alpha_i \alpha_j y_i y_j\, k(x_i, x_j)$$

subject to the same constraints. This is valid as long as $k$ is a **Mercer kernel** (i.e., the kernel matrix $K_{ij} = k(x_i,x_j)$ is positive semi-definite), which guarantees the existence of some feature map $\phi$ with $k(x,x') = \langle \phi(x), \phi(x') \rangle_{\mathcal{H}}$.

### Step 3: Kernelized Decision Function

The primal solution satisfies $\beta = \sum_i \alpha_i y_i \phi(x_i)$. The decision function is

$$\hat{f}(x) = \langle \phi(x), \beta \rangle + \hat{\beta}_0 = \sum_{i=1}^N \hat{\alpha}_i y_i \langle \phi(x_i), \phi(x) \rangle + \hat{\beta}_0 = \sum_{i=1}^N \hat{\alpha}_i y_i\, k(x_i, x) + \hat{\beta}_0.$$

Again, $\phi$ vanishes; only $k(\cdot, \cdot)$ is needed.

### Step 4: Why Geometry = Dot Products

All of Euclidean geometry is expressible through inner products:
- **Distance:** $\|u - v\|^2 = \langle u,u\rangle - 2\langle u,v\rangle + \langle v,v\rangle$
- **Angle / projection:** $\text{proj}_v u = \frac{\langle u,v\rangle}{\langle v,v\rangle} v$
- **Margin width:** $\frac{2}{\|\beta\|} = \frac{2}{\sqrt{\langle \beta, \beta\rangle}}$, and $\langle \beta, \beta\rangle = \sum_{i,j} \alpha_i \alpha_j y_i y_j k(x_i, x_j)$

Since the SVM only cares about the geometry (maximizing the margin), and geometry lives entirely in inner products, replacing $\langle \cdot, \cdot \rangle$ with $k(\cdot, \cdot)$ transplants the entire algorithm into $\mathcal{H}$ — even if $\mathcal{H}$ is infinite-dimensional — **without ever computing a single coordinate of $\phi(x)$**.

### The Punchline

The computational cost of training scales with $N^2$ (size of the Gram matrix), **not** with $\dim(\mathcal{H})$. So an SVM with the RBF kernel $k(x,x') = e^{-\|x-x'\|^2/2\sigma^2}$ implicitly operates in an **infinite-dimensional** Hilbert space at the same cost as a linear SVM on $N$ points.
