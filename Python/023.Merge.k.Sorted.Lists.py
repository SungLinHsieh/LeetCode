# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        if lists ==[]:
            return []
        while(len(lists) > 1):
            i = 0
            tmplist = list()
            while(i+1 < len(lists)):
                if lists[i] == None:
                    tmplist.append(lists[i+1])
                elif lists[i+1] == None:
                    tmplist.append(lists[i])
                else:
                    if lists[i].val < lists[i+1].val:
                        target = lists[i]
                        check = lists[i+1]
                    else:
                        target = lists[i+1]
                        check = lists[i]
                    head = target
                    while check != None and target.next != None:
                        if target.val == target.next.val or target.next.val < check.val:
                            target = target.next
                        else:
                            tmp = check.next
                            check.next = target.next
                            target.next = check
                            target = target.next
                            check = tmp
                    if check != None:
                        target.next = check
                    tmplist.append(head)
                i+=2
            if len(lists)%2 == 1:
                tmplist.append(lists[-1])
            lists = tmplist
        return lists[0]
            
