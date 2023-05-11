#!/usr/bin/env python
# coding: utf-8

# # Trapezoidal Rule

# In[1]:


import numpy as np
import matplotlib.pyplot as plt
from utils import plot_trapezoidal


# In[2]:


def f(x):
    return x*(x-0.7)**2 + 0.1*x + 0.2

x = np.linspace(0, 1)
plt.plot(x, f(x))

plt.show()


# For the trapezoidal rule we approximate the integral of $f(x)$ on the interval $[a-b]$ by constructing the trapezium below:

# In[3]:


fig, ax = plot_trapezoidal(f, 0, 1, 1, [-0.1, 1.1])

plt.show()


# and calculating it's area.
# 
# The area of the trapezium is given by:
# <!--- Illustrate the triangle and rectangle in the figure --->
# $$
# A_\text{trapezoid} = A_{\text{rectangle}} + A_{\text{triangle}}
# $$
# 
# In the case where $f(a) < f(b)$, this area is given by:
# 
# \begin{align*}
# A_\text{trapezoid}  &= (b - a)f(a) + \tfrac{1}{2} (b - a) \left[f(b) - f(a)\right]\\
#                     &= \tfrac{1}{2}(b - a) \left[f(a) + f(b)\right]
# \end{align*}
# 
# In the case where $f(a) > f(b)$, the area is give by:
# 
# \begin{align*}
# A_\text{trapezoid}  &= (b - a)f(b) + \tfrac{1}{2} (b - a) \left[f(a) - f(b)\right]\\
#                     &= \tfrac{1}{2}(b - a) \left[f(a) + f(b)\right]
# \end{align*}
# 
# which is the same as above, so in general we can approximate the integral as:
# 
# $$
# \int_a^b f(x)~ dx \approx \tfrac{1}{2} (b - a) \left[f(a) + f(b)\right]
# $$

# ## Composite Trapezoid Rule

# Now, if we were to break up this interval into $n$ equal sub-intervals, and approximate the integral on each of these, we arrive at the composite trapezoidal rule (illustrated in the diagrams that follow).

# In[4]:


N = 3

figs, axs = N*[None], N*[None]

for i in range(N):
    figs[i], axs[i] = plot_trapezoidal(f, 0, 1, i+2, [-0.1, 1.1])

plt.show()


# To calculate this we use the sum:
# 
# $$
# \int_a^b f(x)~ dx \approx \sum_{i=1}^n \tfrac{1}{2} (x_i - x_{i-1}) \left[f(x_{i-1}) + f(x_i)\right]
# $$
# 
# where $x_0 = a$ and $x_n = b$. As we have specified that each of the $n$ subintervals are of equal sizes, we have that:
# 
# $$
# x_{i} - x_{i - 1} = \frac{b- a}{n}
# $$
# 
# we can therefore write the approximation as:
# 
# $$
# \int_a^b f(x)~ dx \approx \frac{b -a}{2 n} \sum_{i=1}^n \left[f(x_{i-1}) + f(x_i)\right]
# $$
# 
# note how each $f(x_i)$ in the sum above is repeated twice, except for $f(x_0)$ and $f(x_n)$, which only feature once each. We can now write the approximation as:
# 
# $$
# \int_a^b f(x)~ dx \approx \frac{b -a}{2 n} \left[f(a) + 2 \left\{\sum_{i=1}^{n-1} f(x_i)\right\} + f(b)\right]
# $$
# 
# For a choice of $n$ such that $0 < \tfrac{b - a}{n} < 1$, the error for this method is $O\left(\tfrac{1}{n}^2\right)$ {cite}`nm-i-t-epperson-numerical-methods`.

# ### Composite Trapezoidal Rule with a Discrete Data Set

# Again, consider the data set $(x_i, y_i)$ for $i = 0, \dots, n$, where 
# 
# $$
# f(x_i) = y_i
# $$
# 
# If we wanted to approximate the integral of this data set using the trapezoidal rule, we can apply this to each interval individually:
# 
# $$
# \int_{x_0}^{x_n} f(x)~ dx \approx \tfrac{1}{2} \sum_{i = 1}^n (x_i - x_{i-1}) \left[y_{i-1} + y_i\right]
# $$
# 
# If the $x_i$ values are evenly spaced, with $x_i - x_{i-1} = \Delta x$ constant, then we can use the composite formula from the section above:
# 
# $$
# \int_{x_0}^{x_n} f(x)~ dx \approx \frac{\Delta x}{2} \left[ y_0 + 2 \left\{\sum_{i=1}^{n-1} y_i\right\} + y_n \right]
# $$

# ## References
# ```{bibliography} ../../../_bibliography/references.bib
# :cited:
# :style: plain
# :labelprefix: IntTrap
# :keyprefix: nm-i-t-
# ```
