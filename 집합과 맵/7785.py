import sys

inputLines = sys.stdin.readlines()
n = int((inputLines.pop(0)).strip())

# ['Baha enter\n', 'Askar enter\n', 'Baha leave\n', 'Artem enter\n']
# 각 요소의 strip()으로 '\n'을 제거하고
# split() 을 통해서 각각 dict의 키와 value로 만들고  = > ?
# set 으로 만들고 사용하려고 했으나 변동되는 부분이 있기 때문에 key로 빠르게 접근하고
# 변동되는 값을 처리


# result = {}
# for line in inputLines:
#     ls = line.strip().split()
#     value, key = ls[0], ls[1]
#     result[key] = value
# print(result)

# enter = set()
# leave = set()
# for line in inputLines:
#     ls = line.strip().split()
#     # leave이면서 enter에 있을 때
#     # enter이면서 leave에 있을 때
#     # 아무 것도 아닐 경우
#     if ls[1] == "leave" and ls[0] in enter:
#         enter.remove(ls[0])
#         leave.add(ls[0])
#     elif ls[1] == "enter" and ls[1] in leave:
#         leave.remove(ls[0])
#         enter.add(ls[0])
#     else:
#         if ls[1] == "enter":
#             enter.add(ls[0])
#         else:
#             leave.add(ls[0])

# print("\n".join(map(str, enter)))

# print(len(leave))
# result = sum(1 for line in inputLines if line.strip().split()[1] == "enter")
# 일단 dict 로 하면 안되는게 => value가 변동되는 값들이
# 존재하기 떄문에

# enter 하나의 set만을 만들며 들어온 사람들을 확인하는 로직

enter = set()
for line in inputLines:
    ls = line.strip().split()
    if ls[1] == "leave" and ls[0] in enter:
        enter.remove(ls[0])
    elif ls[1] == "enter":
        enter.add(ls[0])

print("\n".join(sorted(enter, reverse=True)))
