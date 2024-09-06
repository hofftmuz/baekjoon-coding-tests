import sys

data = sys.stdin.read().strip()
targVal = int(data)
returnVal = 0
for i in range(1, targVal):
    sumOfdigit = sum(int(digit) for digit in str(i))
    if i + sumOfdigit == targVal:
        returnVal = i
        break
print(returnVal)
