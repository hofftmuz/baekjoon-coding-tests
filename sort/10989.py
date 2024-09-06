# 시간 제한 5초 => O(N log N)
# 메모리 제한 8MB  ( 1<= N <= 10,000,000)
#  value <= 10,000
#  MAX : 4 Byte * 10,000,000
#   40,000,000 / 1024 = 39062KB == 39062 / 1024 == 38MB
import sys


def countingSort(arr):
    maxValue = 10000
    count = [0] * (maxValue + 1)
    for num in arr:
        count[num] += 1
    sorted_arr = []
    for i, cnt in enumerate(count):
        sorted_arr.extend([i] * cnt)

    return sorted_arr


inputLines = sys.stdin.readlines()
data = [int(x.strip()) for x in inputLines]
result = countingSort(data)
print("\n".join(map(str, result)))
