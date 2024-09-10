# X = int(input())
# # O(N) => 이중 루프는 사용하면 안될 거 같은데
# # for i <- 2 ~ N+1
# dp2 = [float("inf")] * (X + 1)
# dp2[0], dp2[1] = float("inf"), 0

# # 점화식 설계 =>
# # dp2[i] = min(dp2[i//3], dp2[i//2], dp2[i-1]) + 1

# # dp2[2] = min(dp2[0]+1, dp2[1]+1, dp2[1]+1)
# # dp2[3] = min(dp2[1]+1, dp[3//2]+1, dp2[3-1]+1) == min(1, inf, 2)

# for i in range(2, X + 1):

#     if i % 3 == 0:
#         x = i // 3
#     else:
#         x = 0
#     if i % 2 == 0:
#         y = i // 2
#     else:
#         y = 0
#     if i - 1 > 0:
#         z = i
#         z = z - 1
#     else:
#         z = 0
#     dp2[i] = min(dp2[x], dp2[y], dp2[z]) + 1
# print(dp2[X])


def countForMakingOne(X: int):
    dp2 = [float("inf")] * (X + 1)
    dp2[0], dp2[1] = float("inf"), 0
    for i in range(2, X + 1):
        if i % 3 == 0:
            x = i // 3
        else:
            x = 0
        if i % 2 == 0:
            y = i // 2
        else:
            y = 0
        if i - 1 > 0:
            z = i
            z = z - 1
        else:
            z = 0
        dp2[i] = min(dp2[x], dp2[y], dp2[z]) + 1
    return dp2[X]
X = int(input())
print(countForMakingOne(X))
