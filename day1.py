calibration = 0
with open('input_day1.txt', 'r') as file:
    for line in file.readlines():
        digits = [char for char in line.strip() if char.isdigit()]
        calibration += int(digits[0]+digits[-1])#concat string and turn into int
    print(calibration)


