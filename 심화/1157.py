# ord():문자를 아스키 코드 또는 유니 코드로 , chr(): 아스키 코드 또는 유니코드를 문자로
## ord('A') => 65
## chr(65)  => 'A'

# data = input().strip()
# data = data.upper()
# ls = [0] * 26
# for digit in data:
#     temp = ord(digit)
#     ls[temp - 65] += 1
# max_value = max(ls)
# print(chr(ls.index(max_value) + 65) if ls.count(max_value) == 1 else "?")

"""
from collections import Counter => 문자열의 빈도수를 저장하고 계산하는데 유용
Counter -> 주어진 시퀀스(문자열, 리스트 등)의 각 요소의 빈도수를 계산하여 딕셔너리와 유사한 객체를 생성
"""

from collections import Counter
import sys

data = sys.stdin.read().strip().upper()
frequency = Counter(data)
max_freq = max(frequency.values())
most_common_chars = [char for char, freq in frequency.items() if freq == max_freq]
if len(most_common_chars) > 1:
    print("?")
else:
    print(most_common_chars[0])
