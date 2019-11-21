# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        if not head or n == 0:
            return None

        # one pass
        # may need to flip the list if we want to do one pass:
        prev = ListNode(None)
        current = head
        while current:
            next_one = current.next
            current.next = prev
            prev = current
            current = next_one
        head = prev


