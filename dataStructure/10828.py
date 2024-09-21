import sys


class Stack:
    def __init__(self):
        self.__st = []

    def push(self, x):
        self.__st.append(x)

    def pop(self):
        if self.empty():
            print(-1)
        else:
            print(self.__st.pop())

    def size(self):
        print(len(self.__st))

    def empty(self):
        return len(self.__st) == 0

    def top(self):
        if self.empty():
            print(-1)
        else:
            print(self.__st[-1])


st = Stack()
length = int(input())
inputlines = sys.stdin.readlines()
for line in inputlines:
    command = line.strip().split()
    if command[0] == "push":
        val = int(command[1])
        st.push(val)
    elif command[0] == "pop":
        st.pop()
    elif command[0] == "size":
        st.size()
    elif command[0] == "empty":
        print(1 if st.empty() else 0)
    elif command[0] == "top":
        st.top()
