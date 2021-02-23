# Nested Loops 

Sometimes it is necessary to nest loops. Loops in Python an be quite slow compared to other programming languages, so unnecessary loops should be avoided.

When nesting loops, it's best to think of the inner loop as a block of code. In every iteration of the outer loop, the inner loop will execute, iterating to completion.

Consider the pseudo code code example of a while loop nested in another while loop:

```python
while condition1:
    while condition2:
        code block
```

This can be illustrated with the control flow diagram:


```{figure} ./figures/while_nested.png
:name: fig-while-nested-control-flow

Control flow diagram of the nested while loop example above.
```

Let's take a closer look with a more concrete example. We will nest a for loop inside a for loop and print the iteration variables of each:

for i in range(3):
    print('Outer loop iteration:', i)
    
    for j in range(4):
        print('    Inner loop iteration:', j)

Note that you are not limited in what you nest inside loops.