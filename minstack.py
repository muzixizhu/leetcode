class MinStack(object):

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = []

    def push(self, x):
        """
        :type x: int
        :rtype: void
        """
        pre_min = 2147483647 if len(self.stack) == 0 else self.stack[-1][1]
        cur_min = min(x, pre_min)
        self.stack.append((x, cur_min))

    def pop(self):
        """
        :rtype: void
        """
        self.stack.pop()

    def top(self):
        """
        :rtype: int
        """
        return self.stack[-1][0]

    def getMin(self):
        """
        :rtype: int
        """
        return self.stack[-1][1]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()

class MinStack(object):

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.min = 2147483648
        self.stack = []

    def push(self, x):
        """
        :type x: int
        :rtype: void
        """
        if not self.stack:
            self.min = x
        self.stack.append(x - self.min)
        if x < self.min:
            self.min = x

    def pop(self):
        """
        :rtype: void
        """
        peak = self.stack.pop()
        if peak < 0:
            self.min = self.min - peak

    def top(self):
        """
        :rtype: int
        """
        if self.stack[-1] < 0:
            return self.min
        else:
            return self.min + self.stack[-1]

    def getMin(self):
        """
        :rtype: int
        """
        return self.min

# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()