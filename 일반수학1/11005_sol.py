import sys


def to_base_b(n, b):
    digits = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    result = []

    if n == 0:
        return "0"
    while n > 0:
        remainer = n % b
        result.append(digits[remainer])
        n //= b
    return "".join(result[::-1])


def main():
    input = sys.stdin.read()
    n, b = map(int, input().strip().split())
    print(to_base_b(n, b))


if __name__ == "__main__":
    main()

# import sys

# data = sys.stdin.read().strip().split()
# num, base = int(data[0]), int(data[1])
# digits = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
# result = []

# # num이 0인 경우 특별 처리
# if num == 0:
#     result.append("0")
# else:
#     while num > 0:
#         result.append(digits[num % base])
#         num //= base

# # 결과를 뒤집어서 출력
# print("".join(result[::-1]))
