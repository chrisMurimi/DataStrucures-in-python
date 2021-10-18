# More on '{CircularLinkedList}' datastructures By {Chris Murimi}.
"""


"""


class Node:
    def __init__(self, data, n=None, p=None):
        self.data = data
        self.next_node = n
        self.prev_node = p

    def __str__(self):
        return '(' + str(self.data) + ')'


class CircularLinkList:
    def __init__(self, r=None):
        self.root_node = r
        self.size = 0

    def add(self, data):
        if self.root_node is None:
            new_node = Node(data)
            self.root_node = new_node
            # self.root_node.next_node = self.root_node
        else:
            new_node = Node(data, self.root_node.next_node)
            self.root_node.next_node = new_node
        self.size += 1

    def remove(self, data):
        this_node = self.root_node.next_node
        prev_node = None
        if self.root_node.data == data:
            self.root_node = self.root_node.next_node
        elif self.root_node.data != data:
            while this_node is not None:
                if this_node.data == data:
                    if prev_node is not None:
                        prev_node.next_node = this_node.next_node
                    else:
                        self.root_node = this_node.next_node
                        self.size -= 1
                    return True
                else:
                    prev_node = this_node
                    this_node = this_node.next_node
            return False

    def find(self, d):
        this_node = self.root_node
        while this_node is not None:
            if this_node.data == d:
                return d
            else:
                this_node = this_node.next_node
            return None

    def print_items(self):
        this_node = self.root_node
        while this_node is not None:
            print(this_node, end='->')
            this_node = this_node.next_node
        print(self.root_node)


link = CircularLinkList()
link.add(5)
link.add(6)
link.add(10)
link.add(21)
link.print_items()
link.add(7)
link.print_items()
link.remove(5)
link.print_items()
