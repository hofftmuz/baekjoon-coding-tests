import sys

data = sys.stdin.read().splitlines()
n, m = int(data[0].split()[0]), int(data[0].split()[1])
s1 = set(data[1 : n + 1])
s2 = set(data[n + 1 :])
result = sorted(s1 & s2)
print(len(result))
print("\n".join(sorted(result)))

# result = []
# minLength = min(n, m)
# if minLength == n:
#     for x in s1:
#         if x in s2:
#             result.append(x)
# else:
#     for x in s2:
#         if x in s1:
#             result.append(x)
# print(len(result))
# print("\n".join(sorted(result)))

# n, m = map(int, input().split())


# # 듣도 못한 사람 명단
# not_heard = set()
# for _ in range(n):
#     not_heard.add(input().strip())

# # 보도 못한 사람 명단
# not_seen = set()
# for _ in range(m):
#     not_seen.add(input().strip())

# # 듣도 보도 못한 사람 (교집합)
# result = sorted(not_heard & not_seen)

# # 결과 출력
# print(len(result))
# print("\n".join(result))
