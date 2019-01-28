# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        pre = ListNode(None)
        pre.next = head
        front = pre
        back = pre
        for i in range(n):
            front = front.next
        while front.next != None:
            front = front.next
            back = back.next
        back.next = back.next.next
        return pre.next
