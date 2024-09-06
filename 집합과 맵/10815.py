import sys

# 입력 데이터 읽기
data = list(map(int, sys.stdin.read().strip().split()))

# 자신의 카드 길이와 카드 리스트 추출
Own_length = data[0]
own_card = data[1 : Own_length + 1]

# 결과를 저장할 딕셔너리 초기화
result = {x: 0 for x in own_card}

# 테스트할 카드의 길이와 카드 리스트 추출
test_card = data[Own_length + 2 :]

# 테스트 카드가 자신의 카드에 포함되어 있는지 확인
for x in test_card:
    if x in result:
        result[x] += 1
    else:
        result[x] = 0
# 딕셔너리 결과를 키를 기준으로 내림차순 정렬
sorted_result = sorted(result.items(), key=lambda item: item[0], reverse=True)

# 값들을 출력
print(" ".join(map(str, [item[1] for item in sorted_result])))


# import sys

# input_lines = sys.stdin.readlines()
# data = [list(map(int, line.strip().split())) for line in input_lines]
# own_length = data[0][0]
# test_length = data[2][0]
# result = {}
# for x in data[3]:
#     if x in data[1]:
#         result[x] = 1
#     else:
#         result[x] = 0
# print(" ".join(map(str, result.values())))


# list에 대한 복사 -> 어떻게 해결하면 좋을까?
# readline으로 읽어서 읽어올 때 각각을 리스트로 취급해서 다루면 조금 더 빠르지 않을까?
#
