#!/bin/bash
mkdir output
pattern='(.*).sh'
for file in $(ls *.sh); do
    if [[ ${file} =~ $pattern ]]; then
        name=${BASH_REMATCH[1]}
        cp ${file} output/${name}_today.sh
    fi
done


