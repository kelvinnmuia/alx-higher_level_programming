# 0x07. Python - Test-driven development
## The Domains/Concepts covered in this project: `Python` `OOP`

The project introduced me to Python built-in objects. In this project I discovered that Python treats everything as an object, from simple data types like integers, and even modules. 

## Background Context

Now that we understand that everything is an object and have a little bit of knowledge, let’s pause and look a little bit closer at how Python works with different types of objects.

BTW, have you ever modified a variable without knowing it or wanting to? I mean:

```
>>> a = 1
>>> b = a
>>> a = 2
>>> b
1
>>>
```
 
OK. But what about this?

```
>>> l = [1, 2, 3]
>>> m = l
>>> l[0] = 'x'
>>> m
['x', 2, 3]
>>> 
```

This project is a little bit different than the usual projects. The first part is only questions about 
Python’s specificity like “What would be the result of…”. You should **read all documentation first (as usual :))**, 
then take the time to **think and brainstorm with your peers** about what you think and why. **Try to do this without 
coding anything for a few hours**.

Trying examples in the Python interpreter will give you most of the answers without having to think about it. 
**Don’t go this route**. First read, then think, then brainstorm together. Only then you can test in the interpreter.

It’s important that you truly understand the reasons behind the answers of all those tasks so that you can apply 
the same logic to other variables and other variable types.

Note that during interviews for Python positions, **you will most likely have to answer to these type of questions**.

All your answers should be only one line in a file. No space before or after the answer.


## Tasks :page_with_curl:

**0. Who am I?**

What function would you use to get the type of an object?

Write the name of the function in the file, without `()`.

  * [0-answer.txt](./0-answer.txt): Answer file for a function used to get the type of an object.

**1. Where are you?**

How do you get the variable identifier (which is the memory address in the CPython implementation)?

Write the name of the function in the file, without `()`.

  * [1-answer.txt](./1-answer.txt): Answer file for a function that gets the variable identifier in python.

**2. Right count**

In the following code, do `a` and `b` point to the same object? Answer with `Yes` or `No`.

```
>>> a = 89
>>> b = 100
```

  * [2-answer.txt](./2-answer.txt): Task 3 answer file.
