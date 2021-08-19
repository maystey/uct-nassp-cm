#!/usr/bin/env python
# coding: utf-8

# # Tuple
# 
# Just as strings are a sequence of characters, tuples are a sequence of objects. This makes their use far more general.
# 
# You can set a tuple by separating the objects using commas. For example:

# In[1]:


t = 1, 2, 3, 'a', 'b', 'c'

print(t)


# This is called tuple packing.
# 
# You can also put brackets around the objects, which is useful if you need to instance a tuple and use it in the same line (for example as a function argument):

# In[2]:


print(('a', 1, 'b', 2, 'c', 3))


# Like strings, tuples can be indexed and sliced:

# In[3]:


print('Index 3:', t[3])
print('Slice from index 3:', t[3:])


# Tuples are also immutable (like strings):

# In[5]:


t[2] = 5


# You can unpack a tuple into multiple variables, just like you can pack multiple values into a tuple:

# In[7]:


t = (1, 2, 3)
print('t is ', t)

x, y, z = t
print('x is', x) 
print('y is', y)
print('z is', z)

