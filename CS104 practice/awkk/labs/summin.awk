BEGIN{
    FS=",";
    OFS=",";
}

{
    print $0
    if (NR>1){
        sum+=$4;
        field[$3]+=$4;
    }
}

END{
    print "====="
    printf "Net : %i\n", sum;
    n=0
    for (area in field){
        fields[n]=area;
        n++;
    }
    for (i=0; i<n; i++){
        for (j=(i+1); j<n; j++){
            if (fields[i]>fields[j]){
                tmp=fields[j];
                fields[j]=fields[i];
                fields[i]=tmp;
            }
        }
    }
    for (i=0; i<n; i++){
        printf "%s : %i\n", fields[i], field[fields[i]];
    }
}