declare -A count
while IFS= read -r line || [[ -n "$line" ]]; do #this code confirms that all lines are read, in usual code, if there is no endl in last line then last line won't be processed
    ar=($line)
    for i in "${ar[@]}"; do #looping through arrays
        ((count[$i]+=1))
    done
done < $1


for key in "${!count[@]}"; do #looping through keys in arrays
    echo "${key}:${count[${key}]}"
done