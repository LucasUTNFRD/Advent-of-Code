# acceder al documento de texto
# part one
calibration = 0
with open('input_day1.txt', 'r') as file:
    for line in file.readlines():
        digits = [char for char in line.strip() if char.isdigit()]
        calibration += int(digits[0]+digits[-1])#concat string and turn into int
    print(calibration)
# part two

# word_to_int = {
#         'one': 1,
#         'two': 2,
#         'three': 3,
#         'four': 4,
#         'five': 5,
#         'six': 6,
#         'seven': 7,
#         'eight': 8,
#         'nine': 9
#     }
# calibration = 0
# with open('input_day1.txt', 'r') as file:
#     for line in file.readlines():
#         digits = [int(word) if word.isdigit() else word_to_int[word] for word in line.split()]
#         calibration += digits[0] + digits[-1]
#
#     print(calibration)
#
#
#
