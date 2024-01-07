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
  * You have to use curl
  * Please test your script in the sandbox provided, using the web server running on port 5000

```
guillaume@ubuntu:~/0x10$ ./0-body_size.sh 0.0.0.0:5000
10
guillaume@ubuntu:~/0x10$ 
```
  * [0-body_size.sh](./0-body_size.sh): Bash script that sends a request to a given URL, and displays 
the size of the body of the response.
