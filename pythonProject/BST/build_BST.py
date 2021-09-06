class Node:

    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


class BST:

    def buildBST(self, root, data):
        if root is None:
            return Node(data)

        if data > root.data:
            root.right = self.buildBST(root.right, data)
        else:
            root.left = self.buildBST(root.left, data)

        return root

    def inOrder(self, root):

        if root is None:
            return
        self.inOrder(root.left)
        print(root.data)
        self.inOrder(root.right)

    def search(self, root, element):
        if root is None or root.data == element:
            return root

        if root.data > element:
            return self.search(root.left, element)
        return self.search(root.right, element)

    def minElement(self, root):
        current = root

        while current.left is not None:
            current = current.left

        return current.data

    def maxElement(self, root):
        current = root

        while current.right is not None:
            current = current.right

        return current.data

    # root, left, right
    def preOrder(self, root):
        if root is None:
            return

        print(root.data)
        self.preOrder(root.left)
        self.preOrder(root.right)

    def iterativePreorder(self, root):
        if root is None:
            return
        stack = [root]
        while stack:
            current = stack.pop()
            print(current.data)

            if current.right:
                stack.append(current.right)

            if current.left:
                stack.append(current.left)

    # left, right, root
    def postOrder(self, root):
        if root is None:
            return

        self.postOrder(root.left)
        self.postOrder(root.right)
        print(root.data)

    def iterativePostorder(self, root):
        if root is None:
            return
        stack = [root]
        while stack:
            current = stack.pop()
            print(current.data)

            if current.right:
                stack.append(current.right)

            if current.left:
                stack.append(current.left)

    def inorder(self, root):
        # set current to root of binary search tree
        current = root
        stack = []

        while True:
            # reach the left most node of the current root
            if current is not None:
                stack.append(current)
                current = current.left
            elif stack:
                current = stack.pop()
                print(current.data)
                current = current.right
            else:
                break

    def stackTwoPost(self, root):

        if root is None:
            return

        rec = []
        fin = []

        rec.append(root)

        while rec:
            current = rec.pop()
            fin.append(current)

            if current.left:
                rec.append(current.left)
            if current.right:
                rec.append(current.right)

        while fin:
            temp = fin.pop()
            print(temp.data)

    def successor(self, root):
        root = root.right
        while root.left:
            root = root.left
        return root.data

    def predecessor(self, root):
        root = root.left
        while root.right:
            root = root.right
        return root.data

    def deletion(self, root, key):
        if not root:
            return None

        if key < root.data:
            root.left = self.deletion(root.left, key)
        elif key > root.data:
            root.right = self.deletion(root.right, key)
        else:
            if not (root.left or root.right):
                root = None

            elif root.right:
                root.data = self.successor(root)
                root.right = self.deletion(root.right, root.data)

            else:
                root.data = self.predecessor(root)
                root.left = self.deletion(root.left, root.data)
        return root


root = None
b = BST()

for element in [10, 5, 25, 2, 7, 30]:
    root = b.buildBST(root, element)

b.iterativePostorder(root)
