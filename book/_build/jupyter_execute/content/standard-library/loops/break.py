# Breaking Out of Loops

Sometimes you want to exit a loop before it's finished, or skip the remainder of a loop and move to the next iteration. To do this you can use the `break` and `continue` statements respectively.

## `break`

 As a first example, consider:

for i in range(10):
    print(i)
    
    if i == 5:
        break

where you can see that the loop terminated before it was finished iterating through `range(10)`. The `break` may be inside the `if` statement, but it's the loop that it affects.  

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

for i in range(10):
    if i == 5:
        continue
    print(i)

As you can see in the example above, `5` is not printed.

