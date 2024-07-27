with open("input.txt") as f:
    lines = f.readlines()

for line in range(len(lines)):
    lines[line] = lines[line].replace("\n", "")

# part 1
# points = 0
# for line in lines:
#     data = line.split(":")
#     numbers = data[1].split("|")
#     win_numbers = list(filter(None, numbers[0].split(" ")))
#     my_numbers = list(filter(None, numbers[1].split(" ")))
#     nb_win_numbers = len([n for n in my_numbers if n in win_numbers]) - 1
#     points += 2**nb_win_numbers if nb_win_numbers >= 0 else 0

# part 2
cards = []
for line in lines:
    data = line.split(":")
    numbers = data[1].split("|")
    win_numbers = list(filter(None, numbers[0].split(" ")))
    my_numbers = list(filter(None, numbers[1].split(" ")))
    cards.append([win_numbers, my_numbers, 1])

copies = 0
for i in range(len(cards)):
    current_card = cards[i]
    copies += current_card[2]
    for _ in range(current_card[2]):
        nb_win_numbers = len([n for n in current_card[1] if n in current_card[0]])
        for j in range(1, nb_win_numbers + 1):
            cards[i + j][2] += 1
print(copies)
