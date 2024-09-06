def countSpot(n: int):
    x = 2
    for i in range(n):
        x += pow(2, i)
    return x * x
n = int(input())
print(countSpot(n))
