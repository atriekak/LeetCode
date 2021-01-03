class MinStack:
​
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = []
        self.min = float('inf')
​
    def push(self, x: int) -> None:
        #Time Complexity: O(1)
        #Space Compllexity: O(1)
        
        if x <= self.min:
            self.stack.append(self.min)
            self.min = x
        self.stack.append(x)
        return
​
    def pop(self) -> None:
        #Time Complexity: O(1)
        #Space Compllexity: O(1)
        
        popped = self.stack.pop()
        if popped == self.min:
            self.min = self.stack.pop()
        return
​
    def top(self) -> int:
        #Time Complexity: O(1)
        #Space Compllexity: O(1)
        
        return self.stack[-1]
​
    def getMin(self) -> int:
        #Time Complexity: O(1)
        #Space Compllexity: O(1)
        
        return self.min
​
​
# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
