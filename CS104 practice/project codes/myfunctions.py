import subprocess
import numpy as np
from matplotlib import pyplot as plt

def maketable(input, start_time, end_time):
    try:
        subprocess.run(['bash', 'parse.sh', input, start_time, end_time], check=True)
        data=[]
        with open("output.csv", "r") as file:
            for line in file:
                #line.strip() #otherwise \n were coming
                data.append(line.split(','))
        return data
    except subprocess.CalledProcessError:
        return []

def levelstate(data):
    levels=np.array([0,0])
    mylabels=["Notice","Error"]
    for row in data[1:]:
        if (row[2]=="notice"):
            levels[0]+=1
        elif (row[2]=="error"):
            levels[1]+=1
    plt.figure(figsize=(6.4, 4.8)) 
    plt.pie(levels, labels=mylabels, autopct='%1.1f%%')
    plt.title('Level state distribution')
    plt.legend()
    plt.savefig('static/plots/levelstate.png')
    plt.savefig('static/plots/levelstate.pdf')
    plt.clf()
    return

def eventcode(data):
    event_occurences=np.zeros(7)
    mylabels=["E1","E2","E3","E4","E5","E6", "Other"]
    for row in data[1:]:
        if (row[4]=="E1"):
            event_occurences[0]+=1
        elif (row[4]=="E2"):
            event_occurences[1]+=1
        elif (row[4]=="E3"):
            event_occurences[2]+=1
        elif (row[4]=="E4"):
            event_occurences[3]+=1
        elif (row[4]=="E5"):
            event_occurences[4]+=1
        elif (row[4]=="E6"):
            event_occurences[5]+=1
        else:
            event_occurences[6]+=1
    plt.figure(figsize=(6.4, 4.8)) 
    plt.bar(mylabels, event_occurences, color='b', width=0.5) 
    plt.title("Event code distribution")
    plt.legend()
    plt.savefig('static/plots/eventcode.png')
    plt.savefig('static/plots/eventcode.pdf')
    plt.clf()
    return

    
def eventtime():
    epochtime=[]
    timestamps=[]
    with open("epochtimes", "r") as file:
        for line in file:
            #line.strip() #otherwise \n were coming
            epochtime.append(int(line.split(',')[0]))
            timestamps.append(line.split(',')[1])
    epochtime=np.array(epochtime)
    freqtime=np.unique(epochtime, return_counts=True)
    timestamps=np.array(timestamps)
    plt.figure(figsize=(14, 8)) 
    plt.plot(freqtime[0], freqtime[1])
    tick_indices=[]
    for i in range(5):
        val=((4-i)*epochtime[0]+i*epochtime[-1])//4
        indx=np.searchsorted(epochtime,val, side="left")
        if indx!=(len(epochtime)-1):
            if (abs(epochtime[indx+1]-val)<abs(epochtime[indx]-val)):
                indx+=1
        tick_indices.append(indx)
    plt.xticks(ticks=epochtime[tick_indices], labels=timestamps[tick_indices], rotation=15)
    plt.title("Events with time")
    plt.xlabel("Time")
    plt.ylabel("Number of events")
    plt.savefig('static/plots/eventtime.png')
    plt.savefig('static/plots/eventtime.pdf')
    plt.clf()
    return
    