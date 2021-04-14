# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        #Approach: Iterative
        #Time Complexity: O(n)
        #Space Complexity: O(1)
        #where, n is the number of nodes in the list
        
        if k == 1:
            return head
        
        dummy = ListNode(-1, head)
        left = dummy
        
        flag = True
        while True:
            last = left
            for i in range(k):
                if not last.next:
                    flag = False
                    break
                last = last.next
            
            if not flag:
                break
            
            first = left.next
            right = last.next
            last.next = None
            
            self.reverse(first)
            left.next = last
            first.next = right
            
            left = first
        
        return dummy.next
        
    def reverse(self, root):
        prev = None
        while root:
            temp = root.next
            root.next = prev
            prev = root
            root = temp
