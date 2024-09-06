import sys

data = sys.stdin.read().strip().split()
num, base = int(data.pop(0)), int(data.pop(0))
dict = {i: str(i) for i in range(10)}
dict.update({i + 10: chr(65 + i) for i in range(0, 26)})
result = []
while num > 0:
    x = num % base
    result.append(dict[x])
    num //= base
result.reverse()
print("".join(map(str, result)))
