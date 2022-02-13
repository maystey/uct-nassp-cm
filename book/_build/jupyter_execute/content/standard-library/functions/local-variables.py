#!/usr/bin/env python
# coding: utf-8

# # Local Namespace and Variables
# <!-- Consider putting this in a more generic chapter -->

# Variable names are stored in a **namespace**, and must be unique within a namespace. Variables that are defined in the main body of a script are stored in the **global namespace** and are referred to as **global** variables.
# 
# The global namespace is accessible both in the script body and inside of functions:

# In[1]:


x = 5

def get_x():
    return x


# In[2]:


get_x()


# however, when variables are defined inside of the function (including arguments) these are only accessible within that function. For example:
# 
# <!--
# The arguments passed into, and the variables defined inside of, the function are **local variables**. They only exist inside the function, and for a particular function call.
# 
# In other words, these variables are not accessible from outside the function. For example:
# -->

# In[3]:


def make_var():
    func_var = 4
    return func_var


# In[4]:


make_var()


# In[5]:


func_var


# This is because a function has it's own namespace, referred to as a **local namespace**. Variables in the global namespace are still accessible inside the local namespace, but variables defined in the local namespace are not available in the global namespace (or any other namespaces that encompasses it).

# If a variable is defined in a local namespace with the same name as a variable in the global namespace, then the local variable will be used by default.
# 
# For example, if we were to define `func_var` as a global variable, `make_var` will instance a local variable instead of reassigning a new value to the global variable:

# In[6]:


func_var = 6

print('Before function', func_var)
print('Function return', make_var())
print('After function', func_var)


# In other words Python will check the local namespace **before** the global namespace.

# As stated above, function arguments can also be treated as local variables.

# In[7]:


def arg_var(x):
    return x


# In[8]:


x = 5

arg_var(2)


# <!--- Note that when you parse a variable into a function, only the variables value is passed into the function-->
# 
# Note that, this remains true when local variable from an argument has it's value reassigned: 

# In[9]:


def arg_change(x):
    x = x + 2
    return x


# In[10]:


y = 4

print('Before function:', y)
print('Function return:', arg_change(y))
print('After function:', y)


# <!--
# <div class="admonition warning" name="warning-object">
#     <p class="title">Warning</p>
# -->
# :::{warning}
# Although variable names are restricted to namespaces, the objects that they represent are not. This is not so important to keep in mind with numbers and strings (which are passed in by value), but it is important for objects that can be altered, such as arrays and dictionaries.
# :::

# For example, if we were to pass a dictionary into a function, any alterations made to that dictionary inside the function would remain outside (as there is only one dictionary object being used).

# In[11]:


def add_to_dict(d):
    d['key'] = 'value'
    return d


# In[12]:


d = {}

print('Dictionary before the function call:', d)
print('Function return:', add_to_dict(d))
print('Dictionary after the function call:', d)

