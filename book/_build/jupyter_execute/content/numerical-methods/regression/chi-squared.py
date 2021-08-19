#!/usr/bin/env python
# coding: utf-8

# # Chi Squared Minimization

# For the least squares minimization we assumed that one of the variables ($y$) contained error that accounted for the deviation of the data from the model we want to fit it to.
# 
# This error was not quantified by the measurement, furthermore we gave each error term equal importance in the total error to be minimized. 
# 
# What if we had a measurement for the uncertainty of each of our $y$ measurements? Let's characterize these uncertainties using the standard deviation of each $y_i$ measurement: $\sigma_i$.
# 
# We now want to weight the contribution that each error value $\epsilon_i$ gives to the total error by the uncertainties $\sigma_i$. Ideally we want the model to fit within the uncertainties of the data points (or at least the fraction of the data points given by the confidence of the uncertainty). This means that we want to prioritize minimizing the error given by points with low uncertainty, or conversely we want to suppress the points with high uncertainty. To solve this we will minimize the $\chi^2$ value of the data:
# 
# $$
# \chi^2  = \sum_{i = 1}^{N} \bigg( \frac{\epsilon_i}{\sigma_i} \bigg)^2
# $$
# 
# where each error value is weighted by dividing it by the uncertainty. Note that if all of the $\sigma_i$ where constant, we'd be dealing with least squares (the multiplicative factor will drop out in the minimization)

# ## With 2 Variables

# Returning to our scenario with two variables $x$ and $y$, modeled by the functional relation:
# 
# $$
# y = a_0 + a_1 x
# $$
# 
# with a data set of measured $x_i$ and $y_i$ variables, with $\sigma_i$ as the uncertainty of the $y_i$ values for $i = 1, \dots, N$, $\chi^2$ can now be written as:
# 
# $$
# \begin{align*}
# \chi^2  &= \sum_{i = 1}^{N} \bigg( \frac{\epsilon_i}{\sigma_i} \bigg)^2\\
#         &= \sum_{i = 1}^{N} \bigg(\frac{a_0 + a_1 x_i - y_i}{\sigma_i}\bigg)^2\\
# \end{align*}
# $$

# Minimizing $\chi^2$ with respect to $a_0$ and $a_1$, will yield:

# \begin{align*}
# a_0 &= \left( \left\langle \frac{y}{\sigma^2} \right\rangle  \left\langle \frac{x^2}{\sigma^2} \right\rangle -  \left\langle \frac{x}{\sigma^2} \right\rangle \left\langle \frac{x y}{\sigma^2} \right\rangle \right)/ D\\
# a_1 &= \left( \left\langle \frac{1}{\sigma^2} \right\rangle  \left\langle \frac{x y}{\sigma^2} \right\rangle - \left\langle \frac{x}{\sigma^2} \right\rangle  \left\langle \frac{y}{\sigma^2} \right\rangle \right)/ D\\
# \end{align*}
# 
# where
# 
# $$
# D = \left\langle \frac{1}{\sigma^2} \right\rangle  \left\langle \frac{x^2}{\sigma^2} \right\rangle  - \left\langle \frac{x}{\sigma^2} \right\rangle^2
# $$
# 
# Note that in practice the $1/N$ factors of the expectation values cancel out. 

# $$
# \begin{align*}
# a_0 &= \left( \sum_{i = 1}^N \frac{y_i}{\sigma_i^2} \sum_{i = 1}^N \frac{x_i^2}{\sigma_i^2} - \sum_{i = 1}^N \frac{x_i}{\sigma_i^2} \sum_{i = 1}^N \frac{x_iy_i}{\sigma_i^2} \right)/ D\\
# a_1 &= \left(\sum_{i = 1}^N \frac{1}{\sigma_i^2} \sum_{i = 1}^N \frac{x_i y_i}{\sigma_i^2} - \sum_{i = 1}^N \frac{x_i}{\sigma_i^2} \sum_{i = 1}^N \frac{y_i}{\sigma_i^2} \right)/ D\\
# \end{align*}
# $$
# 
# where
# 
# $$
# D = \sum_{i = 1}^N \frac{1}{\sigma_i^2} \sum_{i = 1}^N \frac{x^2}{\sigma_i^2} - \left(\sum_{i = 1}^N \frac{x}{\sigma_i^2}\right)^2
# $$
