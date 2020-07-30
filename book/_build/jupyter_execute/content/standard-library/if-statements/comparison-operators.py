# Comparison Operators
Comparison operators operate on two variables and return a boolean result.

## Less-than `<` and  Greater-than `>`
These operators act in the same way as the mathematical objects you are familiar with. If `a` is less than `b`, then `a < b` will return `True` and `a > b` will return `False`. For example:

print('3 > 2 is', 3 > 2)
print('2.54 < 1 is', 2.54 < 1)
print('1 < 1 is', 1 < 1)

Note that these operators act on both integers and floats interchangeably.

## Less-than-equal-to `<=` and Greater-than-equal-to `>=`

As there names suggest, the `<=` operator is related to the $\leq$ assertion in mathematics. Similarly `>=` is related to $\geq$.

print('3.3 < 3.4 is', 3.3 <= 3.4)
print('2 <= 2 is', 2 <= 2)
print('2 >= 3.4 is', 2 >= 3.4)

## Equals-to `==`
The `==` operator is used to check equality. When used on numbers, this is similar to the mathematical $=$.

print('3 == 2 is', 3==2)
print('5.3 == 5.3 is', 5.3 == 5.3)
print('6 == 6.0 is', 6 == 6.0)

The `==` operator is used more generally to compare non-numerical values. For example, it can be used to compare two strings:

print("'apple' == 'apple' is", 'apple' == 'apple')
print("'banana' == 'apple' is", 'banana' == 'apple')
print('''"banana" == 'banana' is''', "banana" == 'banana')

## Not-equal-to `!=`
This operator returns `True` if the two objects being compared aren't equivalent (if `==` would return `False`). For example:

print('3 != 2 is', 3 != 2)
print('7.3 != 7.3 is', 7.3 != 7.3)
print("'apple' != 'banana' is", 'apple' != 'banana')