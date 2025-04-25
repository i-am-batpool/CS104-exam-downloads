n=0
array=()

for arg in $@; do #this way of looping through an arbitrarily long command line argument is really useful in cp based problems..v.imp keep in mind Abhi is making the paper lol..
    array[n]=${arg}
    ((n+=1))
done


swaps=0
swapfoun=1
while [[ ${swapfoun} -gt 0 ]]; do
    i=1
    swapfoun=0
    while [[ ${i} -lt ${n} ]]; do
        if [[ ${array[$((i-1))]} -gt ${array[$i]} ]]; then
            ((swapfoun+=1)) #don't need to put dollar in arithmetic brackets...basically dollar is used for substituting that thing with correcpnding value...do with that in mind
            tmp=${array[$i]}
            array[$i]=${array[$((i-1))]}
            array[$((i-1))]=${tmp}
        fi
        ((i+=1))
    done
    ((swaps+=${swapfoun}))
done

echo ${array[@]}
echo ${swaps}

#learnt a lot about arithmetic, looping in bash from this problem