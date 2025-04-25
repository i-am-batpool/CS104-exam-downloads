#!/usr/bin/env bash


if [[ $# -ne 1 ]]; then
    echo "Usage: ./getEmails.sh <valid_file.txt>"
elif [[ ! -e $1 ]]; then
    echo "Usage: ./getEmails.sh <valid_file.txt>"
else
    grep -E "^[A-Z0-9a-z]+@[A-Za-z]+\.iitb\.ac\.in$" $1 > emails.txt
    sort -fr emails.txt > sortedEmails.txt
    grep -E "^[A-Z0-9a-z]+@cse\.iitb\.ac\.in$" sortedEmails.txt > cseEmails.txt
fi
