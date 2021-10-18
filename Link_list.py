# More on '{LinkedList}' datastructures By {Chris Murimi}.
"""


"""


class Node:
    def __init__(self, d, n=None):
        self.data = d
        self.next_node = n

    def __str__(self):
        return '(' + str(self.data) + ')'


class LinkList:
    def __init__(self, r=None):
        self.root_node = r
        self.size = 0

    def add(self, data):
        new_node = Node(data, self.root_node)
        self.root_node = new_node
        self.size += 1

    def find(self, d):
        this_node = self.root_node
        while this_node is not None:
            if this_node.data == d:
                return d
            else:
                this_node = this_node.next_node
            return None

    def remove(self, data):
        this_node = self.root_node
        prev_node = None
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

    def print_items(self):
        this_node = self.root_node
        while this_node is not None:
            print(this_node, end='->')
            this_node = this_node.next_node
        print('None')


link = LinkList()
link.add(7)
link.add(8)
link.add(9)
link.add(1)
link.print_items()
link.remove(7)
print(link.find(7))
link.print_items()

