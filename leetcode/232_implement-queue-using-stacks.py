# 232. Implement Queue using Stacks - LeetCode
# https://leetcode.com/problems/implement-queue-using-stacks/description/

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

class MyQueue_SingleStack(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.stack = MyStack()

    def push(self, x):
        """
        Push element x to the back of queue.
        :type x: int
        :rtype: void
        """
        self.stack.push(x)

    def pop(self):
        """
        Removes the element from in front of queue and returns that element.
        :rtype: int
        """
        if self.stack.empty():
            return False
        temp_stack = MyStack()
        while not self.stack.empty():
            x = self.stack.pop()
            temp_stack.push(x)
        ret = temp_stack.pop()
        while not temp_stack.empty():
            x = temp_stack.pop()
            self.stack.push(x)
        return ret

    def peek(self):
        """
        Get the front element.
        :rtype: int
        """
        if self.stack.empty():
            return False
        temp_stack = MyStack()
        while not self.stack.empty():
            x = self.stack.pop()
            temp_stack.push(x)
        ret = temp_stack.top()
        while not temp_stack.empty():
            x = temp_stack.pop()
            self.stack.push(x)
        return ret

    def empty(self):
        """
        Returns whether the queue is empty.
        :rtype: bool
        """
        return self.stack.empty()
        
class MyQueue_DoubleStack(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.in_stack = MyStack()
        self.out_stack = MyStack()

    def push(self, x):
        """
        Push element x to the back of queue.
        :type x: int
        :rtype: void
        """
        self.in_stack.push(x)

    def pop(self):
        """
        Removes the element from in front of queue and returns that element.
        :rtype: int
        """
        self.peek()
        return self.out_stack.pop()

    def peek(self):
        """
        Get the front element.
        :rtype: int
        """
        if self.out_stack.empty():
            while not self.in_stack.empty():
                x = self.in_stack.pop()
                self.out_stack.push(x)
        return self.out_stack.top()

    def empty(self):
        """
        Returns whether the queue is empty.
        :rtype: bool
        """
        return self.out_stack.empty() and self.in_stack.empty()

MyQueue = MyQueue_DoubleStack

ans = [
    (["MyQueue","empty","push","pop","push","push","peek","empty"],
     [[],[],[1],[],[2],[3],[],[]],
     [None,True,None,1,None,None,2,False]),    
]
    
for i in ans:
    r = []
    for j in range(len(i[0])):
        if i[0][j] == "MyQueue":
            obj = MyQueue()
            r.append(None)
        if i[0][j] == "push":
            r.append(obj.push(i[1][j][0]))
        if i[0][j] == "pop":
            r.append(obj.pop())
        if i[0][j] == "peek":
            r.append(obj.peek())
        if i[0][j] == "empty":
            r.append(obj.empty())
    print r, r == i[2]