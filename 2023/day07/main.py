with open("input.txt") as f:
    lines = f.readlines()

for line in range(len(lines)):
    lines[line] = lines[line].replace("\n", "")

five_of_a_kind = []
four_of_a_kind = []
full_house = []
three_of_a_kind = []
two_pair = []
one_pair = []
high_card = []
all_cards = "J23456789TQKA"


# part 1
def is_better_hand(hand1, hand2):
    for card1, card2 in zip(hand1, hand2):
        if all_cards.index(card1) < all_cards.index(card2):
            return True
        elif all_cards.index(card1) > all_cards.index(card2):
            return False


def find_pviot_index(A, start, end):
    pivot = A[end]
    p_index = start
    for iter in range(start, end):
        if is_better_hand(A[iter][0], pivot[0]):
            A[p_index], A[iter] = A[iter], A[p_index]
            p_index += 1
    A[p_index], A[end] = pivot, A[p_index]
    return p_index


def quick_sort(A, start, end):
    if start < end:
        pivot_index = find_pviot_index(A, start, end)
        quick_sort(A, start, pivot_index - 1)
        quick_sort(A, pivot_index + 1, end)


# for line in lines:
#     hand, value = line.split(" ")
#     value = int(value)

#     evaluate_hand = {}
#     for card in hand:
#         evaluate_hand[card] = hand.count(card)

#     if 5 in evaluate_hand.values():
#         five_of_a_kind.append((hand, value))
#     elif 4 in evaluate_hand.values():
#         four_of_a_kind.append((hand, value))
#     elif 3 in evaluate_hand.values() and 2 in evaluate_hand.values():
#         full_house.append((hand, value))
#     elif 3 in evaluate_hand.values():
#         three_of_a_kind.append((hand, value))
#     elif list(evaluate_hand.values()).count(2) == 2:
#         two_pair.append((hand, value))
#     elif 2 in evaluate_hand.values():
#         one_pair.append((hand, value))
#     else:
#         high_card.append((hand, value))

# hands = [
#     five_of_a_kind,
#     four_of_a_kind,
#     full_house,
#     three_of_a_kind,
#     two_pair,
#     one_pair,
#     high_card,
# ]
# for hand in hands:
#     quick_sort(hand, 0, len(hand) - 1)

# hands = (
#     high_card
#     + one_pair
#     + two_pair
#     + three_of_a_kind
#     + full_house
#     + four_of_a_kind
#     + five_of_a_kind
# )
# mult = 0
# result = 0
# for hand in hands:
#     mult += 1
#     result += hand[1] * mult

# print(result)

# part 2
for line in lines:
    hand, value = line.split(" ")
    value = int(value)

    evaluate_hand = {}
    for card in hand:
        evaluate_hand[card] = hand.count(card)

    if "J" in evaluate_hand.keys():
        nb_jokers = evaluate_hand["J"]
        if nb_jokers < 5:
            del evaluate_hand["J"]
            max_value = max(evaluate_hand, key=evaluate_hand.get)
            evaluate_hand[max_value] += nb_jokers

    if 5 in evaluate_hand.values():
        five_of_a_kind.append((hand, value))
    elif 4 in evaluate_hand.values():
        four_of_a_kind.append((hand, value))
    elif 3 in evaluate_hand.values() and 2 in evaluate_hand.values():
        full_house.append((hand, value))
    elif 3 in evaluate_hand.values():
        three_of_a_kind.append((hand, value))
    elif list(evaluate_hand.values()).count(2) == 2:
        two_pair.append((hand, value))
    elif 2 in evaluate_hand.values():
        one_pair.append((hand, value))
    else:
        high_card.append((hand, value))

hands = [
    five_of_a_kind,
    four_of_a_kind,
    full_house,
    three_of_a_kind,
    two_pair,
    one_pair,
    high_card,
]
for hand in hands:
    quick_sort(hand, 0, len(hand) - 1)

[print(hand, "\n") for hand in hands]

hands = (
    high_card
    + one_pair
    + two_pair
    + three_of_a_kind
    + full_house
    + four_of_a_kind
    + five_of_a_kind
)
mult = 0
result = 0
for hand in hands:
    mult += 1
    result += hand[1] * mult

print(result)
