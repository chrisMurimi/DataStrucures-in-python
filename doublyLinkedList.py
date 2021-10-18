# More on '{CircularLinkedList}' datastructures By {Chris Murimi}.
"""


"""


class Node:
    def __init__(self, data, n=None, p=None):
        self.data = data
        self.next_node = n
        self.prev_node = p

    def __str__(self):
        return '('+str(self.data)+')'


class DoublyList:
    def __init__(self, r=None):
        self.root_node = r
        self.last = r
        self.size = 0

    def add(self, item):
        if self.root_node is None:
            self.root_node = Node(item)
            self.last = self.root_node
        else:
            new_node = Node(item, self.root_node)
            self.root_node.prev_node = new_node
            self.root_node = new_node
        self.size += 1

    def find(self, data):
        this_node = self.root_node
        while this_node is not None:
            if this_node.data == data:
                return this_node
            elif this_node.data is None:
                return None
            else:
                this_node = this_node.next_node

    def remove(self, data):
        this_node = self.root_node
        while this_node is not None:
            if this_node.data is data:
                if this_node.prev_node is not None:
                    if this_node.next_node is not None:
                        this_node.prev_node.next_node = this_node.next_node
                        this_node.next_node.prev_node = this_node.prev_node
                    else:
                        this_node.prev_node.next_node = None
                        self.last = this_node.prev_node
                else:
                    self.root_node = this_node.next_node
                    this_node.next_node.prev_node = self.root_node
                self.size -= 1
                return True
            else:
                this_node = this_node.next_node
        return False

    def print_items(self):
        if self.root_node is None:
            return None
        this_node = self.root_node
        while this_node is not None:
            print(this_node, end='<=>')
            this_node = this_node.next_node
        print('None')


link = DoublyList()
link.add(1)
link.add(2)
link.add(3)
link.add(4)
link.remove(3)
link.print_items()
print(link.find(1))
print(link.last.prev_node)

