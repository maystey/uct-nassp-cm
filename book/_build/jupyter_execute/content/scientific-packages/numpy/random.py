#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np


# # NumPy Random Module

# The `numpy.random` module provides us with random number generators (RNG). You can find the documentation [here](https://docs.scipy.org/doc/numpy-1.14.0/reference/routines.random.html). As there name suggests, random number generators produce random numbers. In this section we highlight a few essential functions from the module:

# ## `np.random.random()`

# This function produces random floating point numbers from a uniform probability distribution function (PDF) on the interval $[0, 1)$ ($1$ is excluded). If no arguments are provided a single number is generated: 

# In[2]:


np.random.random()


# If the length or shape is specified, `random()` returns an array of random numbers:

# In[3]:


np.random.random(5)


# In[4]:


np.random.random((2, 3))


# If you want to produce uniformly distributed random numbers $R$ on the interval $[a, b)$, you can use random numbers $r$ from the interval $[0, 1)$ by scaling and shifting them:
#     $$
#     R = a + r*(b-a)
#     $$
#     
# For example, to generate uniform random numbers on the interval $[18, 30)$:

# In[5]:


np.random.random(4)*(30 -18) + 18


# To read more about `numpy.random.random()`, see the [documentation](https://docs.scipy.org/doc/numpy-1.14.0/reference/generated/numpy.random.random.html#numpy.random.random).

# ## `np.random.randint()`

# This function produces random integers sampled from a uniform probability distribution on a **specified** interval.
# 
# The interval is defined by the first 2 arguments of `randint()`, the end of the interval (second number) is not included in the interval:

# In[6]:


#Random numbers from 1 up to 10
np.random.randint(1, 10)


# Again, you can specify a size or shape of the output array:

# In[7]:


np.random.randint(1, 10, 3)


# In[8]:


np.random.randint(1, 10, (2, 4))


# ## Random Numbers From Other Distributions

# `numpy.random` provides us with many more RNG functions that sample from many of the most popular PDFs. You can see the full list [in the documentation](https://docs.scipy.org/doc/numpy-1.14.0/reference/routines.random.html#distributions).
# 
# For example, the `np.random.norm()` function produces random numbers sampled from the normal (Gaussian) distribution. Parameters like the mean and standard deviation (or first 2 moments) can be specified.
# 
# All of these functions can generate array outputs
