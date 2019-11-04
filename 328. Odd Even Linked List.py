# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def oddEvenList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        # use two constant to store

        d1 = odd = ListNode(0)
        d2 = even = ListNode(0)
        i = 1
        while head:
            if i % 2:
                # odd
                odd.next, odd = head, head
            else:
                even.next, even = head, head
            head = head.next
            i += 1
        odd.next, even.next = d2.next, None
        return d1.next



