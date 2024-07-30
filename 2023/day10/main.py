with open("input.txt") as f:
    lines = f.readlines()

for line in range(len(lines)):
    lines[line] = lines[line].replace("\n", "")

for i, line in enumerate(lines):
    for j, char in enumerate(line):
        if char == "S":
            start = [i, j]
            break
print(start)
path = []
current_node = start[:]
last_node = start[:]
while not start in path:
    tmp_current_node = current_node[:]
    symbol = lines[current_node[0]][current_node[1]]
    if symbol == "|":
        if current_node[0] > last_node[0]:
            current_node[0] += 1
        else:
            current_node[0] -= 1
    elif symbol == "-":
        if current_node[1] > last_node[1]:
            current_node[1] += 1
        else:
            current_node[1] -= 1
    elif symbol == "7":
        if current_node[0] == last_node[0]:
            current_node[0] += 1
        else:
            current_node[1] -= 1
    elif symbol == "J":
        if current_node[0] == last_node[0]:
            current_node[0] -= 1
        else:
            current_node[1] -= 1
    elif symbol == "L":
        if current_node[0] == last_node[0]:
            current_node[0] -= 1
        else:
            current_node[1] += 1
    elif symbol == "F":
        if current_node[0] == last_node[0]:
            current_node[0] += 1
        else:
            current_node[1] += 1
    elif symbol == "S":
        for index, neighbor in enumerate([[0, 1], [0, -1], [1, 0], [-1, 0]]):
            if index == 0 and lines[current_node[0] + neighbor[0]][
                current_node[1] + neighbor[1]
            ] in ["-", "7"]:
                break
            elif index == 1 and lines[current_node[0] + neighbor[0]][
                current_node[1] + neighbor[1]
            ] in ["-", "F"]:
                break
            elif index == 2 and lines[current_node[0] + neighbor[0]][
                current_node[1] + neighbor[1]
            ] in ["|", "J"]:
                break
        current_node[0] += neighbor[0]
        current_node[1] += neighbor[1]
    path.append(current_node[:])
    last_node = tmp_current_node[:]

# part 2

new_lines = [list(line) for line in lines]
for i, line in enumerate(new_lines):
    for index, char in enumerate(line):
        if [i, index] not in path:
            new_lines[i][index] = " "


count = 0
out_lines = new_lines[:]
for i, line in enumerate(new_lines[:]):
    is_inside = False
    for index, char in enumerate(line):
        if char == " " and is_inside:
            count += 1
            out_lines[i][index] = "O"
        if char in ["|", "J", "L"]:
            is_inside = not is_inside
# write in text
with open("output.txt", "w") as f:
    for line in out_lines:
        f.write("".join(line) + "\n")

print(count)
