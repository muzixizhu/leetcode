N - ary
Tree
Postorder
Traversal
Easy

580

61

Add
to
List

Share
Given
an
n - ary
tree,
return the
postorder
traversal
of
its
nodes
' values.

Nary - Tree
input
serialization is represented in their
level
order
traversal, each
group
of
children is separated
by
the
null
value(See
examples).

Follow
up:

Recursive
solution is trivial, could
you
do
it
iteratively?




"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""


class Solution:
    def postorder(self, root: 'Node') -> List[int]:
        """
        :type root: Node
        :rtype: List[int]
        """
        if not root:
            return []

        stack, counters, retList = [root], [0], []

        while len(stack) != 0:
	    #To English: while the current top of the stack has an unseen child
            while counters[-1] < len(stack[-1].children):
		# Add that child to the top of the stack, with a new corresponding counter to the other stack
                stack.append(stack[-1].children[counters[-1]])
                counters.append(0)
	    # If the current top of the stack has reached the end of its children list, then we pop it, it's done
            retList.append(stack.pop().val)
	    # need to pop its counter as well
            counters.pop()
	    # and increment the counter of the next top of the stack to begin that search
            if len(counters) != 0:
                counters[-1] += 1

        return retList