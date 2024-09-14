import sys


def calShortestTime(arr: list):
    x = 0
    for i in range(len(arr)):
        temp = sum(arr[: i + 1])
        x += temp
    return x


inputLines = sys.stdin.readlines()
data = [list(map(int, line.strip().split())) for line in inputLines]
sortedData = sorted(data[1], reverse=False)
print(calShortestTime(sortedData))
