# Type Conversion

So far we have looked at three variable types: integers, floats and strings; and how to check what type a variable is.

Sometimes we want to convert between different variable types. To do this we can use the `int`, `float` and `str` functions:

int_var = 1
print(int_var, type(int_var))

float_var = float(int_var)
print(float_var, type(float_var))

float_var = 5.7
print(float_var, type(float_var))

int_var = int(float_var)
print(int_var, type(int_var))

Note that when you convert a float to an integer Python does simply discards the decimal part (if you wish to round-off a float you can use the `round` function).<!--- link docs?-->

str_var = '1.43'
print(str_var, type(str_var))

float_var = float(str_var)
print(float_var, type(float_var))

str_var = '12'
print(str_var, type(str_var))

int_var = int(str_var)
print(int_var, type(int_var))

Note that anything other than a number cannot be converted from a string to a float or int:

str_var = 'not a number'
print(str_var, type(str_var))

float_var = float(str_var)
print(float_var, type(float_var))

Even strings that contain a number with a decimal part cannot be converted to an integer:

str_var = '4.563'
print(str_var, type(str_var))

int_var = int(str_var)
print(int_var, type(int_var))

