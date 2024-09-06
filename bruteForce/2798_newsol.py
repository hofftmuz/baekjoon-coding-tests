# Brute Force 최적화 :
# 1.
#   삼중 반복문 대신 Combinations 함수를 사용하여 코드의 가독성을 높이고, 불필요한 Continue문을 제거
#   Itertools 모듈의 combinations 함수를 사용하면 더 깔끔하게 코드 작성 가능.
# 2.
#   조기 종료 : 합이 목표 값과 같으면 바로 결과를 출력하고 종료하도록 하여 불필요한 연산을 줄임.
"""
import sys
from itertools import combinations
data = list(map(int, sys.stdin.read().strip().split()))
length, targetVal = data.pop(0), data.pop(0)
maxVal = 0
for comb in combinations(data, 3):
    sumval = sum(comb)
    if sumval == targetVal:
        maxVal = sumval
        break
    if sumval < targetVal:
        maxVal = max(maxVal, sumval)
print(maxVal)
"""
import sys
from itertools import combinations

data = list(map(int, sys.stdin.read().strip().split()))
length, targetVal = data.pop(0), data.pop(0)
maxVal = 0
for comb in combinations(data, 3):
    sumval = sum(comb)
    if sumval <= targetVal:
        maxVal = max(maxVal, sumval)

print(maxVal)
