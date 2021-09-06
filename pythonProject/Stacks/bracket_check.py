class Parenthesis:

    def __init__(self):
        self.stack = []

    def eval(self, exp):

        for element in exp:
            print(self.stack)

            if element == '(' or element == '[' or element == '{':
                self.stack.append(element)
                continue

            if self.stack != []:

                if element == ')' or element == '}' or element == ']':
                    self.stack.pop()
            else:
                print("Error in Parenth")
                return

        if self.stack == []:
            print("Expression was fine")
        else:
            print("Error in Parenthesis")


pCheck = Parenthesis()
inp = "[}"
print(inp.split('.'))


