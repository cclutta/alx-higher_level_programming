#!/bin/bash
# that takes a URL, sends a GET request with header variable
curl -s "$1" -H "X-School-User-Id:98"
