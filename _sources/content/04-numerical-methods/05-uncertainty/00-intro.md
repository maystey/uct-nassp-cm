# {docnum}`step-super ref step-sub` Uncertainty Analysis for Numerical Methods

In this chapter the measurement uncertainty framework outlined in the Guide to the expression of uncertainty in measurement is introduced. 
This will be adapted to the numerical methods covered in this course more directly in each of the chapters dedicated to the numerical methods.

In this chapter works from the Joint Committee for Guides in Metrology (JCGM) are used, specifically:

- "Guide to the expression of uncertainty in measurement" (GUM) {cite}`u-i-JCGMGUM`
- "International vocabulary of metrology" (VIM) {cite}`u-i-JCGMVIM3`
- Additional GUM supplements  <!-- %TODO cite ones used -->

<!-- Metrology is the science of measurement (normally physical) - terminology will reflect this -->

The context for the GUM framework is metrology - the science of measurement (normally physical). 
The terminology will reflect the physical nature of this framework, and much of our uses for it are adaptations or extensions of the framework.

```{admonition} What is a measurement?
:class: info

The objective of a measurement is to determine the unique value of a physical quantity called the **measurand**.

```

We cannot know the value of the measurand with absolute certainty due to:

- Limitations in the definition of the measurement
- Limitations from the nature of the measurement (apparatus, etc)

The result of a measurement is usually quoted as the **best approximation** of the measurand, along with an estimated uncertainty of the measurand. The **standard uncertainty** is the uncertainty of a measurement expressed as a standard deviation.

```{important}
Some people use the term "error" interchangeably with "uncertainty". In these notes the term "standard uncertainty" will be used precisely as described in the GUM. The term "error" will be used in more general cases:

- Errors as flaws in code (syntax / runtime errors)
- Errors as resulting from approximations / truncations in numerical methods (truncation error)
- Errors as the difference between an approximated value and the analytical value (true error / absolute error)
```

```{admonition} What is the uncertainty of a measurement?
:class: info

From the GUM {cite}`u-i-JCGMGUM` and VIM {cite}`u-i-JCGMVIM3`:

> The uncertainty parameter, associated with the result of a measurement, that characterizes the dispersion of the values that could reasonably be attributed to the measurand.

```

## Sources of Uncertainty

The sources of uncertainty depend entirely on the context of the measurement. For example, for physical measurements some sources may be:

- Precision of measurement instruments
- Randomness due to uncontrollable complexities in a physical system

For numerical algorithms, some sources of uncertainty may be:

- Floating point precision (often negligible)
- Truncation errors (from specific algorithm used)
- Randomness from sampling random variables

## Methods of Uncertainty Evaluation

To determine the standard uncertainty of a measurand, knowledge of what the possible measurand values is needed. 
This is often in the form on a **probability distribution function** (PDF).

There are two types of methodologies on the GUM framework for evaluating the uncertainty of a measurement result:

```{admonition} Type A evaluation of uncertainty
:class:hint

Evaluating uncertainty by **statistical analysis** of a series of observations. 
The PDF is derived from the observed frequency distribution of measurements.
```

```{admonition} Type B evaluation of uncertainty
:class:hint

Evaluation of uncertainty by other means (includes single measurements). 
The PDF is assumed based on knowledge of measurement.
```

## Mathematical Notation

We will be using a consistent mathematical notation for measurements and uncertainty in these notes. Given a measurand $X$:

- An estimation of this (as resulting from a measurement) is denoted as $x$.
- The standard uncertainty of this estimation will be denoted by $u(x)$. Note that this should not necessarily be interpreted as a "function of $x$".

## References

```{bibliography}
:cited:
:style: plain
:labelprefix: U
:keyprefix: u-i-
```
