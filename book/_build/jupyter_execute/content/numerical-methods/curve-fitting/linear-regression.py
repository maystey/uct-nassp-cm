#!/usr/bin/env python
# coding: utf-8

# # Linear Regression
# 
# In linear regression the relationship between a dependent variable and one or more independent variables is modelled by a linear relation, such as:
# 
# $$
# y = a_0 + a_1 x_1 + a_2 x_2 + \dots + a_m x_m
# $$
# 
# where $y$ is the dependent variable, the $x_j$ are the dependent variable, and the $a_j$ are scalar parameters. Note that it is the linearity of the $a_j$ parameters that is important, any non-linear combination of $x_j$ that do not cause a non-linear combination of $a_j$ can be dealt with by redefining the $x_j$ variables. The $a_j$ parameters are often unkown and need to be determined from paired measurements of the $y$ and $x_j$ variables.

# ## Statistical Notation
# 
# Going forward we will use some statistical notation to clean up our equations.
# 
# For a data set of values for a variable $x$, $x_i$ ($i = 1, 2, 3, \dots, N$):
# 
# - Expected value of $f(x)$ (which can be considered the average of $f(x)$):
# 
#     $$
#     \langle f(x) \rangle = \frac{1}{N} \sum_{i=1}^{N} f(x_i)
#     $$
# 
# - Expected value of $x$ is the mean of the data set:
#     
#     $$
#     \langle x \rangle = \frac{1}{N} \sum_{i=1}^{N} x_i
#     $$
# 
# - Standard deviation (which is an indication of the spread of the data):<!--- Should I be using the experimental standard deviation -->
#     
#     $$
#     \sigma = \sqrt{\frac{\sum_{i=1}^{N} (x_i - \langle x \rangle)^2}{N}}
#     $$

# In[ ]:




