import re

with open("input.txt") as f:
    lines = f.readlines()

for line in range(len(lines)):
    lines[line] = lines[line].replace("\n", "")

neighbours = [(1, 1), (1, -1), (-1, 1), (-1, -1), (0, 1), (0, -1), (1, 0), (-1, 0)]
labyrinth = lines


def get_numbers(line):
    numbers = []
    line = re.sub("[^0-9]", ".", line)
    for character in line.split("."):
        if character.isdigit():
            numbers.append(character)

    numbers = numbers[::-1]

    position_of_numbers = []
    tmp_line = line
    for number in numbers:
        tmp_line = tmp_line.split(number)
        position_of_numbers.append(
            [number, len(line) - len(tmp_line[-1]) - len(number)]
        )
        if len(tmp_line) >= 3:
            tmp_line = number.join(tmp_line[:-1]) + (len(number) * ".") + tmp_line[-1]
        else:
            tmp_line = (len(number) * ".").join([tmp_line[0], tmp_line[1]])

    return position_of_numbers


def symbol_in_neighbourhood(x, y):
    for neighbour in neighbours:
        delta_y = (
            y + neighbour[0]
            if y + neighbour[0] >= 0 and y + neighbour[0] <= len(labyrinth) - 1
            else y
        )
        delta_x = (
            x + neighbour[1]
            if x + neighbour[1] >= 0 and x + neighbour[1] <= len(labyrinth[y]) - 1
            else x
        )
        # print("delta_y", delta_y, "delta_x", delta_x)
        if (
            not labyrinth[delta_y][delta_x].isdigit()
            and labyrinth[delta_y][delta_x] != "."
        ):
            return True
    return False


f = open("out.txt", "w")

# sum = 0
# for i, line in enumerate(labyrinth):
#     write_line = list(line)
#     numbers = get_numbers(line)
#     for number in numbers:
#         is_valid = False

#         # print(number)
#         for j, digit in enumerate(number[0]):
#             # print("############################")
#             if symbol_in_neighbourhood(number[1] + j, i):
#                 print(number, digit)
#                 is_valid = True
#                 sum += int(number[0])
#                 break

#         if not is_valid:
#             for j, digit in enumerate(number[0]):
#                 write_line[j + number[1]] = "."
#     f.write("".join(write_line))

# print(sum)

## Part 2
import math


def is_a_part_number(x, y, number):
    for i in range(len(number)):
        if symbol_in_neighbourhood(x + i, y):
            return True


def get_gears(line):
    line = re.sub("[^*]", ".", line)
    gears = ["*"] * line.count("*")

    position_of_gears = []
    tmp_line = line
    for _ in gears:
        tmp_line = tmp_line.split("*")
        position_of_gears.append(("*", len(line) - len(tmp_line[-1]) - 1))
        if len(tmp_line) >= 3:
            tmp_line = "*".join(tmp_line[:-1]) + "." + tmp_line[-1]
        else:
            tmp_line = ".".join([tmp_line[0], tmp_line[1]])

    return position_of_gears


def two_part_number_in_neighbourhood(x, y, numbers):
    near_numbers = {}
    for neighbour in neighbours:
        delta_y = (
            y + neighbour[0]
            if y + neighbour[0] >= 0 and y + neighbour[0] <= len(labyrinth) - 1
            else y
        )
        delta_x = (
            x + neighbour[1]
            if x + neighbour[1] >= 0 and x + neighbour[1] <= len(labyrinth[y]) - 1
            else x
        )
        # print("delta_y", delta_y, "delta_x", delta_x)
        for position, number in numbers.items():
            if (
                delta_x >= position[0]
                and delta_x <= position[0] + len(number) - 1
                and delta_y == position[1]
            ):
                near_numbers[position] = number
    if len(near_numbers) != 2:
        return 0
    return math.prod([int(x) for x in near_numbers.values()])


sum = 0
for i, line in enumerate(labyrinth):
    numbers = get_numbers(line)
    [n.append(i) for n in numbers]
    numbers_up = get_numbers(labyrinth[i - 1]) if i - 1 >= 0 else []
    [n.append(i - 1) for n in numbers_up]
    numbers_down = get_numbers(labyrinth[i + 1]) if i + 1 <= len(labyrinth) - 1 else []
    [n.append(i + 1) for n in numbers_down]
    numbers = numbers + numbers_up + numbers_down
    numbers = {
        (x[1], x[2]): x[0] for x in numbers if is_a_part_number(x[1], x[2], x[0])
    }

    gears = get_gears(line)
    write_line = list(line)
    for gear in gears:
        sum += two_part_number_in_neighbourhood(gear[1], i, numbers)
        if two_part_number_in_neighbourhood(gear[1], i, numbers) != 0:
            write_line[gear[1]] = "."
    f.write("".join(write_line) + "\n")

print(sum)
