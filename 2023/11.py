with open("input.txt") as f:
    lines = f.readlines()

for line in range(len(lines)):
    lines[line] = lines[line].replace("\n", "")

galaxies = []
void_lines = []
void_columns = []
for i, line in enumerate(lines):
    if all([char == "." for char in line]):
        void_lines.append(i)
    for j, char in enumerate(line):
        if char == "#":
            galaxies.append([i, j])

for j in range(len(lines[0])):
    if all([lines[i][j] == "." for i in range(len(lines))]):
        void_columns.append(j)

from itertools import combinations

print(void_lines)
print(void_columns)

all_galaxies_pairs = list(combinations(galaxies, 2))
distances = {}
galaxies_ids = {}
for id, galaxie in enumerate(all_galaxies_pairs):
    x1, y1 = galaxie[0]
    x2, y2 = galaxie[1]
    distance = abs(x1 - x2) + abs(y1 - y2)
    expandided_distance = (
        len([l for l in void_lines if l > min(x1, x2) and l < max(x1, x2)]) * 999999
        + len([c for c in void_columns if c > min(y1, y2) and c < max(y1, y2)]) * 999999
    )
    distances[id] = distance + expandided_distance
    galaxies_ids[id] = galaxie

print(sum(distances.values()))
