with open("input.txt") as f:
    lines = f.readlines()

for line in range(len(lines)):
    lines[line] = lines[line].replace("\n", "")


def roll_map_part_(maps, direction):
    new_map = [list(line) for line in lines]
    nb_lines = len(lines)
    for i in range(len(lines[0])):
        start = -1
        count = 0
        current_score = 0
        for j in range(nb_lines):
            if lines[j][i] == "O":
                count += 1
                new_map[j][i] = "."
            elif lines[j][i] == "#":
                print(list(range(start + 1, start + count + 1)))
                for index in list(range(start + 1, start + count + 1)):
                    new_map[index][i] = "O"
                current_score += sum(
                    [nb_lines - n for n in range(start + 1, start + count + 1)]
                )
                start = j
                count = 0

        for _index in list(range(start + 1, start + count + 1)):
            new_map[_index][i] = "O"
    [print("".join(line)) for line in new_map]


def roll_map(map, direction):
    x, y = direction
    new_map = [list(line) for line in map]
    for i, line in enumerate(map):
        for j, char in enumerate(line):
            if char == "O":
                new_map[i][j] = "."
                new_map[i + x][j + y] = "O"


def get_score(map):
    score = 0
    for i, line in enumerate(map):
        for j, char in enumerate(line):
            if char == "O":
                score += len(map) - i
    return score


def read_list_of_lists(matrix, direction=(1, 0)):
    rows = len(matrix)
    cols = len(matrix[0]) if matrix else 0
    new_matrix = matrix.copy()

    if direction == "EAST":  # Left to Right
        for i in range(rows):
            stones = 0
            for j in range(cols):
                if matrix[i][j] == "O":
                    stones += 1
                    new_matrix[i][j] = "."
                elif matrix[i][j] == "#":
                    for index in range(j - stones, j):
                        new_matrix[i][index] = "O"
                    stones = 0
            for index in range(cols - stones, cols):
                new_matrix[i][index] = "O"

    elif direction == "WEST":  # Right to Left
        for i in range(rows):
            stones = 0
            for j in range(cols - 1, -1, -1):
                if matrix[i][j] == "O":
                    stones += 1
                    new_matrix[i][j] = "."
                elif matrix[i][j] == "#":
                    for index in range(j + stones, j, -1):
                        new_matrix[i][index] = "O"
                    stones = 0
            for index in range(stones):
                new_matrix[i][index] = "O"

    elif direction == "SOUTH":  # Up to Down
        for j in range(cols):
            stones = 0
            for i in range(rows):
                if matrix[i][j] == "O":
                    stones += 1
                    new_matrix[i][j] = "."
                elif matrix[i][j] == "#":
                    for index in range(i - stones, i):
                        new_matrix[index][j] = "O"
                    stones = 0
            for index in range(rows - stones, rows):
                new_matrix[index][j] = "O"

    elif direction == "NORTH":  # Down to Up
        for j in range(cols):
            stones = 0
            for i in range(rows - 1, -1, -1):
                if matrix[i][j] == "O":
                    stones += 1
                    new_matrix[i][j] = "."
                elif matrix[i][j] == "#":
                    for index in range(i + stones, i, -1):
                        new_matrix[index][j] = "O"
                    stones = 0
            for index in range(stones):
                new_matrix[index][j] = "O"
    # [print("".join(line)) for line in new_matrix]
    return new_matrix


# Example usage:
matrix = [list(line) for line in lines]
cycle = ["NORTH", "WEST", "SOUTH", "EAST"]
all_scores = [get_score(matrix)]
start_cycle = False
init_scores = 0
cycle_score = []
last_score = 0
for i in range(250):
    for direction in cycle:
        matrix = read_list_of_lists(matrix, direction)
    score = get_score(matrix)
    if score not in all_scores:
        all_scores.append(score)
        start_cycle = False
        cycle_score = []
        init_scores = 0
        print("ok")
    else:
        start_cycle = True
        init_scores = i if init_scores == 0 else init_scores
        print(i, score)

    if start_cycle:
        if (
            len(cycle_score) > 1
            and score == cycle_score[1]
            and last_score == cycle_score[0]
        ):
            print("cycle", last_score, score, cycle_score.index(score) - 1)
            cycle_score.pop(-1)
            break
        cycle_score.append(score)
    last_score = score
print(init_scores, cycle_score, len(cycle_score))
print(cycle_score[(1000000000 - init_scores - 1) % len(cycle_score)])
