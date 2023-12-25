import re
calibration = 0

def word_to_numb(number):
    word_dict = {"one":"1"
                 ,"two":"2"
                 ,"three":'3'
                 ,"four":"4"
                 ,"five":"5"
                 ,"six":"6"
                 ,"seven":"7"
                 ,"eight":"8"
                 ,"nine":"9"}
    
    if number in word_dict.keys():
        asNum = word_dict.get(number)
        return asNum
    else:
        return str(number)


calibration = 0
with open('input_day1.txt', 'r') as file:
    for line in file.readlines():
        digits = re.findall(r'\d|one|two|three|four|five|six|seven|eight|nine',line)
        mappedDigits = list(map(word_to_numb,digits))
        calibration += int(mappedDigits[0]+mappedDigits[-1])
        print(mappedDigits)
