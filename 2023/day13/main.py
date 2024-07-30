with open("input.txt") as f:
    lines = f.readlines()

for line in range(len(lines)):
    lines[line] = lines[line].replace("\n", "")

patterns = []
current_pattern = []
for line in lines:
    if line == "":
        patterns.append(current_pattern)
        current_pattern = []
    else:
        current_pattern.append(line)
patterns.append(current_pattern)

line_patterns = []
column_patterns = []
for pattern in patterns:
    line_patterns.append(
        [int(line.replace(".", "0").replace("#", "1"), 2) for line in pattern]
    )
    column_patterns.append([])
    for i in range(len(pattern[0])):
        column_patterns[-1].append(
            int(
                "".join(
                    [
                        line.replace(".", "0").replace("#", "1")
                        for line in ([line[i] for line in pattern])
                    ]
                ),
                2,
            )
        )


def get_score_from_pattern(pattern, line):
    score = 0
    for i in range(1, len(pattern) // 2 + 1):
        if pattern[:i] == pattern[i : i + i][::-1]:
            return 100 * i if line else i
        if (
            pattern[len(pattern) - i :]
            == pattern[len(pattern) - 2 * i : len(pattern) - i][::-1]
        ):
            return 100 * (len(pattern) - i) if line else len(pattern) - i
    return 0


def is_power_of_two(x):
    return x and (not (x & (x - 1)))


def equal_with_smudge(left, right):
    if left == right:
        return False
    for index in range(len(left)):
        if left[index] != right[index]:
            if not is_power_of_two(left[index] ^ right[index]):
                return False
    return True


def get_score_from_pattern_with_smudge(pattern, line):
    score = 0
    for i in range(1, len(pattern) // 2 + 1):
        if equal_with_smudge(pattern[:i], pattern[i : i + i][::-1]):
            return 100 * i if line else i
        if equal_with_smudge(
            pattern[len(pattern) - i :],
            pattern[len(pattern) - 2 * i : len(pattern) - i][::-1],
        ):
            return 100 * (len(pattern) - i) if line else len(pattern) - i
    return 0


score = 0
last_score = 0
for pattern_index in range(len(patterns[:])):
    score += get_score_from_pattern_with_smudge(
        column_patterns[pattern_index], False
    ) + get_score_from_pattern_with_smudge(line_patterns[pattern_index], True)
print(score)
