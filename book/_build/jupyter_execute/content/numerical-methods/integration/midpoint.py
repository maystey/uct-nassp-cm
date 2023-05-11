#!/usr/bin/env python
# coding: utf-8

# # Midpoint Rule

# In[1]:


import numpy as np
import matplotlib.pyplot as plt
from utils import plot_midpoint


# In[2]:


def f(x):
    return 3*(x - 0.5)**3 + 0.4*x + 1

x = np.linspace(0, 1)
plt.plot(x, f(x))

plt.show()


# In the midpoint rule you approximate the area under the curve as a rectangle with the height as the function value at the midpoint of the interval:

# In[3]:


fig, ax = plot_midpoint(f, 0, 1, 1, [-0.1, 1.1])

plt.show()


# $$
# \int_a^b f(x)~ dx \approx f\left(\frac{a + b}{2}\right) (b - a)
# $$

# ## Composite Midpoint Rule

# For a more accurate solution we can subdivide the interval further, constructing rectangles for each subinterval, with the function value of the midpoint used as the height:

# In[4]:


N = 2

figs, axs = N*[None], N*[None]

for i in range(0,N):
    figs[i], axs[i] = plot_midpoint(f, 0, 1, i+2, [-0.1, 1.1,])
plt.show()


# For $n$ subdivisions:
# 
# $$
# \int_a^b f(x)~ dx \approx \sum_{i=1}^n (x_i - x_{i-1}) f\left(\frac{x_i + x_{i-1}}{2}\right)
# $$

# If these divisions are equal, then
# 
# $$
# x_i - x_{i-1} = \frac{b - a}{n}
# $$
# 
# which makes the approximation:
# 
# $$
# \int_a^b f(x) ~dx \approx \frac{b - a}{n} \sum_{i=1}^n f\left(\frac{x_i + x_{i-1}}{2}\right)
# $$
# 
# Assuming that $n$ is chosen so that $0 < \tfrac{b - a}{n} < 1$, the error for this method is $O\left(\tfrac{1}{n}^3\right)$ {cite}`nm-i-m-epperson-numerical-methods`.

# ### Composite Midpoint Rule with a Discrete Data Set

# Let's consider the case where we have a discrete set of data points $(x_i, y_i)$ for $i = 0, \dots, n$, where:
# 
# $$
# y_i = f(x_i)
# $$
# 
# <!---
# The values being midpoints is kind of arbitrary, we don't need to 
# --->
# 
# We want to approximate the integral of $f(x)$ using this data and the midpoint rule. We can treat each $x_i$ as the midpoint (except for $x_0$ and $x_n$ at the boundaries) and determine the size of the interval around it using the adjacent values.
# 
# For equally spaced data points, where $\Delta x = x_i - x_{i-1}$ is constant, we can approximate the integral as:
# 
# $$
# \int_{x_0}^{x_n} f(x) ~dx \approx \Delta x \left[ \frac{1}{2} y_0 + \left\{\sum_{i = 1}^{n-1} y_i \right\} + \frac{1}{2} y_n \right]
# $$
# 
# where the first and final contributions are halved as the intervals they represent are halved (note that these aren't at the midpoints of their intervals, rather at the boundaries).

# ## References
# ```{bibliography} ../../../_bibliography/references.bib
# :cited:
# :style: plain
# :labelprefix: IntMid
# :keyprefix: nm-i-m-
# ```
