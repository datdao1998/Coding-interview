class Solution(object):
    def oddEvenList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if (not head): return head
        odd = head
        even = head.next
        evenHead = even
        while (even and odd and even.next and odd.next):
            odd.next = even.next
            odd = odd.next
            even.next = odd.next
            even = even.next
        odd.next = evenHead
        return head


class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


arr = [2, 1, 3, 5, 6, 4, 7]
head = None
for x in arr:
    head = ListNode(x, next=head)

print(Solution().oddEvenList(head).val)
