# Notation

Going forward we will use some notation to clean up our equations.

For a data set of variable $x$, $x_i$ $i = 1, 2, 3, \dots, N$:

- Expected value of $f(x)$:
$$
\langle f(x) \rangle = \frac{1}{N} \sum_{i=1}^{N} f(x_i)
$$

- Expected value of $x$ is the mean:
$$
\langle x \rangle = \frac{1}{N} \sum_{i=1}^{N} x_i
$$

- Standard deviation:
<!--- Should I be using the experimental standard deviation -->
$$
\sigma = \sqrt{\frac{\sum_{i=1}^{N} (x_i - \langle x \rangle)^2}{N}}
$$