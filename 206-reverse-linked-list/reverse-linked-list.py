# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        initial=True
        previous=None
        while head is not None:
            store=head.next
            head.next=previous
            previous=head
            head=store
        return previous

        