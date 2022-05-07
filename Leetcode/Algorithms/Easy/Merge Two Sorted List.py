# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution(object):
    def mergeTwoLists(self, list1, list2):
        """
        :type list1: Optional[ListNode]
        :type list2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        if list1 and list2:
            if list1.val > list2.val:
                list1, list2 = list2, list1
            list1.next = self.mergeTwoLists(list1.next, list2)
        return list1 or list2


def createNewListNode(arr):
    head = None
    for x in arr:
        head = ListNode(x, next=head)
    return head


list1 = createNewListNode([1, 2, 4])
list2 = createNewListNode([1, 3, 4])

res = Solution().mergeTwoLists(list1, list2)

print(res)
