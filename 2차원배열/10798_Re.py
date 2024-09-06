import sys

# rows 와 cols가 몇 몇인지 알지 못할 때 + 행마다 열의 개수가 다르게 존재할 때

data = sys.stdin.read().strip().split()
result = []
max_cols = max(len(word) for word in data)
for i in range(max_cols):
    for word in data:
        if i < len(word):
            result.append(word[i])
print("".join(map(str, result)))
