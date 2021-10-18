# More on '{Queues}' datastructures By {Chris Murimi}.
"""
- Queues are first in first out datastructures (FIFO)
- Queues works on the principle of real life queue lines, i.e you join a queue line to a
  bank teller last you are served last!
- Queue operations
  * Enqueue - this operations adds items to the end of the queue
  * Dequeue - this operation removes elements at the front of the queue
NB : you can use collections built-in library to achieve  queue operations with lists
   i.e

from collections import deque  # importing deque class from collections library

queue = deque()
queue.append(7)  # adding to the end of the queue
queue.append(9)
queue.append(10)
print(queue)
print(queue.popleft())  # removing element from the end of the queue and returning it
print(queue)

"""

# using wrapper class to create a queue


class Queue:
    def __init__(self):  # this the constructor object of the class, helps pass object to the class
        self.queue = []   # creating an empty list called queue

    def enqueue(self, element):   # this function will insert items at the front of the queue
        return self.queue.insert(0, element)

    def dequeue(self):  # this function removes items at the end of the queue
        if len(self.queue) > 0:
            return self.queue.pop()
        else:
            return None

    def __str__(self):
        return str(self.queue)


my_queue = Queue()
my_queue.enqueue(7)  # inserting into the front of the queue
my_queue.enqueue(9)
my_queue.enqueue(10)
print(my_queue)
print(my_queue.dequeue())  # removing items at the end of the queue and returning the removed item
print(my_queue)

