# M : 들어오는 전체 개수 ,  N: 맞춰야하는 문제 수
# M개 이후 숫자로 들어온 것은 포켓몬 이름으로, 포켓몬 이름으로 들어온 것은 숫자로

# import sys

# inputLines = sys.stdin.readlines()
# data = [line.strip() for line in inputLines]
# m, n = int(data[0].split()[0]), int(data[0].split()[1])
# ls = data[1 : m + 1]
# prob = data[m + 1 :]
# dictData1 = {index: value for index, value in enumerate(ls, start=1)}
# dictData2 = {value: index for index, value in enumerate(ls, start=1)}
# for x in prob:
#     try:
#         idx = int(x)
#     except:
#         print(dictData2[x])
#     else:
#         print(dictData1[idx])


import sys

input = sys.stdin.read
data = input().splitlines()
m, n = map(int, data[0].split())
ls = data[1 : m + 1]
prob = data[m + 1 :]
dictData1 = {str(i + 1): ls[i] for i in range(m)}
dictData2 = {ls[i]: str(i + 1) for i in range(m)}

for x in prob:
    if x.isdigit():
        print(dictData1[x])
    else:
        print(dictData2[x])
