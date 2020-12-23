class MinStack:
​
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.mainStack = []
        self.minStack = [float('inf')]
​
    def push(self, x: int) -> None:
        self.mainStack.append(x)
        self.minStack.append(min(self.minStack[-1],x))
        return
​
    def pop(self) -> None:
        self.mainStack.pop()
        self.minStack.pop()
        return
​
    def top(self) -> int:
        return self.mainStack[-1]
​
    def getMin(self) -> int:
        return self.minStack[-1]
​
​
# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
