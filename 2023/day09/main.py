with open("input.txt") as f:
    lines = f.readlines()

for line in range(len(lines)):
    lines[line] = lines[line].replace("\n", "")

# sum = 0
# for line in lines[:]:
#     line = [int(i) for i in line.split(" ")]
#     current_differences = [line]
#     while not all(v == 0 for v in current_differences[-1]):
#         tmp_differences = []
#         for index in range(len(current_differences[-1]) - 1):
#             tmp_differences.append(
#                 current_differences[-1][index + 1] - current_differences[-1][index]
#             )
#         current_differences.append(tmp_differences)

#     current_differences = current_differences[::-1]
#     for index, _line in enumerate(current_differences[:]):
#         if index == 0:
#             continue
#         current_differences[index].append(
#             current_differences[index - 1][-1] + _line[-1]
#         )
#     sum += current_differences[-1][-1]
# print(sum)

# part 2
sum = 0
for line in lines[:]:
    line = [int(i) for i in line.split(" ")]
    current_differences = [line]
    while not all(v == 0 for v in current_differences[-1]):
        tmp_differences = []
        for index in range(len(current_differences[-1]) - 1):
            tmp_differences.append(
                current_differences[-1][index + 1] - current_differences[-1][index]
            )
        current_differences.append(tmp_differences)

    current_differences = current_differences[::-1]
    for index, _line in enumerate(current_differences[:]):
        if index == 0:
            continue
        current_differences[index].insert(
            0, _line[0] - current_differences[index - 1][0]
        )
    sum += current_differences[-1][0]
print(sum)
