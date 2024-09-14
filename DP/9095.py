import sys

inputLines = sys.stdin.read()
data = list(map(int, inputLines.strip().split()))
T = data.pop(0)
maxValue = max(data)
dp = [0] * (maxValue + 1)
dp[1], dp[2], dp[3] = 1, 2, 4
for i in range(4, maxValue + 1):
    dp[i] = dp[i - 1] + dp[i - 2] + dp[i - 3]
for x in data:
    print(dp[x])
