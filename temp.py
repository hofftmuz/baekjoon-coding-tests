import sys

data = sys.stdin.read().strip().split()
count, index = int(data[0]), 1
for _ in range(count):
    c = int(data[index])
    temp = data[index + 1]
    result = "".join(digit * c for digit in temp)
    print(result)
    index += 2
