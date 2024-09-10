import sys

inputLines = sys.stdin.read()
data = list(map(int, inputLines.strip().split()))

# 점화식 설정
# dp[1] = 1 , dp[2] = 1+1,2 , dp[3] = 1+1+1+1, 1+1+2, 1+2+1, 2+1+1, 2+2, 1+3, 3+1
# 합의 내용을 유지해야하냐 아니면 개수만으로도 가능하냐

T = data.pop(0)
maxVal = max(data)
dp = [[] for _ in range(len(maxVal))]
dp[0][0] = 0
for i in range(1, data[T]):
    dp[1] = dp[1] + 1
