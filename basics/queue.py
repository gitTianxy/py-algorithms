# encoding=utf-8
"""
# Queue Abstract Data Type (ADT): FIFO
----------------------------------
# * Queue() creates a new queue that is empty.
#   It needs no parameters and returns an empty queue.
# * enqueue(item) adds a new item to the rear of the queue.
#   It needs the item and returns nothing.
# * dequeue() removes the front item from the queue.
#   It needs no parameters and returns the item. The queue is modified.
# * isEmpty() tests to see whether the queue is empty.
#   It needs no parameters and returns a boolean value.
# * size() returns the number of items in the queue.
#   It needs no parameters and returns an integer.
"""
from abc import abstractmethod


class AbstractQueue:
    def __init__(self):
        self.front = 0
        self.rear = 0

    @abstractmethod
    def enqueue(self, item):
        pass

    @abstractmethod
    def dequeue(self):
        pass

    def is_empty(self):
        return self.front == self.rear

    def size(self):
        return self.rear - self.front


class ArrayQueue(AbstractQueue):
    def __init__(self, size=10):
        AbstractQueue.__init__(self)
        self.array = [None] * size

    def enqueue(self, item):
        self.array[self.rear] = item
        self.rear += 1

    def dequeue(self):
        if self.is_empty():
            raise IndexError('queue is empty')
        front = self.array[self.front]
        self.array[self.front] = None
        self.front += 1
        return front


if __name__ == '__main__':
    queue = ArrayQueue()
    for i in range(0, 10):
        queue.enqueue(i)
        print 'enqueue: %s, front: %s, rear: %s' % (i, queue.front, queue.rear)
    print '---------------------'
    while not queue.is_empty():
        print 'dequeue: %s, front: %s, rear: %s' % (queue.dequeue(), queue.front, queue.rear)
