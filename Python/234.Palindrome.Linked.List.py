# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        if not head or not head.next:
            return True
        
        slow = fast = head
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
        
        slow.next = self.revlist(slow.next)
        slow = slow.next
        
        while slow:
            if head.val != slow.val:
                return False
            slow = slow.next
            head = head.next
        return True
        
        
    def revlist(self, head):
        new = None
        while head:
            tmp = ListNode(head.val)
            tmp.next = new
            head = head.next
            new = tmp
        return new
            
