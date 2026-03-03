# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def length(self,head):
        count=0
        while head is not None:
            count+=1
            head=head.next
        return count
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None or head.next is None:
            return None
        start=head
        l=self.length(head)
        mid = l//2
        i=0
        prev=None
        while i<=mid:
            if i==mid-1:
                prev=head
            if i==mid:
                prev.next=head.next
            head=head.next
            i+=1
        return start

        