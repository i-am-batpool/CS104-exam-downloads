#!/bin/bash

tr -d '\r' < $1 > remgrades.csv

while IFS=',' read -ra ar; do
    if [[ ${ar[5]} = "total-marks" ]]; then
        echo "grades" > mygrades.csv
    elif [[ ${ar[5]} -gt 85 ]]; then
        echo "AA" >> mygrades.csv
    elif [[ ${ar[5]} -gt 65 ]]; then
        echo "AB" >> mygrades.csv
    elif [[ ${ar[5]} -gt 45 ]]; then
        echo "BB" >> mygrades.csv
    elif [[ ${ar[5]} -gt 35 ]]; then
        echo "CC" >> mygrades.csv
    else
        echo "F" >> mygrades.csv
    fi
done < remgrades.csv

paste -d ',' remgrades.csv mygrades.csv > final.csv
echo "rollno,quiz1,quiz2,midsem,endsem,total-marks,grades" > ug24.csv
echo "rollno,quiz1,quiz2,midsem,endsem,total-marks,grades" > ug23.csv

grep -E "^24" final.csv > ug24tmp.csv
grep -E "^23" final.csv > ug23tmp.csv
sort -t ',' -k7 -k1,1 ug24tmp.csv >> ug24.csv
sort -t ',' -k7 -k1,1 ug23tmp.csv >> ug23.csv
rm remgrades.csv mygrades.csv final.csv ug24tmp.csv ug23tmp.csv


