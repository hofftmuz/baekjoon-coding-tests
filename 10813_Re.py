import sys

# 에러 1 => sys.stdin.read().split() 으로 할 경우 리스트에 들어가는 값들이 str
"""
index_data = sys.stdin.read().split()
length, count = index_data[0], index_data[1]
ls = [i for i in range(0, length + 1)]
print(ls)
"""
index_data = list(map(int, sys.stdin.read().split()))
length, count = index_data[0], index_data[1]
ls = [i for i in range(0, length + 1)]
# basket = list(range(length+1))
index = 2
for _ in range(count):
    ls[index_data[index]], ls[index_data[index + 1]] = (
        ls[index_data[index + 1]],
        ls[index_data[index]],
    )
    index += 2
print(" ".join(map(str, ls[1:])))
