# LIFO

class Stack:

    def __init__(self):
        self.stack = []

    def isEmpty(self):
        return self.stack == []

    def push(self, data):
        self.stack.append(data)

    def pop(self):
        if self.stack == []:
            return f"Stack is Empty"

        else:
            return self.stack.pop()

    def peek(self):

        if not self.isEmpty():
            return self.stack[-1]
        else:
            return -1

    def display_stack(self):

        while self.stack != []:
            x = self.pop()
            print(x)


s = Stack()
print("Enter Operation you wish to perform")
test = True
while test:
    inp = int(input("\n 1.Push \n 2. Pop \n 3. Peek \n 4. Display \n 5. Exit"))

    if inp == 1:
        data = int(input())
        s.push(data)

    elif inp == 2:
        op = s.pop()
        print(op)

    elif inp == 3:
        op = s.peek()
        print("Peek ", op)

    elif inp == 4:
        s.display_stack()
    else:
        test = False
        break
