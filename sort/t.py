width, height = map(int, input().split())
n = int(input())
cut_width = [0, width]
cut_height = [0, height]
for _ in range(n):
    direction, position = map(int, input().split())
    if direction == 0:
        cut_height.append(position)
    else:
        cut_width.append(position)

cut_width.sort()
cut_height.sort()
max_width = max(cut_width[i] - cut_width[i - 1] for i in range(1, len(cut_width)))
max_height = max(cut_height[i] - cut_height[i - 1] for i in range(1, len(cut_height)))
print(max_width * max_height)
