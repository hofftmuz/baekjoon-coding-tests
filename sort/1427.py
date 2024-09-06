data = input()

list = [int(x) for x in data]
list.sort(reverse=True)
print("".join(map(str, list)))

# num = input()
# sorted_num = sorted(num, reverse=True)

# result = "".join(map(str, sorted_num))
# print(result)
