#1000 미만의 자연수에서 3, 5의 배수의 총합을 구하라
# ex 10 미만의 자연수에서 3과 5의 배수를 구하면 3,5,6,9 이고 이들의 총합은 23이다
import time

start_time = time.time()

x = 3
y = 5
limit = 1000
multiples = set()
count = 1

while x * count < limit:
    multiples.add(x*count)
    count+=1

count = 1 
while y * count < limit:
    multiples.add(y*count)
    count+=1

result = sum(multiples)
end_time = time.time()
print("코드 1 실행 시간:", end_time - start_time)
print(result)

# 문제는 중첩된 것을 제외해야하잖아 
start_time = time.time()
x = 3
y = 5
limit = 1000
result = 0

count = 1
while x * count < limit:
    result += x * count
    count += 1

count = 1
while y * count < limit:
    if (y * count) % x != 0:
        result += y * count
    count += 1
end_time = time.time()
print("코드 2 실행 시간:", end_time - start_time)
print("3과 5의 배수의 총합:", result)

# Use list comprehension 
start_time = time.time()
x = 3
y = 5
limit = 1000

multiples = { i for i in range(1,limit) if i % x ==0 or i % y == 0}
result = sum(multiples)
end_time = time.time()
print("코드 3 실행 시간:", end_time - start_time)
print("3과 5의 배수의 총합:", result)
#4
start_time =time.time()
sum(list([x for x in range(1000) if x%3 == 0 or x%5 ==0]))
end_time = time.time()
print("코드 4 실행 시간:", end_time - start_time)
print("3과 5의 배수의 총합:", result)