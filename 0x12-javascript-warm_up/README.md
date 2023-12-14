# 0x12. JavaScript - Warm up

This project introduced me into JavaScript Basics. The tasks in this project
focused on writing simple scripts in JavaScript. Through this project I learned 
to work with Node js.

## Tasks :page_with_curl:

**0. First constant, first print**
  * [0-javascript_is_amazing.js](./0-javascript_is_amazing.js): JavaScript script 
that prints “JavaScript is amazing”
    * Usage: `./0-javascript_is_amazing.js`

    **Expected Output**
    ```
    Username@ubuntu:~/0x12$ ./0-javascript_is_amazing.js
    JavaScript is amazing
    Username@ubuntu:~/0x12$ 
    ```

**1. 3 languages**
  * [1-multi_languages.js](./1-multi_languages.js): JavaScript script that prints 
3 lines: `The first line: "C is fine"`, `The second line: "Python is cool"`,
`The third line: "JavaScript is amazing"`
    * Usage: `./1-multi_languages.js`

    **Expected Output**
    ```
    Username@ubuntu:~/0x12$ ./1-multi_languages.js
    C is fun
    Python is cool
    JavaScript is amazing
    Username@ubuntu:~/0x12$
    ```

**2. Arguments**
  * [2-arguments.js](./2-arguments.js): JavaScript script that prints a message depending 
of the number of arguments passed
    * Usage: `./2-arguments.js <arg1> <arg2> ...<arg n>`
    
    **Expected Output**
    ```
    Username@ubuntu:~/0x12$ ./2-arguments.js 
    No argument
    Username@ubuntu:~/0x12$ ./2-arguments.js Best
    Argument found
    Username@ubuntu:~/0x12$ ./2-arguments.js Best School
    Arguments found
    ```


**3. Value of my argument**
  * [3-value_argument.js](./3-value_argument.js): script that prints the first argument 
passed to it and “No argument” If no arguments are passed to the script
    * Usage: `./3-value_argument.js <arg1>`

    **Expected Output**
    ```
    Username@ubuntu:~/0x12$ ./3-value_argument.js
    No argument
    Username@ubuntu:~/0x12$ ./3-value_argument.js School
    School
    Username@ubuntu:~/0x12$ 
    ```

**4. Create a sentence**
  * [4-concat.js](./4-concat.js): JavaScript script that prints two arguments passed to it, 
in the following format: “ is ”
    * Usage: `./4-concat.js <arg1> <arg2`

    **Expected Output**
    ```
    Username@ubuntu:~/0x12$ ./4-concat.js c cool
    c is cool
    Username@ubuntu:~/0x12$ ./4-concat.js c 
    c is undefined
    Username@ubuntu:~/0x12$ ./4-concat.js
    undefined is undefined
    Username@ubuntu:~/0x12$
    ```

**5. An Integer**
  * [5-to_integer.js](./5-to_integer.js): JavaScript script that prints My number: 
<first argument converted in integer> if the first argument can be converted to 
an integer:
    * Usage: `./5-to_integer.js <arg>`

    **Expected Output**
    ```
    Username@ubuntu:~/0x12$ ./5-to_integer.js
    Not a number
    Username@ubuntu:~/0x12$ ./5-to_integer.js 89
    My number: 89
    Username@ubuntu:~/0x12$ ./5-to_integer.js "89"
    My number: 89
    Username@ubuntu:~/0x12$ ./5-to_integer.js School
    Not a number
    Username@ubuntu:~/0x12$
    ```

**6. Loop to languages**
  * [6-multi_languages_loop.js](./6-multi_languages_loop.js): JavaScript script that prints 3 lines: 
(like 1-multi_languages.js) but by using an array of string and a loop
    * Usage: `./6-multi_languages_loop.js`

    **Expected Output**
    ```
    Username@ubuntu:~/0x12$ ./6-multi_languages_loop.js
    C is fun
    Python is cool
    JavaScript is amazing
    Username@ubuntu:~/0x12$
    ```  

**7. I love C**
  * [7-multi_c.js](./7-multi_c.js): JavaScript script script that prints x times “C is fun”
    * Usage: `./7-multi_c.js`

    **Expected Output**
    ```
    Username@ubuntu:~/0x12$ ./6-multi_languages_loop.js 2
    C is fun
    C is fun
    Username@ubuntu:~/0x12$ ./7-multi_c.js
    Missing number of occurrences
    Username@ubuntu:~/0x12$
    ```
