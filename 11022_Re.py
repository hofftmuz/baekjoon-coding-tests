import sys

count = int(input())
data = sys.stdin.read().strip()
lines = data.splitlines()

for i in range(len(lines)):
    a, b = map(int, lines[i].split())
    print(f"Case #{i+1}: {a} + {b} = {a+b}")
