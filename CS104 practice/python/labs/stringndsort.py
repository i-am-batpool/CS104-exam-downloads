mylist=[]
with open("buggy_marksheet.txt", "r") as file:
    for line in file:
        ar=line.strip().split(" ")
        mylist.append(ar)

sortlist=list(sorted(mylist, key=lambda x: (x[0].split('_')[2], -int(x[1])))) #be careful here that we can use - only on int and we need to typecast in python unlike bash

for element in sortlist:
    print(f"{element[0]} {element[1]}")
