line_pattern='\[(.*)\] \[(notice|error)\] (.*)'
event_match() {
    events=()
    events[0]='jk2_init\(\) Found child [0-9]+ in scoreboard slot [0-9]+'
    events[1]='workerEnv.init\(\) ok \S+'
    events[2]='mod_jk child workerEnv in error state [0-9]+'
    events[3]='\[client \S+\] Directory index forbidden by rule: \S+'
    events[4]="jk2_init\(\) Can't find child [0-9]+ in scoreboard"
    events[5]='mod_jk child init \S+ \S+'
    for i in {0..5}; do
        if [[ $1 =~ ${events[$i]} ]]; then
            echo "E$((1+$i))"
            return 0
        fi
    done
    echo ""
    return 1
}
declare -A event_template
event_template["E1"]="jk2_init() Found child <*> in scoreboard slot <*>"
event_template["E2"]="workerEnv.init() ok <*>"
event_template["E3"]="mod_jk child workerEnv in error state <*>"
event_template["E4"]="[client <*>] Directory index forbidden by rule: <*>"
event_template["E5"]="jk2_init() Can't find child <*> in scoreboard"
event_template["E6"]="mod_jk child init <*> <*>"
if [[ -e output.csv ]]; then
    rm output.csv
    rm epochtimes
fi
echo "LineId,Time,Level,Content,EventId,EventTemplate" >> output.csv
counter=1
epochstarttime=$(date -d "$2" +%s)
epochendtime=$(date -d "$3" +%s)
while read -r line; do
    line=${line//$'\r'/}
    if [[ $line =~ $line_pattern ]]; then
        timestamp=${BASH_REMATCH[1]}
        level=${BASH_REMATCH[2]}
        content=${BASH_REMATCH[3]}
        event=$(event_match "$content") 
        if [[ $? -eq 1 ]]; then 
            event=""
            template=""
        else
            template=${event_template[$event]}
        fi
        epochtime=$(date -d "${timestamp}" +%s)
        if [[ $epochstarttime -lt $epochtime && $epochtime -lt $epochendtime ]]; then
            echo "${counter},${timestamp},${level},${content},${event},${template}" >> output.csv
            echo "${epochtime},${timestamp}" >> epochtimes
            (( counter++ ))
        fi
    else 
        if [[ -e output.csv ]]; then
            rm output.csv
            rm epochtimes
        fi
        exit 1
        break
    fi
done < $1

