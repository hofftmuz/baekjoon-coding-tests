# 윤년은 연도가 4의 배수이면서, 100의 배수가 아닐 때 또는 400의 배수일 때
## 4의 배수 =>  year % 4 == 0 and ( year % 100 != 0 or year % 400 == 0 )
year = int(input())
if 1 <= year <= 4000 and (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
    print(1)
else:
    print(0)
