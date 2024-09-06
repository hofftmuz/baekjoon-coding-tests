import sys

datas = sys.stdin.read().strip().split("\n")
count = int(datas.pop(0))

arr = [[0 for _ in range(100)] for _ in range(100)]
for data in datas:
    if data.strip():
        row = list(map(int, data.strip().split()))
        x_min, y_min = row[0], row[1]
        for i in range(x_min, x_min + 10):
            for j in range(y_min, y_min + 10):
                arr[i][j] = 1
totalArea = sum(sum(row) for row in arr)
print(totalArea)


# count = 0
# arr = [[0 for _ in range(100)] for _ in range(100)]
# temp = []
# input = sys.stdin.read
# datas = input().split("\n")
# for data in datas:
#     if data.strip():
#         row = list(map(int, data.strip().split()))
#         t = [[x, x + 10] for x in row]
#         temp.append(t)

# for row in temp:
#     x_min = row[0][0]
#     x_max = row[0][1]
#     y_min = row[1][0]
#     y_max = row[1][1]
#     for i in range(x_min, x_max):
#         for j in range(y_min, y_max):
#             if arr[i][j] == 0:
#                 arr[i][j] = 1

# count = sum(sum(row) for row in arr)
# print(count)
