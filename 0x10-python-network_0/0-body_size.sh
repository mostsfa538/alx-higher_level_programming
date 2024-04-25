#!/usr/bin/bash
# takes in a URL, sends a request to that URL, and displays the size of the body
curl -sI $URL | grep -i Content-Length
