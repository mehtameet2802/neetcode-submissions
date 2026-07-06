# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        start = None
        # end = None
        ahead = None
        before = None
        prev = None
        temp = head
        n = 1

        while temp:
            if n==left:
                before = prev
                start = temp
            
            if n==right:
                ahead = temp.next
                temp.next = None
            
            n+=1
            prev = temp
            temp = temp.next
        
        # end.next = None

        if before:
            before.next = None
        
        temp = start
        prev = None
        while temp:
            temp1 = temp.next
            temp.next = prev
            prev = temp
            temp = temp1
        
        if before:
            before.next = prev
        else:
            head = prev
        
        start.next = ahead

        return head


        