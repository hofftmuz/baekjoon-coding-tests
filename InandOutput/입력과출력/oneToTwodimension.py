rows,cols = map(int,input("cols,rows : ").split())
matrix = []
# for _ in range(rows):
#     row = list(map(int,input().split()))
#     matrix.append(row)
# result = []
# for row in matrix:
#     result.extend(row)
# print(" ".join(map(str,result)))

for _ in range(rows):
    row = list(map(int,input().split()))
    matrix.append(row)

for row in matrix:
    print(" ".join(map(str,row)))