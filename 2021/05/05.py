file = open("input.txt", "r")
lines = file.readlines()

import numpy as np
from numpy import core

coordinates = list()

for line in lines:
    convertedLine = line.replace("->", ",").replace(" ", "")
    coordinates.append([int(n) for n in convertedLine.split(",")])

##Part 2

maxR, maxC = 0,0
for index in range(len(coordinates)-1, 0, -1):
    if max(coordinates[index][0], coordinates[index][2]) > maxC: maxC = max(coordinates[index][0], coordinates[index][2])
    if max(coordinates[index][1], coordinates[index][3]) > maxR: maxR = max(coordinates[index][1], coordinates[index][3])

maxR += 1
maxC += 1
mapP = np.array([[0]*maxR]*maxC)
for coor in coordinates:
    if coor[0] == coor[2]:
        if coor[1] < coor[3]: x, y = 1, 3
        else: x, y = 3, 1

        for trace in range(coor[x], coor[y]+1):
            mapP[trace][coor[0]] += 1

    elif coor[1] == coor[3]:
        if coor[0] < coor[2]: x, y = 0, 2
        else: x, y = 2, 0
        for trace in range(coor[x], coor[y]+1):
            mapP[coor[1]][trace] += 1
        
    else:
        currentPos = [coor[0], coor[1]]
        mapP[currentPos[1], currentPos[0]] += 1
        while currentPos[0] != coor[2] and currentPos[1] != coor[3]:
            
            if currentPos[0] < coor[2]:
                currentPos[0] += 1
                if currentPos[1] < coor[3]: currentPos[1] += 1
                else: currentPos[1] -= 1
            else:
                currentPos[0] -= 1
                if currentPos[1] < coor[3]: currentPos[1] += 1
                else: currentPos[1] -= 1
            mapP[currentPos[1], currentPos[0]] += 1

unique, counts = np.unique(mapP, return_counts=True)
count = dict(zip(unique, counts))

answer = 0
for key, value in count.items():
    if key >= 2: answer += value
print(mapP)
print(answer)

##Part 1

maxR, maxC = 0,0
for index in range(len(coordinates)-1, 0, -1):
    if not(coordinates[index][0] == coordinates[index][2] or coordinates[index][1] == coordinates[index][3]):
        coordinates.pop(index)
    else:
        if max(coordinates[index][0], coordinates[index][2]) > maxC: maxC = max(coordinates[index][0], coordinates[index][2])
        if max(coordinates[index][1], coordinates[index][3]) > maxR: maxR = max(coordinates[index][1], coordinates[index][3])

maxR += 1
maxC += 1
mapP = np.array([[0]*maxR]*maxC)
for coor in coordinates:
    if coor[0] == coor[2]:
        if coor[1] < coor[3]: x, y = 1, 3
        else: x, y = 3, 1

        for trace in range(coor[x], coor[y]+1):
            mapP[trace][coor[0]] += 1

    else:
        if coor[0] < coor[2]: x, y = 0, 2
        else: x, y = 2, 0
        for trace in range(coor[x], coor[y]+1):
            mapP[coor[1]][trace] += 1

unique, counts = np.unique(mapP, return_counts=True)
count = dict(zip(unique, counts))

answer = 0
for key, value in count.items():
    if key >= 2: answer += value

print(answer)
