#!/usr/bin/env bash




query1() {
    maxval=0
    maxcolor="NRF"
    if [[ $# -eq 2 ]]; then
        while IFS=',' read -ra ar; do
            if [[ ${ar[4]} -ge ${maxval} ]]; then
                maxval=${ar[4]}
                maxcolor=${ar[3]}
            fi
        done < $1
        echo ${maxcolor}
    elif [[ $3 = "type" ]]; then
        while IFS=',' read -ra ar; do
            if [[ ${ar[0]} = $4 && ${ar[4]} -ge ${maxval} ]]; then
                maxval=${ar[4]}
                maxcolor=${ar[3]}
            fi
        done < $1
        echo ${maxcolor}
    elif [[ $3 = "year" ]]; then
        while IFS=',' read -ra ar; do
            if [[ ${ar[2]} -eq $4 && ${ar[4]} -ge ${maxval} ]]; then
                maxval=${ar[4]}
                maxcolor=${ar[3]}
            fi
        done < $1
        echo ${maxcolor}
    elif [[ $3 = "price" ]]; then
        while IFS=',' read -ra ar; do
            if [[ ${ar[1]} -eq $4 && ${ar[4]} -ge ${maxval} ]]; then
                maxval=${ar[4]}
                maxcolor=${ar[3]}
            fi
        done < $1
        echo ${maxcolor}
    fi
}

query2() {
    amount=0
    if [[ $# -eq 2 ]]; then
        while IFS=',' read -ra ar; do
            add=$((${ar[1]}*${ar[4]}))
            amount=$((${amount}+${add}))
        done < $1
        echo ${amount}
    elif [[ $# -eq 3 ]]; then
        while IFS=',' read -ra ar; do
            if [[ ${ar[1]} -gt $3 ]]; then
                add=$((${ar[1]}*${ar[4]}))
                amount=$((${amount}+${add}))
            fi
        done < $1
        echo ${amount}
    elif [[ $# -eq 4 ]]; then
        while IFS=',' read -ra ar; do
            if [[ ${ar[1]} -gt $3 && $4 = ${ar[3]} ]]; then
                add=$((${ar[1]}*${ar[4]}))
                amount=$((${amount}+${add}))
            fi
        done < $1
        echo ${amount}
    fi
}

if [[ $# -eq 0 ]]; then
    echo "ERROR: No arguments provided"
    exit 1
elif [[ $# -eq 1 ]]; then
    echo "ERROR: No query type provided"
    exit 1
elif [[ ! -e $1 ]]; then
    echo "ERROR: File does not exist"
    exit 1
elif [[ $2 -ne 1 && $2 -ne 2 ]]; then
    echo "ERROR: Invalid query type"
    exit 1
fi #error handling complete
if [[ $2 -eq 1 ]]; then
    echo $(query1 "$@")
elif [[ $2 -eq 2 ]]; then
    echo $(query2 "$@")
fi