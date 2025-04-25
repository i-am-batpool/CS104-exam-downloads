BEGIN{
    FS=",";
    OFS=",";
}

{
    if (NR==1){
        printf "%s,Amount\n", $0;
    }
    else{
        split($2, dur, " "); #split gives 1 indexed array apparently
        amoun=$3;
        for (i=0; i<dur[1]; i++){
            amoun=amoun*$5;
        }
        printf "%s,%d\n", $0, amoun;
    }
}