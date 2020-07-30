# Defining Functions

In this chapter we cover how to define custom functions. <!--- Reasons for making functions --->



Functions are defined using the keyword `def`. 

The basic syntax for creating a function is:
```python
def function_name(arguments):
    Code block
    return return_value
```
where
- everything indented after the `:` is part of the function body
- `arguments` can be multiple arguments with names to refer to in the function body
- the `return` statement exits the function and returns the `return_value`

The function above can be called in the usual way: `function_name(argument_values)`

## Worked Example

As a first example, let's create a function that takes a single argument and doubles it's value

def double(value):
    return 2*value

Again, we can call this argument by name and enter a value or variable as an argument:

double(1)

double(5.5)

double('a')


```{toctree}
:hidden:
:titlesonly:


return
arguments
local-variables
recursive
```
