# import sys


# data = sys.stdin.read().strip().split()
# N = int(data.pop())
# dict = {}
# result = 1
# for i in range(10, N):
#     digit = chr(65 + i - 10)
#     dict[digit] = i + 1
# for x in data[0]:
#     if x in dict:
#         temp = dict[x]
#     else:
#         temp = int(x)
#     result *= temp
# print(result)


import sys

data = sys.stdin.read().strip().split()
base = int(data.pop())
num = data[0]
result = 0
power = 1
dict = {str(i): i for i in range(10)}
dict.update({chr(65 + i): 10 + i for i in range(26)})

for x in reversed(num):
    result += dict[x] * power
    power *= base
print(result)


# import sys

# data = sys.stdin.read().strip().split()
# num = data[0]
# base = int(data[1])
# result = int(num, base)
# print(result)

""" 

Python - dictionary - update 메서드 
update()  다른 딕셔너리나 키-값 쌍의 이터러블을 사용하여 기존 딕셔너리에 요소 추가나 갱신.

"""
