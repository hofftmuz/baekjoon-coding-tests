import sys

data = sys.stdin.read().strip().split()
n = int(data[0])
for i in range(1, n + 1):
    temp = data[i]
    print(temp[0], temp[-1], sep="")
