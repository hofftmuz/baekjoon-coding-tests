"""
import sys

data = list(map(int, sys.stdin.read().strip().split()))
length, targetVal = data.pop(0), data.pop(0)
maxVal = 0
ls = []

for i in range(length):
    sumval = 0
    for j in range(i + 1, length):
        for k in range(j + 1, length):
            sumval = data[i] + data[j] + data[k]
            if sumval > targetVal:
                continue
            ls.append(sumval)
maxVal = max(ls)
print(maxVal)

"""

# 최적화

import sys

data = list(map(int, sys.stdin.read().strip().split()))
length, targetVal = data.pop(0), data.pop(0)
maxVal = 0
for i in range(length):
    for j in range(i + 1, length):
        for k in range(j + 1, length):
            sumVal = data[i] + data[j] + data[k]
            if sumVal <= targetVal:
                maxVal = max(maxVal, sumVal)
print(maxVal)

# 리스트 ls를 사용하지 않고 바로 maxVal을 갱신해서 메모리 사용량을 최적화.
# 조건문 최적화
