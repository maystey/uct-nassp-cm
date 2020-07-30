import numpy as np

# Arrays

Arrays are one of NumPy's most important objects. 

An array is a sequence of homogeneous data (each element must be the same data type). NumPy arrays use NumPy specific data types which are listed [here](https://numpy.org/devdocs/user/basics.types.html).

Though we shall see that arrays can be indexed and sliced similarly to strings, tuples and lists, they behave differently under operations.

Arrays can have any number of dimensions. In this section we will only consider the 1 dimensional case.

## Creating Arrays

Arrays can be created using the `np.array()` function with a list, tuple or another array as the argument:

#Array of integers
np.array([1, 2, 3, 4])

#Array pf strings
np.array(('a', 'b', 'c'))

Remember that arrays are homogeneous:

#Trying to create an array with different types
np.array([1, 2.3, 'x'])

## Indexing and Slicing

As said before, arrays can be indexed and sliced similarly to lists and strings

letters = np.array(['a', 'b', 'c', 'd', 'e'])
print('Letters:', letters)
print('First character:', letters[0])
print('Second character:', letters[1])
print('Last character:', letters[-1])
print('Every second character:', letters[::2])

## Mutable But Tricky To Resize

Similarly to lists, arrays are mutable (you can change the array after initializing it). For example, you can change an element of an array:

arr = np.array((1, 2, 3 ,4))
print('Array:', arr)

print('')
print('Changing element 2')
print('')

arr[2] = 7
print('Array:', arr)

However, unlike lists, it's not easy or efficient to alter the size of an array. It is still possible to resize (with `np.resize()` ) and to concatenate (with `np.concatenate()` ) arrays, but they don't have certain handy functions for lists like `.append()` and `.insert()`.

In general you should only create an array once you know how big it needs to be. If you need to add elements to an array, consider starting with a list and converting that to an array when you need the array properties.

## Iterating Through Arrays

Like strings, tuples and lists, arrays are iterable:

arr = np.array([1, 2, 3, 4])

for a in arr:
    print(a)

## Vectorized Operations

One of the most useful properties of NumPy arrays is their vectorized operations. That is arithmetic operations between an array and array, and an array and scalar are performed element by element.

For example consider the scalar operations:

2*np.array([1, 2, 3, 4])

np.array([1, 4, 5]) + 1

Array on array operations are also performed element by element:

arr1 = np.array([1, 2, 3, 4])
arr2 = np.array([2, 4, 6, 8])

print(arr2, '-', arr1, 'is', arr2 - arr1)
print(arr2, '/', arr1, 'is', arr2/arr1)

These vectorized operations are far more efficient than iterating through the arrays and operating on each element individually, i.e.

#More efficient:
print(arr1, '+', arr2, 'is', arr1 + arr2)

#Less efficient
arr3 = np.array(4*[0])

for  i in range(4):
    arr3[i] = arr1[i] + arr2[i]

print(arr1, '+', arr2, 'is', arr3) 

## Creating Structured Arrays <!--- Rename this -->

Often we would like to create a large array with a particular structure. We could create these arrays from lists using list comprehension, but NumPy provides some useful built in functions to use instead.

### `np.arange()`

This function is analogous to the `range()` function. It produces a series of values where you can specify the starting value, stopping value and the step size. 

The syntax is:
```python
np.arange(start, stop, step)
```
Similar to the `range()` function, you can use 1, 2 or 3 arguments:

#1 argument: stop
np.arange(5)

#2 arguments: start, stop
np.arange(1, 5)

#3 arguments: start, stop, step
np.arange(1, 10 ,2)

Unlike the `range()` function. `np.arange()` also allows for floating point values:

np.arange(2.3, 3, 0.1)

### `np.linspace()`



This function creates a series of evenly spaced values between a stopping and starting value. The number of items in the array can also be specified.

The syntax:
```python
np.linspace(start, stop, number)
```
If `number` is not specified an array of length 50 is created. 

np.linspace(0, 1, 10)

### `np.zeroes()`

This function creates a uniform array of zeros. It takes the shape of the array you want to generate as an argument.
```python
np.zeros(shape)
```

For a one dimensional array `shape` is just the size of the array:

np.zeros(5)

`np.zeros()` can be useful if you wish to create an array with a particular size, but will only be filling in the values later.

### `np.ones()` 

`np.ones()` is similar to `np.zeros()`, except it generates a uniform array of ones.

np.ones(7)

Note that, if you want a uniform array of a different value, you can either add that value to an array of zeros or multiply that value with an array of ones.