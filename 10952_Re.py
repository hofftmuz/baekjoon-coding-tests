import sys

lines = []
while True:
    line = sys.stdin.readline().strip()
    if line == "0 0":
        break
    lines.append(line)
index_count = int(len(lines))
for i in range(0, index_count):
    a, b = map(int, lines[i].split())
    print(a + b)

# sys.stdin.readlines()에서 '\n'를 제외하고 리스트화시키는 방법
# lines = sys.stdin.readlines()
# lines = [ line.strip() for line in lines]