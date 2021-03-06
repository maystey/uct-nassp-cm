#!/usr/bin/env python
# coding: utf-8

# # Units and Quantities

# The `astropy.units` module gives us the tools to work with units and quantities (values paired with units). The documentation can be found [here](https://docs.astropy.org/en/stable/units/).
# 
# The `astropy.units.Unit` class is used to represent base units of measurement, such as meters, seconds, kilograms, ect). These units can be manipulated, for example to determine conversion factors from one set of units to another.
# 
# You can also define your own units, either as standalone base units or by composing other units together. It is also possible to decompose units into its base units.

# As an example, consider the SI unit for mass : kilograms (kg)

# In[2]:


from astropy import units as u

u.kg


# ## Quantities

# Quantities are created by multiplying a float/integer with units, for example a mass:

# In[7]:


mass = 3.0*u.kg
mass


# The `value` and `unit` of the quantity can be accessed separately:

# In[8]:


mass.value


# In[10]:


mass.unit


# Quantities can be combined mathematically, the units combine accordingly. For example, consider the force:

# In[13]:


acceleration = 4 * u.m/(u.s*u.s)

force = mass*acceleration
force


# ## Converting Units

# Units can be converted to like units. For example, let's convert the force calculated above into Newtons:

# In[14]:


force_N = force.to(u.N)
force_N


# The conversion above is still within the SI system. We can also convert to units from other systems. For example, converting the force to dynes from the cgs system:

# In[15]:


force_dyn = force.to(u.dyn)
force_dyn


# Astropy gives us a more convenient way to convert between unit systems without requiring us to do any book keeping. Again, lets convert the force in SI units to the cgs units:

# In[18]:


force_cgs = force.cgs
force_cgs


# ## Quantities and NumPy Arrays

# Astropy quantities support NumPy arrays. The whole array will have the same units.

# In[21]:


import numpy as np

distances = np.array([1, 2, 3, 4]) * u.m
distances


# In[22]:


distances.to(u.cm)


# In[23]:


distances/(1 * u.s)


# ## Compose Units

# Above we converted our force from kg.m.s$^{-2}$ to N directly. We can let Astropy compose those units for us:

# In[25]:


force.unit.compose()


# As you can see this gives us all the standard options available.

# ## Decompose Units

# You can also decompose units back into base units:

# In[26]:


force_N.decompose()


# ## Dimensionless Quantities

# Astropy understands dimensionless quantities. For example, lets take the ratio of 2 lengths:

# In[28]:


r1 = 10 * u.m
r2 = 2 * u.m

r1 / r2


# Sometimes you will need to decompose units first:

# In[31]:


force1 = 3 * u.N
force2 = 6 * u.kg * u.m / u.s / u.s

force_ratio = force1 / force2
force_ratio


# In[32]:


force_ratio.decompose()


# ## Find Equivalent Units

# You can find equivalent units by using the `find_equivalent_units()` method. For example, for miliseconds (ms):

# In[33]:


u.ms.find_equivalent_units()


# ## Set Equivalencies

# In some contexts we want to use certain units interchangeably, that are not actually equivalent.
# 
# For example, the energy of a photon ($E$) is related to it's wavelength ($\lambda$) and frequency ($\nu$) as:
# 
# $$
# E = h \nu = h c / \lambda
# $$
# 
# where $h$ is Planck's constant. Radio astronomers refer to the energy of an emission line of neutral hydrogen being 1420 MHz or 21 cm. These units are obviously not that of energy, but in this context they can be treated as such.
# 
# Astropy allows for this kind of treatment of our units:

# In[35]:


wavelength = 21.106 * u.cm

wavelength.to(u.MHz, equivalencies = u.spectral())


# ### Finding Equivalent Units with Set Equivalencies

# You can also find equivalent within the context of the equivalencies:

# In[36]:


freq = 1 * u.Hz

freq.unit.find_equivalent_units(equivalencies = u.spectral())


# ## Fractional Units

# Sometimes we'll need to work with fractional units (units with a fractional power). Floats can work for this, but it is better to use the Standard Library's `fraction.Fraction` objects:

# In[37]:


from fractions import Fraction

T = 3000.0 * u.K
T


# In[38]:


T ** Fraction(3/2)


# ## Defining Your Own Units

# You can define your own units derived from other units. For example, lets make a unit called a baker's fortnight (bf), which is a fortnight (14 days) and an extra day:

# In[40]:


bakers_fortnight = u.def_unit('bf', 15 * u.day)

bakers_fortnight


# In[41]:


time = 3 * bakers_fortnight
time


# In[42]:


time.to(u.day)

