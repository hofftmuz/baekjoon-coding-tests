# 정수 X에 3가지 연산들을 사용해서 숫자 1을 만드는 것.
# 반복되는 방법을 통해서 특정 숫자로 만드는 것이고,
# 가장 적은 연산 횟수를 이용하는 것이 목표.
# 반복, 최솟값 => DP

# 3으로도 나뉘어지고, 2로도 나뉘어지는 상황
# 예를들어서 6인 경우
# 1.을 이용하는 경우 => 6 / 3 == 2 ->  2 - 1 == 1 or 2 / 2 == 1 (2회)
# 2.을 이용하는 경우 => 6 / 2 == 3 ->  3 / 3 == 1               (2회)
# 3.을 이용하는 경우 => 6 - 1 == 5 ->  5 - 1 == 4 -> 4 // 2 == 2 -> 2-1 (4회)

# dp[i] => X가 i일 때의 최소 연산 수.
# dp[i] = min(dp[i/3]+1, dp[i/2]+1,dp[i-1]+1)

# dp2[6] = [ 2, 2, ]
X = int(input())
dp2 = [[float("inf") for _ in range(4)] for _ in range(X + 1)]
dp2[0] = [0, 0, 0, 0]
dp2[1] = [0, 0, 0, 0]

"""
dp = [float("inf")] * (X + 1)
dp[0] = 0
"""

for i in range(2, X + 1):

    if i == 10:
        print(1)

    count = 0
    x = i
    if i % 3 == 0:
        j = 0
        count += 1
        x //= 3
        if x == 1:
            dp2[i][j] = count
        while x > 1:
            if x % 3 == 0:
                x //= 3
                count += 1
            elif x % 2 == 0:
                x //= 2
                count += 1
            else:
                x -= 1
                count += 1
            if x < 1:
                dp2[i][j] = float("inf")
            if x == 1:
                dp2[i][j] = count
                break
    elif i % 2 == 0:
        j = 1
        count += 1
        x //= 2
        if x == 1:
            dp2[i][j] = count
        while x > 1:
            if x % 3 == 0:
                x //= 3
                count += 1
            elif x % 2 == 0:
                x //= 2
                count += 1
            else:
                x -= 1
                count += 1
            if x < 1:
                dp2[i][j] = float("inf")
            if x == 1:
                dp2[i][j] = count
                break
    else:
        j = 2
        count += 1
        x -= 1
        if x == 1:
            dp2[i][j] = count
        while x > 1:
            if x % 3 == 0:
                x //= 3
                count += 1
            elif x % 2 == 0:
                x //= 2
                count += 1
            else:
                x -= 1
                count += 1
            if x < 1:
                dp2[i][j] = float("inf")
            if x == 1:
                dp2[i][j] = count
                break

    """
    for j in range(3):
    

        while x > 1:
            if x % 3 == 0:
                x //= 3
                # j = 0
                # count += 1
                dp2[i][j] += 1
            elif x % 2 == 0:
                x //= 2
                j = 1
                count += 1
            else:  # i -1 을 해야하는 경우
                x -= 1
                count += 1
            if x < 1:
                dp2[i][j] = float("inf")
            elif x == 1:
                dp2[i][j] = count
        """

    dp2[i][3] = min(dp2[i][0], dp2[i][1], dp2[i][2])

print(dp2[X][3])
# 값이 1로 만들어 지는 지 => 값을 1로 만들어서 확인하는 알고리즘이 필요
# ex :  '2' 를 1로 만드는 연산에 필요한 수 => 2. 연산 : 1회 , 3. 연산 : 1회
# 2 % 2 =0 and 2 // 2 == 0
# 2 - 1 == 0
# dp[2] = min(dp[2//3]+1,dp[2//2]+1,dp[2-1]+1)
#         min( dp[0]+1, )

# i == 10 =>  X == 10 => 1회 10//2  == 5  => 2회 5 - 1 == 4 => 3회  4//2 == 1
