import sys


def isGroupword(word):
    temp = set()
    lastWord = ""
    for digit in word:
        if digit != lastWord:
            if digit in temp:
                return False
            temp.add(digit)
            lastWord = digit
    return True


def countGroupword(n, words):
    result = 0
    for i in range(n):
        if isGroupword(words[i]):
            result += 1
    return result


data = sys.stdin.read().strip().split()
count = int(data.pop(0))
print(countGroupword(count, data))
