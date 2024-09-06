import sys

input = sys.stdin.read
data = list(map(int, input().strip().split()))
ownLength = data[0]
testLength = data[ownLength + 1]
ownCard = set(data[1 : ownLength + 1])
testCard = data[ownLength + 2 :]
result = {}
for x in testCard:
    if x in ownCard:
        result[x] = 1
    else:
        result[x] = 0
print(" ".join(map(str, result.values())))
