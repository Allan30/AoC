with open("input.txt") as f:
    lines = f.readlines()

for line in range(len(lines)):
    lines[line] = lines[line].replace("\n", "")

from tqdm import tqdm

# part 1
seed_to_soil_map = []
soil_to_fertilizer_map = []
fertilizer_to_water_map = []
water_to_light_map = []
light_to_temperature_map = []
temperature_to_humidity_map = []
humidity_to_location_map = []
seed_to_soil = False
soil_to_fertilizer = False
fertilizer_to_water = False
water_to_light = False
light_to_temperature = False
temperature_to_humidity = False
humidity_to_location = False
for line in lines:
    if line.startswith("seeds"):
        seeds = [int(n) for n in line.split("seeds: ")[-1].split(" ")]
    elif line.startswith("seed-to-soil map:"):
        seed_to_soil = True
    elif line.startswith("soil-to-fertilizer map:"):
        soil_to_fertilizer = True
    elif line.startswith("fertilizer-to-water map:"):
        fertilizer_to_water = True
    elif line.startswith("water-to-light map:"):
        water_to_light = True
    elif line.startswith("light-to-temperature map:"):
        light_to_temperature = True
    elif line.startswith("temperature-to-humidity map:"):
        temperature_to_humidity = True
    elif line.startswith("humidity-to-location map:"):
        humidity_to_location = True
    elif line == "":
        seed_to_soil = False
        soil_to_fertilizer = False
        fertilizer_to_water = False
        water_to_light = False
        light_to_temperature = False
        temperature_to_humidity = False
        humidity_to_location = False
    elif seed_to_soil:
        seed_to_soil_map.append([int(n) for n in line.split(" ")])
    elif soil_to_fertilizer:
        soil_to_fertilizer_map.append([int(n) for n in line.split(" ")])
    elif fertilizer_to_water:
        fertilizer_to_water_map.append([int(n) for n in line.split(" ")])
    elif water_to_light:
        water_to_light_map.append([int(n) for n in line.split(" ")])
    elif light_to_temperature:
        light_to_temperature_map.append([int(n) for n in line.split(" ")])
    elif temperature_to_humidity:
        temperature_to_humidity_map.append([int(n) for n in line.split(" ")])
    elif humidity_to_location:
        humidity_to_location_map.append([int(n) for n in line.split(" ")])

locations = []
maps = [
    seed_to_soil_map,
    soil_to_fertilizer_map,
    fertilizer_to_water_map,
    water_to_light_map,
    light_to_temperature_map,
    temperature_to_humidity_map,
    humidity_to_location_map,
]
for seed in seeds[:]:
    current_var = seed
    for map in maps:
        for conditions in map:
            if (
                current_var >= conditions[1]
                and current_var <= conditions[1] + conditions[2]
            ):
                current_var = conditions[0] + current_var - conditions[1]
                break
    locations.append(current_var)

print(min(locations))


# part 2
def get_all_partitioned_ranges(init_range, conditions):
    ranges = []
    for new_range in conditions:
        if (
            init_range[0] >= new_range[0]
            and init_range[1] <= new_range[0] + new_range[2]
        ):
            ranges.append((init_range[0], init_range[1], new_range[1] - new_range[0]))
        elif (
            init_range[0] <= new_range[0]
            and init_range[1] >= new_range[0] + new_range[2]
        ):
            ranges.append(
                (new_range[0], new_range[0] + new_range[2], new_range[1] - new_range[0])
            )
        elif (
            init_range[0] <= new_range[0]
            and init_range[1] >= new_range[0]
            and init_range[1] <= new_range[0] + new_range[2]
        ):
            ranges.append((new_range[0], init_range[1], new_range[1] - new_range[0]))
        elif (
            init_range[0] >= new_range[0]
            and init_range[0] <= new_range[0] + new_range[2]
            and init_range[1] >= new_range[0] + new_range[2]
        ):
            ranges.append(
                (
                    init_range[0],
                    new_range[0] + new_range[2],
                    new_range[1] - new_range[0],
                )
            )
    print(conditions)
    print(ranges)
    return ranges


import os

maps.pop(-1)
ranges_seeds = [
    (seeds[i], seeds[i] + seeds[i + 1]) for i in range(0, len(seeds) - 1, 2)
]
print(ranges_seeds)
print(humidity_to_location_map)
last_b2 = -1
for range in sorted(humidity_to_location_map, key=lambda x: x[2], reverse=True):
    b1, b2, change = range[0], range[0] + range[2], range[1] - range[0]
    all_change = -change
    print(range)
    print(b1, b2, change)
    print("start")
    for map in maps[::-1]:
        new_ranges = get_all_partitioned_ranges((b1, b2), map)
        for new_range in new_ranges:
            b1, b2, change = new_range
            b1 += change
            b2 += change
            # print(map)
            print("chaaaange", change)
        if len(new_ranges) > 0:
            all_change -= change

    for range_seed in ranges_seeds:
        # if b1, b2 have a part or more in common with range_seed
        print(b1, b2, range_seed)
        if b1 >= range_seed[0] and b1 <= range_seed[1]:
            print(b1 + all_change)
            os._exit(0)
        elif (b2 >= range_seed[0] and b2 <= range_seed[1]) or (
            b1 <= range_seed[0] and b2 >= range_seed[1]
        ):
            print(range_seed[0] + all_change)
            os._exit(0)
    last_b2 = b2
    all_change = range[1] - range[0]
