file = open("input.txt", "r")
lines = file.readlines()

import operator

NEIGHBOURS = [(0, 1), (1, 0), (-1, 0), (0, -1), (1, 1), (1, -1), (-1, 1), (-1, -1)]
TURNS = 100
flash_counter = 0
turn_flash_counter = 0

def addTuples(a, b): return tuple(map(operator.add, a, b))

class Octopus:

    def __init__(self, energy) -> None:
        self.energy = energy
        self.neighboors = list()
        self.alreadyFlashed = False

    def addNeighboor(self,neighboor):
        self.neighboors.append(neighboor)

    def incrementEnergy(self):
        global flash_counter, turn_flash_counter
        if not self.alreadyFlashed: 
            self.energy += 1
            if self.energy > 9: 
                flash_counter += 1
                turn_flash_counter += 1
                self.energy = 0
                self.alreadyFlashed = True
                self.flashNeighboors()

    def flashNeighboors(self):
        for neighboor in self.neighboors: neighboor.incrementEnergy()

    def newTurn(self):
        self.alreadyFlashed = False

    ## debug
    def howManyNeighboors(self): return len(self.neighboors)
    def getEnergy(self): return self.energy
    

board = list()
for line in lines:
    board.append(list())
    for energy in line:
        if energy != '\n': board[-1].append(Octopus(int(energy)))

allOctopus = list()
for row, line in enumerate(board):
    for column, octopus in enumerate(line):
        allOctopus.append(octopus)
        for neighboor in NEIGHBOURS:
            x, y = tuple(map(operator.add, (row, column), neighboor))
            if x >= 0 and y >= 0:
                try: octopus.addNeighboor(board[x][y])
                except: pass

"""
for turn in range(TURNS):
    for octopus in allOctopus: octopus.incrementEnergy()
    for octopus in allOctopus: octopus.newTurn()
    

print(flash_counter)
"""

##debug
def printBoard(turn):
    print(f"**********************           tour : {turn}           **********************")
    for line in board:
        print([octopus.getEnergy() for octopus in line])

##Part 2

turn = 0
while(turn_flash_counter < 100):
    turn+=1
    turn_flash_counter = 0
    for octopus in allOctopus: octopus.incrementEnergy()
    for octopus in allOctopus: octopus.newTurn()

print(turn, flash_counter)
