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

    def iterativeMaxDepth(self, root):
        stack = []
        if root:
            stack.append((1, root))
        depth = 0
        while stack:
            current_depth, root = stack.pop()
            if root:
                depth = max(depth, current_depth)
                stack.append((current_depth + 1, root.left))
                stack.append((current_depth + 1, root.right))
        return depth


root = None
b = BinaryTree()
for ele in [2, 1, 33, 0, 25, 40, 11, 34, 7, 12, 36, 13]:
    root = b.buildBT(root, ele)
total = b.countNodes(root)
print(total)
print("Total number of leaf nodes in a given binary tree")
leafcount = b.leafCount(root)
print(leafcount)
print('maximum depth of a binary tree')
height = b.maxDepth(root)
print(height)
height1 = b.iterativeMaxDepth(root)
print(height1)
