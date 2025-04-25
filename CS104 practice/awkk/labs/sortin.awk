BEGIN{
    FS=",";
    OS=",";
    total=0;
}

{
    if (NR>1){
        total+=$6;
        type[$4]+=$6;
    }
}

END{
    printf "Total:%d\n", total;
    n=0;
    for (types in type){
        sortar[n]=types;
        n++;
    }
    for (i=0; i<n; i++){
        for (j=(i+1); j<n; j++){
            if (type[sortar[i]]<=type[sortar[j]]){
                tmp=sortar[j];
                sortar[j]=sortar[i];
                sortar[i]=tmp;
            }
        }
    }
    for (i=0; i<n; i++){
        printf "%s:%d\n", sortar[i], ((100*type[sortar[i]])/total);
    }
}