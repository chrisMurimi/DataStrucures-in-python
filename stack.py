# More on '{stacks}' datastructures By {Chris Murimi}.
"""
- Stacks are last in, first out sequential datastructures (LIFO)
  NB: the last added item get removed first
Some stack operations include:
    * Push - adding elements to the end of the stack
    * Pop - removing last added item from the end of the stack
    * peek - checking the last added item without removing it
    * clear - deleting all elements of the stack
Note we can implement a stack using list operations such as append, pop, del and checking for the item at
index 1
- Stacks are widely used, most common stack use is the undo action in most programs
   When you write in your word doc, you can undo to remove last written item
"""

# creating a stack using a wrapper class


class Stack:
    def __init__(self):  # this the constructor object of the class, helps pass object to the class
        self.stack = []  # creates an empty list named stack

    def push(self, element):  # this class will add items to the end of our  stack
        return self.stack.append(element)  # using list function append

    def pop(self):  # this class will remove items from the end of our  stack
        if len(self.stack) >= 1:  # we have to check if item exist to avoid our program from breaking
            return self.stack.pop()   # using list function pop
        else:
            return None  # if stack is empty return none

    def peek(self):  # checking item at the end of stack
        if len(self.stack) > 0:
            return self.stack[-1]  # if elements exist, return the element at the last index
        else:
            return None

    def clear(self):  # clearing the stack
        return self.stack.clear()

    def __str__(self):   # this converts the stack into a list and returns it out of class when invoked
        return str(self.stack)


stack = Stack()
stack.push(7)  # adding to the stack
stack.push(7)
stack.push(6)
stack.push('nakamoto')
print(stack)
print(stack.peek())   # checking the peek of the stack
print(stack.pop())    # removing the item at stack end and returning it
print(stack)
stack.clear()   # deleting elements of the stack
print(stack)
