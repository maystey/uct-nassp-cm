#!/usr/bin/env python
# coding: utf-8

# # `return` Statement

# ## `return None`

# Some functions return nothing (for example the `print()` function). To achieve this you can either return `None`, leave the return value blank after `return`, or  put no `return` statement at all.

# In[1]:


def none1():
    return

def none2():
    return None

def none3():
    x = 2 #Needs code to work


# In[2]:


type(none1())


# In[3]:


type(none2())


# In[4]:


type(none3())


# ## `return` Breaks Out of the Function

# It was stated above that the `return` statement breaks out of the function. This means that anything that comes directly after a `return` inside the function body will not execute. Consider the following example to illustrate this:

# In[5]:


def message():
    print('This code will execute')
    return
    print('This code will not execute')


# In[6]:


message()


# It can be useful to use this feature of `return` to break out of a loop, or even to ignore the `else` or `elif` parts of an `if` statement. 
# 
# For example, consider the function that checks if it's argument is even or odd:

# In[7]:


def is_even(value):
    if value%2 == 0:
        return True
    else:
        return False


# In[8]:


is_even(3)


# In[9]:


is_even(6)


# The else part of the function is unnecessary:

# In[10]:


def is_even(value):
    if value%2 == 0:
        return True
    return False


# In[11]:


is_even(3)

