import sys


def find_generator(N):
    start = max(1, N - 9 * len(str(N)))
    for i in range(start, N):
        sumOfdigit = sum(int(digit) for digit in str(i))
        if i + sumOfdigit == N:
            return i
    return 0


data = sys.stdin.read().strip()
targVal = int(data)
print(find_generator(targVal))
