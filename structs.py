# Data structs implementation

class LinkedListNode:
    """Implement linked list node in python."""

    def __init__(self, data=None):
        self.next = None
        self.data = data


class LinkedList():
    """Implment linked list in python."""

    def __init__(self):
        self.head = None
        self.size = 0

    def prepend(self, item):
        new_link = LinkedListNode(item)
        new_link.next = self.head
        self.head = new_link
        self.size = self.size + 1

    def append(self, item):
        pass
