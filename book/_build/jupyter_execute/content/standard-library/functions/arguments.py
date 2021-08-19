#!/usr/bin/env python
# coding: utf-8

# # Function Arguments

# You can include as many arguments as you want in your function definition. Inside the function, these arguments can be treated as variables.
# 
# <!--- The names you give these arguments can be treated as variable names inside the function. -->

# In[1]:


def arg3(arg1, arg2, arg3):
    print(arg1)
    print(arg2)
    return arg3


# In[2]:


arg3(1, 2, 3)


# You may use variables or statements (anything that resolves to a value or object) as arguments:

# In[3]:


var1 = 45

arg3(var1, 3*4, 7)


# ## Positional Arguments

# The arguments defined above are called **positional arguments**. In order to set them correctly, you need to parse them in the order they are defined in the function. You must also provide a value for each argument:

# In[4]:


arg3('a', 'b')


# ## Keyword Arguments

# If you want to set optional arguments with a default value, you can use keyword arguments. The syntax is:
# ```python
# def function_name(keyword_arg = default_value):
# ```
# 
# For example:
# <!--- Should I really be using string formatting here? I guess it's as good a time as any... -->

# In[5]:


def hello(name = 'World', time = 'today'):
    return f'Hello {name}! How are you {time}?' 


# (If you are unfamiliar with f-strings `f''`, see the page on [**The Python Standard Library/Strings/String Formatting**](../strings/string-formatting))

# This function can be called with no arguments, in which case the default values will be used:

# In[6]:


hello()


# We can also parse the arguments like positional arguments:

# In[7]:


hello('reader', 'feeling')


# In[8]:


hello('reader')


# Keyword arguments can be referred to by name, and out of order:

# In[9]:


hello(time = 'this morning')


# ## Combining Positional and Keyword Arguments

# If you define a function with both positional and keyword arguments, the positional arguments must appear **before** the keyword arguments.
# 
# For example:

# In[10]:


def hello_hello(num, name = 'World', time = 'today', weather = 'good'):
    
    return f"Hello {num*'hello'} {name}! How are you {time}?"


# Here the positional argument `num` must be provided

# In[11]:


hello_hello()


# As before, the keyword arguments can be provided like positional arguments or by name:

# In[12]:


hello_hello(1, 'there', 'doing')


# In[13]:


hello_hello(0, time = 'awake this early', name = 'sleepy head')

