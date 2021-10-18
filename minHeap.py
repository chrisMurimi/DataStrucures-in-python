# More on '{minHeap}' datastructures By {Chris Murimi}.
"""
- minHeap is a binary tree in which the value of the parent node is always smaller than the value of
  its all children nodes
- Operations in a minHeap:
  * push - appends an item to the end of the minHeap and floats it up to its required position
  * Pop - removes the min value in the min heap and floats up the other values to their required position
  * Peek - checks the minimum value in the minHeap
"""


class MinHeap:
    def __init__(self, my_heap):
        super().__init__()
        self.min_heap = [None]
        for item in my_heap:
            self. min_heap.append(item)

    def push(self, item):
        self.min_heap.append(item)
        self.__float_up(len(self.min_heap)-1)
        return self.min_heap

    def peek(self):
        return self.min_heap[1]

    def pop(self):
        if len(self.min_heap) > 2:
            self.__swap(1, len(self.min_heap)-1)
            min_value = self.min_heap.pop()
            self.__sink_down(1)
        elif len(self.min_heap) == 2:
            min_value = self.min_heap.pop()
        else:
            min_value = None
        return min_value

    def __float_up(self, index):
        parent = index // 2
        if index <= 1:
            return self.min_heap
        elif self.min_heap[parent] > self.min_heap[index]:
            self.__swap(parent, index)
            self.__float_up(parent)

    def __sink_down(self, parent):
        left = parent * 2
        right = (parent * 2) + 1
        small = parent
        if left < len(self.min_heap)-1 and self.min_heap[small] > self.min_heap[left]:
            small = left
        if right < len(self.min_heap) - 1 and self.min_heap[small] > self.min_heap[right]:
            small = right
        if small != parent:
            self.__swap(small, parent)
            self.__sink_down(parent)

    def __swap(self, i, j):
        self.min_heap[i], self.min_heap[j] = self.min_heap[j], self.min_heap[i]

    def __str__(self):
        return str(self.min_heap[1:])


heap = MinHeap([1, 4, 5, 10, 12, 13, 20])
heap.push(6)
heap.push(2)
heap.pop()
print(heap)