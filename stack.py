class Stack:
    def __init__(self):
        self.__data = []

    def empty(self):
        return len(self.__data) == 0

    def size(self):
        return len(self.__data)

    def push(self, x):
        self.__data.append(x)

    def pop(self):
        return self.__data.pop()


stack = Stack()
print("Ile liczb umiescic na stosie: ")
d = input()
d = int(d)
for x in range(d):
    try:
        stack.push(input())
    except Exception:
        print("Bad input")

print(stack.empty())
print(stack.size())

print("ile liczb wyjac ze stosu: ")
d = input()
d = int(d)
for x in range(d):
    try:
        print(stack.pop())
    except Exception:
        print("Stos pusty")

print("Na stosie zostalo liczb: ")

print(stack.size())