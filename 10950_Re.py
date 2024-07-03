## list와 반목문을 이용한 input
# count = int(input())
# li = []
# for _ in range(count):
#     temp = list(map(int, input().split()))
#     if all(0 < x <= 10 for x in temp):
#         li.append(temp)
# for i in range(count):
#     print(sum(li[i]))
import sys

input = sys.stdin.read
data = input().split()
n = int(data[0])
result = []
index = 1
for _ in range(n):
    a = int(data[index])
    b = int(data[index + 1])
    result.append(a + b)
    index += 2
sys.stdout.write("\n".join(map(str, result)) + "\n")
