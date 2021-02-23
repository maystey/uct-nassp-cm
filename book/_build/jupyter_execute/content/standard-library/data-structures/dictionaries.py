# Dictionaries

So far we have only looked at sequence data structures, where elements are referred to by their position in the sequence. In dictionaries, however, the objects stored are referred to by a key. Keys must be an immutable type, for example a string, number or tuple containing only immutable types.

You can create a dictionary using the `dict` function; and assign values using the subscript notation: <!--- Look this up. Introduce earlier. Make a glossary! -->
```
dictionary[key] = value
```

d = dict()

d[1] = 'a'
d['lst'] = [1, 2, 3]

print(d)

You can also access dictionary values using the subscript notation:

print(d[1])

An alternative way to initialize a dictionary with key-value pairs is:
```
{key1 : value1, key2 : value2}
```
much like it appears in the print output:

d = {1 : 'a',  'lst' : [1, 2, 3]}

print(d)

Note that using a key that doesn't exist in the dictionary will give you a `KeyError`:

print(d[2])

<!--- Add section on get -->

## Listing the Keys Which Exist

Often you will want a list of the keys which a dictionary has. For this you can use the `dict.keys()` method:

print(d.keys())

One use for this is to check if a dictionary has the key you're looking for if you want to avoid an error:

if 2 in d.keys():
    print(d[2])
else:
    print(2, 'not a key in d')