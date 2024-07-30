file = open("15/input.txt", "r")
lines = file.readlines()

import operator

def getIndexMinPath(paths):
    #print(open)
    min = paths[0]["value"]
    smallestPath = 0

    for index, path in enumerate(paths):
        if path["value"] < min:
            min = path["value"]
            smallestPath = index

    return smallestPath

def addTuple(a, b): return tuple(map(operator.add, a, b))

def manathan(a, b): return abs(b[0] - a [0]) + abs(b[1] - a[1])

def getNode(position, nodes):
    for node in nodes:
        if node["position"] == (position[0], position[1]): return node
    return None

NEIGHBOURS = [(0, 1), (1, 0)]

LAB = list()
for line in lines:
    LAB.append([int(c) for c in line.replace('\n', '')])

#[print(line) for line in LAB]
stopPosition = (len(LAB)-1, len(LAB[0])-1)

MANATHAN = list()
for row, _ in enumerate(LAB):
    MANATHAN.append([manathan((row, column), stopPosition) for column in range(len(LAB[0]))])

#[print(line) for line in MANATHAN]

start = {"position": (0, 0), "value": MANATHAN[0][0], "parent": None}

open = [start]
closed = list()
solution = False

while not solution:

    path = open.pop(getIndexMinPath(open))
    closed.append(path)
    #print(path)
    #closed = closed[-100:]

    for neighbour in NEIGHBOURS:
        x, y = addTuple(path["position"], neighbour)

        if x >= 0 and y >=0 and x < len(LAB) and y < len(LAB[0]) and (x, y) != path["parent"] and (x, y) not in [n["position"] for n in closed]:

            node = path.copy()
            node["position"] = (x, y)
            node["value"] += LAB[x][y] + MANATHAN[x][y] - MANATHAN[path["position"][0]][path["position"][1]]
            node["parent"] = path["position"]

            nodeInOpen = getNode(node["position"], open)
            if nodeInOpen:
                if nodeInOpen["value"] > node["value"]: open.pop(open.index(nodeInOpen))
                else: pass
            else:
                nodeInClosed = getNode(node["position"], closed)
                if nodeInClosed and nodeInClosed["value"] < node["value"]: node = closed.pop(closed.index(nodeInClosed))
                open.append(node)
            
            if (x, y) == stopPosition: 
                solution = True
                print(node)

        
    


