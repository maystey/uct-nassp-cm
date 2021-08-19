#!/usr/bin/env python
# coding: utf-8

# # For Loops
# 
# For loops can be used to repeat a block of code by iterating through specified values. Python for loops are technically "foreach" loops. Though the distinction is important in other programming languages, we will refer to these as "for" loops for the entirety of the book.
# 
# The syntax for a for loop is:
# 
# ```python
# for i in iterable:
#     code block
# ```
# 
# As with the while loop, code indented after the `:` is inside the loop and will be executed with each loop iteration (here this code is represented by `code block`). 
# 
# The `iterable` is an **iterable** object. <!--- technically this means it implements the ... method (maybe put this in glossary--> These are objects that can be prompted to return a sequence of objects. Strings, lists and tuples are all examples of iterable objects. 
# 
# When the loop is executed Python instances a new object from `iterable` called an **iterator**. The iterator is asked for the next object in the sequence before each loop iteration, until there isn't a next object and control leaves the loop.
# 
# `i` is referred to as the **iteration variable**. It can be seen as a variable, and can be given any viable variable name. Before each loop iteration `i` is set to the next value of the iterator. This value can then be used in the `code block` by referring to `i` as a variable.
# 
# **Note:** be careful not to alter `iterable` inside the loop (`code block`), as this will cause an error.

# The for loop can be illustrated using the control flow diagram:
# 
# ```{figure} ./figures/foreach.png
# :name: fig-for-control-flow
# 
# Control flow diagram of the for loop.
# ```
# 
# Note that elements of {numref}`fig-for-control-flow` have been simplified. <!--- If you are interested in how a for loop can be constructed using a while loop (or another form of recursion) see ... no next iterator error -->

# ## Looping Through Sequences
# 
# As mentioned, sequences such as tuples, lists and strings can also be used as iterables. For example, if we want to print the individual characters of a string separately:

# In[6]:


for char in 'This string':
    print(char)


# Note that we called the iteration variable `char`. We can give it any name we want.
# 
# Similarly we can print each object in a list:

# In[7]:


for item in [1, 2, 3, 'a', 'b', 'c']:
    print(item)


# ## The `range()` Function
# 
# If you need to loop through a sequence of values that aren't already in an instanced data collection, you can use the `range()` function. The `range()` function takes integer arguments and returns an iterable the produces a series of integers. As we shall see, the `range()` function's arguments are very similar to slicing.
# <!--- Maybe remove the latter sentence -->
# 
# Range can be used with a single argument:
# 
# ```
# range(stop)
# ```
# 
# Here `range()` will produce a series of integers starting at zero and ending **before** the `stop` value. For example:

# In[8]:


for i in range(5):
    print(i)


# If we were to use range with 2 arguments:
# ```
# range(start, stop)
# ```
# `range()` will produce a series of integers starting with the `start` value and ending with the `stop` value. 
# 
# For example:

# In[1]:


for i in range (2, 5):
    print(i)


# Lastly if we were to use `range()` with 3 arguments:
# ```
# range(start, stop, step)
# ```
# `range()` returns a series starting with the `start` value and with step sizes of `step` in between each value until it reaches the value before `stop`. 
# 
# For example:

# In[2]:


for i in range(2, 10, 3):
    print(i)


# The default value for `step` is 1. If you want the series to descend, you can use a negative step size:

# In[5]:


for i in range(11, 3, -2):
    print(i)


# ## Useful Functions for Iterables

# ### `enumerate()` To Iterate Through Sequence and Index
# 
# Sometimes you want to loop through a sequence but also want to keep track of the index. The most convenient way to do this is using the `enumerate()` function:

# In[1]:


for i,char in enumerate('string'):
    print(i, char)


# where the iteration value is a tuple of the index and value from the original iterator (unpacked as `i` and `char` respectively).

# Alternatively, the same can be achieved using the range function and indexing the iterable sequence manually:

# In[3]:


string = 'string'

for i in range(len(string)):
    print(i, string[i])


# ### `zip()` To Iterate Through More Than One Sequence Simultaneously
# 
# If you wanted to loop through more than one sequence at a time you can use the `zip` function:

# In[7]:


for a,b in zip([1,2,3], ['a', 'b', 'c']):
    print(a, b)


# Note that the loop will only iterate as much as the shortest sequence.

# This can also be achieved manually:

# In[3]:


list_a = [1,2,3]
list_b = ['a', 'b', 'c']

for i in range(min(len(list_a), len(list_b))):
    print(list_a[i], list_b[i])


# ## Looping Through Dictionaries
# 
# To loop through the key-value pairs of a dictionary you can use the `dict.items()` method:

# In[5]:


d = {'a' : 54, 'b' : 754, 'c' : 42}

for k,v in d.items():
    print(k, v)


# You can also loop through only the keys:

# In[6]:


for k in d.keys():
    print(k, d[k])


# or only the values:

# In[7]:


for v in d.values():
    print(v)


# Note that the values returned from `dictionary.values()` won't always appear in the same order. If this is a requirement it is better to use an ordered dictionary. <!--- provide link --> <!-- perhaps this is better off in the dictionary section -->

# ## Using a `while` Loop in Place of a `for` Loop

# Although it's not as clean, you can use while loops in place of for loops. We will not cover how to do this in general here <!--- Link to external resource doing this -->, a simple example is using a while loop instead of a for loop with a `range()` iterable:

# In[1]:


#For loop:
print('For loop')

for i in range(5):
    print(i)

#Equivalent while loop:
print('')
print('While loop')

i = 0

while i < 5:
    print(i)
    
    i += 1


# Perhaps return this to the `range` function section.
# 
# ## Worked Example
# As a simple example, let's say we wanted to print out the first $n$ integer squares starting with 0.
# 
# This can be achieved manually for small $n$, for example $n = 5$:

# In[3]:


print('0 squared is', 0**2)
print('1 squared is', 1**2)
print('2 squared is', 2**2)
print('3 squared is', 3**2)
print('4 squared is', 4**2)
print('5 squared is', 5**2)


# This quickly becomes tedious and produces messy code. To achieve the same goal using a `for` loop we can do the following:

# In[5]:


for i in range(6):
    print(i, 'squared is', i**2)


# Here we have made use of the `range` function to create our iterator.
# 
# <!--- Give a more detailed breakdown of what's happening -->
