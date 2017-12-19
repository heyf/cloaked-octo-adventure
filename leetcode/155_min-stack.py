# 155. Min Stack - LeetCode
# https://leetcode.com/problems/min-stack/description/

# Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.

class MinStack(object):

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = []
        self.min_stack = []
        

    def push(self, x):
        """
        :type x: int
        :rtype: void
        """
        self.stack.append(x)
        if len(self.min_stack) == 0:
            self.min_stack.append(x)
        else:
            self.min_stack.append( x if x < self.min_stack[-1] else self.min_stack[-1] )
        
    def pop(self):
        """
        :rtype: void
        """
        if len(self.stack) > 0:
            self.stack.pop()
            self.min_stack.pop()
        
    def top(self):
        """
        :rtype: int
        """
        if len(self.stack) > 0:
            return self.stack[-1]
        
    def getMin(self):
        """
        :rtype: int
        """
        if len(self.min_stack) > 0 :
            return self.min_stack[-1]

# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()

minStack = MinStack();
minStack.push(-2);
minStack.push(0);
minStack.push(-3);
print minStack.getMin();   # --> Returns -3.
minStack.pop();
print minStack.top();      # --> Returns 0.
print minStack.getMin();   # --> Returns -2.