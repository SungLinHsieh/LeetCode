# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        n1 = l1
        n2 = l2
        ans = ListNode(0)
        ansnum = 0
        i = 0
        tmp = ans
        while (n1!=None or n2!= None):
            if n1 == None:
                tmp.next = ListNode((tmp.val + n2.val)//10)
                tmp.val = (tmp.val + n2.val)%10      
                n2 = n2.next
            elif n2 == None:
                tmp.next = ListNode((tmp.val + n1.val)//10)
                tmp.val = (tmp.val + n1.val)%10
                n1 = n1.next
            else:
                tmp.next = ListNode((tmp.val + n1.val + n2.val)//10)
                tmp.val = (tmp.val + n1.val + n2.val)%10
                n1 = n1.next
                n2 = n2.next
            tmp = tmp.next
        tmp = ans
        while tmp.next != None:
            if tmp.next.val == 0 and tmp.next.next == None:
                tmp.next = None
            else:
                tmp = tmp.next
        return ans
