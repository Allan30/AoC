file = open("input.txt", "r")
lines = file.readlines()

##Part 1
last = 999999999
counter = 0
for line in lines:
    if int(line) > last: counter += 1
    last = int(line)

print(counter)

##Part 2
sums = list()
for line in lines:
    try: sums[-1] += int(line)
    except: pass
    try: sums[-2] += int(line)
    except: pass
    sums.append(int(line))

last = 999999999
counter = 0
for s in sums:
    if s > last: counter += 1
    last = s

print(counter)
    

