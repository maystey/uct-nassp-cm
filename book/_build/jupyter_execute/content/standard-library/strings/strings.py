# Strings

In this chapter we shall take a closer look at the string data type and some of the operations associated with it. The following page makes heavy reference to online notes by Dr. Andrew N. Harrington, [Hands-on Python 3 Tutorial](http://anh.cs.luc.edu/python/hands-on/3.1/handsonHtml/index.html) {cite}`sl-s-s-harrington-python3-tut`.

## String Literals

A string literal simply refers to how you specify that the data you are writing is a string. In Python this is achieved by placing quotes around the string contents. For example:

str_single = 'This is a string'

You are not limited to single quotes. For single line strings you can use double quotes as well:

str_double = "This is a string"

Note that these two strings are identical. <!-- Haven't introduced == or booleans yet -->

In most cases you are free to decide which quotes you want to use. The standard for Python is to use single quotes where possible, but what's most important is that your style choice is consistent within a project.

Sometimes it is advantages to use single or double quotes specifically. For example, if you want to use double quotes inside your string this will break a double quote string literal, but not a single quote one, and vice versa.

print('String using single quotes, " does not break the string.')
print("String using double quotes, ' doesn't break the string.")

For strings containing line breaks, you can use either `'''` (three single quotes) or `"""` (three double quotes) to enclose the string contents:

print(
'''String with a
line break'''
)

print(
"""Another string with a
line break"""
)

Note that white space (like indentations) will show up in these strings:

print(
    '''
    A string with
    Indented lines
    '''
)

This can give you trouble when you are defining strings in an indented code block, in these cases you may be better off using the `\n` special character, which creates new lines.

Triple quotes can be used for single line strings as well. This may come in handy when single or double quotes are no longer an option:

print('''I said: "Hello world! How's it going?" ''')

## Concatenation `+`
For strings the `+` symbol is used to concatenate two strings together. For example:

print('One string' + ' and another')

## Duplication `*`
The duplication `*` operator takes a string and an integer and repeats the string as many times as the integer value:

print('hello '*4)
print(2*'bye ')

## Indexing `[]`
Strings can be seen as a collection of characters. Each of these character has an integer index associated with it, based on it's position in the string. For example, take the string `'computer'`:

<!---
|---------|-|-|-|-|-|-|-|-|
character |c|o|m|p|u|t|e|r|
index     |0|1|2|3|4|5|6|7|
-->

<table>
    <tr>
        <td>character</td>
        <td><code>c</code></td>
        <td><code>o</code></td>
        <td><code>m</code></td>
        <td><code>p</code></td>
        <td><code>u</code></td>
        <td><code>t</code></td>
        <td><code>e</code></td>
        <td><code>r</code></td>
    </tr>
    <tr>
        <td>index</td>
        <td><code>0</code></td>
        <td><code>1</code></td>
        <td><code>2</code></td>
        <td><code>3</code></td>
        <td><code>4</code></td>
        <td><code>5</code></td>
        <td><code>6</code></td>
        <td><code>7</code></td>
    </tr>
</table>

You can access individual characters in the string by index using:
```
string[index]
```
for example:

computer_string = 'computer'

print('Index 3:', computer_string[3])

print('Index 7:', computer_string[7])

If you use an index that is too large for the given string, Python will return an error:

print('Index 11', computer_string[11])

You can find the number of characters in a string using the `len()` function:

print('There are', len(computer_string), 'characters in the string')

Notice how the length of `computer_string` is one greater than its largest index. This is because Python indexes from `0`.

Thus, if we don't know how long a string is before hand (if a variable holding a string is subject to change for instance) and we want to index the last value of the string, we could use `len() - 1` as the index:

print('The last character:', computer_string[len(computer_string) - 1])

This method works, but Python gives us a far cleaner way of doing this: using an index of `-1`. This won't work for most other programming languages. 

print('The last character:', computer_string[-1])

In general, negative indices in Python index the strings (and other objects) backwards:

print('Second last character', computer_string[-2])

print('Third last character', computer_string[-3])

Note that the index `-8` corresponds to the `0` index (`len(computer_string) - 8` is `0`) so anything less than this would be out of bounds.

## Slicing
Slicing allows us to extract segments of the string, as apposed to individual characters. The syntax for string slicing is:
```
string[start_index:stop_index]
```
where the `stop_index` is not included in the slice, rather the slice stops before this index. For example, consider the slice:

print(computer_string[2:5])

where the last character is `'u'`, but the character with index `5` is `'t'`.

If we want to take a slice from the beginning of a string we could use `0` as the `start_index`:

print(computer_string[0:3])

Alternatively if we left the `start_index` blank Python will interprate this as starting from the beginning of the string:

print(computer_string[:3])

Similarly if we wanted to take a slice up to and including the last character in the string, we can use: 

print(computer_string[3:len(computer_string)])

or simply leave the `stop_index` blank:

print(computer_string[3:])

Notice the slice above is not the same as if we used `-1` as the `stop_index`:

print(computer_string[3:-1])

even though the same rules apply as with indexing, the slice always stops **before** the `stop_index`.

We can use a third index when slicing as a step size:
```
string[start_index: stop_index: step_size]
```
For example, we can get every second character from a string using a step size of `2`:

print('Starting from 0:', computer_string[0:8:2])
print('Starting from 1:', computer_string[1:8:2])

The step size can be any integer. Note that by default it is set to 1. As another example lets print out every second character from `computer_string` starting from the first:

print(computer_string[::3])

The step size need not be positive. If a negative step size is used the string will be sliced backwards. For example if we want to print out the whole of `computer_string` backwards:

print(computer_string[::-1])

Note, when slicing with a negative step size you must ensure that `start_index` is greater than `stop_index`, otherwise your slice will be empty.

print('Empty slice:', computer_string[0:6:-1])
print('Not empty slice:', computer_string[6:0:-1])

Also notice how, in the second slice above, the `0` index character is not present. Even when slicing with a negative step size the `stop_index` is **not** included in the slice.

## References

```{bibliography} ../../../_bibliography/references.bib
:cited:
:style: plain
:labelprefix: S
:keyprefix: sl-s-s-
```


```{toctree}
:hidden:
:titlesonly:


string-formatting
```
