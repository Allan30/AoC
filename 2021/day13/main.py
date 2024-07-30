from typing import Counter


file = open("input.txt", "r")
lines = file.readlines()

dots = list()
folds = list()

foldStart = False
for line in lines:
    if foldStart: 
        line = line.replace('fold along ', '')
        xOry, value = line.split('=')
        folds.append((xOry, int(value)))
    elif line == '\n': foldStart = True
    else: 
        y, x = line.split(',')
        dots.append((int(x), int(y)))

print(dots, folds)


width, length  =(max([dot[1] for dot in dots])+1, max([dot[0] for dot in dots])+1)
print(width, length)

sheet = list()
for x in range(length):
    sheet.append(list())
    for y in range(width):
        if (x,y) in dots: sheet[x].append('#')
        else: sheet[x].append('.')

#folds = [folds[0]] #part 1

for fold in folds:
    if fold[0] == "y":
        for x in range(length):
            for y in range(width):
                if x > fold[1] and sheet[x][y] == '#': 
                    sheet[2*fold[1]-x][y] = '#'
        sheet = sheet[:fold[1]]
        length = fold[1]
    
    else:
        for x in range(length):
            for y in range(width):
                if y > fold[1] and sheet[x][y] == '#': 
                    sheet[x][2*fold[1]-y] = '#'
        
        sheet = [l[:fold[1]] for l in sheet]
        width = fold[1]

##part 1
"""
counter = 0 
for line in sheet:
    for d in line:
        if d == "#": counter += 1

print(counter)
"""

##part 2
[print(l) for l in sheet]