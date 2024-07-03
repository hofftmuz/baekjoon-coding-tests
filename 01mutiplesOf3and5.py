#1000 미만의 자연수에서 3, 5의 배수의 총합을 구하라
# ex 10 미만의 자연수에서 3과 5의 배수를 구하면 3,5,6,9 이고 이들의 총합은 23이다

#code 1 => use Loop and set

x = 3
y = 5
limit = 1000
result = set()
count = 1

while x * count < limit : 
    result.add(x*count)
    count+=1

count = 1
while y * count < limit:
    result.add(y*count)
    count += 1

result = sum(result)

#code 2 => tuple , list comprehension
x = 3
y = 5
limit = 1000
multiples = { i for i in range(1,limit) if i%x==0 or i%y == 0}
result = sum(multiples)

#code 3 => list comprehension
x = 3
y = 5
limit = 1000
result = sum([x for x in range(1000) if x%3 or x%5 == 0])
