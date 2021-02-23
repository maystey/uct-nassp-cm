# Breaking Out of Loops

Sometimes you want to exit a loop before it's finished, or skip the remainder of a loop and move to the next iteration. To do this you can use the `break` and `continue` statements respectively.

## `break`

The `break` statement causes control to exit the loop it is situated in. For example, if we were to put a break directly in the loop's code block:

for i in range(5):
    print(i)
    break

You can see that only the first loop iteration completed.

Let's illustrate this with a pseudo code example:

```python
while condition1:
    code_block_1
    
    if condition2:
        break
    
    code_block_2
```

In the example above `condition2` is evaluated as **true** in a loop iteration, then control will exit the loop before executing `code_block_2` for that iteration.

Illustrating this using a control flow diagram:

```{figure} ./figures/while_break.png
:name: fig-while-control-flow-break

Control flow diagram of the break example above.
```

Let's consider a similar script that loops through a sequence of numbers and stops when it reaches `5`:

for i in range(10):
    print(i)
    
    if i == 5:
        break
    
    print('next iteration')

As you can see in the example above the loop terminated before it finished iterating through `range(10)`. When `i` had a value of `5` the `break` statement was called, exiting from the loop.

Note that it doesn't matter that the `break` is nested in an if statement, it will always make control exit the nearest loop that it is nested in.

The `break` statement exits the first loop that it's nested in. For example, if we had multiple nested loops:

for i in range(3):
    print('Loop1', i)
    for j in range(3):
        print('    Loop2', j)
        
        if j == 1:
            break

We can see that the outer loop (Loop1) iterated through all of `range(3)`, while Loop2 terminates before it can reach the last iteration.

<!---
If we put another loop inside Loop2, the `break` statement would not affect it:
-->

<!---
for i in range(3):
    print('Loop1', i)
    for j in range(3):
        print('    Loop2', j)
        
        for k in range(3):
            print('        Loop3', k)
        
        if j == 1:
            break
-->

## `continue`

If you want to end the current loop iteration, but you don't want to break out of the loop, you can use the `continue` statement.

Consider the pseudo code example:

```python
while condition1:
    code_block_1
    
    if condition2:
        continue
       
    code_block_2
```

Here if `condition2` is found to be **true** in a loop iteration, the `continue` statement will cause control to move directly to the next loop iteration, skipping `code_block_2` for that iteration.

Illustrating this example in a control flow diagram:

```{figure} ./figures/while_continue.png
:name: fig-while-control-flow-continue

Control flow diagram of the continue example above.
```

Let's look at real code example:

for i in range(10):
    if i == 5:
        continue
    print(i)

As you can see in the example above, `5` is not printed as the `continue` statement has caused control to 'skip' the print statement.