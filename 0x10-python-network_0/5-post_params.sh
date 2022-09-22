#!/bin/bash                                                   
# sends a POST and variables and displayes body of response   
curl -sX POST -d 'email: test@gmail.com' -d 'subject: I will always be here for PLD' "$1"
