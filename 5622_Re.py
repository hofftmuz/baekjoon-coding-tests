# 알파벳에 대한 분석 -> 이를 통해서 시간 계산
import sys

"""
time = 0
data = sys.stdin.read().strip()
dial_mapping = {
    "A": 3,
    "B": 3,
    "C": 3,
    "D": 4,
    "E": 4,
    "F": 4,
    "G": 5,
    "H": 5,
    "I": 5,
    "J": 6,
    "K": 6,
    "L": 6,
    "M": 7,
    "N": 7,
    "O": 7,
    "P": 8,
    "Q": 8,
    "R": 8,
    "S": 8,
    "T": 9,
    "U": 9,
    "V": 9,
    "W": 10,
    "X": 10,
    "Y": 10,
    "Z": 10,
}
for digit in data:
    time += dial_mapping[digit]
print(time)
"""


dic = {
    "A B C": 3,
    "D E F": 4,
    "G H I": 5,
    "J K L": 6,
    "M N O": 7,
    "P Q R S": 8,
    "T U V": 9,
    "W X Y Z": 10,
}
input_string = sys.stdin.read().strip()


def calculate_time(dial_dict, input_string):
    total_time = 0

    for char in input_string:
        for key in dial_dict:
            if char in key.split():
                total_time += dial_dict[key]
                break
    return total_time


total_time = calculate_time(dic, input_string)
print(total_time)
"""
key로 여러 개의 Digit을 설정해놓았을 때 들어온 문자열의 값과
비교하기 위해서 어떻게 해야하나 고민하고 있었는데
중첩 Loop로 사용하고 in 메소드와 split을 사용해서 문제를 해결.
"""
