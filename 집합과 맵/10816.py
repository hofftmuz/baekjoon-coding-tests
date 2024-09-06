# import sys

# data = sys.stdin.readlines()
# resultCard = list(map(int, data[3].strip().split()))
# ownCard = list(map(int, data[1].strip().split()))
# maxValue = max(ownCard)
# minValue = min(ownCard)
# dictionaryData = {x: 0 for x in range(minValue, maxValue + 1)}
# for x in ownCard:
#     dictionaryData[x] += 1
# result = [dictionaryData[x] for x in resultCard]
# print(" ".join(map(str, result)))

import sys

input = sys.stdin.read
data = input().split()
N = int(data[0])
ownCard = map(int, data[1 : N + 1])
M = int(data[N + 1])
resultCard = map(int, data[N + 2 :])

count_dict = {}
for card in ownCard:
    if card in count_dict:
        count_dict[card] += 1
    else:
        count_dict[card] = 1

result = [str(count_dict.get(card, 0)) for card in resultCard]
print(" ".join(result))
