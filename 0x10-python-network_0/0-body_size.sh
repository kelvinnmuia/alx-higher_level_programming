#!/bin/bash
# Bash script that sends a request to a given URL, and displays the size of the body of the response
curl -s "$1" | wc -c
