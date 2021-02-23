# Programming and Python in a Nutshell

In this chapter we will go over a brief overview of programming languages and Python. While important, not having a full grasp of this chapter should not hinder your ability to program using Python.

## What is a programming language?

Programming is, in essence, writing a series of instructions for the computer to execute. This is done using a programming language, which can be understood or translated to a form that can be understood by the computer.

At the lowest level the language of computers is called machine code. This language is used to communicate with the computer's CPU through binary or hexadecimal instructions.
Machine code is dependent on the computer hardware being used and is not easy to understand as humans. A step up from this is 
an assembly language, which uses some human language, but is still difficult to understand and dependent on the computer architecture {cite}`i-i-wikipedia_machine_code,i-i-wikipedia_assembly`.


Hardware dependence could be a big problem. Programs written for one computer would not necessarily work on another computer, they would have to be translated (by a human) first. To bridge this difference between hardware specifications high level programming languages were developed.

Most of the programming languages you are likely to use these days are high-level programming languages. Besides being CPU independent, these languages are designed to be readable by humans. <!--They also allow for programs to be written independently (to some degree) from the hardware in question. --> 
At some level these languages will need to be compiled (translated {cite}`i-i-wikipedia_compiler`)
to machine code {cite}`i-i-wikipedia_machine_code`.

## What is a Script?
A script is a text file containing source code (instructions for the computer) written in a programming language. Programs can be composed of a single script, or many scripts working together.

Generally scripts for a particular language are given a specific file suffix. Relevant to us, Python scripts end with a `.py`.

## Python, a Dynamic Programming Language.
Python is a high level language and thus needs to eventually be compiled down. <!-- translated into machine code. Python is a dynamic programming language. -->

Many high level programming languages' source code is compiled to machine code once, and then can be executed in this form. These are called static programming languages (C is an example). 

Dynamic programming languages are languages where operations that would normally take place at compile-time (when the code is compiled) can instead be done at run-time (when the program is executed) {cite}`i-i-mozilla_dynamic`. Python is a dynamic programming language.

When you run a python script it is compiled to byte code (if it hasn't been already). This byte code is a lower-level, platform independent representation of your source code <!--- sic --> {cite}`i-i-ned_python_interp,i-i-net-info_compiling_python`.

Byte code is similar to the CPU <!--- Necessary repeatition?--> specific assembly code, but is instead executed by software called a virtual machine (which simulates a CPU environment). {cite}`i-i-ned_python_interp`. The Python Virtual Machine is always present in the Python system and is the last step of the Python Interpreter {cite}`i-i-net-info_compiling_python`. <!-- Too much jargon invoked? -->

<!--- These virtual machines can be written in any language. {%cite ned %} -->

<!-- Briefly mention dynamic typing? -->

## References
<!-- ```{bibliography} ../../_bibliography/references.bib -->
```{bibliography}
:cited:
:style: plain
:labelprefix: I
:keyprefix: i-i-
```
