# 총 N개의 바구니( 1 - N 번 ), 한 바구니에는 공을 1개만 넣을 수 있다.
# M번 공을 넣으려고함. 공을 넣을 바구니의 범위-> 정한 바구니에 모두 같은 번호가 적혀있는 공을 넣음
# 만약 바구니에 공이 이미 들어잇는 경우, 공을 빼고 새로 공을 넣는다.
# 공을 넣을 바구니는 연속되어 있어야 한다.
length, count = map(int, input().split())
ls = [0 for _ in range(length)]
# ls = [0] * length
for _ in range(count):
    start_index, end_index, value = map(int, input().split())
    ls[start_index - 1 : end_index] = [value] * (end_index - start_index + 1)
print(" ".join(map(str, ls)))


# 리스트 슬라이싱으로 초기화,인덱스 관리하는 법
# 1. ls = [0 for _ in range(length)] 2. ls = sys.stdin.read.split()
# 0 번 인덱스는 사용하지 않고 , 기존 배열보다 하나 더 크게 만들고-> basket[i:j+1] => i는 포함, j+1은 j까지 포함
#
""" 
import sys
input = sys.stdin.read
data = input().split()
n = int(data[0])
m = int(data[1])

basket = [0] * (n+1)
index = 2
for _ in range(m):
    i = int(data[index])
    j = int(data[index+1])
    k = int(data[index+2])
    basket[i:j+1]=[k]*(j-i+1)
    index += 3

print(" ".join(map(str,basket[1:])))
"""
