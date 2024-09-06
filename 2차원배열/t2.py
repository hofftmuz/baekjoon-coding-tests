import sys
import numpy as np

"""
data = list(map(int, sys.stdin.read().strip().split()))
n, m = data.pop(0), data.pop(0)
m1 = np.array(data[: n * m], dtype=int).reshape(n, m)
m2 = np.array(data[n * m :], dtype=int).reshape(n, m)

result = m1 + m2
for row in result:
    print(" ".join(map(str, row)))
"""

arr = np.zeros((100, 100), dtype=int)
arr2 = [[0 for _ in range(10)] for _ in range(10)]


def main():
    arr = [[0 for _ in range(100)] for _ in range(100)]
    datas = sys.stdin.read().strip().split("\n")
    count = int(datas.pop(0))

    for data in datas:
        if data.strip():
            row = list(map(int, data.strip().split()))
            x_min, y_min = row[0], row[1]
            for i in range(x_min, x_min + 10):
                for j in range(y_min, y_min + 10):
                    arr[i][j] = 1

    totalArea = sum(sum(row) for row in arr)

    print(totalArea)


if __name__ == "__main__":
    main()
