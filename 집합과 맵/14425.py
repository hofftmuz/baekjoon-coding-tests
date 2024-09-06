# import sys

# input = sys.stdin.read
# data = input().strip().split()
# n, m = int(data[0]), int(data[1])
# stringInS = set(data[2 : 2 + n])
# stringForTest = data[2 + n :]
# result = 0
# for x in stringForTest:
#     if x in stringInS:
#         result += 1
# print(result)


def main():
    import sys

    input = sys.stdin.read
    data = input().split()
    n, m = int(data[0]), int(data[1])
    stringInS = set(data[2 : n + 2])
    result = sum(1 for x in data[n + 2 :] if x in stringInS)
    print(result)
if __name__ == "__main__":
    main()
