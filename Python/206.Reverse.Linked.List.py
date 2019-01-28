# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        prev = None
        while(head != None):
            new = ListNode(head.val)
            new.next = prev
            prev = new
            head = head.next
        return prev
            
        
