# {docnum}`step ref` Combined Standard Uncertainty

Sometimes a measurand is determined by combining other measurements.
The combined standard uncertainty is defined as the standard uncertainty of the result of a measurement, 
where this result was acquired by combining a number of other quantities with standard uncertainties. 
These standard uncertainties are generally combined in quadrature.
The framework that GUM provides for combining uncertainties is quite robust and one of the framewors' strengths.


Consider a measurand $Y$ obtained by combining measurands $X_1, \dots, X_N$ through the relation:

$$
Y = f(X_1, \dots, X_N)
$$

The combined standard uncertainty can be determined using a Taylor expansion, the resulting form of this depends on if $X_i$ are correlated (dependant) or uncorrelated (independant).
We will not look into the derivation, but rather the results in the next two sections.

## Combining Uncorrelated Measurements

If the measurands $X_1, \dots, X_N$ are **uncorrelated / independant**, then the combined variance of measurement $y$ is given by:

$$        
u^2(y) = \sum_{i=1}^N \left( \frac{\partial f}{\partial x_i} \right)^2 u^2 (x_i)
$$(u_com:uncorr)

where $\tfrac{\partial f}{\partial x_i}$ represents $\tfrac{\partial f}{\partial X_i}$ at $X_i = x_i$.

## Combining Correlated  Measurements

If the measurands $X_1, \dots, X_N$ are **correlated / dependant**, then the combined variance of measurement $y$ is given by:

$$
\begin{align}
    u^2(y) & = \sum_{i=1}^N \sum_{j = 1}^N \frac{\partial f}{\partial x_i}\frac{\partial f}{\partial x_j} u(x_i, x_j) \\
    & = \sum_{i=1}^N \left( \frac{\partial f}{\partial x_i} \right)^2 u^2 (x_i) + 2 \sum_{i=1}^{N-1}\sum_{j=i+1}^{N} \frac{\partial f}{\partial x_i}\frac{\partial f}{\partial x_j} u(x_i, x_j)\\
\end{align}
$$(u_com:corr)

where $u(x_i, x_j)$ is the covariance between $x_i$ and $x_j$.