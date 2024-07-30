file = open("input.txt", "r")
lines = file.readlines()

#part 1

import operator

mapD = list()
for line in lines:
    mapD.append(list())
    for d in line:
        if d != '\n': mapD[-1].append(int(d))


NEIGHBOURS = [(0, 1), (1, 0), (-1, 0), (0, -1)]

lowDigits = list()
lowDigitsPos = dict()

LENGTH, WIDTH = len(mapD), len(mapD[0])

for row, line in enumerate(mapD):
    for column, digit in enumerate(line):
        
        lowDigit = True
        for neighbour in NEIGHBOURS:
            r, c = tuple(map(operator.sub, (row, column), neighbour))
            if r >= 0 and r < LENGTH and c >= 0 and c < WIDTH:
                
                nx = mapD[r][c]
            else: nx = -1

            if nx <= digit and nx != -1: 
                lowDigit = False
                break
        
        if lowDigit: 
            lowDigits.append(digit)
            lowDigitsPos[row, column] = digit


print(sum([d+1 for d in lowDigits]))

#part 2

STOP = 9

def getNeighbours(position, alreadyVisited):
    listOfNeighboors = list()
    row, column = position[0], position[1]
    for neighbour in NEIGHBOURS:
        r, c = tuple(map(operator.sub, (row, column), neighbour))
        if r >= 0 and r < LENGTH and c >= 0 and c < WIDTH:
            if mapD[r][c] != 9 and (r,c) not in alreadyVisited: listOfNeighboors.append((r,c))
    return listOfNeighboors

allBassins = list()

for position, value in lowDigitsPos.items():
    visited = list()
    notVisited = list()
    visited.append(position)
    neighbours = getNeighbours(position, visited)

    for n in neighbours:
        notVisited.append(n)

    while len(notVisited) > 0:
        tmp = list()
        for neigbour in notVisited:
            tmp.append(getNeighbours(neigbour, visited))

        for n in notVisited:
            visited.append(n)

        notVisited = list()

        for n1 in tmp:
            for n2 in n1:
                notVisited.append(n2)
        
        
    #for v in set(visited): print(v)
    allBassins.append(len(set(visited)))

answer = 1
for i in range(3):
    maxi = max(allBassins)
    allBassins.pop(allBassins.index(maxi))
    answer *= maxi

print(answer)
        
