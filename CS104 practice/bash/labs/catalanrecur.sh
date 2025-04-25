n=$1

recur() {
    if [[ $1 -eq 0 || $1 -eq 1 ]]; then
        echo 1
    else
        sum=0
        i=0
        while [[ ${i} -lt $1 ]]; do
            a=$(recur "$i")
            b=$(recur "$(($1-i-1))")
            ((sum+=a*b))
            ((i+=1))
        done
        echo ${sum}
    fi
}

echo $(recur "$n")