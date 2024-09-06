# import sys

# print("여러 줄의 입력을 처리합니다. (종료 : EOF)")

# data = sys.stdin.read()
# lines = data.splitlines()

# for line in lines:
#     print(line)


import sys

print("여러 줄의 입력을 처리합니다. (종료: EOF)")

# 모든 입력을 읽어들임
data = sys.stdin.read()

# 줄 단위로 분리 <-> inp
lines = data.splitlines()

# 각 줄의 단어 수를 세어 출력
for line in lines:
    word_count = len(line.split())
    print(f"'{line}' - 단어 수: {word_count}")
