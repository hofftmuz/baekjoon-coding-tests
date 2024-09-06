import sys

data = list(map(int, sys.stdin.read().strip().split()))
a1, b1, c1, a2, b2, c2 = data

# a*x + b*y = c
# d*x + e*y = f

det_a = a1 * b2 - a2 * b1
if det_a != 0:
    det_Ax = c1 * b2 - c2 * b1
    det_Ay = a1 * c2 - a2 * c1
    x = det_Ax // det_a
    y = det_Ay // det_a
    print(x, y)
