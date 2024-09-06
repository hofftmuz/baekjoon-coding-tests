import sys

data = list(map(int, sys.stdin.read().split()))
n, m = data.pop(0), data.pop(0)
matrix1 = data[: n * m]
matrix2 = data[n * m :]
for i in range(n):
    row = [matrix1[i * m + j] + matrix2[i * m + j] for j in range(m)]
    print(" ".join(map(str, row)))

"""
Using Numpy 

import sys
import numpy as np

data = list(map(int, sys.stdin.read().strip().split()))
n, m = data.pop(0), data.pop(0)
m1 = np.array(data[: n * m], dtype=int).reshape(n, m)
m2 = np.array(data[n * m :], dtype=int).reshape(n, m)

result = m1 + m2
for row in result:
    print(" ".join(map(str, row)))

"""
