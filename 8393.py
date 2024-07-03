n = int(input())
if 1 <= n <= 10000:
    sum = 0
    for i in range(1, n + 1):
        sum += i
    print(sum)
