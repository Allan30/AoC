file = open("input.txt", "r")
lines = file.readlines()

import statistics as st

def fuelsCost(position, point):
    if position < point: return sum([i-position for i in range(position, point+1)])
    return sum([i-point for i in range(point, position+1)])

positions = [int(p) for p in lines[0].split(",")]

moy = st.mean(positions)
q1, median, q3 = st.quantiles(positions)

leastFuel = 9999999999999999999999999999999999
leastPoint = 0
for point in range(int(q1), int(q3)):

    fuels = 0
    for pos in positions: fuels += fuelsCost(pos, point)

    if fuels < leastFuel: 
        leastFuel = fuels
        leastPoint = point

print(leastFuel, leastPoint)

