import sys

# data = sys.stdin.read().strip()
# count = 1
# for i in range(1, len(data)):
#     # "=","-","j"
#     count += 1
#     if (data[i] == "j" and data[i - 1] == "l") or (
#         data[i] == "j" and data[i - 1] == "n"
#     ):
#         count -= 1
#         continue
#     if (
#         (data[i] == "=" and data[i - 1] == "s")
#         or (data[i] == "=" and data[i - 1] == "z" and data[i - 2] != "d")
#         or (data[i] == "=" and data[i - 1] == "c")
#     ):
#         count -= 1
#         continue
#     if data[i] == "=" and data[i - 1] == "z" and data[i - 2] == "d":
#         count -= 2
#         continue
#     if (data[i] == "-" and data[i - 1] == "c") or (
#         data[i] == "-" and data[i - 1] == "d"
#     ):
#         count -= 1
#         continue
# print(count)

"""
문자열 - replace 
문자열에서 원하는 구간만큼의 문자들을 변경할 수 있는 함수.
"""


def count_croatian_alphabets(word):
    croatian_alphabets = ["c=", "c-", "dz=", "d-", "lj", "nj", "s=", "z="]
    for ca in croatian_alphabets:
        word = word.replace(ca, "*")
    return len(word)


input_data = sys.stdin.read().strip()
print(count_croatian_alphabets(input_data))
