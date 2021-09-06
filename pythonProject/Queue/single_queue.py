class Node:

    def __init__(self, data, next=None):
        self.data = data
        self.next = next


class Queue:

    def __init__(self):
        self.front = None
        self.rear = None

    def enqueue(self, data):
        newNode = Node(data)
        if self.rear is None:
            self.front = self.rear = newNode
        else:
            self.rear.next = newNode
            self.rear = newNode

    def isEmpty(self):

        return self.front is None

    def dequeue(self):

        if self.isEmpty():
            print("Queue is Empty")

        else:
            temp = self.front
            self.front = temp.next

        if self.front is None:
            self.rear = None

    def display(self):

        if self.front is None:
            print("Queue is Empty")

        else:
            temp = self.front
            while temp.next is not None:
                print(temp.data)
                temp = temp.next
            print(temp.data)




q = Queue()
q.enqueue(15)
q.enqueue(14)
q.enqueue(154)
q.display()
