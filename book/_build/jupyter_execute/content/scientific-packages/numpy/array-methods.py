#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np


# # Array Methods and Attributes
# 
# In this section we will look at some methods and attributes that arrays have. This is not a complete list, but rather highlighting things you may find useful.
# 
# Let's start off by creating a fairly large array, for example a collection of human height measurements:

# In[2]:


heights = np.array(
      [ 2.13159377,  1.8864508 ,  1.63504183,  1.71173878,  1.78826872,
        1.60621813,  1.74630706,  2.11123384,  1.54212979,  1.39184441,
        1.7919224 ,  1.80299245,  1.73770464,  1.95233673,  1.47179093,
        1.70506609,  1.41194434,  2.05643464,  1.8262583 ,  1.47764985,
        1.61362183,  1.65600316,  1.42078883,  1.78059602,  1.80600655,
        1.91634004,  1.82746488,  1.82688072,  1.82053352,  1.84882458,
        1.80672297,  1.4646136 ,  1.71033286,  1.83272236,  1.97074545,
        1.96265325,  1.39817665,  1.55933323,  1.59111903,  1.53108805,
        1.33635392,  1.74971951,  1.56885338,  1.6614742 ,  1.70868504,
        1.58476337,  1.69233894,  1.73520641,  1.71248418,  1.75484377])


# To get the number of elements in an array, we can use the `size` attribute:

# In[12]:


print('The size of the heights array:', heights.size)


# For 1 dimensional arrays this is gives us the same value as using `len()`, but for multidimensional arrays, `len()` will not return the total number of elements.

# ## Minimum and Maximum Values
# 
# You can use the `min()` and `max()` methods to get the minimum and maximum values of an array respectively.

# In[13]:


print('Minimum height:', heights.min())
print('Maximum height', heights.max())


# Again, this gives you similar results to the functions in the Standard Library, but is the only option for arrays of higher dimensions.

# ## Statistical Functions

# NumPy provides us with some basic statistical functions out of the box. For example the `mean()` (arithmetic mean or average) and `std()` (standard deviation).

# In[9]:


print('Average height: ', heights.mean())
print('Standard deviation of heights: ', heights.std())


# In[8]:


print('Average height:', np.mean(heights))
print('Standard deviation of heights:', np.std(heights))
print('Maximum height:', np.max(heights))
print('Mimimum height:', np.min(heights))

