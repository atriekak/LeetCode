class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None

class MyHashMap:
    def __init__(self):
        """
        Initialize your data structure here.
        """
        #Time Complexity: O(1) // because the max size of a linked list can be 100
        
        self.szNodes = 10000
        self.nodes = [None] * self.szNodes
        
    def index(self, key):
        return hash(key) % self.szNodes
    
    def find(self, head, key):
        curr = head
        prev = None
        
        while curr != None and curr.key != key:
            prev = curr
            curr = curr.next
        return prev
        
    def put(self, key: int, value: int) -> None:
        """
        value will always be non-negative.
        """
        i = self.index(key)
        if not self.nodes[i]:
            self.nodes[i] = Node(-1, -1)                #Dummy node for convenience
        prev = self.find(self.nodes[i], key)
        if not prev.next:
            prev.next = Node(key, value)
        else:
            prev.next.value = value
        return
            
    def get(self, key: int) -> int:
        """
        Returns the value to which the specified key is mapped, or -1 if this map contains no mapping for the key
        """
        i = self.index(key)
        if not self.nodes[i]:
            return -1
        prev = self.find(self.nodes[i], key)
        if not prev.next:
            return -1
        else:
            return prev.next.value

    def remove(self, key: int) -> None:
        """
        Removes the mapping of the specified value key if this map contains a mapping for the key
        """
        i = self.index(key)
        if not self.nodes[i]:
            return
        prev = self.find(self.nodes[i], key)
        if not prev.next:
            return
        else:
            prev.next = prev.next.next
            return


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)
