class Node:

    def __init__(self, data, next=None, prev=None):
        self.data = data
        self.next = next
        self.prev = prev


class DoubleLL:

    def __init__(self):
        self.head = None

    def insert_at_start(self, data):
        newNode = Node(data)

        if self.head is None:
            self.head = newNode
        else:
            self.head.prev = newNode
            newNode.next = self.head
            self.head = newNode

    def insert_at_end(self, data):
        newNode = Node(data)

        if self.head is None:
            self.head = newNode
        else:
            current = self.head

            while current.next is not None:
                current = current.next

            current.next = newNode
            newNode.prev = current

    def display(self):

        if self.head is None:
            print("List is Empty")
        else:
            current = self.head

            while current is not None:
                print(current.data)
                current = current.next


dll = DoubleLL()
dll.insert_at_start(12)
dll.insert_at_start(14)
dll.insert_at_end(16)
dll.display()
