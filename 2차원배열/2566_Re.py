import numpy as np
import sys


data = list(map(int, sys.stdin.read().split()))
max_value = -float("inf")
max_idx = (0, 0)

for i in range(9):
    for j in range(9):
        val = data[i * 9 + j]
        if val > max_value:
            max_value = val
            max_idx = (i + 1, j + 1)
print(max_value)
print(max_idx[0], max_idx[1])

"""
data = list(map(int, sys.stdin.read().split()))
idx = np.max(data)
data = np.array(data, dtype=int).reshape(9, 9)
i = np.argmax(data)
idx2 = np.unravel_index(i, data.shape)
print(np.max(data))
print(idx2[0] + 1, idx2[1] + 1)
"""