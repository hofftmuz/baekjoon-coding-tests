import sys

data = sys.stdin.read().strip().split()
data = list(map(float, data))
count = int(data[0])
scores = data[1:]
max_value = max(scores)
normalized_scores = [(score / max_value) * 100 for score in scores]
average = sum(normalized_scores) / count
print(average)
