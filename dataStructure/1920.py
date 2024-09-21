import sys

N = int(input())
sol = set(map(int, sys.stdin.readline().strip().split()))
M = int(input())
pro = list(map(int, sys.stdin.readline().strip().split()))
for x in pro:
    if x in sol:
        print(1)
    else:
        print(0)

# 이분 탐색을 이용한 풀이 ( 정렬 + 이분 탐색)
from bisect import bisect_left

N = int(input())
sol = sorted(list(map(int, sys.stdin.readline().strip().split())))


# 이분 탐색 함수
def binary_search(arr, target):
    idx = bisect_left(arr, target)  # 이분 탐색으로 찾을 위치
    if idx < len(arr) and arr[idx] == target:  # 찾은 위치의 값이 타겟과 같으면 존재
        return 1
    else:
        return 0


# M개의 정수 입력 받기
M = int(input())  # 세 번째 입력: M
pro = list(
    map(int, sys.stdin.readline().strip().split())
)  # 네 번째 입력: M개의 정수 저장

# 각 정수에 대해 이분 탐색 수행
for x in pro:
    print(binary_search(sol, x))
