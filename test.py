import sys

# input = sys.stdin.read
# data = input()
# lines = data.splitlines()
# t = int(lines[0])
# results = []
# for i in range(1, t + 1):
#     a, b = map(int, lines[i].split())
#     results.append()
# sys.stdout.write("\n".join(map(str, results)) + "\n")
"""
my_list = [0, 0, 0, 0, 0]  # 예시로 초기화된 리스트
i = 1
j = 4
# 인덱스 1부터 3까지의 범위에 모두 1 할당
my_list[i:j] = [1] * (j - i)

print(my_list)  # 출력: [0, 1, 1, 1, 0]
"""

import sys

input = sys.stdin.read
data = input().split()
n = int(data[0])
m = int(data[1])
basket = [0] * (n + 1)
index = 2
for _ in range(m):
    i, j, k = int(data[index]), int(data[index + 1]), int(data[index + 2])
    basket[i : j + 1] = [k] * (j - i + 1)
    index += 3
print(" ".join(map(str, basket[1:])))
