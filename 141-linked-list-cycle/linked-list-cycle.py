# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if not head:
            return
        turtle = head
        fast = head.next
        while fast and fast.next :
            if turtle == fast:
                return True
            turtle=turtle.next
            fast=fast.next.next

            

        return False
        