# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        length = 0
        temp = head
        while temp:
            length += 1
            temp = temp.next

        if length == 1:
            return None
        
        n = length - n 

        prev = None
        ahead = None
        cur = head

        while n>0:
            prev = cur
            cur = cur.next
            n -= 1
        
        ahead = cur.next

        if prev == None:
            head = head.next
        elif ahead == None:
            prev.next = ahead
        else:
            cur.next = None
            prev.next = ahead
        
        return head


