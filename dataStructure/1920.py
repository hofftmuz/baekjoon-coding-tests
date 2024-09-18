import sys

N = int(input())
sol = set(map(int, sys.stdin.readline().strip().split()))
M = int(input())
pro = list(map(int, sys.stdin.readline().strip().split()))
for x in pro:
    if x in sol:
        print(1)
    else:
        print(0)
