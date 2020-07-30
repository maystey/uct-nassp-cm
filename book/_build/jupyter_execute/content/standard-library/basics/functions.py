# Introduction to Using Functions
In this section we shall discuss some of the details on how to use functions from the Standard Library. We have already come across a few functions, namely `print()` and `type()`. We shall cover how to define your own functions in a later section.

Python functions essentially take variables or values/objects as arguments, perform a task and them return values/objects. As we have seen before the syntax of a function call is:
```
function_name(argument, argument, ...)
```

Note that some functions return a `None` type when a return value isn't necessary. For example, the `print()` function:

print_return = print('print out')

print('print function return:', print_return)

If you want to know what a particular function does or how to use it, a quick way to find out is to pull up the docstring. In an IPython environment (such as a Jupyter notebook) this can be done by typing a `?` symbol after the function name and pressing enter. For example:

print?

In a default Python shell or script you can print out the docstring using the `help()` function. For example:

help(print)

Alternatively you can refer to the [Python documentation](https://docs.python.org/3/).

Now, let's take a look at the `print()` docstring itself. The first line of the docstring shows us the function name; and the name of the function arguments and their default values (if they have). Following this is a description of what the function does. Following this is a list of optional keyword arguments.

Sometimes a docstring will also contain examples on how to use the function, though none are present in this one.

We will see more examples of how optional keyword arguments work (in particular in the Chapter discussing Matplotlib...), for now let's use one of them. Let's change the argument `sep`, which is the string inserted between the values you put into the `print()` function. As we can see, it's default value is a space `' '`. As a first example, let's change the separation to an empty string (no space):

print('There', 'are', 'no', 'spaces', sep = '')

As another example, let's put commas (`','`) in between the values:

print('There', 'are', 'commas', 'between', 'values', sep = ',')

## The `input()` Function


Another important function in the Python Standard Library is the `input()` function. This function allows us to collect user inputs from the terminal.

`input()` takes a string as an argument, this gets printed to the terminal and the script is halted until the user has entered a string and pressed enter. This string that the user has entered is returned by the `input()` function; and can, therefore, be used in the rest of the script.

As a first example, consider the following code that asks the user for their name:

user_name = input('What is your name?')

print('Hello', user_name, ', nice to meet you!')

Remember that the program will wait for your input before it continues. If you are using a Jupyter Notebook, this means that other cells from the notebook will not run until the code has been fully executed or terminated.

Now, something that is important to note is that the return value from input is a string, even when a number is typed into the terminal:

user_number = input('Enter a number: ')

print(user_number, type(user_number))

If you intend for the input to be used as a number, you must remember to convert it to one (an `int` or `float`):

user_int = int(input('Enter an integer: '))

print('Entered:', user_int, type(user_int))

user_float = float(input('Enter a number: '))

print('Entered:', user_float, type(user_float))