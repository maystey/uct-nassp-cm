#!/usr/bin/env python
# coding: utf-8

# # Local Variables

# Variables defined in the main body of a script are called **global** variables. <!--- Fact check! --> These variables are accessible inside of functions:

# In[1]:


x = 5

def get_x():
    return x


# In[2]:


get_x()


# The arguments parsed into and the variables defined inside the function are **local variables**. They only exist in a particular instance of a function. <!--- namespace --->
# 
# In other words, these variables are not accessable from outside the function. For example:

# In[3]:


def make_var():
    func_var = 4
    return func_var


# In[4]:


make_var()


# In[5]:


func_var


# If we were to define `func_var` as a global variable, `make_var` will instance a local variable instead of reassigning the global variable:

# In[6]:


func_var = 6

print('Before function', func_var)
print('Function return', make_var())
print('After function', func_var)


# Note that when referencing a variable, Python will check the local namespace **before** the global namespace (i.e. local variables are given preference).

# As stated above, function arguments can also be treated as local variables.

# In[7]:


def arg_var(x):
    return x


# In[8]:


x = 5

arg_var(2)


# <!--- Note that when you parse a variable into a function, only the variables value is passed into the function-->
# 
# Note that, for variables that return values when referenced, 

# In[9]:


def arg_change(x):
    x = x + 2
    return x


# In[10]:


y = 4

print(arg_change(y))
print(y)


# In[11]:


def add_to_dict(d):
    d['key'] = 'value'
    return d


# In[12]:


d = {}

print(d)
print(add_to_dict(d))
print(d)


# In[ ]:




