# input_val = input()
# count_ls = [-1 for _ in range(26)]
# dict = {
#     "a": -1,
#     "b": -1,
#     "c": -1,
#     "d": -1,
#     "e": -1,
#     "f": -1,
#     "g": -1,
#     "h": -1,
#     "i": -1,
#     "j": -1,
#     "k": -1,
#     "l": -1,
#     "m": -1,
#     "n": -1,
#     "o": -1,
#     "p": -1,
#     "q": -1,
#     "r": -1,
#     "s": -1,
#     "t": -1,
#     "u": -1,
#     "v": -1,
#     "w": -1,
#     "x": -1,
#     "y": -1,
#     "z": -1,
# }
# for i in range(len(input_val)):
#     temp = input_val[i]
#     if dict[temp] != -1:
#         continue
#     dict[temp] = i
# print(" ".join(map(str, dict.values())))

"""
dictionary를 이용한 코드 최적화

input_val = input()
alphabet = "abcdefghijklmnopqrstuvwxyz"
positions = {char : -1 for char in alhabet}
for index,char in enumerate(input_val):
    if positions[char] == -1:
        positions[char] = index
print(" ".join(str(positions[char]) for char in alphabet))
"""

import sys
import string

input = sys.stdin.read().strip()
alphabet = string.ascii_lowercase
positions = [-1] * 26
for idx, char in enumerate(input):
    if positions[ord(char) - ord("a")] == -1:
        positions[ord(char) - ord("a")] = idx
print(" ".join(map(str, positions)))
