class TreeNode():
    def __init__(self,val):
        self.val = val
        self.left = None
        self.right = None

class Solution():
    def __init__(self):
        self.prev = None

    def flatten(self, root):
        if not root:
            return None
        self.flatten(root.right)
        self.flatten(root.left)

        root.right = self.prev
        root.left = None
        self.prev = root

class Solution_2():
    def flatten(self, root):
        if not root: return
        stack = []
        stack.append(root)
        while stack:
            cur = stack.pop()
            if cur.right is not None: stack.append(cur.right)
            if cur.left is not None: stack.append(cur.left)
            if len(stack)>=1: cur.right = stack[-1]
            cur.left = None


if __name__=="__main__":
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(5)
    root.left.left = TreeNode(3)
    root.left.right = TreeNode(4)
    root.right.right = TreeNode(6)
    solver = Solution()
    solver.flatten(root)
    while root:
        print(root.val)
        root = root.right


