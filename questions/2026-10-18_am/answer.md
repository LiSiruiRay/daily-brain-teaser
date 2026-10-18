# Answer: Why ICA Cannot Unmix Gaussians

## Key Idea / Intuition

Second-order statistics (covariances) see only $AA^\top$. After whitening, the only remaining unknown is a rotation, and covariances are blind to rotations.

A standard Gaussian is the one distribution that looks identical from every direction. So for Gaussian sources the rotation is truly invisible.

For non-Gaussian sources, rotating a square cloud of independent coordinates produces a diamond. The rotated coordinates are still uncorrelated, but they are visibly dependent. That leftover dependence shows up exactly in fourth-order statistics, through kurtosis. ICA works by rotating until this higher-order dependence disappears, which is why it needs non-Gaussianity.

---

## Formal Proof / Solution

### (a) Whitening leaves only a rotation

Since $\operatorname{Cov}(S)=I$, we have
$$
\Sigma=\operatorname{Cov}(AS)=AA^\top.
$$
Set $R=\Sigma^{-1/2}A$, so that $Z=\Sigma^{-1/2}AS=RS$. Then
$$
RR^\top=\Sigma^{-1/2}AA^\top\Sigma^{-1/2}=\Sigma^{-1/2}\Sigma\,\Sigma^{-1/2}=I,
$$
so $R$ is orthogonal.

Conversely, for any orthogonal $Q$ we have $(AQ)(AQ)^\top=AA^\top$. Hence the mixing matrices $A$ and $AQ$ produce the same covariance. Second-order information therefore pins $A$ down only up to right-multiplication by an orthogonal matrix.

This is why practical ICA algorithms first whiten the data and then search over orthogonal matrices. An example is ESL's ProDenICA, whose update re-orthogonalizes via $A\leftarrow UV^\top$.

### (b) Gaussian sources: the rotation is invisible

The density of $S$ is
$$
(2\pi)^{-1}e^{-\|s\|^2/2}.
$$
This depends only on $\|s\|$, so it is invariant under orthogonal maps. Hence $QS\stackrel{d}{=}S$ for every orthogonal $Q$, and therefore
$$
(AQ)S = A(QS)\stackrel{d}{=}AS.
$$
Equivalently, $X\sim N(0,AA^\top)$, whose law depends only on $AA^\top$.

No statistic of $X$, of any order and computed from any amount of data, can distinguish $A$ from $AQ$. The mixing matrix is not identifiable.

### (c) Non-Gaussian sources: rotation creates detectable dependence

**Uncorrelated.**
$$
\operatorname{Cov}(Y_1,Y_2)=\tfrac12\big(\operatorname{Var}S_1-\operatorname{Var}S_2\big)=0.
$$
Also $\mathbb E Y_1^2=\mathbb E Y_2^2=1$.

**Fourth-order cross moment.** Since $Y_1Y_2=\tfrac12(S_1^2-S_2^2)$,
$$
\mathbb E[Y_1^2Y_2^2]=\tfrac14\,\mathbb E\big[(S_1^2-S_2^2)^2\big]
=\tfrac14\big(\mathbb E S_1^4+\mathbb E S_2^4-2\,\mathbb E S_1^2\,\mathbb E S_2^2\big)
=\tfrac14\big(\mathbb E S_1^4+\mathbb E S_2^4-2\big).
$$
Subtracting $\mathbb E Y_1^2\,\mathbb E Y_2^2=1$ gives
$$
\boxed{\ \mathbb E[Y_1^2Y_2^2]-\mathbb E[Y_1^2]\,\mathbb E[Y_2^2]=\frac{(\mathbb E S_1^4-3)+(\mathbb E S_2^4-3)}{4}=\frac{\kappa_1+\kappa_2}{4}\ }
$$

**Uniform case.** For $\mathrm{Unif}[-a,a]$ we have $\mathbb E S^4=a^4/5$. With $a=\sqrt3$ this gives $\mathbb E S^4=9/5$, so $\kappa=-6/5$. Hence
$$
\mathbb E[Y_1^2Y_2^2]-1=\tfrac14\left(-\tfrac{6}{5}-\tfrac{6}{5}\right)=-\tfrac35\neq 0.
$$
Independence would force this difference to be $0$, so $Y_1$ and $Y_2$ are dependent.

Geometrically, the support of $Y$ is a diamond. If $Y_1$ is close to its maximum $\sqrt6$, then $Y_2$ is forced to be close to $0$.

**Consistency check.** For Gaussian sources $\kappa_1=\kappa_2=0$, and the difference vanishes, as part (b) requires.

### Punchline

After whitening, the only information that can identify the rotation is non-Gaussian, higher-order structure such as kurtosis or negentropy.

ICA's contrast functions measure exactly this structure. Examples are FastICA's kurtosis- or negentropy-based contrasts and ProDenICA's log-likelihood ratio against a Gaussian. The algorithm rotates until the components look "as non-Gaussian / as independent as possible."

The sharp form of this statement is the **Darmois–Skitovich theorem**: if two different linear combinations of independent variables are independent, then every variable appearing in both combinations is Gaussian. Consequently, ICA identifies $A$ (up to permutation and scaling of the columns) if and only if **at most one** source is Gaussian.
