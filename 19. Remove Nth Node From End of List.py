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

        # one pass with fast ans slow:

        temp = ListNode(0)
        temp.next = head
        fast = slow = temp
        # Here we move fast n ahead slow,
        for i in range(n):
            fast = fast.next
        while fast and fast.next:
            fast = fast.next
            slow = slow.next
        # we want slow, and we skip nth in slow
        slow.next = slow.next.next

        return temp.next



