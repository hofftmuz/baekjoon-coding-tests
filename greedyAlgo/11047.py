# 동전을 적절히 사용해서 그 가치의 합을 K로 만들려고 한다.
# 이때 필요한 동전 개수의 최솟값을 구하는 프로그램을 작성하시오.
# N : 동전의 총 종류
# 가장 큰 것으로 많이 나눈 것으로 개수를 늘려나가는 방식으로 설계
import sys


def minNumOfCoin(n, k, arr):
    x = 0
    for i in range(n - 1, -1, -1):
        if k >= arr[i]:
            x = x + (k // arr[i])
            k = k % arr[i]
        if k == 0:
            break
    return x


def minNumOfCoin2(n, k, coins: list):
    dp = [float("inf")] * (k + 1)
    dp[0] = 0
    for i in range(1, k + 1):
        for coin in coins:
            if i - coin >= 0:
                dp[i] = min(dp[i - coin] + 1, dp[i])
    return dp[k] if dp[k] != float("inf") else -1


N, K = map(int, input().split())
coins = [int(input()) for _ in range(N)]
print(minNumOfCoin2(N, K, coins))
