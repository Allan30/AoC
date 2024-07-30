file = open("input.txt", "r")
lines = file.readlines()

fishsRaw = [int(f) for f in lines[0].split(",")]
fishs = dict()
fishsEmpy = dict()

for day in range(9):
    counter = 0
    for fish in fishsRaw:
        if fish == day: counter += 1
    
    fishs[day] = counter
    fishsEmpy[day] = 0


days = 256

for day in range(days):
    fishsCurrent = fishsEmpy.copy()
    for fishDay, nFishs in fishs.items():
        if fishDay == 0:
            fishsCurrent[6] += nFishs
            fishsCurrent[8] += nFishs
        elif fishDay == 7: fishsCurrent[fishDay-1] += nFishs
        else: fishsCurrent[fishDay-1] = nFishs
    fishs = fishsCurrent.copy()

print(sum(fishs.values()))
