class Node:

    def __init__(self, data):
        self.data = data
        self.right = None
        self.left = None


class BinaryTree:

    def buildBT(self, root, data):
        if root is None:
            return Node(data)

        elif data > root.data:
            root.right = self.buildBT(root.right, data)
        else:
            root.left = self.buildBT(root.left, data)

        return root

    def countNodes(self, root):
        if root is None:
            return 0
        return 1 + self.countNodes(root.left) + self.countNodes(root.right)

    def leafCount(self, root):

        if root is None:
            return 0

        if root.left and root.right is not None:
            return 1

        else:
            return self.leafCount(root.left) + self.leafCount(root.right)

    def maxDepth(self, root):

        if root is None:
            return 0
        else:
            lDepth = self.maxDepth(root.left)
            rDepth = self.maxDepth(root.right)
            return max(lDepth, rDepth) + 1
