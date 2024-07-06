# 바구니 뒤집기
# ex : 5 4
# 5: 총 5개의 바구니
# 4: 바구니를 역순으로 바꿀 횟수.
import sys

data = sys.stdin.read().strip().split()
data = list(map(int, data))
basket_range, count = data[0], data[1]
basket = [x for x in range(0, basket_range + 1)]
index = 2
for _ in range(count):
    i = data[index]
    j = data[index + 1]
    basket[i : j + 1] = basket[i : j + 1][::-1]
    index += 2
print(" ".join(map(str, basket[1 : basket_range + 1])))
