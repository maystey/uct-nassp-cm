# While Loops

While loops are used to repeat a block of code **while** a given condition is true. If this condition is false (or becomes false), the code block will not be repeated. I will refer to individual loop repetitions as **"iterations"** (the first time the code in the loop is run is the **first iteration**, the next time is the **second iteration**, etc.).

The syntax for a `while` loop is:

```python
while condition:
    code block
```

Note the use of the `while` statement and the `:` following the condition. All the code indented after the `:` is inside the loop, represented by `code block` here. The `condition` used in the loop must either evaluate to or be a boolean value.


In each loop iteration `condition` is evaluated. If `condition` is found to be **true** then the loop will go through another iteration, executing `code block`, and checking for another iteration. If `condition` is found to be **false**, then control will leave the loop and it will not undergo another iteration.

Note that if `condition` starts as false, then `code block` will never be executed.


<!-- example -->

The while loop can be illustrated with the control flow diagram:

```{figure} ./figures/while.png
:name: fig-while-control-flow

Control flow diagram of the while loop.
```

<div class="worked-example">
    <h5 class="worked-example-title"><b>Worked Example</b></h5>

Let's consider the following problem where we can make use of a `while` loop to solve the recursive series: <!--- Introduce recursive series in For Loop Examples -->

$$
\begin{eqnarray}
T_n & = & T_{n-1}^{3/4} \\
T_0 & = & 100
\end{eqnarray}
$$

Let's say we want to know when this series drops below 2 (what is the first value of $n$ for which $T_n < 2$). One solution is:

T = 100 #T_0 term

n = 0

while T >= 2:
    T = T**(3/4.) #T_{n+1} term
    n += 1

print('T_n is less than 2 for n =', n)

Notice how the condition is `T >= 2` and not `T < 2`. That is because the loop continues **while** the condition is true and we want the loop to stop when `T < 2` is `True` (and the converse `T >= 2` is `False`).

</div>

## Avoiding Infinite Recursion

Something to be careful of when using `while` loops is a loop that doesn't stop looping. If `condition` never evaluates to `False`, or if you never break out of the loop in another way, control will never leave the loop. Sometimes it is useful to use a maximum number of loop iterations to avoid this:

```python
counter = 0

while condition and counter < max_count:
    block of code
```

where `max_count` is the chosen maximum number of recursions (normally chosen as a very large number). <!--- rather give a concrete example -->

## Replacing For Loops

`while` loops can be used to replace for `loops`, for example:

## For loop
print('for loop')

for i in range(5):
    print(i)
    
## While loop
print('')
print('while loop')

i = 0

while i < 5:
    print(i)
    i+=1

As you can see the `while` loop is a bit less convenient than the `for` loop in this case. The `while` loop becomes even less convenient when looping through a collection:

string = 'a string'

## For loop
print('for loop')

for char in string:
    print(char)

## While loop
print('')
print('while loop')

index = 0

while index < len(string):
    print(string[index])
    index += 1

