def CalChange(n):
    changes = [25, 10, 5, 1]
    result = []
    for change in changes:
        result.append(n // change)
        n %= change
    print(" ".join(map(str, result)))


import sys

input = sys.stdin.read
data = list(map(int, input().strip().split()))
n = data.pop(0)
for i in range(n):
    CalChange(data[i])


# import sys
# def CalChange(n: int):
#     changes = [25, 10, 5, 1]
#     result = []
#     for i in range(len(changes)):
#         if n // changes[i] < 1:
#             result.append(0)
#             continue
#         quot = n // changes[i]
#         result.append(int(quot))
#         n = n - quot * changes[i]
#     print(" ".join(map(str, result)))


# input = sys.stdin.read
# data = list(map(int, input().strip().split()))
# n = data.pop(0)
# for i in range(n):
#     CalChange(data[i])
