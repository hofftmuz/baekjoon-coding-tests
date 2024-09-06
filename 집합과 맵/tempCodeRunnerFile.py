import sys

data = sys.stdin.read().splitlines()
n, m = int(data[0].split()[0]), int(data[0].split()[1])
s1, s2 = set(), set()
for i in range(1, len(data)):
    if i >= 1 and n + 1 > i:
        s1.add(data[i])
    else:
        s2.add(data[i])

result = []
minLength = min(n, m)
if minLength == n:
    for x in s1:
        if x in s2:
            result.append(x)
else:
    for x in s2:
        if x in s1:
            result.append(x)
print(len(result))
print("\n".join(sorted(result)))