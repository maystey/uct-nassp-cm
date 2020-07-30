# While Loops

For loops are useful if you know what you want to iterate over, but what if you wanted to keep looping until a certain condition is met? `while` loops are the tool for this job.

<!--- Give an example problem that isn't exactly solvable using a for loop -->

The syntax for a `while` loop is:
```
while condition:
    block of code to be repeated
```

where `condition` is/evaluates to a boolean value. The loop will keep repeating, executing the block of code indented after the `:` as long as `condition` evaluates to `True`. When `condition` evaluates to `False` the loop will no longer be repeated and control will progress to the code after the loop. <!--- is control the correct term here? --> Note that if `condition` starts as `False`, the code inside the loop will never be executed.

<!-- example -->

## Worked Example

Let's consider the following problem where we can make use of a `while` loop. Consider the recursive series: <!--- Introduce recursive series in For Loop Examples -->

$$
\begin{eqnarray}
T_n & = & T_{n-1}^{3/4} \\
T_0 & = & 100
\end{eqnarray}
$$

We want to know when this series drops below 2 (what is the first value of $n$ for which $T_n < 2$). One solution is:

T = 100 #T_0 term

n = 0

while T >= 2:
    T = T**(3/4.) #T_{n+1} term
    n += 1

print('T_n is less than 2 for n =', n)

Notice how the condition is `T >= 2` and not `T < 2`. That is because the loop continues **while** the condition is true and we want the loop to stop when `T < 2` is `True` (and the converse `T >= 2` is `False`).

## Avoiding Infinite Recursion

Something to be careful of when using `while` loops is a loop that doesn't stop looping. If `condition` never evaluates to `False`, or if you never break out of the loop in another way, control will never leave the loop. Sometimes it is useful to use a maximum number of loop iterations to avoid this:
```
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

