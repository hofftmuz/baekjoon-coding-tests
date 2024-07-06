# [ 1- 30 ]까지 주어져있을 때
# read로 주어지지 않은 값을 찾는 .
# import sys

# attended_data = sys.stdin.read().split()
# ls = [int(x) for x in attended_data]
# notSubmit = [x for x in range(1, 31)]
# for i in range(len(ls)):
#     notSubmit.remove(ls[i])
# for i in range(len(notSubmit)):
#     print(notSubmit[i])

import sys

input = sys.stdin.read().strip().split()
submitted = list(map(int, input))
total_students = 30
not_submitted = []

# not in
for student in range(1, total_students + 1):
    if student not in submitted:
        not_submitted.append(student)

not_submitted.sort()

for student in not_submitted:
    print(student)
