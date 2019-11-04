# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    # first convert k lists into 2 lists
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        # h is the mininum in this list since they are sorted!
        h = [(l.val, index) for index, l in enumerate(lists) if l]
        heapq.heapify(h)
        head = current = ListNode(None)
        while h:
            val, index = heapq.heappop(h)
            current.next = ListNode(val)
            current = current.next
            lists[index] = lists[index].next
            node = lists[index]
            if node:
                heapq.heappush(h, (node.val, index))
        return head.next
