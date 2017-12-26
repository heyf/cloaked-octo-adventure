# 225. Implement Stack using Queues - LeetCode
# https://leetcode.com/problems/implement-stack-using-queues/description/

class MyStack(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.lst = list()
        self.top_ptr = -1

    def push(self, x):
        """
        Push element x onto stack.
        :type x: int
        :rtype: void
        """
        if self.top_ptr == len(self.lst) - 1:
            self.lst.append(x)
            self.top_ptr += 1
        else:
            self.top_ptr += 1
            self.lst[self.top_ptr] = x
        return

    def pop(self):
        """
        Removes the element on top of the stack and returns that element.
        :rtype: int
        """
        if self.top_ptr == -1:
            return False
        ret = self.top()
        self.top_ptr -= 1
        return ret

    def top(self):
        """
        Get the top element.
        :rtype: int
        """
        if self.top == -1:
            return False
        return self.lst[self.top_ptr]
        
    def empty(self):
        """
        Returns whether the stack is empty.
        :rtype: bool
        """
        return self.top_ptr == -1

ans = [
    (["MyStack","push","pop","push","top"],
     [[],[1],[],[2],[]],
     [None,None,1,None,2]),    
]
    
# Your MyStack object will be instantiated and called as such:
for i in ans:
    r = []
    for j in range(len(i[0])):
        if i[0][j] == "MyStack":
            obj = MyStack()
            r.append(None)
        if i[0][j] == "push":
            r.append(obj.push(i[1][j][0]))
        if i[0][j] == "pop":
            r.append(obj.pop())
        if i[0][j] == "top":
            r.append(obj.top())
    print r, r == i[2]