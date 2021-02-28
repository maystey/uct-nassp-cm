# Logical Operators

Logical operators act on booleans and return booleans. The logical operators are `and`, `or` and `not`. 

<!--- Maybe mention bitwise operations? Python doesn't expose these in the Standard Library afaik, but just so that they are aware of the difference -->

## Logical `and`

This acts on 2 booleans. It returns `True` if both booleans are `True` and `False` otherwise. For example:

print('True and True is', True and True)
print('True and False is', True and False)
print('False and True is', False and True)
print('False and False is', False and False)

<!-- Add examples with comparison operators? Or do it all later? -->

## Logical `or`

This operator acts on 2 booleans. It returns `True` if at least one of the booleans is `True` and `False` if both booleans are `False`. For example:

print('True or True is', True or True)
print('True or False is', True or False)
print('False or True is', False or True)
print('False or False is', False or False)

## Logical `not`
This operator acts on a single boolean. It returns the opposite of the boolean:

print('not True is', not True)
print('not False is', not False)

## Combining Logical Operations
Although logical operations only act on up to 2 booleans at a time, just like arithmetic operators they can be combined in a single statement. For example:

print('True and False or True is ', True and False or True)
print('True or True and False is', True or True and False)
print('not True or True and False', not True or True and False)

<!---The order in which the logical operators are executed if no brackets are used is: `not`, `and`, `or`.

If you want to control the order in which the operators execute you can use brackets: --->

Although it isn't important for the cases above, if you need to ensure a specific order for the operations you can use brackets to group them.