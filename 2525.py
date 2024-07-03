# 시작하는 시각과 오븐 구이를 하는데 필요한 시간이 분 단위로 주어졌을 때, 끝나는 시각을 계산하는 프로그램.
# / : 두 숫자를 나눌 때 사용되며, 결과는 항상 부동 소수점값으로 반환됨. 즉 실수형이됨.
# // : 몫 계산
# % : 나머지 계산


# a,b = map(int,input().split())
# c = int(input())
# if 0 <= a <= 23 and 0<= b <= 59 and 0 <= c <= 1000 :
#     if b + c < 60 :
#         print(f"{a} {b+c}")
#     else:
#         a = a + (b+c)//60
#         b = int((b+c) % 60)
#         if a >= 24 :
#             a = a - 24
#         print(f"{a} {b}")
        
h,m = map(int,input().split())
c = int(input())
total_minutes = h*60+m
total_minutes += c
new_h = (total_minutes//60)%24
new_m = (total_minutes%60)
print(new_h, new_m)