import sys

data = sys.stdin.read().strip().split()
print(
    int(data[0][::-1])
    if int(data[0][::-1]) > int(data[1][::-1])
    else int(data[1][::-1])
)

"""

C 스타일의 삼항 연산자 vs Python 스타일 조건부 표현식

1.
int max = (x>y) ? x : y

2.
max_value = x if x > y else y
x, y = (y, x) if x > y else (x, y)

"""
