# 원래 설정되어 있는 알람을 45분 앞서는 시간으로 바꾸는 것 => -45분 
## 첫째 줄에 두 정수 H,M

# h,m = map(int,input().split())
# if 0 <= h <= 23 and 0 <= m <= 59 :
#     if m - 45 < 0 :
#         if h == 0 :
#             h = 23  
#             print(f"{h} {m+60-45}")
#         else :
#             print(f"{h-1} {m+60-45}")
#     else :
#         print(f"{h} {m-45}")

h,m = map(int,input().split())
if m >= 45:
    m -= 45
else:
    m += 15
    h -= 1
    if h < 0:
        h = 23
print(h,m)