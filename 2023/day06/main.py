import math

with open("input.txt") as f:
    lines = f.readlines()

for line in range(len(lines)):
    lines[line] = lines[line].replace("\n", "")

times = []
distances = []
for line in lines:
    if line.startswith("Time: "):
        times = [int(v) for v in list(filter(None, line.split(" ")))[1:]]
    elif line.startswith("Distance: "):
        distances = [int(v) for v in list(filter(None, line.split(" ")))[1:]]

# part 1

# for part 2
times = [int("".join([str(t) for t in times]))]
distances = [int("".join([str(d) for d in distances]))]

prod = 1
for i in range(len(times)):
    time = times[i]
    distance = distances[i]
    min_button_hold = math.ceil(distance / time)
    nb_win_paths = 0
    for button_time_hold in range(min_button_hold, time - min_button_hold + 1):
        if distance < button_time_hold * (time - button_time_hold):
            nb_win_paths += 1
    prod *= nb_win_paths
print(prod)
