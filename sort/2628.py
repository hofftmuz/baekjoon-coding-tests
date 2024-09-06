import sys

inputLines = sys.stdin.readlines()
data = [list(map(int, x.strip().split())) for x in inputLines]
rows, cols = data[0][1], data[0][0]
count = data[1][0]
cutingRows = [0, rows]
cutingCols = [0, cols]
for idx in range(2, 2 + count):
    direction, cutingLine = data[idx][0], data[idx][1]
    if direction == 0:
        cutingRows.append(cutingLine)
    else:
        cutingCols.append(cutingLine)
cutingRows.sort()
cutingCols.sort()
max_widht = max(cutingRows[i] - cutingRows[i - 1] for i in range(len(cutingRows)))
max_height = max(cutingCols[i] - cutingCols[i - 1] for i in range(len(cutingCols)))
print(max_widht * max_height)
