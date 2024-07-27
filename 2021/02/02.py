file = open("input.txt", "r")
lines = file.readlines()

##Part 1
horizontal, depth = 0, 0
for line in lines:
    command, value = line.split(" ")
    if command == "forward": horizontal += int(value)
    elif command == "down": depth += int(value)
    else: depth -= int(value)

answer = horizontal*depth

##Part 2
horizontal, aim, depth = 0, 0, 0
for line in lines:
    command, value = line.split(" ")
    if command == "down": aim += int(value)
    elif command == "up": aim -= int(value)
    else:
        horizontal += int(value)
        depth += aim*int(value)

answer = horizontal*depth
print(answer)