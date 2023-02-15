#!/usr/bin/env python
# coding: utf-8

# In[1]:


from mpl_toolkits import mplot3d

import numpy as np
import matplotlib.pyplot as plt


# # 3D Plotting

# To use Matplotlib's 3D plotting functionality you first need to import the [`mplot3d`](https://matplotlib.org/stable/api/toolkits/mplot3d.html) module:
# 
# ```python
# from mpl_toolkits import mplot3d
# ```
# 
# Then you need to pass the keyword argument `projection="3d"` into any of Matplotlib's axis creating functions. For example:

# In[2]:


from mpl_toolkits import mplot3d

import numpy as np
import matplotlib.pyplot as plt

fig = plt.figure()
ax = fig.add_subplot(111, projection="3d")

ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_zlabel('z')

plt.show()


# Note that this is a little less straight forward for the `plt.subplots()` function:

# In[3]:


from mpl_toolkits import mplot3d

import numpy as np
import matplotlib.pyplot as plt

fig, ax = plt.subplots(subplot_kw=dict(projection='3d'))

ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_zlabel('z')

plt.show()


# ## Rotating the Viewing Angle

# You can rotate the viewing angle of the figure programmatically using the [`view_init()`](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.mplot3d.axes3d.Axes3D.html?highlight=view_init#mpl_toolkits.mplot3d.axes3d.Axes3D.view_init) function:
# 
# ```python
# view_init(elev=None, azim=None)
# ```
# 
# where 
# 
# - `elev` is the elevation angle in the vertical plane in degrees
# - `azim` is the angle in the horizontal plane in degrees
# 

# In[4]:


from mpl_toolkits import mplot3d

import numpy as np
import matplotlib.pyplot as plt

fig, ax = plt.subplots(1, 2, subplot_kw=dict(projection='3d'), figsize=(10,8))


# Vertical Rotation
ax[0].set_xlabel('x')
ax[0].set_ylabel('y')
ax[0].set_zlabel('z')

ax[0].set_title('Vertical Rotation')

ax[0].view_init(elev=5) #Vertical rotation


# Horizontal Rotation
ax[1].set_xlabel('x')
ax[1].set_ylabel('y')
ax[1].set_zlabel('z')

ax[1].set_title('Horizontal Rotation')

ax[1].view_init(azim=30) #Horizontal rotation


plt.show()


# Of course vertical and horizontal rotation can be combined.

# ## 3D Plotting Functions

# Now you can use the [plotting functions](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.mplot3d.axes3d.Axes3D.html) available in the [mplot3d](https://matplotlib.org/stable/api/toolkits/mplot3d.html) module. We shall cover a few here, but note that these are not the full extend of what is available.

# ### Plotting a line with `plot()` or `plot3D()`

# You can plot a line on a 3D axis using [`plot()` or `plot3D()`](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.mplot3d.axes3d.Axes3D.html#mpl_toolkits.mplot3d.axes3d.Axes3D.plot), which has the call signature:
# 
# ```python
# plot(xs, ys, zs)
# ```
# 
# where `xs`, `ys` and `zs` are 1D array-like objects that contain the $x$, $y$ and $z$ coordinates of each point/vertex making up the line. Note that you can use the same keyword arguments as the 2D `plot()` function.

# <div class="worked-example">
#     <h5 class="worked-example-title"><b>Worked Example</b> - Plotting a 3D Spiral Line</h5>

# For example, let's plot a spiral, defined by:
# 
# \begin{align*}
# x(s) &= \sin(s)\\
# y(s) &= \cos(s)\\
# z(s) &= s
# \end{align*}
# 

# In[5]:


from mpl_toolkits import mplot3d

import numpy as np
import matplotlib.pyplot as plt


fig, ax = plt.subplots(subplot_kw=dict(projection='3d'))

s = np.linspace(0, 50, 1000)

ax.plot(np.sin(s), np.cos(s), s)

ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_zlabel('z')

plt.show()


# </div>

# ### Plotting surfaces with `plot_surface()`

# The [`plot_surface()`](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.mplot3d.axes3d.Axes3D.html#mpl_toolkits.mplot3d.axes3d.Axes3D.plot_surface) function creates a surface plot using a grid of points (or vertices) arranged to form quadrelaterals. 
# 
# ```python
# plot_surface(X, Y, Z)
# ```
# 
# The arguments `X`, `Y` and `Z` are 2D arrays containing the $x$, $y$ and $z$ coordinates of the points on the grid respectively. Pairs of adjacent points make the edges of the quadrelaterals.

# <div class="worked-example">
#     <h5 class="worked-example-title"><b>Worked Example</b> - Plotting a Rectangle</h5>

# For this first example, let's plot a square with one side elevated. We will give it points with the $(x, y, z)$ coordinates:
# 
# 1. $(0, 0, 0)$
# 2. $(1, 0, 0)$
# 3. $(0, 1, 1)$
# 4. $(1, 1, 1)$
# 
# These coordinates will be stored in separate arrays for $x$, $y$ and $z$ in the following order:
# 
# \begin{equation*}
# \begin{bmatrix}
# 1 & 2 \\
# 3 & 4
# \end{bmatrix}
# \end{equation*}

# In[6]:


from mpl_toolkits import mplot3d

import numpy as np
import matplotlib.pyplot as plt

fig, ax = plt.subplots(subplot_kw=dict(projection='3d'), figsize=(10,8))

X = np.array([
    [0, 1], 
    [0, 1]
])

Y = np.array([
    [0, 0],
    [1, 1]
])

Z = np.array([
    [0, 0],
    [1, 1]
])

ax.plot_surface(X, Y, Z)

ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_zlabel('z')

plt.show()


# In[7]:


from mpl_toolkits import mplot3d

import numpy as np
import matplotlib.pyplot as plt

fig, ax = plt.subplots(subplot_kw=dict(projection='3d'), figsize=(10,8))

X = np.array([
    [0, 1], 
    [0, 1]
])

Y = np.array([
    [0, 0],
    [1, 1]
])

Z = np.array([
    [0, 0],
    [1, 1]
])


ax.plot_surface(X, Y, Z, color = '0.8')

for i in range(2):
    for j in range(2):
        num = str(1 + j + 2*i)
        
        ax.text(X[i, j], Y[i, j], Z[i, j], num, color = 'r', fontsize = 20, fontweight = 'bold')
        #text = mplot3d.art3d.Text3D(X[i, j], Y[i, j], Z[i, j], text=num)
        


ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_zlabel('z')

plt.show()


# Note that the code used to select the color of the surface and create the numerical annotations is not included above.

# </div>

# Now, we will often create surfaces where $Z(X, Y)$ is some function of $X$ and $Y$, where $X$ and $Y$ can be treated as independent variables. In these cases we can generate a grid of $x$ and $y$ coordinates, and use these to calculate the corresponding $z$ values.
# 
# To create this grid we will use the [`numpy.meshgrid()`](https://numpy.org/doc/stable/reference/generated/numpy.meshgrid.html) function. For our interests, the call signature of `meshgrid()` is:
# 
# ```python
# meshgrid(*xi)
# ```
# where `xi` is sequence of arrays. Here we are only interested in passing 2 arrays into `meshgrid()` (one for a sequence of $x$ values and another for a sequence of $y$ values) to produce a 2D grid.
# 
# Consider the arrays `x` and `y` where:
# 
# \begin{align*}
# x &= [x_1, x_2, x_3, \dots, x_n] \\
# y &= [y_1, y_2, y_3, \dots, y_m]
# \end{align*}
# 
# if we were to put these into `meshgrid()`:
# 
# ```python
# X, Y = np.meshgrid(x, y)
# ```
# 
# then the resulting 2D arrays would be of the form:
# 
# \begin{equation*}
# X = \begin{bmatrix}
# x_1 & x_2 & x_3 & \cdots & x_n\\
# x_1 & x_2 & x_3 & \cdots & x_n\\
# \vdots & \vdots & \vdots & \ddots & \vdots\\
# x_1 & x_2 & x_3 & \dots & x_n\\
# \end{bmatrix}
# \end{equation*}
# 
# and
# 
# \begin{equation*}
# Y = \begin{bmatrix}
# y_1 & y_1 & y_1 & \cdots & y_1\\
# y_2 & y_2 & y_2 & \cdots & y_2\\
# \vdots & \vdots & \vdots & \ddots & \vdots\\
# y_m & y_m & y_m & \cdots & y_m\\
# \end{bmatrix}
# \end{equation*}
# 
# both with $m$ rows and $n$ columns.

# Let's consider an example of a grid like this generated from the arrays:
# 
# \begin{align*}
# x &= [0, 1, 2, 3, 4, 5] \\
# y &= [0, 1, 2, 3]
# \end{align*}
# 
# used to generate a flat surface with $z = 0$.

# In[8]:


from mpl_toolkits import mplot3d

import numpy as np
import matplotlib.pyplot as plt


fig, ax = plt.subplots(subplot_kw=dict(projection='3d'), figsize=(10,8))

x = np.arange(0, 6)
y = np.arange(0, 4)

X, Y = np.meshgrid(x, y)
Z = np.zeros(X.shape)

ax.plot_surface(X, Y, Z)

ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_zlabel('z')

plt.show()


# <div class="worked-example">
#     <h5 class="worked-example-title"><b>Worked Example</b> - Plotting a Surface Using a Rectangular Grid</h5>

# Let's consider a simple surface:
# 
# $$
# z = x y
# $$

# In[9]:


from mpl_toolkits import mplot3d

import numpy as np
import matplotlib.pyplot as plt


fig, ax = plt.subplots(subplot_kw=dict(projection='3d'))

x = np.linspace(-1, 1, 10)
y = np.linspace(-1, 1, 10)

X, Y = np.meshgrid(x, y)

Z = X * Y

ax.plot_surface(X, Y, Z)

ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_zlabel('z')

plt.show()


# </div>

# <div class="worked-example">
#     <h5 class="worked-example-title"><b>Worked Example</b> - Plotting a Surface Using a Radial Grid</h5>

# You may not always want to use a rectangular grid. For example, if we have a radially symmetric surface (or just a surface defined using polar coordinates):
# 
# $$
# z = 1 - (x^2 + y^2)
# $$
# 
# then we may want to use a radial grid, by creating a rectangular grid of $r$ and $\theta$ coordinates, where:
# 
# \begin{align*}
# x &= r \cos(\theta) \\
# y &= r \sin(\theta)
# \end{align*}
# 
# and then calculating an $x$, $y$ grid from this. Note that $x$, $y$ and $z$ can be considered as parameterized by $r$ and $theta$.

# In[10]:


from mpl_toolkits import mplot3d

import numpy as np
import matplotlib.pyplot as plt


fig, ax = plt.subplots(subplot_kw=dict(projection='3d'))

r = np.linspace(0, 10, 10)
theta = np.linspace(0, 2 * np.pi, 20)

R, THETA = np.meshgrid(r, theta)

X = R * np.cos(THETA)
Y = R * np.sin(THETA)
Z = 1 - R * R # X**2 + Y**2 == R**2

ax.plot_surface(X, Y, Z)

ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_zlabel('z')

plt.show()


# </div>

# There's much more that you can do with these surface plots, such as [coloring them in using a colormap](https://matplotlib.org/stable/gallery/mplot3d/surface3d.html).

# ### Plotting wireframes with `plot_wireframe()`

# The [`plot_wireframe()`](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.mplot3d.axes3d.Axes3D.html#mpl_toolkits.mplot3d.axes3d.Axes3D.plot_wireframe) function is similar to the `plot_surface()` function, except it produces a plot of the edges of the quadrilaterals only, with the faces unfilled.

# <div class="worked-example">
#     <h5 class="worked-example-title"><b>Worked Example</b> - Plotting a Simple Wireframe</h5>

# Let's consider the same surface as before:
# 
# $$
# z = x y
# $$

# In[11]:


from mpl_toolkits import mplot3d

import numpy as np
import matplotlib.pyplot as plt


fig, ax = plt.subplots(1, 2, subplot_kw=dict(projection='3d'), figsize=(10,8))

x = np.linspace(-1, 1, 10)
y = np.linspace(-1, 1, 10)

X, Y = np.meshgrid(x, y)

Z = X * Y


#Surface Plot
ax[0].plot_surface(X, Y, Z)

ax[0].set_title('Surface Plot')

ax[0].set_xlabel('x')
ax[0].set_ylabel('y')
ax[0].set_zlabel('z')


#Wireframe plot
ax[1].plot_wireframe(X, Y, Z)

ax[1].set_title('Wireframe Plot')

ax[1].set_xlabel('x')
ax[1].set_ylabel('y')
ax[1].set_zlabel('z')


plt.show()


# </div>
