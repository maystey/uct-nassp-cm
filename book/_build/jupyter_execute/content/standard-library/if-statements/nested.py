# Nested If Statements

The code blocks inside the if statement can contain any valid Python code. This means that you can also nest other if statements inside an if statement. For example:

```python
if condition1:
    code_block_1
    
    if condition2:
        code_block_2
    else:
        code_block_3

else:
    code_block_4
```

which can be illustrated with the control flow diagram:

```{figure} ./figures/if_else_nested.png
:name: fig-if-else-nested-control-flow

Control flow diagram of the pseudo code example of an if statement nested inside an if statement.
```

:::{Hint}
While there are situations which call for nested if statements, always consider whether a series of `elif`s will serve instead. Nested code blocks can make scripts harder to read.
:::

