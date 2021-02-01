class Logger:
    #Time Complexity: O(1) // for each message
    #Space Complexity: O(m)
    #where, m is the total number of (unique) messages
​
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.map = {}
​
    def shouldPrintMessage(self, timestamp: int, message: str) -> bool:
        """
        Returns true if the message should be printed in the given timestamp, otherwise returns false.
        If this method returns false, the message will not be printed.
        The timestamp is in seconds granularity.
        """
        if message not in self.map or timestamp - self.map[message] >= 10:
            self.map[message] = timestamp
            return True
        
        else:
            return False
​
​
# Your Logger object will be instantiated and called as such:
# obj = Logger()
# param_1 = obj.shouldPrintMessage(timestamp,message)
