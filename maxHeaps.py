# More on '{maxHeaps}' datastructures By {Chris Murimi}.
""""
- maxHeap is a binary tree in which the value of the parent node is always greater than the value of
  its all children nodes
- Operations in a maxHeap:
  * push - appends an item to the end of the maxHeap and floats it up to its required position
  * Pop - removes the max value in the max heap and floats up the other values to their required position
  * Peek - checks the maximum value in the maxHeap
"""

# creating a maxHeap using a wrapper class


class MaxHeap:
    def __init__(self, heaps):  # constructor of the class
        super().__init__()
        self.maxHeap = [0]   # fill a value to the index 0 of the maxHeap since we won't use it
        for item in heaps:
            self.maxHeap.append(item)  # append the passed heap to our maxHeap

    def push(self, element):
        self.maxHeap.append(element)   # appends the element to the end of the maxHeap
        self.__float_up(len(self.maxHeap)-1)  # private class to float the appended element up to its required position

    def peek(self):  # this class checks the maximum value which is always floated to index 1
        if self.maxHeap[1]:
            return self.maxHeap[1]
        else:   # if it doesn't exist return none
            return None

    def pop(self):
        if len(self.maxHeap) > 2:
            self.__swap(1, len(self.maxHeap)-1)  # swaps the max value with the value at the end of the maxHeap
            max_value = self.maxHeap.pop()   # pops the max value which was swapped at the end of the maxHeap
            self.__float_down(1)   # float the item swapped to the top of the tree down to its required position
        elif len(self.maxHeap) == 2:  # if the len is 2, means the end element is max since index[0] = 0
            max_value = self.maxHeap.pop()  # pops the max value which was swapped at the end of the maxHeap
        else:
            max_value = None
        return max_value

    def __float_up(self, child_index):  # this function will float items up depending on their seniority
        self.parent_index = child_index // 2
        if child_index <= 1:
            return self.maxHeap
        elif self.maxHeap[child_index] > self.maxHeap[self.parent_index]:
            self.__swap(child_index, self.parent_index)
            self.__float_up(self.parent_index)

    def __float_down(self, parent_index):   # this function will float items down if they are less than their children
        left_child_index = parent_index * 2
        right_child_index = (parent_index * 2) + 1
        floater = parent_index

        if len(self.maxHeap) - 1 > left_child_index and self.maxHeap[floater] < self.maxHeap[left_child_index]:
            floater = left_child_index
        if len(self.maxHeap) - 1 > right_child_index and self.maxHeap[floater] < self.maxHeap[right_child_index]:
            floater = right_child_index

        if floater != parent_index:
            self.__swap(parent_index, floater)
            self.__float_down(floater)

    def __swap(self, i, j):  # this function swaps elements
        self.maxHeap[i], self.maxHeap[j] = self.maxHeap[j], self.maxHeap[i]

    def __str__(self):  # this function converts the maxHeap into a string and returns it out of the class
        return str(self.maxHeap[1:])


heap = MaxHeap([20, 16, 19, 5, 4, 12, 10])   # [20, 16, 19, 5, 4, 12, 10] passed heap
heap.push(13)  # adding to the heap
print(heap)
print(heap.peek())  # checking the max value in the heap
print(heap.pop())   # removing the max value and returning it
print(heap)
