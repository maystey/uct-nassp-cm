# Multivariate Linear Least Squares Minimization

In **{doc}`Numerical Methods/Linear Regression Algorithms/Linear Least Squares Minimization<./least-squares>`**, we considered the linear functional relation between two measurable variables, $x$ and $y$:

$$
y = a_0 + a_1 x
$$

where $a_0$ and $a_1$ are unknown conditions to be determined.

On this page we will look at the more generic case, where we solve the problem for an arbitrary number of variables and constants.

## Three Variables

Let's start by solving this problem for three measurable variables: $y$, $x_1$ and $x_2$, in the linear functional relation:

$$
y = a_0 + a_1 x_1 + a_2 x_2
$$

where $a_0$, $a_1$ and $a_2$ are unknown coefficients.

Consider a data set of measured $(x_{1,~i}, x_{2,~i}, y_i)$ pairs for $i = 1, 2, 3, \dots , N$. If we attribute the dispersion of this data from the functional relation to error in the $y_i$ terms, $\epsilon_i$, then we can relate the data points with:

\begin{align*}
y_i + \epsilon_i &= a_0 + a_1 x_{1,~i} + a_2 x_{2,~ i}\\
\therefore \epsilon_i &= a_0 + a_1 x_{1,~ i} + a_2 x_{2,~ i} - y_i\\
\end{align*}

The sum of errors squared is given by:

\begin{align*}
S &= \sum_{i = 1}^N \epsilon_i^2 \\
  &= \sum_{i=1}^N (a_0 + a_1 x_{1,~i} + a_2 x_{2,~i} - y_i)^2\\
\end{align*}

We want to minimize $S$ with respect to each of the constants, $a_0$, $a_1$ and $a_2$:

$$
\frac{\partial S}{\partial a_0} = 2 \sum_{i=0}^n (a_0 + a_1 x_{1, ~i} + a_2 x_{2, ~i} - y_i) = 0
$$

,

$$
\frac{\partial S}{\partial a_1} = 2 \sum_{i=0}^n (a_0 + a_1 x_{1,~i} + a_2 x_{2,~i} - y_i)x_{1,~i} = 0
$$

and

$$
\frac{\partial S}{\partial a_2} = 2 \sum_{i=0}^n (a_0 + a_1 x_{1,~i} + a_2 x_{2,~i} - y_i)x_{2,~i} = 0
$$

Re-arranging the above equations and using our statistical notation yields:

$$
a_0 + a_1 \langle x_1 \rangle + a_2 \langle x_2 \rangle = \langle y \rangle
$$

,

$$
a_0\langle x_1\rangle + a_1\langle x_1^2\rangle + a_2\langle x_1 x_2 \rangle = \langle x_1 y \rangle\\
$$

and

$$
a_0\langle x_2\rangle + a_1\langle x_1 x_2\rangle + a_2\langle x_2^{~~2}\rangle = \langle x_2 y\rangle
$$

This time algebraic manipulation is a lot more work, instead we shall use a matrix equation (which will serve us better in the more generic case to come). The matrix equation representation is:

$$
\begin{pmatrix}
  1		&\langle x_1\rangle		&\langle{x_2}\rangle\\
  \langle{x_1}\rangle	&\langle{x_1^2}\rangle		&\langle{x_1x_2}\rangle\\
  \langle{x_2}\rangle	&\langle{x_1x_2}\rangle	&\langle{x_2^2}\rangle\\
 \end{pmatrix}
  \begin{pmatrix}
  a_0\\
  a_1\\
  a_2\\
 \end{pmatrix}
 = 
 \begin{pmatrix}
  \langle{y}\rangle\\
  \langle{x_1 y}\rangle\\
  \langle{x_2 y}\rangle
 \end{pmatrix}
$$

This can easily be solved numerically using:

\begin{align*}
\boldsymbol{X}\boldsymbol{A} &= \boldsymbol{Y}\\ 
\therefore \boldsymbol{A} &= \boldsymbol{X}^{-1} \boldsymbol{Y}\\
\end{align*}


<div class="worked-example">
    <h5 class="worked-example-title"><b>Worked Example</b> - Cepheid Variables</h5>

You now have all you need to find the unknown coefficients for the full functional relation of the magnitude ($M$), period ($P$) and color ($B-V$) of the Cepheid variables:

$$
M = a_0 + a_1 \log P + a_2 (B - V)
$$

using the same data file as before. (You should find the values $a_0 = -2.15$ mag, $a_1 = -3.12$ mag and $a_2 = 1.49$). You may wish to use NumPy matrices, which have the inverse property `I` ($\boldsymbol{X}^{-1}$ is achieved using `X.I`, for the appropriately defined `X` matrix), and can be multiplied directly 

Try this yourself before reading the solution that follows.

**Solution:**

As in the  **{doc}`Numerical Methods/Linear Regression Algorithms/Linear Least Squares Minimization<./least-squares>`** worked example, we shall read in the data using `numpy.loadtxt()`:

import numpy as np
import matplotlib.pyplot as plt

logP, M, color = np.loadtxt('./data/cepheid_data.csv', delimiter = ',', skiprows = 1, unpack = True)

Here we have:

\begin{align*}
y   &= M\\
x_1 &= logP\\
x_2 &= (B - V)\\
\end{align*}

We will now proceed to construct the matrices using the data. Starting with simpler $\boldsymbol{Y}$ matrix:

#Defining Y as a column matrix
Y = np.matrix([
    [np.mean(M)],
    [np.mean(logP * M)],
    [np.mean(color * M)]
])

Note that $\boldsymbol{X}$ is symmetric about the diagonal, i.e. $\boldsymbol{X}_{k~l} = \boldsymbol{X}_{l~k}$, we will make use of this to reduce the number of calculations we need to perform.

X = np.matrix(np.ones( (3, 3) )) #Using an array generating function

# X[0, 0] is just 1, so we leave it

#The first row
X[0, 1] = np.mean(logP)
X[0, 2] = np.mean(color)

#The first column (which is the transpose of the first row)
X[1, 0] = X[0, 1]
X[2, 0] = X[0, 2]

#The diagonal
X[1, 1] = np.mean(logP * logP)
X[2, 2] = np.mean(color * color)

#The off-diagonal elements
X[1, 2] = np.mean(logP * color)
X[2, 1] = X[1, 2]

Now we calculate the $\boldsymbol{A}$ matrix:

A = X.I * Y

#Printing the constants

for i in range(3):
    print(f'a{i+1} =', '{:.3}'.format(A[i,0]) )

</div>

## Arbitrarily Many Variables

Consider a linear functional relation between measurable variables $x_1$, $x_2$, $x_3$, $\dots$, $x_m$ and $y$:

$$
\begin{align*}
y   &= a_0 + a_1 x_1 + a_2 x_2 + \dots + a_m x_m\\
    &= a_0 + \sum_{j = 1}^m a_j x_j\\
\end{align*}
$$

where $a_0$, $a_1$, $\dots$ and $a_m$ are unknown constants.

Suppose we have a data set of measured $(x_{1,~i}, x_{2,~i}, \dots, x_{mi}, y_i)$ values for $i = 1, 2, 3, \dots, N$. As before, we assume that the dispersion in our data from the functional relation is due to error in the $y_i$ data points only. Therefore we can write the relation between our data points as:

$$
y_i + \epsilon_i = a_0 + \sum_{j = 1}^m a_j x_{j, ~i}
$$

The sum of errors squared can thus be written as:

$$
S = \sum_{i=1}^N \bigg(a_0 + \bigg(\sum_{j=1}^m a_j x_{j,~i} \bigg) - y_i\bigg)^2
$$

We want to find the values of $a_0$, $a_1$, $\dots$ and $a_m$ which gives us the minimum value of $S$. Minimizing $S$ with respect to $a_0$ gives us:

$$
\frac{\partial S}{\partial a_0} = 2 \sum_{i=1}^N \bigg(a_0 + \bigg(\sum_{j=1}^m a_j x_{j,~i} \bigg) - y_i\bigg) = 0
$$

Distributing the sum over $i$ amongst the terms: 

$$
\therefore N a_0 + \bigg(\sum_{j=1}^m a_j \sum_{i=1}^N x_{j,~i} \bigg) - \sum_{i=1}^N y_i = 0
$$

Dividing by $N$:

$$
\therefore a_0 + \bigg(\sum_{j=1}^m a_j \frac{1}{N}\sum_{i=1}^N x_{j,~i} \bigg) - \frac{1}{N}\sum_{i=1}^N y_i = 0
$$


Using our stats notation:

$$
\therefore a_0 + \sum_{j=1}^m a_j \langle{x_{j}}\rangle = \langle{y}\rangle
$$

Now, let's minimize $S$ with respect to one of the $a_k$ for $k = 1, 2, \dots, m$, following a similar line of algebraic manipulation as above:

$$
\begin{align*}
\frac{\partial S}{\partial a_k} = \sum_{i=1}^N 2 x_{k,~i} \bigg(a_0 + \bigg(\sum_{j=1}^m a_j x_{j,~i} \bigg) - y_i\bigg) &= 0\\
\therefore a_0 \sum_{i=1}^N x_{k, ~i} + \sum_{j=1}^m a_j \bigg(\sum_{i=1}^N x_{k,~i} x_{j,~i} \bigg) - \sum_{i=1}^N x_{k,~i} y_i &= 0\\
\therefore a_0 \langle{x_{k}}\rangle + \sum_{j=1}^m a_j \langle{x_k x_j}\rangle &= \langle{x_k y}\rangle\\
\end{align*}
$$

Writing the results for $a_0$ and $a_k$ ($k = 1,\dots,m$) into a system of equations, expanding the sum over $j$:


$$\begin{eqnarray*}
a_0 &+& a_1 \langle{x_1}\rangle &+& a_2 \langle{x_2}\rangle  &+& \dots &+& a_m \langle{x_m}\rangle &=& \langle{y}\rangle\\
a_0 \langle{x_{1}}\rangle &+& a_1 \langle{x_1~^2}\rangle &+& a_2 \langle{x_1 x_2}\rangle &+& \cdots &+& a_m \langle{x_1 x_m}\rangle &=&  \langle{x_1 y}\rangle\\
a_0 \langle{x_{2}}\rangle &+& a_1 \langle{x_2 x_1}\rangle &+& a_2 \langle{x_2~^2}\rangle &+& \cdots &+& a_m \langle{x_2 x_m}\rangle &=&  \langle{x_2 y}\rangle\\
a_0 \langle{x_{3}}\rangle &+& a_1 \langle{x_3 x_1}\rangle &+& a_2 \langle{x_3 x_2}\rangle &+& \cdots &+& a_m \langle{x_3 x_m}\rangle &=&  \langle{x_3 y}\rangle\\
\vdots ~~~~ &+& ~~~~\vdots &+& ~~~~\vdots &+& \ddots &+& ~~~~\vdots &=& ~~~\vdots\\
a_0 \langle{x_{m}}\rangle &+& a_1 \langle{x_m x_1}\rangle &+& a_2 \langle{x_m x_2}\rangle &+& \cdots &+& a_m \langle{x_m~^2}\rangle &=&  \langle{x_m y}\rangle\\
\end{eqnarray*}$$

To solve these equations numerically, we can reformulate these equations into a matrix equation:

$$
\begin{pmatrix}
1                     & \langle{x_1}\rangle      & \langle{x_2}\rangle      & \cdots & \langle{x_m}\rangle\\
\langle{x_1}\rangle   & \langle{x_1^{~~2}}\rangle   & \langle{x_1 x_2}\rangle  & \cdots & \langle{x_1 x_m}\rangle\\
\langle{x_2}\rangle   & \langle{x_2 x_1}\rangle  & \langle{x_2^{~~2}}\rangle   & \cdots & \langle{x_2 x_m}\rangle\\
\vdots                & \vdots                   & \vdots                   & \ddots & \vdots\\
\langle{x_m}\rangle   & \langle{x_m x_1}\rangle  & \langle{x_m x_2}\rangle  & \cdots & \langle{x_m^{~~2}}\rangle\\
\end{pmatrix}
\begin{pmatrix}
a_0\\
a_1\\
a_2\\
\vdots\\
a_m\\
\end{pmatrix}
=
\begin{pmatrix}
\langle{y}\rangle\\
\langle{x_1 y}\rangle\\
\langle{x_2 y}\rangle\\
\vdots\\
\langle{x_m y}\rangle\\
\end{pmatrix}
$$

Notice that the left most matrix is symmetric about the diagonal, this can come in handy when computing the matrix elements. As before, this equation can be solved for the $a_i$ by inverting the left most matrix, i.e.

$$
\begin{align*}
\boldsymbol{X} \boldsymbol{A} &= \boldsymbol{Y}\\
\therefore \boldsymbol{A} &= \boldsymbol{X}^{-1} \boldsymbol{Y}\\
\end{align*}
$$

### Python Implementation

Let's work on a Python implementation of this solution. You may want to try it yourself before reading further. In order to verify our implementation we will use the Cepheid data we've used so far, though we shall design it to support any number of $x_j$ variables.

We will start by designing a function that takes the data in as two arguments:

$$
\texttt{y_data} = [y_{1}, y_{2}, y_{3}, \dots, y_{N}]
$$

$$
\begin{matrix}
\texttt{x_data} = [ & [ & x_{1,~1}, & x_{1,~2}, & \cdots, & x_{1,~N} &], \\
                    & [ & x_{2,~1}, & x_{2,~2}, & \cdots, & x_{2,~N} &],\\
                    & [ & x_{3,~1}, & x_{3,~2}, & \cdots, & x_{3~N} &],\\
                    & [ & \vdots~~, & \vdots~~, & \ddots, & \vdots &],\\
                    & [ & x_{m,~1}, & x_{m,~2}, & \cdots, & x_{m,~N} &]]\\
\end{matrix}
$$

as NumPy arrays.

#### Calculating Expectation Values

Note that for each of the sums along the data sets ($\sum_{i = 1}^N$), we will be summing along the rows. For example, for the quantity:

$$
\langle x_1 \rangle = \frac{1}{N} \sum_{i = 1}^N x_{1,~i}
$$

we can use:

```Python
np.mean(x_data[0, :])
```

and for

$$
\langle x_1 x_2 \rangle = \frac{1}{N} \sum_{i = 1}^N x_{1,~ i} x_{2,~ i}
$$

we can use

```Python
np.mean(x_data[0, :] * x_data[1, :])
```
where we have made use of NumPy array's vectorized operations.

#### Constructing the $\boldsymbol{X}$ Matrix

Now, let's break down the structure of the matrix:

$$
\boldsymbol{X} = 
\begin{pmatrix}
1                     & \langle{x_1}\rangle      & \langle{x_2}\rangle      & \langle{x_3}\rangle      & \cdots & \langle{x_m}\rangle\\
\langle{x_1}\rangle   & \langle{x_1^{~~2}}\rangle   & \langle{x_1 x_2}\rangle  & \langle{x_1 x_3}\rangle  & \cdots & \langle{x_1 x_m}\rangle\\
\langle{x_2}\rangle   & \langle{x_2 x_1}\rangle  & \langle{x_2^{~~2}}\rangle   & \langle{x_2 x_3}\rangle  & \cdots & \langle{x_2 x_m}\rangle\\
\langle{x_3}\rangle   & \langle{x_3 x_1}\rangle  & \langle{x_3 x_2}\rangle  & \langle{x_3^{~2}}\rangle   & \cdots & \langle{x_3 x_m}\rangle\\
\vdots                & \vdots                   & \vdots                   & \vdots                   & \ddots & \vdots\\
\langle{x_m}\rangle   & \langle{x_m x_1}\rangle  & \langle{x_m x_2}\rangle  & \langle{x_m x_3}\rangle  & \cdots & \langle{x_m^{~~2}}\rangle\\
\end{pmatrix}
$$

the dimensions of this matrix is $(m+1)\times(m+1)$, we can get the value for $m$ from the dimensions of the `x_data` array:

```Python
m = x_data.shape[0]
```

from this we can create a matrix of ones, which we will populate later:

```Python
X = np.array(np.ones((m+1, m+1))
```


Now, as we have noted before, $\boldsymbol{X}$ is a symmetric matrix. That is for for row $k$ and column $l$, $\boldsymbol{X}_{k l} = \boldsymbol{X}_{l k}$. We only need to construct one of the triangles of the matrix, the other is obtained for free.

Let's work with the upper triangle of the matrix. Here there are 3 regions with distinguishable structures

1. The first row
2. The diagonal
3. The remaining triangle

<!--**1. The First Row**-->
The first element of the matrix is just one. The remainder of the first row is simply the expectation value of each of the $x_j$:

$$
\boldsymbol{X}_{0 ~0} = 1
$$

and 

$$
\boldsymbol{X}_{0~ l} = \langle{x_l}\rangle ~~~~ \text{where}~ l = 1, 2, \dots, m
$$

Note that here we are indexing $\boldsymbol{X}$ from 0 to better translate it to code (keep in mind that the `x_data` array also starts with a 0 index, so the $x_l$ data is in row $l - 1$):

```Python
for l in range(m):
    X[0, l + 1] = np.mean(x_data[l, :])
    
    # Setting the values for the first column
    # remember that X[k, l] = X[l, k]
    X[l + 1, 0] = X[0, l + 1]
```

Now, consider the triangle off of the diagonal. That is the region:
<!-- Consider showing the diagonal in this, or perhaps find a way to annotate the matrix regions in the matrix drawn further up -->

$$
\begin{pmatrix}
-         & -        & -                         & -                        & \cdots  & - \\
-         & -        & \langle{x_1 x_2}\rangle   & \langle{x_1 x_3}\rangle  & \cdots  & \langle{x_1 x_m}\rangle\\
-         & -        & -                         & \langle{x_2 x_3}\rangle  & \cdots  & \langle{x_2 x_m}\rangle\\
-         & -        & -                         & -                        & \cdots  & \langle{x_3 x_m}\rangle\\
\vdots    & \vdots   & \vdots                    & \vdots                   & \ddots  & \vdots \\
-         & -        & -                         & -                        & \cdots  & -\\
\end{pmatrix}
$$

This region exhibits the pattern:

$$
\boldsymbol{X}_{k l} = \langle{x_k x_l}\rangle ~~~~ \text{where}~ 1 \leq k \leq m ~~\text{and}~~  l > k
$$

The diagonal has a fairly simple pattern, starting from (row, column) $(1,1)$:

$$
\boldsymbol{X}_{k k} = \langle{x_k~^2}\rangle ~~~~ \text{where}~ 1 \leq k \leq m
$$

Note, however, that this is a special case of the rules for constructing region 3. We can therefore combine regions 2 and 3 with the rule:

$$
\boldsymbol{X}_{k l} = \langle{x_k x_l}\rangle ~~~~\text{where}~ 1 \leq k \leq m ~~\text{and}~~  l \geq k
$$

In the code this becomes:

```Python
# Inner matrix

for k in range(m):
    for l in range(k, m):
        X[k + 1, l + 1] = np.mean( x_data[k, :] * x_data[l, :] )
        
        #Setting the value for the lower triangle
        X[l + 1, k + 1] = X[k + 1, l + 1]
```

That covers the $\boldsymbol{X}$ matrix.

#### Constructing the $\boldsymbol{Y}$ Matrix

Now let's construct the matrix:

$$
\boldsymbol{Y} =
\begin{pmatrix}
\langle{y}\rangle\\
\langle{x_1 y}\rangle\\
\langle{x_2 y}\rangle\\
\vdots\\
\langle{x_m y}\rangle\\
\end{pmatrix}
$$

This is fairly straight forward, with

$$
\boldsymbol{Y}_{0~ 0} = \langle{y}\rangle
$$

and

$$
\boldsymbol{Y}_{k~ 0} = \langle{x_k y}\rangle ~~~~\text{where}~ k = 1, \dots, m
$$

```Python
#Creating the Y column matrix:
Y = np.matrix( np.zeros( (m + 1, 1) ) )

#First entry
Y[0, 0] = np.mean(y_data)

#The remainder of the entries
for k in range(m):
    Y[k + 1, 0] = np.mean( x_data[k, :] * y_data )
```

#### Finding Matrix $\boldsymbol{A}$ (Or Solving For the $a_j$)

Lastly, to solve for our $a_j$ values, we consider the matrix:

$$
\boldsymbol{A}=
\begin{pmatrix}
a_0 \\
a_1\\
a_2\\
\vdots\\
a_m\\
\end{pmatrix}
$$

This fits into the matrix equation 

$$
\boldsymbol{X}\boldsymbol{A} = \boldsymbol{Y}
$$

where we've already constructed $\boldsymbol{X}$ and $\boldsymbol{Y}$. All that's left is to solve the equation be inverting $\boldsymbol{X}$:

$$
\boldsymbol{A} = \boldsymbol{X}^{-1} \boldsymbol{Y}
$$

To achieve this numerically, we simply take the inverse of `X`, `X.I`:

```Python
#Finding A:

A = X.I*Y
```

This `A` matrix is a column matrix. As a bonus, if we wanted to turn it into a one-dimensional array, we can use the `flatten()` method:

```Python
np.array(A).flatten()
```

#### Putting It All Together

Putting this all together into a function:

import numpy as np
import matplotlib.pyplot as plt


def least_squares(y_data, x_data):
    m = x_data.shape[0]

    X = np.matrix(np.ones((m+1, m+1)))

    #First row
    for l in range(m):
        X[0, l + 1] = np.mean(x_data[l, :])

        # Setting the values for the first column
        # remember that X[k, l] = X[l, k]
        X[l + 1, 0] = X[0, l + 1]


    # Upper triangle
    for k in range(m):
        for l in range(k, m):
            X[k + 1, l + 1] = np.mean( x_data[k, :] * x_data[l, :] )

            #Setting the value for the lower triangle
            X[l + 1, k + 1] = X[k + 1, l + 1]


    #Creating the Y column matrix:
    Y = np.matrix( np.zeros( (m + 1, 1) ) )

    #First entry
    Y[0, 0] = np.mean(y_data)

    #The remainder of the entries
    for k in range(m):
        Y[k + 1, 0] = np.mean( x_data[k, :] * y_data )
    
    #Finding A:

    A = X.I*Y
    
    return np.array(A).flatten()

<div class="worked-example">
    <h5 class="worked-example-title"><b>Worked Example</b> - Applying the Solution to the Cepheid Variables Data</h5>

Now, lets apply this function to the Cepheid Variables data to find the unknown coefficients for the functional relation of the magnitude ($M$), period ($P$) and color ($B-V$):
    
$$
M = a_0 + a_1 \log P + a_2 (B - V)
$$    
    
We'll unpack the data as in the **{doc}`Numerical Methods/Linear Regression Algorithms/Linear Least Squares Minimization<./least-squares>`** example, and then pack it into the structure that is required by the function.

#Reading the data
logP, M, color = np.loadtxt('./data/cepheid_data.csv', delimiter = ',', skiprows = 1, unpack = True)

a_arr = least_squares(M, np.array([logP, color]))

for i, a in enumerate(a_arr):
    print(f'a_{i} =', '{:.3}'.format(a))

Which matches the results from the worked example above.

</div>