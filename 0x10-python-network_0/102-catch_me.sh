#!/bin/bash                                                   
# sends a JSON POST request to a URL passed
curl -sLX OPTIONS -d "user_id=98" "0.0.0.0:5000/catch_me"
