file = open("input.txt", "r")
lines = file.readlines()

allToFind = list()

##part 1

def getInv(character):
    if character == '(': return ')'
    elif character == '{': return '}'
    elif character == '[': return ']'
    elif character == '<': return '>'
    else: return -1

def getPoints(character):
    if character == ')': return 3
    elif character == ']': return 57
    elif character == '}': return 1197
    elif character == '>': return 25137
    else: return 0

ilegalsCharacters = list()

for line in lines:
    toFind = [getInv(line[0])]
    if(toFind[0] != -1):
        for character in line[1:]:
            if(getInv(character) != -1):
                toFind.append(getInv(character))
            elif(character != toFind[-1]): 
                ilegalsCharacters.append(character)
                if ilegalsCharacters[-1] == '\n': allToFind.append(toFind)
                break
            else:
                toFind.pop(-1)

print(ilegalsCharacters)
answer = sum([getPoints(c) for c in ilegalsCharacters])
print(answer)

##part 2

def getPointsPart2(character):
    if character == ')': return 1
    elif character == ']': return 2
    elif character == '}': return 3
    elif character == '>': return 4
    else: return 0

answers = []
for line in allToFind:
    points = 0
    for c in reversed(line): points = 5*points + getPointsPart2(c)
    answers.append(points)

print(sorted(answers)[len(answers)//2-1])