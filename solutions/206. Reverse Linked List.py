# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    #Solution 1
    def reverseList(self, head: ListNode) -> ListNode:
        #Approach: Recursive
        #Time Complexity: O(n) // equivalent to Solution 2
        #Space Complexity: O(n)
        #where, n is the length of the linked list
        
        #base
        if not head or not head.next:
            return head
        
        #logic
        reversedHead = self.reverseList(head.next)
        head.next.next = head
        head.next = None
        return reversedHead
    
    #Solution 2
    """
    def reverseList(self, head: ListNode) -> ListNode:
        #Approach: Iterative
        #Time Complexity: O(n)
        #Space Complexity: O(n)
        #where, n is the length of the linked list
        
        if not head:
            return None
        
        st = []
        while head.next:
            st.append(head)
            head = head.next
            
        reversedHead = head
        
        while st:
            head = st.pop()
            head.next.next = head
            head.next = None
            
        return reversedHead
    """
    
    #Solution 3
