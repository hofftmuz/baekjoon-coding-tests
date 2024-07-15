import sys

data = sys.stdin.read().strip().split()
length, number_string = int(data[0]), data[1]
sum = 0
for i in range(length):
    temp = int(number_string[i])
    sum += temp
print(sum)

"""
import sys

data = sys.stdin.read().strip().split()
length, number_string = int(data[0]), data[1]
total_sum = sum(int(digit) for digit in number_string)
print(total_sum)

"""
