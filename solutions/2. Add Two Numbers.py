# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        #Time Complexity: O(m + n)
        #Space Complexity: O(1)
        #where, m and n are the lengths of l1 and l2, respectively
        
        carryover = 0
        head = pointer = ListNode(-1)
        while l1 or l2 or carryover:
            if l1 and l2:
                temp = l1.val + l2.val + carryover
                l1 = l1.next
                l2 = l2.next
            elif l1:
                temp = l1.val + carryover
                l1 = l1.next
            elif l2:
                temp = l2.val + carryover
                l2 = l2.next
            else:
                temp = carryover
            
            pointer.next = ListNode(temp % 10)
            pointer = pointer.next
            carryover = temp // 10
            
        return head.next
