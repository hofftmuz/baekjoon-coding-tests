# input_val = list(map(int, input().split()))
# if 1 <= input_val[0] <= 6 and 1 <= input_val[1] <= 6 and 1 <= input_val[2] <= 6:
#     if input_val.count(input_val[0]) == 3:
#         print(10000 + input_val[0] * 1000)
#     elif input_val[0] != input_val[1] != input_val[2]: ==> 이 부분이 문제가 돼
#         print(max(input_val) * 100)
#     else:
#         if input_val[0] == input_val[1]:
#             print(1000 + input_val[0] * 100)
#         elif input_val[0] == input_val[2]:
#             print(1000 + input_val[0] * 100)
#         else:
#             print(1000 + input_val[1] * 100)

li = list(map(int, input().split()))
if all(1 <= x <= 6 for x in li):
    if li.count(li[0]) == 3:
        print(10000 + li[0] * 1000)
    # 중복된 원소의 개수를 제거하고 세고싶을 때
    elif len(set(li)) == 3:
        print(max(li) * 100)
    else:
        if li[0] == li[1]:
            print(1000 + li[0] * 100)
        elif li[0] == li[2]:
            print(1000 + li[0] * 100)
        else:
            print(1000 + li[1] * 100)
