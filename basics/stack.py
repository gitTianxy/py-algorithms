# encoding=utf-8
"""
# Stack Abstract Data Type (ADT): LIFO
-------------------------------------------
# * Stack() creates a new stack that is empty.
#    It needs no parameters and returns an empty stack.
# * push(item) adds a new item to the top of the stack.
#    It needs the item and returns nothing.
# * pop() removes the top item from the stack.
#    It needs no parameters and returns the item. The stack is modified.
# * peek() returns the top item from the stack but does not remove it.
#    It needs no parameters. The stack is not modified.
# * isEmpty() tests to see whether the stack is empty.
#    It needs no parameters and returns a boolean value.
# * size() returns the number of items on the stack.
#    It needs no parameters and returns an integer.
"""
from abc import abstractmethod


class AbstractStack:
    """
    stack ADT
    """

    def __init__(self):
        self.top = 0

    @abstractmethod
    def push(self, item):
        pass

    @abstractmethod
    def pop(self):
        pass

    @abstractmethod
    def peek(self):
        pass

    def is_empty(self):
        return self.top == 0

    def size(self):
        return self.top


class ArrayStack(AbstractStack):
    """
    implementation of stack
    """

    def __init__(self, size=10):
        AbstractStack.__init__(self)
        self.array = [None] * size

    def push(self, item):
        self.array[self.top] = item
        self.top += 1

    def pop(self):
        if self.is_empty():
            raise IndexError("stack is empty")
        top = self.array[self.top - 1]
        self.array[self.top - 1] = None
        self.top -= 1
        return top

    def peek(self):
        if self.is_empty():
            raise IndexError("stack is empty")
        return self.array[self.top - 1]


if __name__ == '__main__':
    stack = ArrayStack()
    for i in range(0, 10):
        stack.push(i)
        print 'push: %s, top: %s, size: %s' % (i, stack.peek(), stack.size())
    print '---------------'
    while not stack.is_empty():
        print stack.pop()
