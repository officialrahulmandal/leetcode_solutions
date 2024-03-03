# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def len_ll(self, head):
        length=0
        while head is not None:
            head = head.next
            length += 1
        return length
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        length_ll = self.len_ll(head)
        if length_ll==1 and n==1:
            return None
        last_node= None
        start = head
        upto = length_ll-n
        while upto >0:
            last_node=head
            head=head.next
            upto -= 1
        if last_node:
            last_node.next = head.next
        if last_node is None and head.next is not None:
            return head.next
        return start
    
        