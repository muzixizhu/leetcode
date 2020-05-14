#         self.left = left
#         self.right = right
import collections


class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []
        deque = collections.deque()
        res = collections.defaultdict(list)
        deque.append((root, 0))
        while deque:
            node, dep = deque.popleft()
            # if len(res) - 1< dep:
            #     res.append([])
            res[dep].append(node.val)
            if node.left:
                deque.append((node.left, dep+1))
            if node.right:
                deque.append((node.right, dep+1))
        return res.values()