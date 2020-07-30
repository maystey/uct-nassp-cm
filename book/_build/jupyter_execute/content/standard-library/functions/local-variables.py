# Local Variables

Variables defined in the main body of a script are called **global** variables. <!--- Fact check! --> These variables are accessible inside of functions:

x = 5

def get_x():
    return x

get_x()

The arguments parsed into and the variables defined inside the function are **local variables**. They only exist in a particular instance of a function. <!--- namespace --->

In other words, these variables are not accessable from outside the function. For example:

def make_var():
    func_var = 4
    return func_var

make_var()

func_var

If we were to define `func_var` as a global variable, `make_var` will instance a local variable instead of reassigning the global variable:

func_var = 6

print('Before function', func_var)
print('Function return', make_var())
print('After function', func_var)

Note that when referencing a variable, Python will check the local namespace **before** the global namespace (i.e. local variables are given preference).

As stated above, function arguments can also be treated as local variables.

def arg_var(x):
    return x

x = 5

arg_var(2)

<!--- Note that when you parse a variable into a function, only the variables value is passed into the function-->

Note that, for variables that return values when referenced, 

def arg_change(x):
    x = x + 2
    return x

y = 4

print(arg_change(y))
print(y)

def add_to_dict(d):
    d['key'] = 'value'
    return d

d = {}

print(d)
print(add_to_dict(d))
print(d)

