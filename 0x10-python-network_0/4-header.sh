#!/bin/bash
# that takes a URL, sends a GET request with header variable
curl -sH "X-School-User-Id: 98" "$1"
