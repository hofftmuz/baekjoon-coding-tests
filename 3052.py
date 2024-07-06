"""
# 배열 안에서 서로 다른 요소 개를 세는 가장 효과적인 방법
# 1. set 2. 리스트 내포를 사용하여 각 요소의 개수를 세기 3. 딕셔너리를 사용하여 각 요소의 개수 세기

1.
s = set()

2.
unique_numbers = []
for num in numbers:
    if num not in unique_numbers:
        unique_numbers.append(num)
print(len(unique_numbers))
        

3.
frequency = {}
for num in numbers:
    if num in frequency: # num이 이미 딕셔너리의 키로 존재하면
        frequency[num] += 1 #해당 값에 1을 더함.
    else:  # 만약 num이 딕셔너리의 키로 존재하지 않으면 
        frequency[num] = 1 # 해당 값을 1로 설정한다.
print(len(frequency))

"""

import sys

data = sys.stdin.read().strip().split()
data = list(map(int, data))
s = set()
for i in range(len(data)):
    s.add(data[i] % 42)
print(len(s))
