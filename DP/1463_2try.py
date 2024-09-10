X = int(input())
dp2 = [[float("inf") for _ in range(4)] for _ in range(X + 1)]
dp2[0] = [0, 0, 0, 0]
dp2[1] = [0, 0, 0, 0]

for i in range(2, X + 1):
    for j in range(3):
        count, x = 0, i
        if j == 0 and x % 3 == 0:
            x //= 3
            count += 1
            if x == 1:
                dp2[i][j] = count
                continue
            while x > 1:
                if x % 3 == 0:
                    x //= 3
                    count += 1
                elif x % 2 == 0:
                    x //= 2
                    count += 1
                else:
                    x -= 1
                    count += 1
                if x == 1:
                    dp2[i][j] = count
                elif x > 1:
                    continue
                else:
                    dp2[i][j] = float("inf")
        elif j == 1 and x % 2 == 0:
            x //= 2
            count += 1
            if x == 1:
                dp2[i][j] = count
                continue
            while x > 1:
                if x % 3 == 0:
                    x //= 3
                    count += 1
                elif x % 2 == 0:
                    x //= 2
                    count += 1
                else:
                    x -= 1
                    count += 1
                if x == 1:
                    dp2[i][j] = count
                elif x > 1:
                    continue
                else:
                    dp2[i][j] = float("inf")
        elif j == 2:
            x -= 1
            count += 1
            if x == 1:
                dp2[i][j] = count
                continue
            while x > 1:
                if x % 3 == 0:
                    x //= 3
                    count += 1
                elif x % 2 == 0:
                    x //= 2
                    count += 1
                else:
                    x -= 1
                    count += 1
                if x == 1:
                    dp2[i][j] = count
                elif x > 1:
                    continue
                else:
                    dp2[i][j] = float("inf")
    dp2[i][3] = min(dp2[i][0], dp2[i][1], dp2[i][2])

print(dp2[X][3])
