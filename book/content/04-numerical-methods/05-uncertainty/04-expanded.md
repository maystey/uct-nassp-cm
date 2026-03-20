# {docnum}`step ref` Expanded Uncertainty

In many cases we want to use the standard uncertainty to create an interval in which we have a specified level of confidence that it contains the value of the measurand.
This is called the expanded uncertainty, as is acheived by multiplying the standard uncertainty by a coverage factor ($k$).
For measurand $X$ with best approximation $x$ with a standard uncertainty $u(x)$, we can construct the interval $[x - k \times u(x), x + k \times u(x)]$, which can also be written as:

$$
X = x \pm k u(x)
$$

To determine $k$ for the required level of confidence $p$, we need to solve the intergral equation:

$$
p = \int_{x - k u(x)}^{x + k u(x)} f(x') dx'
$$

where $f$ is the PDF.

The equations for the coverage factors for a given confidence level, as well as some example confidence levels and coverage factors, are shown for a normal, rectangular and triangular distribution in the table below.
Note the $erf^{-1}$ in the normal distribution's equation is the inverse error-function, which cannot be solved analytically.

Confidence level | Normal Distribution $k$ | Rectangular Distribution $k$ | Triangular Distribution $k$
--- | --- | --- | ---
p | $\sqrt{2}erf^{-1}(p)$ | $\sqrt{3} p$ | $\sqrt{6}\left(1 - \sqrt{1 - p}\right)$ 
68.27% | 1 | 1.18 | 1.07
95.45% | 2 | 1.65 | 1.93
99.73% | 3 | 1.73 | 2.32

```{note}
For combined standard uncertianties we may assume a normal distribution by evoking the central limit theorom.
```