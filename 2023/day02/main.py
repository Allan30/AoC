with open("input.txt") as f:
    lines = f.readlines()

for line in range(len(lines)):
    lines[line] = lines[line].replace("\n", "")

sum = 0
for line in lines:
    id = int(line.split(":")[0].split(" ")[-1])
    possible = True
    colors = {"red": 0, "blue": 0, "green": 0}
    for bag in line.split(":")[1].split(";"):
        # print(bag)
        for cubes in bag.split(","):
            cubes = cubes[1:]
            nb = int(cubes.split(" ")[0])
            color = cubes.split(" ")[1]
            # print(color)
            if nb > colors[color]:
                colors[color] = nb

    sum += colors["red"] * colors["blue"] * colors["green"]
    # print(colors)
    print(colors["red"] * colors["blue"] * colors["green"])

print(sum)
