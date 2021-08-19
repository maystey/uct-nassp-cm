#!/usr/bin/env python
# coding: utf-8

# # Comparing the Methods

# Let's compare the three root finding algorithms we have covered to each other.

# ## Bisection Method

# The bisection method starts with an interval that is known to contain the root. The size of this interval is halved with each iteration (improving the precision. For a desired tolerance (or precision), it is possible to calculate how many iterations the Bisection method will take.
# 
# If $f$ is continuous on the interval, the interval only contains one root, and the function changes signs as it passes through the root, then the root is guaranteed to be found.

# ## Secant Method

# The Secant method requires two points near the root to start off with. If it will converge to the root, then it generally converges quicker than the bisection method, although it's not possible to calculate how many iterations the method will need for a given tolerance.
# 
# It is possible for this method not to converge, especially in the case where the gradient of $f$ becomes shallow, which would cause one of the calculated points to shoot off.
# 
# It is also possible for this method to converge on a different root if there is one nearby.

# ## Newton-Raphson Method

# The Newton-Rhaphson method is similar to the secant method, except it makes use of the derivative of $f$.
# 
# As for the secant method, the Newton-Raphson method converges to the root faster than the bisection method. Also like the secant method, it is possible the method not to converge, or to converge on another nearby root.

# ## In Summary

# <table>
#     <tr>
#         <th></th>
#         <th>Bisection</th>
#         <th>Secant</th>
#         <th>Newton-Raphson</th>
#     </tr>
#     <tr>
#         <th>Convergence</th>
#         <td>Will always converge to a root inside the interval, as long as the function is well behaved.</td>
#         <td colspan="2">May not converge to a root if the function has stationary points near it. May converge on neighboring roots.</td>
#     </tr>
#     <tr>
#         <th>Rate of Convergence</th>
#         <td>Relatively slow convergence.</td>
#         <td colspan="2">Fast convergence</td>
#     </tr>
#     <tr>
#         <th>Complexity</th>
#         <td colspan="2">Only requires the function, which must simply return values for given arguments on the interval.</td>
#         <td>Requires knowledge of the first derivative of the function.</td>
#     </tr>
# </table>

# In[ ]:




