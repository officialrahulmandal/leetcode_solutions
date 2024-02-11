# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        start=head
        last_element=''
        last_node=''
        while head is not None:
            if head.val==last_element:
                last_node.next=head.next
                head=head.next
            else:
                last_element=head.val
                last_node=head
                head=head.next
        return start

        
        
        