import sys

data = sys.stdin.read().strip()
lines = data.splitlines()
index_count = int(lines[0])
for i in range(1, index_count + 1):
    a, b = map(int, lines[i].split())
    print(f"Case #{i}: {a+b}")
