#!/bin/bash

for file in $(ls *.out); do
    echo $* >> ${file}
done