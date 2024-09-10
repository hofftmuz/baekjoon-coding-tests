N = int(input())
count, x = 0, 666
while True:
    if "666" in str(x):
        count += 1
    if count == N:
        print(x)
        break
    x += 1
