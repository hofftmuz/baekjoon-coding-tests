# 입출력 방식이 느리면 여러 줄을 입력받거나 출력할 때 시간 초과가 날 수 있다는 점.
# import sys

# data = sys.stdin.read().strip()
# lines = data.splitlines()
# t = int(lines[0])
# for i in range(1, t + 1):
#     temp = lines[i].split()
#     print(int(temp[0]) + int(temp[1]))

import sys

input = sys.stdin.read
data = input()
lines = data.splitlines()
t = int(lines[0])
result = []
for i in range(1, t + 1):
    a, b = map(int, lines[i].split())
    result.append(a + b)
sys.stdout.write("\n".join(map(str, result)) + "\n")
