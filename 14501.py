import sys

inputLines = sys.stdin.readlines()
data = [list(map(int, x.strip().split())) for x in inputLines]
# #key : Ti , value Pi =>
# N = data.pop(0)[0]
# dict_d = {}
# for x in data:
#     Ti,Pi = x[0],x[1]
#     dict_d[Ti]= Pi

# for i in range(N+1):
# DP _
N = data.pop(0)[0]
T = []
P = []
for x in data:
    T.append(x[0])
    P.append(x[1])

dp = [0] * (N + 1)
for i in range(N - 1, -1, -1):
    if i + T[i] <= N:
        dp[i] = max(dp[i + 1], P[i] + dp[i + T[i]])
    else:
        dp[i] = dp[i + 1]
print(dp[0])

# index를 조금 더 직관적으로 이해할 수 있도록 설정하고싶은데
