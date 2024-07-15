data = input().strip()
length = len(data)
result = 1
for i in range(length // 2):
    if data[i] != data[length - 1 - i]:
        result = 0
        break
print(result)


"""
스택을 이용한 구현

data = input().strip()
n = len(data)
stack = []
for i in range(n // 2):
    stack.append(data[i])
start_index = n // 2
if n % 2 == 1:
    start_index += 1
is_palindrome = True
for i in range(start_index, n):
    if stack.pop() != data[i]:
        is_palindrome = False
        break
print(1 if is_palindrome else 0)
"""
