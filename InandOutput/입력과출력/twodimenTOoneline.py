# 이차원 배열 형태로 입력받은 숫자를 한 줄로 공백으로 구분하여 출력

rows,cols = map(int,input("Enter the number of rows and columns: ").split())
matrix=[]
result = []
for _ in range(rows):
    row = list(map(int,input().split()))
    matrix.append(row)

for row in matrix:
    result.extend(row)

print(" ".join(map(str,result)))
