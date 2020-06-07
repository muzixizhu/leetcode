class TreeNode():
    def __init__(self, val):
        self.val = val
        self.left= None
        self.right = None

class Solution():
    def print_tree(self, root):
        if not root:
            return
        cusin_nodes = []
        depth = 0
        cusin_nodes.append(root)
        while len(cusin_nodes):
            tem = []
            for node in cusin_nodes:
                if node.left is not None:
                    tem.append(node.left)
                if node.right is not None:
                    tem.append(node.right)
            if depth % 2 == 0:
                print([node.val for node in cusin_nodes])
            else:
                print([node.val for node in cusin_nodes[::-1]])
            depth += 1
            cusin_nodes = tem


if __name__=="__main__":
    root = TreeNode(3)
    root.left = TreeNode(9)
    root.right = TreeNode(20)
    root.right.left = TreeNode(15)
    root.right.right = TreeNode(7)
    solver = Solution()
    print(solver.print_tree(root))