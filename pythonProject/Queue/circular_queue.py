class Node:

    def __init__(self, data, link=None):
        self.data = data
        self.link = link


class CircularQueue:

    def __init__(self):
        self.front = self.rear = None

    def enQueue(self, data):
        newNode = Node(data)

        if self.front is None:
            self.front = newNode
        else:
            self.rear.link = newNode

        self.rear = newNode
        self.rear.link = self.front

    def deQueue(self):
        temp = self.front

        if self.front is None:
            print("Queue is Empty")
            return

        else:

            if self.front == self.rear:
                self.front = self.rear = None
            else:
                self.front = temp.link
                self.rear.link = self.front

        return temp.data

    def display(self):
        current = self.front

        while current.link is not self.front:
            print(current.data)
            current=current.link
        print(current.data)

cq = CircularQueue()
cq.enQueue(12)
cq.enQueue(123)
cq.enQueue(1234)
# print(cq.front.data)
# print(cq.rear.data)
cq.deQueue()
cq.display()

