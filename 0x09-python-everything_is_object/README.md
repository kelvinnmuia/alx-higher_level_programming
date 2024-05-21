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

**3. Right count =**

In the following code, do `a` and `b` point to the same object? Answer with `Yes` or `No`.

```
>>> a = 89
>>> b = 89
```

  * [3-answer.txt](./3-answer.txt): Task 4 answer file.

**4. Right count =**

In the following code, do `a` and `b` point to the same object? Answer with `Yes` or `No`.

```
>>> a = 89
>>> b = a
```

  * [4-answer.txt](./4-answer.txt): Task 5 answer file.

**5. Right count =+**

In the following code, do a and b point to the same object? Answer with Yes or No.

```
>>> a = 89
>>> b = a + 1
```

  * [5-answer.txt](./5-answer.txt): Task 6 answer file.

**6. Is equal**

What do these 3 lines print?

```
>>> s1 = "Best School"
>>> s2 = s1
>>> print(s1 == s2)
```

  * [6-answer.txt](./6-answer.txt): Task 7 answer file.

**7. Is the same**

What do these 3 lines print?

```
>>> s1 = "Best"
>>> s2 = s1
>>> print(s1 is s2)
```

  * [7-answer.txt](./7-answer.txt): Task 8 answer file.

**8. Is really equal**

What do these 3 lines print?

```
>>> s1 = "Best School"
>>> s2 = "Best School"
>>> print(s1 == s2)
```

  * [8-answer.txt](./8-answer.txt): Task 9 answer file.

**9. Is really the same**

What do these 3 lines print?

```
>>> s1 = "Best School"
>>> s2 = "Best School"
>>> print(s1 is s2)
```

  * [9-answer.txt](./9-answer.txt): Task 10 answer file.

**10. And with a list, is it equal**

What do these 3 lines print?

```
>>> l1 = [1, 2, 3]
>>> l2 = [1, 2, 3] 
>>> print(l1 == l2)
```

  * [10-answer.txt](./10-answer.txt): Task 11 answer file.

**11. And with a list, is it the same**

What do these 3 lines print?

```
>>> l1 = [1, 2, 3]
>>> l2 = [1, 2, 3] 
>>> print(l1 is l2)
```

  * [11-answer.txt](./11-answer.txt): Task 12 answer file.

**12. And with a list, is it really equal**

What do these 3 lines print?

```
>>> l1 = [1, 2, 3]
>>> l2 = l1
>>> print(l1 == l2)
```

  * [12-answer.txt](./12-answer.txt): Task 13 answer file.

**13. And with a list, is it really the same**

What do these 3 lines print?

```
>>> l1 = [1, 2, 3]
>>> l2 = l1
>>> print(l1 is l2)
```

  * [13-answer.txt](./13-answer.txt): Task 14 answer file.

**14. List append**

What does this script print?

```
l1 = [1, 2, 3]
l2 = l1
l1.append(4)
print(l2)
```

  * [14-answer.txt](./14-answer.txt): Task 15 answer file.

**15. List add**

What does this script print?

```
l1 = [1, 2, 3]
l2 = l1
l1 = l1 + [4]
print(l2)
```

  * [15-answer.txt](./15-answer.txt): Task 16 answer file.

**16. Integer incrementation**

What does this script print?

```
def increment(n):
    n += 1

a = 1
increment(a)
print(a)
```

  * [16-answer.txt](./16-answer.txt): Task 17 answer file.

**17. List incrementation**

What does this script print?

```
def increment(n):
    n.append(4)

l = [1, 2, 3]
increment(l)
print(l)
```

  * [17-answer.txt](./17-answer.txt): Task 18 answer file.

**18. List assignation**

What does this script print?

```
def assign_value(n, v):
    n = v

l1 = [1, 2, 3]
l2 = [4, 5, 6]
assign_value(l1, l2)
print(l1)
```

  * [18-answer.txt](./18-answer.txt): Task 19 answer file.

**19. Copy a list object**

Write a function def `copy_list(l):` that returns a **copy** of a list.

  * The input list can contain any type of objects
  * Your file should be maximum 3-line long (no documentation needed)
  * You are not allowed to import any module

```
guillaume@ubuntu:~/0x09$ cat 19-main.py
#!/usr/bin/python3
copy_list = __import__('19-copy_list').copy_list

my_list = [1, 2, 3]
print(my_list)

new_list = copy_list(my_list)

print(my_list)
print(new_list)

print(new_list == my_list)
print(new_list is my_list)

guillaume@ubuntu:~/0x09$ ./19-main.py
[1, 2, 3]
[1, 2, 3]
[1, 2, 3]
True
False
guillaume@ubuntu:~/0x09$ wc -l 19-copy_list.py 
3 19-copy_list.py
guillaume@ubuntu:~/0x09$ 
```

  * [19-copy_list.py](./19-copy_list.py): Task 20 answer file.

**20. Tuple or not?**

```
a = ()
```

Is `a` a tuple? Answer with `Yes` or `No`.

  * [20-answer.txt](./20-answer.txt): Task 21 answer file.

**21. Tuple or not?**

```
21. Tuple or not?
```

Is `a` a tuple? Answer with `Yes` or `No`.

  * [21-answer.txt](./21-answer.txt): Task 22 answer file.

**22. Tuple or not?**

```
a = (1)
```

Is `a` a tuple? Answer with `Yes` or `No`.

  * [22-answer.txt](./22-answer.txt): Task 23 answer file.

**23. Tuple or not?**

```
a = (1, )
```

Is `a` a tuple? Answer with `Yes` or `No`.

  * [23-answer.txt](./23-answer.txt): Task 24 answer file.

**24. Who I am?**

What does this script print?

```
a = (1)
b = (1)
a is b
```

  * [24-answer.txt](./24-answer.txt): Task 25 answer file.

**25. Tuple or not**

What does this script print?

```
a = (1, 2)
b = (1, 2)
a is b
```

  * [25-answer.txt](./25-answer.txt): Task 26 answer file.

**26. Empty is not empty**

What does this script print?

```
a = ()
b = ()
a is b
```

  * [26-answer.txt](./26-answer.txt): Task 27 answer file.

**27. Still the same?**

```
>>> id(a)
139926795932424
>>> a
[1, 2, 3, 4]
>>> a = a + [5]
>>> id(a)
```

Will the last line of this script print `139926795932424`? Answer with `Yes` or `No`.

  * [27-answer.txt](./27-answer.txt): Task 28 answer file.

**28. Same or not?**

```
>>> a
[1, 2, 3]
>>> id (a)
139926795932424
>>> a += [4]
>>> id(a)
```

Will the last line of this script print `139926795932424`? Answer with `Yes` or `No`.

  * [28-answer.txt](./28-answer.txt): Task 29 answer file.

**29. #pythonic**

Write a function `magic_string()` that returns a string “BestSchool” n times the number of the iteration (see code):

  * Format: see example
  * Your file should be maximum 4-line long (no documentation needed)
  * You are not allowed to import any module

```
guillaume@ubuntu:~/0x09$ cat 100-main.py
#!/usr/bin/python3
magic_string = __import__('100-magic_string').magic_string

for i in range(10):
    print(magic_string())

guillaume@ubuntu:~/0x09$ ./100-main.py | cat -e
BestSchool$
BestSchool, BestSchool$
BestSchool, BestSchool, BestSchool$
BestSchool, BestSchool, BestSchool, BestSchool$
BestSchool, BestSchool, BestSchool, BestSchool, BestSchool$
BestSchool, BestSchool, BestSchool, BestSchool, BestSchool, BestSchool$
BestSchool, BestSchool, BestSchool, BestSchool, BestSchool, BestSchool, BestSchool$
BestSchool, BestSchool, BestSchool, BestSchool, BestSchool, BestSchool, BestSchool, BestSchool$
BestSchool, BestSchool, BestSchool, BestSchool, BestSchool, BestSchool, BestSchool, BestSchool, BestSchool$
BestSchool, BestSchool, BestSchool, BestSchool, BestSchool, BestSchool, BestSchool, BestSchool, BestSchool, BestSchool$
guillaume@ubuntu:~/0x09$ wc -l 100-magic_string.py 
4 100-magic_string.py
guillaume@ubuntu:~/0x09$ 
```

  * [100-magic_string.py](./100-magic_string.py): Python function that returns a string "BestSchool" n times the number of the iteration.

**30. Low memory cost**

Write a class `LockedClass` with no class or object attribute, that prevents the user from dynamically creating new instance 
attributes, except if the new instance attribute is called `first_name`.

  * You are not allowed to import any module

```
guillaume@ubuntu:~/0x09$ cat 101-main.py
#!/usr/bin/python3
LockedClass = __import__('101-locked_class').LockedClass

lc = LockedClass()
lc.first_name = "John"
try:
    lc.last_name = "Snow"
except Exception as e:
    print("[{}] {}".format(e.__class__.__name__, e))

guillaume@ubuntu:~/0x09$ ./101-main.py
[AttributeError] 'LockedClass' object has no attribute 'last_name'
guillaume@ubuntu:~/0x09$ 
```

  * [101-locked_class.py](./101-locked_class.py): Python locked class that prevents users from dynamically 
creating new instance attribute except if the new instance is called first_name.

**31. int 1/3**

```
julien@ubuntu:/python3$ cat int.py 
a = 1
b = 1
julien@ubuntu:/python3$ 
```

Assuming we are using a CPython implementation of Python3 with default options/configuration:

  * How many int objects are created by the execution of the first line of the script? (`103-line1.txt`)
  * How many int objects are created by the execution of the second line of the script (`103-line2.txt`)

  * [103-line1.txt](./103-line1.txt)
  * [103-line2.txt](./103-line2.txt)

