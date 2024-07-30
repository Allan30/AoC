with open("input.txt") as f:
    lines = f.readlines()

# part 1
# sum = 0
# for line in lines:
#     digits = ""
#     for c in line:
#         if c.isdigit():
#             digits += c
#             break
#     for c in line[::-1]:
#         if c.isdigit():
#             digits += c
#             break
#     sum += int(digits)
# print(sum)

# part 2
import re

DIGITS = {
    "one": "1",
    "two": "2",
    "three": "3",
    "four": "4",
    "five": "5",
    "six": "6",
    "seven": "7",
    "eight": "8",
    "nine": "9",
    "1": "1",
    "2": "2",
    "3": "3",
    "4": "4",
    "5": "5",
    "6": "6",
    "7": "7",
    "8": "8",
    "9": "9",
}
sum = 0
for line in lines:
    first_index = 10000000000
    firs_digit = ""
    last_index = -1
    last_digit = ""
    for digit in DIGITS.keys():
        reg = r"" + digit
        for match in re.finditer(reg, line):
            print("match", match.group(), "start index", match.start())
            if match.start() < first_index:
                first_index = match.start()
                firs_digit = DIGITS[digit]
            if match.start() > last_index:
                last_index = match.start()
                last_digit = DIGITS[digit]
    print(line)
    print("first", firs_digit, "last", last_digit)
    sum += int(firs_digit + last_digit)
    print(sum)

print(sum)
