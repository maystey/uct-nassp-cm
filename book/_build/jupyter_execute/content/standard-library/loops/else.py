# Else Statement and Loops

You can use an else statement after a `for` or `while` loop. The code in this `else` statement is executed if the loop completed without being terminated.

for i in range(3):
    print(i)
else:
    print('Loop completed')

The only time the `else` part will not be executed is if you `break` out of a loop:

for i in range(5):
    print(i)
    
    if i == 3:
        break
else:
    print('Loop completed')

<div class="worked-example">
    <h5 class="worked-example-title"><b>Worked Example</b></h5>

A common use for this structure is if you're searching for an object. Consider this example where we are trying to find a `'fish'` in a list:

animals = ['zebra', 'cow', 'crow', 'eel']

for animal in animals:
    if animal == 'fish':
        print('We caught a fish!')
        break
else:
    print('We did not catch a fish.')

animals = ['human', 'bear', 'fish', 'squid', 'crab']

for animal in animals:
    if animal == 'fish':
        print('We caught a fish!')
        break
else:
    print('We did not catch a fish.')

Of course, finding a particular object in a list is quicker and simpler using:

animals = animals = ['human', 'bear', 'fish', 'squid', 'crab']

if 'fish' in animals:
    print('We caught a fish!')
else:
    print('We did not catch a fish.')

but for more complex procedures this may not be an option.

</div>