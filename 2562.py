# 9개의 서로 다른 자연수가 주어질 때, 이들 . 중최댓값을 찾고 . 그최댓값이 몇 번째 수인지를 구하는 문제.
# 입력은 9개의 줄에 걸쳐 하나씩 주어지며, 각 줄에는 하나의 자연수가 있음.
# ls = []
# for i in range(9):
#     temp = int(input())
#     ls.append(temp)
# max_value = max(ls)
# ls_index = ls.index(max_value)
# print(max_value)
# print(ls_index + 1)

import sys

numbers = [int(sys.stdin.readline().strip()) for _ in range(9)]
max_value = max(numbers)
max_index = numbers.index(max_value) + 1
print(max_value, max_index, sep="\n")
