#!/usr/bin/env python
# coding: utf-8

# # Numerical Operators
# <!--- Rename to arithmatic operators? -->

# Coding, in the simplest sense, is merely the action of assigning values to variables, and then 'doing things' with those variables.
# 
# In this section we will look at some of the basic operators used for integers and floats. Other variable types have different operators, which we shall see later.
# 
# An obvious starting point is basic arithmetic; addition, subtraction, multiplication and division:

# In[1]:


a = 2.0
b = 3.0
c = 10.0

print('a added to b is', a + b)
print('a multiplied by c is', a*c)
print('c divided by b is', c/b)
print('a subtracted from c', c - a)


# These operators can also be used for integers:

# In[2]:


print('2 multiplied by 3 is', 2*3)


# and between integers and floats:

# In[3]:


print('1.5 multiplied by 2 is', 1.5*2)


# If you are using Python version 2.xxx or below, beware of dividing by integers...

# ## The Exponential Operator `**`
# Another useful operator is the exponential operator `**`. This returns the left number to the power of the right:

# In[4]:


print(2**3)


# which can be read as $2^3$.
# 
# Note that this operator also works on floats and float-integer combinations:

# In[5]:


print(4**0.5) #square root of 4


# ## The Modulo Operator `%`
# The modulo operator returns the remainder of the left number divided by the right:

# In[6]:


print(16%3)


# In mathematics this would be expressed as 
# 
# $16$ mod $3$.
# 
# This operator can also act on floats and integer-float combinations:

# In[7]:


print(16.3%3)


# ## The Floor Division Operator `//`
# This returns the result of the left number divided by the right, but without the remainder:

# In[8]:


print(16//3)


# Like the others this works for both integers and floats.

# ## Special Functions and Advanced Mathematics
# For more complex mathematics involving logs, trigonometry, etc. we'll rely on the scientific packages SciPy and NumPy. We'll discuss these at a later stage.

# ## Multiple Operations in a Single Expression
# Though we have only seen one operation or function used per line, you can combine as many as you'd like:

# In[9]:


print( 2**3 + 4)


# If you want to group or control the order in which operations are executed use brackets. For example:

# In[10]:


print( (2 + 17//2)**5 )


# where the `//` is applied first, then the `+` and lastly the `**`. We shall discuss the order in which operations and function calls are executed later. <!--- in Section.... Make a url -->

# In[ ]:




