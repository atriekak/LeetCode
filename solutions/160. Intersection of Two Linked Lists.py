# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
​
class Solution:
    #Solution 1
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        #Approach: Skip nodes
        #Time Complexity: O(m + n)
        #Space Complexity: O(1)
        
        lenA = 0
        curr = headA
        while curr:
            curr = curr.next
            lenA += 1
        
        lenB = 0
        curr = headB
        while curr:
            curr = curr.next
            lenB += 1
            
        while lenA > lenB:
            headA = headA.next
            lenA -= 1
            
        while lenB > lenA:
            headB = headB.next
            lenB -= 1
