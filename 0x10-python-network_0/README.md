# 0x10. Python - Network #0
## The Domains/Concepts covered in this project: `Bash` `Python` `Scripting` `Back-end` `API`

The project introduced me into Client URL `curl`, an open source command line tool used for 
transfering data to or from a server using any supported network protocol. I learned the major 
components of HTTP protocol and how it works, Uniform Resource Locator `URL` (webpages addresses) 
elements, reading `URL`. Making requests to servers using curl, as well as creating bash scripts 
that automate this process.

## Tasks :page_with_curl:
**0. cURL body size**

Write a Bash script that takes in a URL, sends a request to that URL, and displays the size of 
the body of the response

 * The size must be displayed in bytes
 * You have to use `curl`

Please test your script in the sandbox provided, using the web server running on port 5000

```
guillaume@ubuntu:~/0x10$ ./0-body_size.sh 0.0.0.0:5000
10
guillaume@ubuntu:~/0x10$ 
```

  * [0-body_size.sh](./0-body_size.sh): Bash script that sends a request to a given URL, and displays 
the size of the body of the response.

**1. cURL to the end**

Write a Bash script that takes in a URL, sends a `GET` request to the URL, and displays the body of the response

* Display only body of a `200` status code response
* You have to use `curl`

Please test your script in the sandbox provided, using the web server running on port 5000

```
guillaume@ubuntu:~/0x10$ ./1-body.sh 0.0.0.0:5000/route_1 ; echo ""
Route 2
guillaume@ubuntu:~/0x10$ 
```

  * [1-body.sh](./1-body.sh): Bash script that sends a GET request to a given URL, Displays only the body of `200` status 
code.

**2. cURL Method**

Write a Bash script that sends a `DELETE` request to the URL passed as the first argument and displays the body of the 
response

* You have to use `curl`

Please test your script in the sandbox provided, using the web server running on port 5000

```
guillaume@ubuntu:~/0x10$ ./2-delete.sh 0.0.0.0:5000/route_3 ; echo ""
I'm a DELETE request
guillaume@ubuntu:~/0x10$ 
```

  * [2-delete.sh](./2-delete.sh): Bash script that sends DELETE request to the given URL and displays the body of the 
response

**3. cURL only methods**

Write a Bash script that takes in a URL and displays all HTTP methods the server will accept.

* You have to use `curl`

Please test your script in the sandbox provided, using the web server running on port 5000

```
guillaume@ubuntu:~/0x10$ ./3-methods.sh 0.0.0.0:5000/route_4
OPTIONS, HEAD, PUT
guillaume@ubuntu:~/0x10$ 
```

  * [3-methods.sh](./3-methods.sh): Bash script that takes in a URL and displays all HTTP methods the server will accept.

**4. cURL headers**

Write a Bash script that takes in a URL as an argument, sends a `GET` request to the URL, and displays the body of the response

* A header variable `X-School-User-Id` must be sent with the value `98`
* You have to use `curl`

Please test your script in the sandbox provided, using the web server running on port 5000

```
guillaume@ubuntu:~/0x10$ ./4-header.sh 0.0.0.0:5000/route_5 ; echo ""
Hello School!
guillaume@ubuntu:~/0x10$ 
```

  * [4-header.sh](./4-header.sh):  Bash script that sends a GET request to the URL, and displays the custom header value.

**5. cURL POST parameters**

Write a Bash script that takes in a URL, sends a `POST` request to the passed URL, and displays the body of the response

* A variable `email` must be sent with the value `test@gmail.com`
* A variable `subject` must be sent with the value `I will always be here for PLD`
* You have to use `curl`

Please test your script in the sandbox provided, using the web server running on port 5000

```
guillaume@ubuntu:~/0x10$ ./5-post_params.sh 0.0.0.0:5000/route_6 ; echo ""
POST params:
    email: test@gmail.com
    subject: I will always be here for PLD
guillaume@ubuntu:~/0x10$ 
```

  * [5-post_params.sh](./5-post_params.sh): Bash script that sends a POST request to a URL, and displays the body of the 
response

**6. Find a peak**

**Technical interview preparation:**

* You are not allowed to google anything
* Whiteboard first

Write a function that finds **a peak** in a list of unsorted integers.

* Prototype: `def find_peak(list_of_integers):`
* You are not allowed to import any module
* Your algorithm must have the lowest complexity (hint: you don’t need to go through all numbers to find a peak)
* **6-peak.py** must contain the function
* **6-peak.txt** must contain the complexity of your algorithm: `O(log(n))`, `O(n)`, `O(nlog(n))` or `O(n2)`
* **Note:** there may be more than one peak in the list

```
guillaume@ubuntu:~/0x10$ cat 6-main.py
#!/usr/bin/python3
""" Test function find_peak """
find_peak = __import__('6-peak').find_peak

print(find_peak([1, 2, 4, 6, 3]))
print(find_peak([4, 2, 1, 2, 3, 1]))
print(find_peak([2, 2, 2]))
print(find_peak([]))
print(find_peak([-2, -4, 2, 1]))
print(find_peak([4, 2, 1, 2, 2, 2, 3, 1]))

guillaume@ubuntu:~/0x10$ ./6-main.py
6
3
2
None
2
4
guillaume@ubuntu:~/0x10$ wc -l 6-peak.txt 
2 6-peak.txt
guillaume@ubuntu:~/0x10$ 
```

  * [6-peak.py](./6-peak.py): The peak function.
  * [6-peak.txt](./6-peak.txt): The algorithm time complexity.

**7. Only status code**

Write a Bash script that sends a request to a URL passed as an argument, and displays only the status code of the response.

* You are not allowed to use any pipe, redirection, etc.
* You are not allowed to use `;` and `&&`
* You have to use `curl`

Please test your script in the sandbox provided, using the web server running on port 5000

```
guillaume@ubuntu:~/0x10$ ./100-status_code.sh 0.0.0.0:5000 ; echo ""
200
guillaume@ubuntu:~/0x10$ 
guillaume@ubuntu:~/0x10$ ./100-status_code.sh 0.0.0.0:5000/nop ; echo ""
404
guillaume@ubuntu:~/0x10$ 
```

  * [100-status_code.sh](./100-status_code.sh): Bash script that sends a request to a URL, and displays only the status code of 
the response.

**8. cURL a JSON file**

Write a Bash script that sends a JSON `POST` request to a URL passed as the first argument, and displays the body of the 
response.

* Your script must send a `POST` request with the contents of a file, passed with the filename as the second argument of 
the script, in the body of the request
* You have to use `curl`

Please test your scripts in the sandbox provided, using the web server running on port 5000

```
guillaume@ubuntu:~/0x10$ cat my_json_0
{
    "name": "John Doe",
    "age": 33
}
guillaume@ubuntu:~/0x10$ ./101-post_json.sh 0.0.0.0:5000/route_json my_json_0 ; echo ""
Valid JSON
guillaume@ubuntu:~/0x10$ 
guillaume@ubuntu:~/0x10$ cat my_json_1
I'm a JSON! really!
guillaume@ubuntu:~/0x10$ ./101-post_json.sh 0.0.0.0:5000/route_json my_json_1 ; echo ""
Not a valid JSON
guillaume@ubuntu:~/0x10$ 
guillaume@ubuntu:~/0x10$ cat my_json_2
{
    "name": "John Doe",
    "age": 33,
}
guillaume@ubuntu:~/0x10$ ./101-post_json.sh 0.0.0.0:5000/route_json my_json_2 ; echo ""
Not a valid JSON
guillaume@ubuntu:~/0x10$ 
```

  * [101-post_json.sh](./101-post_json.sh): Bash script that sends a JSON `POST` request to a URL, and displays 
the body of the response. 

**9. Catch me if you can!**

Write a Bash script that makes a request to 0.0.0.0:5000/catch_me that causes the server to respond with a message 
containing You got me!, in the body of the response.

* You have to use curl
* You are not allow to use echo, cat, etc. to display the final result

Please test your script in the sandbox provided, using the web server running on port 5000

  * [102-catch_me.sh](./102-catch_me.sh): Bash script that makes a request to 0.0.0.0:5000/catch_me that causes the server 
to respond with a message containing You got me!, in the body of the response.

## 0x10. Python - Network #0
* [0x10. Python - Network #0](https://drive.google.com/file/d/10YMNrqRCJODki06xw-MfnpuyOW0xcRwO/view?usp=drive_link)

## Additional Project Resources
* [HTTP (HyperText Transfer Protocol](https://www3.ntu.edu.sg/home/ehchua/programming/webprogramming/HTTP_Basics.html)
* [HTTP Cookies](https://developer.mozilla.org/en-US/docs/Web/HTTP/Cookies)
