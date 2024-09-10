# 3kg , 5kg
# 18kg == 5kg * 3 + 3kg * 1
# 더 적은 봉지 개수를 들고 가는게 목표
# 그러면 일단 5kg 봉지로 최대한 채우고, 남는 걸 3kg로 채우는게 베스트 이긴한데

N = int(input())
result = 0
while N >= 0:
    if N % 5 == 0:
        result += N // 5
        print(result)
        break
    N -= 3
    result += 1
else:
    print(-1)
