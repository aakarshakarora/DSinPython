class Node:

    def __init__(self, data, link=None):
        self.data = data
        self.link = link


class Stack:

    def __init__(self):
        self.head = None

    def push(self, data):
        newNode = Node(data)
        newNode.link = self.head
        self.head = newNode

    def pop(self):

        if self.head is None:
            print("Stack is Empty")
            return
        else:
            temp = self.head
            print("Poped Element is:", temp.data)
            self.head = self.head.link
            temp = None

    def display(self):

        if self.head is None:
            print("Stack is Empty")
        else:
            current = self.head

            while current is not None:
                print(current.data)
                current = current.link



sll = Stack()
sll.push(45)
sll.push(14)
sll.push(88)
sll.pop()
sll.display()
