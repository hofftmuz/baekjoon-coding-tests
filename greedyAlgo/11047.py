# 동전을 적절히 사용해서 그 가치의 합을 K로 만들려고 한다. 이때 필요한 동전 개수의 최솟값을 구하는 프로그램을 작성하시오.
# N : 동전의 총 종류
# 일단 가장 큰 것으로 많이 나눈 것으로 개수를 늘려나가는 방식으로 설계
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


inputLines = list(map(int, sys.stdin.read().strip().split()))
N, K = inputLines[0:2]
print(minNumOfCoin(N, K, inputLines[2:]))
