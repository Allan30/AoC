with open("input.txt") as f:
    lines = f.readlines()

for line in range(len(lines)):
    lines[line] = lines[line].replace("\n", "")

# part 1
# from tqdm import tqdm

# nb_arrangements = 0
# for line in tqdm(lines):
#     field, qte = line.split(" ")
#     qte = list(map(int, qte.split(",")))
#     unknown = [i for i, elem in enumerate(field) if elem == "?"]
#     target = 2 ** len(unknown)
#     counted_fields = []
#     field = field.replace("?", ".")
#     for b in range(target):
#         for i, pos in enumerate(unknown):
#             field = field[:pos] + ("#" if ((b >> i) & 1) else ".") + field[pos + 1 :]
#             if [
#                 len(l) for l in list(filter(None, field.split(".")))
#             ] == qte and field not in counted_fields:
#                 counted_fields.append(field)
#                 nb_arrangements += 1

# print(nb_arrangements)


# part 2
def get_arranged(splited_field, num_trees):
    pass
