# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        pre = ListNode(None)
        pre.next = head
        curr = head
        prev = pre
        while curr != None and curr.next !=None:
            next = curr.next
            curr.next = next.next
            prev.next = next
            next.next = curr
            prev = curr
            curr = curr.next
        return pre.next
        
