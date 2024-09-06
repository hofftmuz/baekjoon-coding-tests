
#여러개의 문자열을 리스트로 만들어서 출력

words1 = "sex on the bitch"
words2 = "hello world!"

list1= words1.split()
list2= words2.split()
result = list1 + list2
print(result)

list1.extend(list2)


print(list1)

# matrix = []
# rows,cols = map(str,input("행,열을 입력: ").split())
# for _ in range(rows):
#     row = list(map(int,input().split()))

