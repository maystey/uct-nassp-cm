#!/usr/bin/env python
# coding: utf-8

# # `return` Statement

# As was already mentioned, the `return` statement can be used to return values from a function call. There are more properties of the `return` statement that are worth covering.

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
# For example, consider the function that checks if its argument is even or odd:

# In[7]:


def is_even(value):
    if value % 2 == 0:
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
    if value % 2 == 0:
        return True
    return False


# In[11]:


is_even(3)


# ## `return` Tuples

# Although not a feature of the `return` statement itself, it's worth noting that tuple packing can be used for the value returned. This can be particularly useful when you need to return multiple values.

# For example consider a function that splits a floating point number into it's whole and decimal parts, returning both:

# In[12]:


def floor_rem(num):
    whole = int(num)
    frac = num - whole
    
    return whole, frac


# In[13]:


floor_rem(2.13)


# Note that tuple unpacking can also be used to collect the return values of the function into multiple variables:

# In[14]:


num = 3.14

whole, frac = floor_rem(num)

print('Number:', num)
print('Whole part:', whole)
print('Decimal part:', frac)


# In[ ]:




