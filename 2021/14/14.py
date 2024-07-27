file = open("input.txt", "r")
lines = file.readlines()

polymer = lines[0]
rules = dict()

for rule in lines[2:]:
    pair, result = rule.replace('\n', '').split(' -> ')
    rules[pair] = result

print(polymer, rules)

pairs = dict()
for index, element in enumerate(polymer):
    next = index + 1
    if next < len(polymer)-1:
        pair1 = element+polymer[next]
        if pair1 in pairs.keys(): pairs[pair1] += 1
        else: pairs[pair1] = 1

print(pairs)

STEPS = 40
for step in range(STEPS):
    pairsCopy = dict()
    for pair in pairs:
        if pair in rules.keys():
            newPair1 = pair[0]+rules[pair]
            newPair2 = rules[pair]+pair[1]
            
            if newPair1 in pairsCopy.keys(): pairsCopy[newPair1] += pairs[pair]
            else: pairsCopy[newPair1] = pairs[pair]

            if newPair2 in pairsCopy.keys(): pairsCopy[newPair2] += pairs[pair]
            else: pairsCopy[newPair2] = pairs[pair]

    pairs = pairsCopy

#print(pairs, sum(pairs.values()))
elements = dict()

for element in rules.values():
    if element not in elements.keys(): elements[element] = 0

for pair, occ in pairs.items():
    e1, e2 = pair
    elements[e1] += occ
    elements[e2] += occ

for element in elements.keys(): elements[element] = elements[element]/2

print(elements)
print(int(max(elements.values())-min(elements.values()))+1)
