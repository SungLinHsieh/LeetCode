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
        if not headA or not headB:
            return None
        lenA = 0
        slowA = headA
        while slowA.next and slowA.next.next:
            lenA = lenA + 2
            slowA = slowA.next.next
        if slowA.next:
            lenA = lenA + 1
        lenB = 0
        slowB = headB
        while slowB.next and slowB.next.next:
            lenB = lenB + 2
            slowB = slowB.next.next
        if slowB.next:
            lenB = lenB + 1  
        
        if lenA > lenB:
            headlong = headA
            headshort = headB
            diff = lenA - lenB
        else:
            headlong = headB
            headshort = headA
            diff = lenB - lenA
        for i in range(diff):
            headlong = headlong.next
        while headlong:
            if headlong == headshort:
                return headlong
            headlong = headlong.next
            headshort = headshort.next
        return None
        
            
