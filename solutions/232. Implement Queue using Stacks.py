class MyQueue:
​
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.inStack = []
        self.outStack = []
​
    def push(self, x: int) -> None:
        """
        Push element x to the back of queue.
        """
        #Time Complexity: O(1)
        #Space Complexity: O(1)
        
        self.inStack.append(x)
        return
​
    def pop(self) -> int:
        """
        Removes the element from in front of queue and returns that element.
        """
        #Time Complexity: O(1)
        #Space Complexity: O(1)
        
        self.peek()
        return self.outStack.pop()
​
    def peek(self) -> int:
        """
        Get the front element.
        """
        #Time Complexity: O(1)
        #Space Complexity: O(1)
        
        if not self.outStack:
            while self.inStack:
                self.outStack.append(self.inStack.pop())
        return self.outStack[-1]
​
    def empty(self) -> bool:
        """
        Returns whether the queue is empty.
        """
        #Time Complexity: O(1)
        #Space Complexity: O(1)
        
        return len(self.inStack) == 0 and len(self.outStack) == 0
​
​
# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()
