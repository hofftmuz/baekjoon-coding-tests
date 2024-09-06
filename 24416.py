recursive_count = 0


def fib_recursive(n):
    global recursive_count
    if n == 1 or n == 2:
        recursive_count += 1
        return 1
    else:
        return fib_recursive(n - 1) + fib_recursive(n - 2)


def fib_dp(n):
    dp_count = 0
    dp = [0] * (n + 1)
    dp[1] = dp[2] = 1
    for i in range(3, n + 1):
        dp[i] = dp[i - 1] + dp[i - 2]
        dp_count += 1
    return dp[n], dp_count


n = int(input())
fib_recursive(n)
_, dp_count = fib_dp(n)
print(recursive_count, dp_count)
