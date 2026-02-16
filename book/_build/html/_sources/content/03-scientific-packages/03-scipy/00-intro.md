# {docnum}`step-super ref step-sub` SciPy

[SciPy](https://scipy.org/) is a Python module that provides scientific algorithms and specialized data structures, and works well with NumPy. All of the numerical methods covered in this course have implementations in SciPy.

Though it is important that you are able to create your own implementations of these methods (especially if you find yourself working in a programming language that doesn't have a library like SciPy available), when using Python in practice it is better to use the SciPy algorithms. One reason for this is that the algorithms in SciPy make use of lower level programming languages, allowing them to be far more performant then what is possible with Python alone. Another is that it is generally good practice to use well maintain and reputable packages that provide functionality you need, rather than putting unnecessary time and effort into foundational parts of your program (though there are sometimes good reasons for making your own solutions).

How to use SciPy for each numerical method will be discussed further in the chapters for each method, however a brief overview will be given here. The numerical methods are organized in various sub-modules, which are as follows.

## Minimization and Root Finding

The [`scipy.optimize`](https://docs.scipy.org/doc/scipy/reference/optimize.html) sub-module contains functions for minimization, curve fitting and root finding.

### Curve Fitting

We have already made use of the [`least_squares()`](https://docs.scipy.org/doc/scipy/reference/generated/scipy.optimize.least_squares.html#scipy.optimize.least_squares) and [`curve_fit()`](https://docs.scipy.org/doc/scipy/reference/generated/scipy.optimize.curve_fit.html#scipy.optimize.curve_fit) functions.

### Root Finding

For the types of problems we cover in this course, you could use the root finding methods for [scalar functions](https://docs.scipy.org/doc/scipy/reference/optimize.html#scalar-functions). The [`root_scalar()`](https://docs.scipy.org/doc/scipy/reference/generated/scipy.optimize.root_scalar.html#scipy.optimize.root_scalar) function makes use of one of the other functions listed below it in the documentation, as specified by the function arguments.

There are also functions for multidimensional root finding, though this is outside the scope of the course.

## Integration and ODE Solving

The [`scipy.integrate`](https://docs.scipy.org/doc/scipy/reference/integrate.html#module-scipy.integrate) sub-module contains functions for integrating and solving ODEs.

### Integration

For the integration functions, there are options for integrating [given the function](https://docs.scipy.org/doc/scipy/reference/integrate.html#integrating-functions-given-function-object) or [given fixed samples](https://docs.scipy.org/doc/scipy/reference/integrate.html#integrating-functions-given-fixed-samples) (or a data set).

### ODE Solving

There are a few functions for [solving initial value problems](https://docs.scipy.org/doc/scipy/reference/integrate.html#solving-initial-value-problems-for-ode-systems). The [`solve_ivp()`](https://docs.scipy.org/doc/scipy/reference/generated/scipy.integrate.solve_ivp.html#scipy.integrate.solve_ivp) function makes use of the ones listed below it in the documentation, as specified by the arguments given. Many of these methods use adaptive step sizes, where the step size is dynamically decreased if the approximated error of the solution exceeds a given tolerance.

There is also a method for [solving boundary value problems](https://docs.scipy.org/doc/scipy/reference/integrate.html#solving-boundary-value-problems-for-ode-systems).
