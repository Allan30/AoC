with open("input.txt") as f:
    lines = f.readlines()

for line in range(len(lines)):
    lines[line] = lines[line].strip()


def get_value(len):
    current_value = 0
    for char in len:
        current_value = ((current_value + ord(char)) * 17) % 256
    return current_value


# part 1
score = 0
for value in lines[0].split(","):
    score += get_value(value)

print(score)

# part 2
boxes = {}
for len in lines[0].split(","):
    if "=" in len:
        len_name, len_value = len.split("=")
        len_value = int(len_value)
        key = get_value(len_name)
        if key not in boxes:
            boxes[key] = []
        added = False
        for index, _len in enumerate(boxes[key][:]):
            if _len[0] == len_name:
                boxes[key][index][1] = len_value
                added = True
                break
        if not added:
            boxes[key].append([len_name, len_value])

    elif "-" in len:
        len_name = len.split("-")[0]
        key = get_value(len_name)
        if key not in boxes:
            continue
        for index, _len in enumerate(boxes[key][:]):
            if _len[0] == len_name:
                del boxes[key][index]
                break

score = sum(
    [
        sum([(box + 1) * (index + 1) * len[1] for index, len in enumerate(lens)])
        for box, lens in boxes.items()
    ]
)
print(score)
