with open("input.txt") as f:
    lines = f.readlines()

for line in range(len(lines)):
    lines[line] = lines[line].replace("\n", "")


def filter_string(string):
    return list(filter(None, string))


instructions = lines.pop(0)
nodes = {}
start_node = "AAA"
end_node = "ZZZ"
for line in lines[1:]:
    node, elements = line.split("=")
    nodes[node[:-1]] = (
        elements.split(",")[0][2:],
        elements.split(",")[1][1:-1],
    )

# current_node = start_node
# counter = 0
# while current_node != end_node:
#     for step in instructions:
#         counter += 1
#         if step == "L":
#             current_node = nodes[current_node][0]
#         elif step == "R":
#             current_node = nodes[current_node][1]

#         if current_node == end_node:
#             break
# print(counter)

# part 1
import collections

start_nodes = [n for n in nodes if n.endswith("A")]
end_nodes = [n for n in nodes if n.endswith("Z")]
current_nodes = start_nodes
counter = 0
print(start_nodes)
print(end_nodes)
while not collections.Counter(current_nodes) == collections.Counter(end_nodes):
    for step in instructions:
        counter += 1
        for index, current_node in enumerate(current_nodes):
            if step == "L":
                current_nodes[index] = nodes[current_node][0]
            elif step == "R":
                current_nodes[index] = nodes[current_node][1]

        if collections.Counter(current_nodes) == collections.Counter(end_nodes):
            break
print(counter)
