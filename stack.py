#!/usr/bin/python

import unittest

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


#stack = Stack()
#print("Ile liczb umiescic na stosie: ")
#d = input()
#d = int(d)
#for x in range(d):
#    try:
#        stack.push(input())
#    except Exception:
#        print("Bad input")
#
#print(stack.empty())
#print(stack.size())
#print("ile liczb wyjac ze stosu: ")
#d = input()
#d = int(d)
#for x in range(d):
#    try:
#        print(stack.pop())
#    except Exception:
#        print("Stos pusty")

#print("Na stosie zostalo liczb: ")
#print(stack.size())


class TestStackMethods(unittest.TestCase):

    def test_empty(self):
	s = Stack()
        self.assertEqual(s.empty(), True)
	s.push(2)
	self.assertEqual(s.empty(), False)

    def test_size(self):
        s = Stack()
        self.assertEqual(s.size(), 0)
	s.push(2)
	self.assertEqual(s.size(), 1)
	s.push(3)
	self.assertEqual(s.size(), 2)

    def test_push(self):
        s = Stack()
	s.push(2)
	s.push(3)
	s.push(4)
	self.assertEqual(s.pop(), 4)
	self.assertEqual(s.pop(), 3)
	self.assertEqual(s.pop(), 2)


if __name__ == '__main__':
    unittest.main()








