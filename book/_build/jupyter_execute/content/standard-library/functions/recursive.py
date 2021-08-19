#!/usr/bin/env python
# coding: utf-8

# # Recursive Functions

# Recursive functions are functions that make calls to themselves.
# 
# They can be used in place of loops. Though in Python they don't necessarily provide a more efficient solution, there are many problems for which a recursive function is the most elegant and convenient solution.

# <div class="worked-example">
#     <h5 class="worked-example-title"><b>Worked Example</b></h5>

# One of the most famous implementations of a recursive function is to implement the factorial:
# 
# $$
# \begin{align*}
# 0! &= 1\\
# n! &= n\times(n-1)\times(n-2)\times(n-3)\times\dots\times2\times1\\
# \end{align*}
# $$
# 
# This is achieved by using the recurrence relation:
# 
# $$
# n! = n\times(n-1)!
# $$
# 
# The recursive function which solves this is:

# In[1]:


def factorial(n):
    if not type(n) is int:
        print('n must be an integer')
        return
    if n <0:
        print('n must be greater than or equal to 0')
        return
    
    if n == 0:
        return 1
    
    return n*factorial(n-1)


# Note, an important aspect of this function is the return value of 1 for `n == 0`. This is called the base class, without it the function would never finish it's recursion.
# 
# Putting this function into action:

# In[2]:


factorial(-1)


# In[3]:


factorial(0.5)


# In[4]:


factorial(0)


# In[5]:


factorial(1)


# In[6]:


factorial(5)


# In[7]:


factorial(10)


# ### Illustration of How a Function Call Works

# The inner workings of this `factorial()` function are fairly subtle. The (informal) flow diagram below illustrates the function call for `factorial(5)`:
# 
# ![Factorial flow chart](function_recursion_factorial.png)

# </div>

# ## The Base Class

# As mentioned earlier, a recursive function must have at least one base class. The base class is a return state that **doesn't** make another recursive function call.
# 
# It's also important to make sure that the recursion eventually reaches the base class when designing your function.

# In[ ]:




