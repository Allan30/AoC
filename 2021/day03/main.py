file = open("input.txt", "r")
lines = file.readlines()

##Part 1
import numpy as np

binList = list()
for index, line in enumerate(lines): 
    binList.append(list())
    for b in line: 
        if b != '\n': binList[index].append(int(b))
binList = np.array(binList)

lenRow, _ = np.shape(binList)
lenRow /= 2

firstBin, secondBin = "",""


for b in np.sum(binList, axis=0):
    if b > lenRow:
        firstBin += '1'
        secondBin += '0'
    else:
        firstBin += '0'
        secondBin += '1' 



#firstBin = ''.join(['1' if b > lenRow//2 else '0' for b in np.sum(binList, axis=0)])
#secondBin = ''.join(['0' if b > lenRow//2 else '0' for b in np.sum(binList, axis=0)])

answer = int(firstBin, 2)*int(secondBin, 2)

##Part 2
import numpy as np

binList = list()
for index, line in enumerate(lines): 
    binList.append(list())
    for b in line: 
        if b != '\n': binList[index].append(int(b))
binList = np.array(binList)

OXYGEN = True

def generatorRating(oxygenList, index):
    if np.shape(oxygenList)[0] > 1 or index > np.shape(oxygenList)[1]:
        lenRow = np.shape(oxygenList)[0]/2
        sumb = np.sum(oxygenList, axis=0)[index]
        if sumb >= lenRow: return(generatorRating(np.array([b for b in oxygenList if b[index] == OXYGEN]), index+1))
        else: return(generatorRating(np.array([b for b in oxygenList if b[index] == (not OXYGEN)]), index+1))
        
    return oxygenList[0]

oxygenRating = int(''.join([str(a) for a in generatorRating(binList, 0)]), 2)
OXYGEN = False
co2Rating = int(''.join([str(a) for a in generatorRating(binList, 0)]), 2)

answer = oxygenRating*co2Rating

print(answer)


