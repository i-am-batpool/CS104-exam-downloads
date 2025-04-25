#!/bin/bash

while read -r line; do
    ar=($line)
    echo ${ar[0]}
    if [[ -e ${ar[0]}.pdf ]]; then
        mv ${ar[0]}.pdf ${ar[0]}_${ar[1]}.pdf
    fi
done < $1