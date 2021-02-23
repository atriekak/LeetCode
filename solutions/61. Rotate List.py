# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: ListNode, k: int) -> ListNode:
        #Time Complexity: O(n)
        #Space Complexity: O(1)
        #where, n is the length of the given list
        
        if not head or not head.next or k == 0:
            return head
        
        curr = head
        n = 0
        tail = None
        while curr:
            tail = curr
            curr = curr.next
            n += 1
            
        k %= n
        if k == 0:
            return head
        
        curr = head
        for i in range(n - k - 1):
            curr = curr.next
            
        newHead = curr.next
        tail.next = head
        curr.next = None
        
        return newHead
