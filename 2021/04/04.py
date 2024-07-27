file = open("input.txt", "r")
lines = file.readlines()

import numpy as np

## Part1

serie = [int(n) for n in lines.pop(0).split(",")]

boards = list()
for index, line in enumerate(lines): 
    if len(line) == 1:
        
        boards.append(list())
        
    else:
        boards[-1].append(list())
        for number in line.split(" "): 
            try:
                boards[-1][-1].append(int(number))
            except: pass

boards = [np.array(board) for board in boards]

stop = False

for number in serie:
    if stop: break
    print(number)
    for index, board in enumerate(boards):
        if number in board:
            boards[index] = np.where(board==number, -1, board)
            if -5 in np.sum(boards[index], axis=0) or -5 in np.sum(boards[index], axis=1):
                boards[index] = np.where(boards[index]==-1, 0, board)
                answer = np.sum(boards[index])*number
                print(answer)
                stop = True
                break


## Part2
file = open("input.txt", "r")
lines = file.readlines()

serie = [int(n) for n in lines.pop(0).split(",")]

boards = list()
for index, line in enumerate(lines): 
    if len(line) == 1:
        
        boards.append(list())
        
    else:
        boards[-1].append(list())
        for number in line.split(" "): 
            try:
                boards[-1][-1].append(int(number))
            except: pass

boards = [np.array(board) for board in boards]
winner = [False]*len(boards)

stop = False
lastWinner = 0
indexToPop = list()

for number in serie:
    for index, board in enumerate(boards):
        if number in board:
            boards[index] = np.where(board==number, -1, board)
            if (-5 in np.sum(boards[index], axis=0) or -5 in np.sum(boards[index], axis=1)) and not winner[index]:
                boards[index] = np.where(boards[index]==-1, 0, board)
                answer = np.sum(boards[index])*number
                lastWinner = answer
                winner[index] = True


print(lastWinner)