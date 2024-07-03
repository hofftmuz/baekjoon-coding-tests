import sys

lines = sys.stdin.readlines()
lines = [line.strip() for line in lines]
for i in range(len(lines)):
    a, b = map(int, lines[i].split())
    print(a + b)
