# import sys

# data = sys.stdin.read().strip().split()
# count, j = int(data[0]), 1
# for i in range(count):
#     temp   = data[j + 1]
#     c = int(data[j])
#     # for digit i n temp:
#     #     # print(    digit * c)
#     print("".join(digit * c for digit in temp))
#     j += 2

import sys

data = sys.stdin.read().strip().split()
count, j = int(data[0]), 1
for i in range(count):
    print("".join(digit * int(data[j]) for digit in data[j + 1]))
    j += 2
0
"""
import sys

data = sys.stdin.read().strip().split()
test_case_count , index = int(data[0]), 1
for _ in range(test_case_count):
    repeat_count = int(data[index])
    string_to_repeat = data[index+1]
    result = ''.join(char * repeat_count for char in string_to_repeat)
    print(result)
    index += 2
"""
