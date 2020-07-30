# Function Arguments

You can include as many arguments as you want in your function definition. Inside the function, these arguments can be treated as variables.

<!--- The names you give these arguments can be treated as variable names inside the function. -->

def arg3(arg1, arg2, arg3):
    print(arg1)
    print(arg2)
    return arg3

arg3(1, 2, 3)

You may use variables or statements (anything that resolves to a value or object) as arguments:

var1 = 45

arg3(var1, 3*4, 7)

## Positional Arguments

The arguments defined above are called **positional arguments**. In order to set them correctly, you need to parse them in the order they are defined in the function. You must also provide a value for each argument:

arg3('a', 'b')

## Keyword Arguments

If you want to set optional arguments with a default value, you can use keyword arguments. The syntax is:
```python
def function_name(keyword_arg = default_value):
```

For example:
<!--- Should I really be using string formatting here? I guess it's as good a time as any... -->

def hello(name = 'World', time = 'today'):
    return f'Hello {name}! How are you {time}?' 

(If you are unfamiliar with f-strings `f''`, see the page on {doc}`String Formatting <../basics/string-formatting>`)

This function can be called with no arguments, in which case the default values will be used:

hello()

We can also parse the arguments like positional arguments:

hello('reader', 'feeling')

hello('reader')

Keyword arguments can be referred to by name, and out of order:

hello(time = 'this morning')

## Combining Positional and Keyword Arguments

If you define a function with both positional and keyword arguments, the positional arguments must appear **before** the keyword arguments.

For example:

def hello_hello(num, name = 'World', time = 'today', weather = 'good'):
    
    return f"Hello {num*'hello'} {name}! How are you {time}?"

Here the positional argument `num` must be provided

hello_hello()

As before, the keyword arguments can be provided like positional arguments or by name:

hello_hello(1, 'there', 'doing')

hello_hello(0, time = 'awake this early', name = 'sleepy head')