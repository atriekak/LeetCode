# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: ListNode, m: int, n: int) -> ListNode:
        #Approach: Iterative
        #Time Complexity: O(n)
        #Space Complexity: O(1)
        
        if m == n:
            return head
        
        dummy = ListNode(-1, head)
        prev = dummy
        curr = head
        
        idx = 1
        while idx < m:
            prev = curr
            curr = curr.next
            idx += 1
        
        left = prev
        midHead = left.next
        
        while idx < n:
            prev = curr
            curr = curr.next
            idx += 1
        
        right = curr.next
        curr.next = None
        midReversed = self.reverse(midHead)
        
        left.next = midReversed
        midHead.next = right
        
        return dummy.next
        
    def reverse(self, root):
        prev = None
        
        while root:
            temp = root.next
            root.next = prev
            prev = root
            root = temp
        
        return prev
