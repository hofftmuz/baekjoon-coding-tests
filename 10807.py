# 총 N개의 정수가 주어졌을 때, 정수 v가 몇 개인지 구하는 프로그램을 작성하시오.

count = int(input())
data = list(map(int, input().split()))
x = int(input())
print(data.count(x))
