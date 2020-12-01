#!/usr/bin/env python
# coding: utf-8

# # Numerical Solutions to Ordinary Differential Equations

# In many cases you will come across ordinary differential equations (ODEs) with no analytic solution. In this chapter we will explore numerical methods that we can use to solve ODEs that can be expressed in the form:
# 
# $$
# \frac{dy}{dx} = f(x, y)
# $$
# 
# with a given initial value for $y(x_0)$.
# 
# We shall also look at ODEs of higher order:
# 
# $$
# \frac{d^n y}{dx^n} = f\left(x, y, \frac{dy}{dx}, \frac{d^2 y}{dx^2}, \dots, \frac{d^{n-1}y}{dx^{n-1}}\right)
# $$
# 
# with given initial conditions for $y(x_0)$, $\tfrac{d}{dx}y(x_0)$, $\tfrac{d^2}{dx^2}y(x_0)$, $\tfrac{d^3}{dx^3}y(x_0)$, $\dots$, $\tfrac{d^{n-1}}{dx^{n-1}}y(x_0)$.
# 
# These are called initial value problems. To solve them you to set as many initial conditions as the order of the equation.

# 
# ```{toctree}
# :hidden:
# :titlesonly:
# 
# 
# euler
# euler-error
# higher-order
# runge-kutta
# ```
# 
