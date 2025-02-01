class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head

        odd = head
        even = head.next
        even_head = even  # Keep track of the start of the even list

        while even and even.next:
            odd.next = even.next  # Link odd nodes
            odd = odd.next
            even.next = odd.next  # Link even nodes
            even = even.next

        # Append the even list to the end of the odd list
        odd.next = even_head
        return head