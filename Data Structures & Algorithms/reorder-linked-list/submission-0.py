# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        n = 1
        temp = head
        while temp:
            n+=1 
            temp = temp.next
        
        mid = n//2

        head2 = None
        temp = head
        prev = None
        while mid>0:
            prev = temp
            temp = temp.next
            mid-=1

        head2 = temp
        prev.next = None

        prev=None
        temp=head2

        while temp:
            temp = head2.next
            head2.next = prev
            prev = head2
            head2 = temp
        
        head2 = prev

        temp1 = head
        temp2 = head2

        while temp1 and temp2:
            ahead = temp2.next
            temp2.next = temp1.next
            temp1.next = temp2
            temp1 = temp2.next
            temp2 = ahead
        