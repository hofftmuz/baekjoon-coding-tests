import sys

data = list(map(int, sys.stdin.read().strip().split()))
length, count = data[0], data[1]
data = data[2:]
data.sort(reverse=True)
print(data[count - 1])
