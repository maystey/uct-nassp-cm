#!/usr/bin/env python
# coding: utf-8

# # Newton-Raphson Method

# In[1]:


import numpy as np
import matplotlib.pyplot as plt
from utils import newton_plot


# In[2]:


m = 1

def f(x):
    return -(x - m)**2 + 0.5

def f_prime(x):
    return -2*(x - m)

x = np.linspace(0, 1)
plt.plot(x, f(x))
plt.show()


# The Newton-Raphson method is similar to the secant method, except here we construct a straight line that passes through a point $(x_0, f(x_0))$ with a gradient of $f^\prime (x_0)$, the tangent of $f(x)$ at that point. The next point, $x_1$, is the intersection of this line with the $x$-axis:

# In[3]:


fig, ax = newton_plot(f, f_prime, 0.7, 0, [-0.1, 1.1])

plt.show()


# As before, this process can be repeated with $x_1$, and the rest of the points after it, converging closer to the root. Further iterations are illustrated in the following figures:

# In[4]:


N = 2

x = 0.7

figs,axs = [None]*3, [None]*3



for i in range(N):
    x = x - f(x)/f_prime(x)
    
    figs[i], axs[i] = newton_plot(f, f_prime, x, i+1,
                                 [-0.1, 1.1])

plt.show()


# To calculate the point $x_n$ using the previous point $x_{n-1}$, we start by constructing the line running through $(x_{n-1}, f(x_{n-1}))$:
# 
# $$
# \frac{y - f(x_{n-1})}{x - x_{n-1}} = f^\prime (x_{n-1})
# $$
# 
# at the $x$-intercept, $y = 0$ and $x = x_n$:
# 
# $$
# \begin{align*}
# \frac{0 - f(x_{n-1})}{x_n - x_{n-1}} &= f^\prime(x_{n-1})\\
# \therefore x_n &= x_{n-1} - \frac{f(x_{n-1})}{f^\prime(x_{n-1})}\\
# \end{align*}
# $$

# ## Precision

# Similarly to the secant method, the precision for the Newton-Raphson method can be set for a given tolerance by finding $n$ such that:
# 
# $$
# |x_n - x_{n-1}| < \text{tolerance}
# $$

# ## Instability

# The Newton-Raphson method suffers from much the same issues as the secant method.

# In[ ]:




