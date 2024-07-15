"""
count = int(input())
j = 1
ls = []
for i in range(1, count * 2, 2):
    result = " " * (count - j) + "*" * i
    ls.append(result)
    print(result)
    j += 1
ls.pop()
ls.reverse()
for i in range(len(ls)):
    print(ls[i])
"""

n = int(input())
for i in range(1, n + 1):
    print(" " * (n - i) + "*" * (2 * i - 1))
for i in range(n - 1, 0, -1):
    print(" " * (n - i) + "*" * (2 * i - 1))
