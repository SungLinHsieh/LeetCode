# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def reverseKGroup(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        pre = ListNode(None)
        pre.next = head
        prev = pre
        curr = head
        front = head
        back = pre
        i = 1
        while front!= None:
            front = front.next
            if i%k==0:
                for j in range(k):
                    next = curr.next
                    curr.next = prev
                    prev = curr
                    curr = next
                back.next.next = curr
                tmp = back.next
                back.next = prev
                prev = tmp
                back = tmp
            i += 1
        return pre.next
                
                
