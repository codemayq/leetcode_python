# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        if head is None or head.next is None:
            return False

        pre = head
        tail = head

        while tail and tail.next:
            tail = tail.next.next
            pre = pre.next

            if pre == tail:
                break

        return pre == tail