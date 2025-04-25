'''
    Olympics Medals
    Author: Saksham Rathi
'''

from argparse import ArgumentParser as ap
import os

parser = ap()
parser.add_argument('--path', type=str, required = True)
args = parser.parse_args()

# dictionary for the data
totalData = {}

# looping through the directory
for fileName in os.listdir(args.path):
    # read the file
    filepath=os.path.join(args.path, fileName)
    file = open(filepath, "r")
    # loop through data of file and set the values for the data
    for line in file:
        data=line.split('-')
        if totalData.get(data[0]) is None:
            totalData[data[0]]=[0,0,0]
        for i in range(3):
            totalData[data[0]][i]+=int(data[i+1])
    file.close()

# sort as per gold medals and break ties lexicographically
totalData=dict(sorted(totalData.items(), key=lambda x: (-x[1][0], x[0])))
print(totalData)