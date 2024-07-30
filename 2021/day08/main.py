file = open("input.txt", "r")
lines = file.readlines()

inp = [d.split(' ') for d in [d.split(' | ')[0] for d in [line.replace("\n", "") for line in lines]]]
out = [d.split(' ') for d in [d.split(' | ')[1] for d in [line.replace("\n", "") for line in lines]]]

from enum import Enum
from itertools import combinations, permutations

from numpy import array

class DL(Enum):
    ZERO = 6
    ONE = 2
    TWO = 5
    THREE = 5
    FOUR = 4
    FIVE = 5
    SIX = 6
    SEVEN = 3
    HEIGHT = 7
    NINE = 6

class DF(Enum):
    ZERO = [1, 2, 3, 5, 6, 7]
    ONE = [3, 5]
    TWO = [1, 3, 4, 5, 7]
    THREE = [1, 3, 4, 6, 7]
    FOUR = [2, 3, 4, 6]
    FIVE = [1, 2, 4, 6, 7]
    SIX = [1, 2, 4, 5, 6, 7]
    SEVEN = [1, 3, 6]
    HEIGHT = [1, 2, 3, 4, 5, 6, 7]
    NINE = [1, 2, 3, 4, 6, 7]

UNIQUES_NUMBERS = [DL.ONE.value, DL.FOUR.value, DL.SEVEN.value, DL.HEIGHT.value]

#Part1

uniquerCounter = 0
for digits in out:
    for digit in digits:
        if len(digit) in UNIQUES_NUMBERS: uniquerCounter += 1

print(uniquerCounter)

#Part 2

class Unique:

    def __init__(self, value) -> None:
        self.value = value
        self.id = len(value)

        if self.id == 2: self.position = [3, 6]
        elif self.id == 4: self.position = [2, 3, 4, 6]
        elif self.id == 3: self.position = [1, 3, 6]
        else: self.position = [1, 2, 3, 4, 5, 6, 7]

    def shufflePositions(self):
        return [list(zip(x,self.position)) for x in permutations(self.value,len(self.position))]

    def getPosition(self):
        return self.position
    
    def getValue(self):
        return self.value

def findUniques(digits):
    uniques = list()
    for digit in digits:
        if len(digit) in UNIQUES_NUMBERS: uniques.append(Unique(digit))
    return uniques


def finPossibleFormsOfDigitsWith(uniques):
    possibleForms = list()
    for unique in uniques: 
        possibleForms.append(unique.shufflePositions())
    return possibleForms

def isInclude(L1, L2):
    """Renvoie True si L2 est incluse dans L1, False sinon"""
    return set(L2) <= set(L1)

def getLarger(l):
    theLarger = l[0]
    saveIndex = 0
    for index, formGroup in enumerate(l):
        if len(formGroup) > len(theLarger): 
            saveIndex = index
            theLarger = formGroup
    l.pop(saveIndex)

    return theLarger, l

def getSmaller(l):
    theSmaller = l[0]
    saveIndex = 0
    for index, formGroup in enumerate(l):
        if len(formGroup) < len(theSmaller): 
            saveIndex = index
            theSmaller = formGroup
    l.pop(saveIndex)

    return theSmaller, l


def findTheUniqueForm(possibleFormsGroup): 
    
    possibleFormsGroupCopy = possibleFormsGroup.copy()


    theVeryLarger, _ = getLarger(possibleFormsGroupCopy)
    theVerySmaller, _ = getSmaller(possibleFormsGroupCopy.copy())
    newPossible = theVeryLarger

   
    while len(possibleFormsGroupCopy) > 0:
        toPoped = list()
        theLarger, possibleFormsGroupCopy = getLarger(possibleFormsGroupCopy)
        print(theLarger)
        for index, form1 in enumerate(newPossible):
            includ = False
            for form2 in theLarger:
                if isInclude(form1, form2):
                    includ = True 
                    break
            if not includ: 
                toPoped.append(index)
        
        if len(toPoped) > 0:
            toPoped.sort(reverse=True)
            for i in toPoped:
                newPossible.pop(i)
                    

    return newPossible


def testAllTrames(decodes, outp):
    theGood = True
    for trame in decodes:
        for digits in outp:
            positions = list()
            for digit in digits:
                positions.append(trame[digit])

            if not positions in list(map(lambda c: c.value, DF)):
                theGood = False
                break
        if theGood: 
            return trame

                


for digits in inp:
    decodes = list()
    print([d.value for d in findUniques(digits)])
    uniqueWithUniques = findTheUniqueForm(finPossibleFormsOfDigitsWith(findUniques(digits)))
    print("THE UNIQUE")
    for u in uniqueWithUniques: 
        decodes.append(dict())
        for trame in uniqueWithUniques:
            for d in trame:
                decodes[-1][d[0]] = d[1] 
    for d in decodes: print(d)

for o in out:
    print(testAllTrames(decodes, o))