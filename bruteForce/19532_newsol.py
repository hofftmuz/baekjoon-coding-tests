import sys

data = list(map(int, sys.stdin.read().strip().split()))
a, b, c, d, e, f = data
for x in range(-999, 1000):
    for y in range(-999, 1000):
        if a * x + b * y == c and d * x + e * y == f:
            print(x, y)
            exit()
