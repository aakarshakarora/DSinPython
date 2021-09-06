# to Evaluate prefix reverse the expression

class Evaluate:

    def __init__(self):
        self.stack = []

    def isEmpty(self):
        return self.stack == []

    def push(self, exp):
        self.stack.append(exp)

    def pop(self):
        if not self.isEmpty():
            return self.stack.pop()
        else:
            return '$'

    def evaluate_postfix(self, exp):
        for element in exp:

            if element.isdigit():

                self.push(element)
            else:
                a = self.pop()
                b = self.pop()
                self.push(str(eval(b + element + a)))

        return int(self.pop())


e = Evaluate()
n1 = '234*6*+'
n2 = '+2**346'
x = n2[::-1]
print(e.evaluate_postfix(n1))
print(e.evaluate_postfix(x))
