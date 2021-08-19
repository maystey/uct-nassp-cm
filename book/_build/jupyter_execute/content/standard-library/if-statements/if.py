#!/usr/bin/env python
# coding: utf-8

# # If Statements

# If statements give us the ability to execute different blocks of code depending on the outcome of a logical statement (or boolean value).
# 
# The syntax for an if statement is:
# 
# ```python
# if condition:
#     block of code
# ```
# 
# where `block of code` following the `:` and indented is considered as the code inside the if statement. `block of code` will only be executed if condition is/evaluates to `true`.
# 
# Consider an if statement with code around it:
# 
# ```python
# code block before
# 
# if condition:
#     code block inside
# 
# code block after
# ```
# 
# here `code block before` will be executed first, then `condition` will be evaluated. If `condition` is true, `code block inside` will be executed. Finally `code block after` will be executed (regardless of whether or not `condition` is true). Illustrated in a control flow diagram:

# ```{figure} ./figures/if.png
# :name: fig-if-control-flow
# 
# Control flow diagram of the pseudo code if statement example.
# ```

# <div class="worked-example">
#     <h5 class="worked-example-title"><b>Worked Example</b></h5>

# Let's consider the problem where we want to check if one variable is greater than the other. One solution using an if statement is:

# In[1]:


a = 3
b = 2

if a > b:
    print(a, 'is greater than', b)


# If we ran the code above but with
# ```
# a = 2
# b = 2
# ```
# then we would see nothing printed out as `a > b` would evaluate to `False` and the code block contained in the if statement would not be executed.

# </div>

# ## Else
# 
# What if you wanted to execute a code block if a statement is true; and another if it's false? The `else` part of an if statement can be used for this:
# 
# ```python
# if condition:
#     code_block_1
# else:
#     code_block_2
# ```
# 
# If `condition` evaluates to `True` then `code_block_1` will be executed. If, on the other hand, `condition` evaluates to `False`, `code_block_2` will be executed.
# 
# This pseudo code can be illustrated by the control flow diagram:

# ```{figure} ./figures/if_else.png
# :name: fig-if-else-control-flow
# 
# Control flow diagram of the pseudo code if statement with an else part example.
# ```

# :::{note}
# The `else` statement cannot stand by itself. It requires a preceding if statement or loop for context.
# :::

# <div class="worked-example">
#     <h5 class="worked-example-title"><b>Worked Example</b></h5>

# Let's take our first example and add an `else` part to it:

# In[2]:


a = 3
b = 2

if a > b:
    print(a, 'is greater than', b)
else:
    print(a, 'is less than or equal to', b)


# In[3]:


a = 1
b = 2

if a > b:
    print(a, 'is greater than', b)
else:
    print(a, 'is less than or equal to', b)


# </div>

# ## Elif

# Now, what if we had 2 conditions which are mutually exclusive (if one is true the other is necessarily false) and the one isn't just the converse of the other. For this we can use the `elif` part of the if statement (to be read "else if"):
# 
# ```python
# if condition1:
#     code_block_1
# elif condition2:
#     code_block_2
# ```
# 
# If `condition 1` is false, `condition 2` will be evaluated. If `condition 2` is found to be true, then `code block 2` will be executed, if not then control will move from the if statement. Illustrated as a control flow diagram:

# ```{figure} ./figures/if_elif.png
# :name: fig-if-elif-control-flow
# 
# Control flow diagram of the pseudo code example of an if statement with an elif part.
# ```

# <div class="worked-example">
#     <h5 class="worked-example-title"><b>Worked Example</b></h5>

# Let's continue with our worked example and change the `else` part to be more specific:

# In[4]:


a = 1
b = 2

if a > b:
    print(a, 'is greater than', b)
elif a < b:
    print(a, 'is less than', b)


# In[5]:


a = 1
b = 1

if a > b:
    print(a, 'is greater than', b)
elif a < b:
    print(a, 'is less than', b)


# </div>

# ## Else After an Elif

# Now, if we want to catch the case where both the conditions in the `if` and `elif` parts of the if statement are false, we can use an `else` part at the very end of the if statement. In pseudo code:
# 
# ```python
# if condition1:
#     code_block_1
# elif condition2:
#     code_block_2
# else:
#     code_block_3
# ```
# 
# Illustrated in a control flow diagram:

# ```{figure} ./figures/if_elif_else.png
# :name: fig-if-elif-else-control-flow
# 
# Control flow diagram of the pseudo code example of an if statement with an elif and else part.
# ```

# :::{warning}
# The `else` must **always** be the last part of the if statement and **there can only be one**.
# :::

# <div class="worked-example">
#     <h5 class="worked-example-title"><b>Worked Example</b></h5>

# Now, let's re-introduce an `else` part to our worked example:

# In[6]:


a = 1
b = 1

if a > b:
    print(a, 'is greater than', b)
elif a < b:
    print(a, 'is less than', b)
else:
    print(a, 'is equal to', b)


# </div>

# ## Multiple Elif Parts

# Though you may only use one `else` part in an if statement, you are not limited by how many `elif` parts you wish to use. For example:
# 
# ```python
# if condition1:
#     code_block_1
#     
# elif condition2:
#     code_block_2
# 
# elif condition3:
#     code_block_3
# 
# else:
#     code_block_4
# ```
# 
# This can be illustrated using a control flow diagram:

# ```{figure} ./figures/if_elif_elif_else.png
# :name: fig-if-elif-elif-else-control-flow
# 
# Control flow diagram of the pseudo code example of an if statement with two elif parts and an else part.
# ```

# <div class="worked-example">
#     <h5 class="worked-example-title"><b>Worked Example</b></h5>

# As an example of a script with multiple `elif` parts, lets write a script that checks if a variable is a multiple of 2, 3, or 5:

# In[7]:


var = 21

if var % 2 == 0:
    print('Variable is a multiple of 2')
elif var % 3 == 0:
    print('Variable is a multiple of 3')
elif var % 5 == 0:
    print('Variable is a multiple of 5')
else:
    print('Variable is not a multiple of 2, 3 or 5')


# Note that if we put in a value that is both a multiple of 2 and 3, the script will only print out that it is a multiple of 2:

# In[8]:


var = 6

if var % 2 == 0:
    print('Variable is a multiple of 2')
elif var % 3 == 0:
    print('Variable is a multiple of 3')
elif var % 5 == 0:
    print('Variable is a multiple of 5')
else:
    print('Variable is not a multiple of 2, 3 or 5')


# This is because the check to so if it's a multiple of 2 is placed before the check for 3 in the `if` statement.

# </div>
