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


# Note that for the function defined above, all of the arguments need to be passed into the functions:

# In[4]:


arg3('a', 'b')


# In[ ]:





# ## Default Values for Function Arguments

# You can assign default values to arguments by using the `=` operator, for example:

# In[5]:


def hello(name = 'World', time = 'today'):
    return f'Hello {name}! How are you {time}?' 


# (If you are unfamiliar with f-strings `f''`, see the page on [**The Python Standard Library/Strings/String Formatting**](../strings/string-formatting))

# If `hello()` is called without passing arguments, the values defined in the function will be used:

# In[6]:


hello()


# alternatively you pass in new values:

# In[7]:


hello('reader', 'feeling')


# Not all arguments need be replaced:

# In[8]:


hello('reader')


# You don't need to assign default values for every argument, for example:

# In[9]:


def hello_hello(num, name = 'World', time = 'today'):
    return f"Hello {num*'hello '}{name}! How are you {time}?"


# Note that the `num` argument needs to have a value passed into it, but the others do not:

# In[10]:


hello_hello(1)


# Also note that an argument without a default value cannot be defined after an argument that does:

# In[11]:


def hello_again(name = 'World', time = 'today', num):
    return f"Hello {num*'hello '}{name}! How are you {time}?"


# In[ ]:





# ## Positional and Keyword Arguments

# In the examples above, we have been entering argument values directly into the function in the order in which they are defined. These are called **positional arguments**. Alternatively, arguments can be passed in by name:

# In[12]:


arg3(arg1 = 1, arg2 = 2, arg3 = 3)


# These are called **keyword arguments**. Keyword arguments can be passed into the function in any order:

# In[13]:


arg3(arg2 = 1, arg3 = 2, arg1 = 3)


# Both positional and keyword arguments can be used in the same function call:

# In[14]:


arg3(1, arg2 = 2, arg3 = 3)


# Note that positional arguments cannot be passed into a function after keyword arguments:

# In[15]:


arg3(arg2 = 1, arg1 = 2, 3)


# ## Unpacking Data Structures As Arguments

# You can unpack data structures to be passed into functions as individual arguments, this can be useful if you need to store the values of arguments to be used in functions later. Tuples and lists can be unpacked using the `*` operator, and will behave like positional arguments:

# In[16]:


print( *(1, 2, 3) ) #Unpacking a tuple as 3 positional arguments
print( *['a', 'b', 'c'] ) #Unpacking a list as 3 positional arguments


# Dictionaries can be unpacked as keyword arguments using the `**` operator, using our `hello` function from above:

# In[17]:


hello_hello(2, **{'name' : 'everybody', 'time' : 'you all doing'}) #Unpacking a dictionary for the keyword arguments


# ## Defining Functions That Take Arbitrary Many Positional and Keyword Arguments

# You can define functions that take an arbitrary number of positional or keyword arguments. So far we have encountered this in the `print()` function which can take an arbitrary amount of positional arguments. 

# ### Positional Arguments

# You can collect arbitrarily many positional arguments by using the `*` operator before the argument name. Non-keyword arguments that are passed into the function from the position of this argument on will be collected as a tuple and passed in as this argument. For example:

# In[18]:


def argn(*args):
    for arg in args:
        print(arg)


# In[19]:


argn(1, 2)


# In[20]:


argn(1, 2, 3, 4, 5)


# As implied above, any positional arguments that are defined before the `*args` argument will be collected separately:

# In[21]:


def arg2n(arg1, arg2, *args):
    print('Arg1:', arg1)
    print('Arg2:', arg2)
    
    print('Args:')
    for arg in args:
        print('     ', arg)


# In[22]:


arg2n('a', 'b', 1, 2, 3)


# Note that arguments defined after `*args` must be passed into the function as keyword arguments:

# In[23]:


def arg2n1(arg1, arg2, *args, arg3):
    print('Arg1:', arg1)
    print('Arg2:', arg2)
    
    print('Args:')
    for arg in args:
        print('     ', arg)
    
    print('Arg3:', arg3)


# In[24]:


arg2n1(1, 2, 3, 4, 5)


# In[25]:


arg2n1(1, 2, 3, 4, 5, arg3 = 6)


# If you define arguments with default values, these must appear after the `*args` argument:

# In[26]:


#TODO: rename or replace this with something a little more sensible
def arg2nkw(arg1, arg2, *args, kwarg1 = 'kwarg1', kwarg2 = 'kwarg2'):
    print('Arg1:', arg1)
    print('Arg2:', arg2)
    
    print('Args:')
    for arg in args:
        print('     ', arg)
    
    print('Kwarg1:', kwarg1)
    print('Kwarg2:', kwarg2)


# In[27]:


arg2nkw('a', 'b', 1, 2, 3, 4, 5, kwarg1 = 'c', kwarg2 = 'd') 


# ### Keyword Arguments

# You can collect arbitrary keyword arguments using the `**` 

# In[28]:


def kwargs(arg1, arg2, **kwargs):
    print('Arg1', arg1)
    print('Arg2', arg2)
    print(kwargs)


# In[29]:


kwargs(1, 2, kwarg1 = 2, kwarg3 = 3)


# Note that no other arguments can be used after `**kwargs`:

# In[30]:


def kwargs_arg(arg1, **kwargs, arg2):
    pass


# ## Old Stuff

# In[31]:


hello(time = 'this morning')


# In[32]:


hello(time = 'this fine day', name = 'friend')


# In[33]:


hello_hello(1, 'there', 'doing')


# In[34]:


hello_hello(0, time = 'awake this early', name = 'sleepy head')

