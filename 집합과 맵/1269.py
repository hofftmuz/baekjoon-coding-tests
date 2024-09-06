# import sys

# data = sys.stdin.read().strip().split()
# numberOfa, numberOfb = int(data[0]), int(data[1])
# a = set(data[2 : numberOfa + 2])
# b = set(data[2 + numberOfa :])
# result = a ^ b
# print(len(result))

import sys

inputLines = sys.stdin.readlines()
data = [list(map(int, x.strip().split())) for x in inputLines]
a = set(data[1])
b = set(data[2])
print(len(a ^ b))
