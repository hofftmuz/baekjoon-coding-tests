n = int(input())
# type = "long"
# if 4 <= n <= 1000 and n % 4 == 0:
#     print((type + " ") * (n // 4) + "int")
long_count = n // 4
print("long " * long_count + "int")
