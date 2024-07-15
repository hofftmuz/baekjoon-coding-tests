import sys

data = sys.stdin.read().strip().split()
word, index = data[0], int(data[1])
print(word[index - 1])
