# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        if headA == None or headB == None:
            return None
        # two pointer:
        m1 = headA
        m2 = headB
        while m1 != m2:
            m1 = headB if m1 == None else m1.next
            m2 = headA if m2 == None else m2.next
        return m1


