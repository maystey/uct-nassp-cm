#!/usr/bin/env python
# coding: utf-8

# # Inclusion Operators
# 
# Inclusion operators are used to check if a value/object is in a collection and return boolean values.

# ## `in`
# 
# The `in` operator returns a `True` if the left value/object is **in** the collection on the right and `False` if it is not:

# In[1]:


print(1 in [0, 1, 2, 3])


# In[2]:


print('a' in 'abc')


# In[3]:


print(2.4 in [1, 2, 3])


# ## `not in`

# The `not in` operator returns the converse of the `in` operator:

# In[4]:


print('a' not in 'abc')


# In[5]:


print(7 not in [1, 2, 3, 4, 5])


# In[ ]:




